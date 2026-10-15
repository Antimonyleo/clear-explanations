# Terminal presentation preview

A standalone Rich preview for exploring Chinese/English grouping and emphasis. It does not change Claude Code's or Codex's native renderer, fonts, or settings. The dependencies are preview-only.

## Samples and styles

[Chinese](zh.md) and [English](en.md) each contain four layouts of a fictional report. A/B/C retain the same wording and facts; D implements the reader's requested combination of bold short labels, selective emphasis, and bullets for parallel items. D changes wording and hierarchy, so it is not a controlled wording comparison.

```sh
./tests/presentation/preview.sh
./tests/presentation/preview.sh --language en
./tests/presentation/preview.sh --all
./tests/presentation/preview.sh --style duotone --color always
```

The default is Chinese D, current terminal width, and `quiet` styling. Available styles:

- `stock`: Rich's default Markdown styling.
- `quiet`: normal terminal foreground/background for inline code, retaining Markdown emphasis.
- `accent`: cyan for existing bold spans, useful as a simple comparison.
- `duotone`: explicit document-scoped roles from [highlights.json](highlights.json). Labels/key conclusions use cyan; necessary actions and important limitations use amber; evidence can remain bold without color.

Colors use the terminal palette; contrast in a particular theme is not guaranteed. `--color auto` respects `NO_COLOR`; `always` explicitly enables styling for that command; `never` disables it. Bold and wording must carry the meaning when color is unavailable.

The [highlighting guide](../../references/highlighting.md) governs phrase selection. The renderer validates unique complete bold spans and known roles, rejecting missing, partial, ambiguous, or overlapping selections. It cannot determine whether the author chose the right phrase or role. No additional model call is made.

## Checks

```sh
./tests/presentation/preview.sh --audit
uv run --no-project --with-requirements tests/presentation/requirements.txt python -m unittest discover -s tests/presentation -p test_highlighting.py -v
```

The audit reports 96 conditions: two languages, four variants, three widths (60/80/120), and four styles. Check content preservation, ANSI/plain layout, and overflow separately from token splitting. The D sample keeps the copy command contiguous in all 24 D conditions; some A/B/C layouts split it across lines.

Generated audits are not committed. Save local outputs under ignored `tests/results/` if needed. `uv` may download pinned preview packages into its cache; it does not install packages into the skill or change agent configuration.

## Reading checks

Compare one variant at a time at the same width, font, and theme. Check whether the result, unresolved issue, and next action are easy to locate after looking away. Check wrapping, punctuation, identifiers, and command copying in the actual interface. A separate Rich preview cannot verify an agent client's native display.

See [RESULTS.md](RESULTS.md) for the bounded findings, [the evaluation summary](../SUMMARY.md) for historical reader decisions, and [the context review](context-review.md) for loading behavior. Broader reading and multi-model tests are optional follow-up work, not completed claims.
