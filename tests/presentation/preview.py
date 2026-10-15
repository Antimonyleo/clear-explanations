#!/usr/bin/env python3
"""Render the fixed presentation samples; optional audit measures layout, not ease."""
import argparse
from collections import Counter
import hashlib
from importlib.metadata import version
from io import StringIO
import json
import os
from pathlib import Path
import re
import sys

try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.theme import Theme
    from rich.text import Text
    from wcwidth import wcswidth
except ImportError:
    raise SystemExit(
        "Preview dependencies are missing. From the repository root, run:\n"
        "./tests/presentation/preview.sh --all"
    )

HERE = Path(__file__).resolve().parent
QUIET = Theme({"markdown.code": "default on default"})
ACCENT = Theme({"markdown.code": "default on default", "markdown.strong": "bold cyan"})
STYLES = {"stock": None, "quiet": QUIET, "accent": ACCENT, "duotone": QUIET}
ROLE_STYLES = {
    "label": "bold cyan", "key": "bold cyan", "fact": "bold",
    "attention": "bold yellow", "action": "bold yellow",
}
COMMAND = "python3 -m pytest -q"
TOKENS = ("median()", "parse()", "discount()", "test_convert_live", "api.rates.invalid", "legacy.py", COMMAND)


def samples(language):
    parts = re.split(r"^## ([ABCD])\s*$", (HERE / f"{language}.md").read_text(), flags=re.M)
    result = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    expected = {"A", "B", "C", "D"}
    if set(result) != expected:
        raise ValueError(f"Expected sample variants {sorted(expected)}")
    return result


def content(text):
    """Ignore presentation markers and whitespace only, for these fixed fixtures."""
    text = re.sub(r"^\s*[-•]\s+", "", text, flags=re.M)
    text = re.sub(r"^```[^\n]*$", "", text, flags=re.M)
    return re.sub(r"\s+", "", text.replace("**", "").replace("`", ""))


def console_for(style, **kwargs):
    return Console(theme=STYLES[style], **kwargs)


def annotations_for(language, variant):
    return json.loads((HERE / "highlights.json").read_text()).get(language, {}).get(variant, [])


def strong_phrases(text):
    """Read complete bold spans from the same Markdown parser as the renderer."""
    phrases = []
    for token in Markdown(text).parsed:
        depth, parts = 0, []
        for child in token.children or []:
            if child.type == "strong_open":
                if depth == 0:
                    parts = []
                depth += 1
            elif child.type == "strong_close":
                depth -= 1
                if depth == 0:
                    phrases.append(re.sub(r"\s+", "", "".join(parts)))
            elif depth and child.type in ("text", "code_inline"):
                parts.append(child.content)
    return phrases


def highlight_ranges(text, annotations, rendered_plain):
    """Validate explicit selections; never guess semantic roles from keywords."""
    bold = strong_phrases(text)
    positions = [i for i, char in enumerate(rendered_plain) if not char.isspace()]
    normalized = "".join(rendered_plain[i] for i in positions)
    ranges = []
    for selection in annotations:
        role, phrase = selection["role"], selection["text"]
        if role not in ROLE_STYLES:
            raise ValueError(f"Unknown highlighting role: {role}")
        needle = re.sub(r"\s+", "", phrase)
        if not needle or bold.count(needle) != 1:
            raise ValueError(f"Selection must match one complete bold span: {phrase!r}")
        if normalized.count(needle) != 1:
            raise ValueError(f"Selection is absent or ambiguous in this document: {phrase!r}")
        start = normalized.index(needle)
        left, right = positions[start], positions[start + len(needle) - 1] + 1
        if any(left < end and right > begin for begin, end, _ in ranges):
            raise ValueError(f"Overlapping highlighting selections: {phrase!r}")
        ranges.append((left, right, role))
    return ranges


class DuotoneMarkdown:
    """Apply document-scoped semantic selections after wrapping."""

    def __init__(self, text, annotations):
        self.text = text
        self.annotations = annotations

    def __rich_console__(self, console, options):
        segments = list(console.render(Markdown(self.text), options))
        rendered = Text.assemble(*[(s.text, s.style or "") for s in segments])
        for start, end, role in highlight_ranges(self.text, self.annotations, rendered.plain):
            rendered.stylize(ROLE_STYLES[role], start, end)
        yield from rendered.render(console, end="")


def document(text, style, annotations=()):
    return DuotoneMarkdown(text, annotations) if style == "duotone" else Markdown(text)


def render(text, style, width, annotations=()):
    stream = StringIO()
    console = console_for(style, file=stream, width=width, color_system=None, force_terminal=False)
    console.print(document(text, style, annotations))
    return stream.getvalue()


def audit():
    cells = []
    for language in ("zh", "en"):
        variants = samples(language)
        reference = content(variants["A"])
        if any(content(variants[label]) != reference for label in ("A", "B", "C")):
            raise ValueError(f"{language}: wording differs across layouts")
        for width in (60, 80, 120):
            for style in STYLES:
                for label, text in variants.items():
                    annotations = annotations_for(language, label)
                    plain = render(text, style, width, annotations)
                    styled_stream = StringIO()
                    styled_console = console_for(
                        style, file=styled_stream, width=width, force_terminal=True,
                        color_system="truecolor", no_color=False,
                    )
                    styled_console.print(document(text, style, annotations))
                    styled_plain = Text.from_ansi(styled_stream.getvalue()).plain
                    lines = plain.splitlines()
                    widths = [wcswidth(line) for line in lines]
                    cells.append({
                        "language": language, "width": width, "style": style, "variant": label,
                        "lines": len(lines), "blank_lines": sum(not line.strip() for line in lines),
                        "max_cells": max(widths, default=0),
                        "overflow_lines": [i + 1 for i, size in enumerate(widths) if size > width or size < 0],
                        "content_preserved": content(plain) == content(text),
                        "ansi_content_preserved": content(styled_plain) == content(text),
                        "ansi_layout_matches_plain": styled_plain == plain,
                        "split_tokens": [token for token in TOKENS if token not in plain],
                        "closing_punctuation_at_start": [
                            i + 1 for i, line in enumerate(lines)
                            if re.match(r"^[，。、；：？！）》】」』]", line.lstrip())
                        ],
                    })
    counts = Counter()
    for cell in cells:
        counts["content_preserved"] += cell["content_preserved"]
        counts["ansi_content_preserved"] += cell["ansi_content_preserved"]
        counts["ansi_layout_matches_plain"] += cell["ansi_layout_matches_plain"]
        counts["no_overflow"] += not cell["overflow_lines"]
        counts["no_split_tokens"] += not cell["split_tokens"]
        counts["no_line_start_closing_punctuation"] += not cell["closing_punctuation_at_start"]
    return {
        "renderer": f"Rich {version('rich')}", "width_measurement": f"wcwidth {version('wcwidth')}",
        "runner_environment": {key: os.environ.get(key) for key in ("TERM_PROGRAM", "TERM", "NO_COLOR")},
        "input_sha256": {
            name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
            for name in ("zh.md", "en.md", "preview.py", "requirements.txt", "highlights.json")
        },
        "conditions": len(cells), "counts": dict(counts),
        "standalone_command_probe": [
            {"width": width, "style": style,
             "command_on_one_line": COMMAND in render(f"```sh\n{COMMAND}\n```", style, width)}
            for width in (60, 80, 120) for style in STYLES
        ],
        "limits": "One fictional report per language; A/B/C share wording, D is a reader-requested revision with different wording and hierarchy. Duotone validates document-scoped complete-bold-span annotations, not semantic correctness or automatic status classification. Content preservation compares each render with its own source. Measured string layout only: no native agent UI, font, actual clipboard, or controlled reading test. Punctuation flags are diagnostic, not a full Chinese line-breaking validator.",
        "cells": cells,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("zh", "en"), default="zh")
    parser.add_argument("--variant", choices=("A", "B", "C", "D"))
    parser.add_argument("--style", choices=tuple(STYLES), default="quiet")
    parser.add_argument("--width", type=int, help="terminal columns; default: current terminal width")
    parser.add_argument("--color", choices=("auto", "always", "never"), default="auto",
                        help="auto respects terminal settings and NO_COLOR; always explicitly enables ANSI styling")
    parser.add_argument("--all", action="store_true", help="show layouts A through D sequentially")
    parser.add_argument("--audit", action="store_true", help="emit JSON layout observations instead of a preview")
    args = parser.parse_args()
    if args.width is not None and not 20 <= args.width <= 400:
        parser.error("--width must be between 20 and 400")
    if args.audit:
        print(json.dumps(audit(), ensure_ascii=False, indent=2))
        return
    color_options = {}
    if args.color == "always":
        color_options = {"force_terminal": True, "color_system": "truecolor", "no_color": False}
    elif args.color == "never":
        color_options = {"force_terminal": False, "color_system": None}
    console = console_for(args.style, width=args.width, **color_options)
    label = "虚构汇报 · 独立 Rich 预览" if args.language == "zh" else "Fictional report · standalone Rich preview"
    console.print(label, markup=False, highlight=False)
    console.print()
    variants = samples(args.language)
    selected = args.variant or "D"
    for name in variants if args.all else (selected,):
        if args.all:
            console.print(f"{name} / {args.style}", markup=False, highlight=False)
        console.print(document(variants[name], args.style, annotations_for(args.language, name)))
        if args.all:
            console.print()


if __name__ == "__main__":
    main()
