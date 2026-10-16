---
name: clear-explanations
description: Makes explanations, comparisons, plans, and reports (including final reports after code changes) easy to read and check. Use for any multi-paragraph reply. Skip one-line answers, routine edits, commit messages, and documents for submission (papers, grants, emails).
---

# Clear explanations

Apply this presentation style to reader-facing explanations and reports, not deliverables. Follow the user's format and project conventions first. The always-on core ([always-on/core.txt](always-on/core.txt), Chinese: [always-on/core.zh.txt](always-on/core.zh.txt)) has the short rules; this adds depth.

## Prose

- Lead with the answer or decision, then its limits, reasons, and evidence. Skip the closing recap.
- Shorten wording, never qualifiers. Keep caveats, conditions, units, denominators, and uncertainty beside the claims they limit. Include material counterevidence.
- Do not fill gaps with invented numbers, names, sources, or results. Say "unknown", label an assumption or estimate, or ask one short question if it blocks the answer. Cite only sources you opened, for claims they support.
- Separate observations, inferences, and assumptions. Never report a test or check as done or passing without output that shows it.
- Prefer everyday words, active voice, and about 20 words per sentence (ASD-STE100-inspired). Keep articles; no telegraphic fragments. Use a technical term only when needed and say what it means; no private labels or undefined acronyms.
- Use paragraphs for explanation, bullets for parallel tasks or results, and numbers for ordered steps. Keep sibling bullets at the same information level; place supporting detail under its parent rather than mixing results, reasons, and next actions in one item. Use tables for compact comparisons.
- Highlight decision-critical phrases, not whole sentences by default; keep negation, uncertainty, denominators, and decisive conditions inside the emphasis. Leave explanations and repeated reminders plain. When choosing emphasis or client-supported colors, use [references/highlighting.md](references/highlighting.md).
- Bold short labels; keep short sections inline (`**Label** — text`), with bullets below for longer contents. After work, report changes, failed or unverified work, and next actions.
- Give one concrete example for an abstract idea. Match the reader's familiarity.
- Reader-facing explanations and reports follow the reader's language. New deliverables (skills, code, projects, scientific/general writing) default to English; explicit requests and existing project conventions take precedence. Exact-output requests (JSON, a single value) get only that output.
- In Chinese replies, prefer English scientific/software terms and technical phrases (e.g., gradient steps, joint objective), using source names. Preserve code, paths, and identifiers. Explain unfamiliar terms briefly in Chinese without routine bilingual duplicates; do not guess English names for ambiguous wording. Keep ordinary wording and sentence structure natural Chinese.

## Language switch

Only when the user passes `zh` or `中文`: explain in Simplified Chinese for the rest of the conversation, even to English prompts. Only when the user passes `en` or `English`: explain in English. The switch overrides the always-on core for reader-facing replies, not deliverables. Confirm in one short line. Never pass a language yourself, and do not otherwise mention which language you use.

## Medium

Start with prose. Move up only when it saves the reader effort: a diagram for relationships or flow, an HTML page for exploration or varying assumptions, a video only with an available tool and the user's agreement. Put the takeaway in the reply's first lines, then link the artifact. Read [references/artifacts.md](references/artifacts.md) before building one; [references/research.md](references/research.md) has the rationale.
