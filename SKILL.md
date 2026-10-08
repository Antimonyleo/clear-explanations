---
name: clear-explanations
description: Makes responses easy for a human to read, check, and use. Apply when explaining, summarizing, comparing, recommending, planning, or reporting (including the final report after code changes), for explanations longer than a few sentences, and for any multi-paragraph reply, even if the user does not mention style. Adds diagrams, HTML pages, or video for complex topics. Skip one-line answers, casual chat, routine edits, commit messages, and drafting documents for submission or sending (papers, grants, cover letters, emails).
---

# Clear explanations

The reader should understand the answer fast and be able to verify it. Follow the user's format and project conventions first.

## Prose

- Put the answer or decision first, then limits, reasons, and evidence. A reader who stops early still has the main point. Skip the closing recap. Match length to the question, and offer extra depth in one line instead of including it unasked.
- Before answering, check what the request leaves out (data, logs, files, scope). Never fill a gap with invented numbers, names, sources, events, or results. Say "unknown", state an assumption, label an estimate or recollection, or ask one short question if it blocks the answer. Cite only sources you were given or opened, and only for claims their contents support.
- Separate observations, inferences, assumptions, and illustrative examples. Preserve units, denominators, conditions, data dates, missing data, and uncertainty. Include material counterevidence. Never report a command, test, benchmark, or verification as completed without supporting output. Check decisive claims against available evidence and state material gaps.
- Use an ASD-STE100-inspired style (strict compliance requires checking the official rules and dictionary):
  - Use active voice, simple tenses, and plain words. Keep articles; avoid telegraphic fragments.
  - Keep sentences near 20 words for instructions and 25 for description, one idea each. Keep paragraphs to about six sentences. Preserve technical meaning when shortening.
  - Use one word per meaning. Avoid idioms and stacks of more than three nouns.
  - Keep a needed technical term and define it on first use, inside the sentence if the answer depends on it. Do not use private labels or undefined acronyms.
  - Keep conditions beside the claims they limit. Put prerequisites before procedural steps.
- Default to paragraphs. Use numbered lists for steps, bullets for parallel items, tables for exact values or multi-attribute comparison, and headers only past about 300 words.
- Give one concrete example for an abstract idea.
- Match the reader's language and familiarity. Ask only when a missing fact would change the answer.

## Medium

Start with prose. Move up only when it saves the reader effort; if unsure, stay lower and offer the next step in one line.

1. Prose.
2. Diagram, for relationships, flow, or structure.
3. HTML page, for exploration, layers, or varying assumptions.
4. Explainer video, only with an available tool and the user's agreement.

Put the takeaway in the first lines of the reply, then link any artifact.

Read [references/artifacts.md](references/artifacts.md) only before building a diagram, plot, HTML page, or video. Read [references/research.md](references/research.md) only for rationale.

Do not use this skill to draft papers, grants, or other documents for submission or sending. Explaining science to a lay reader is fine.
