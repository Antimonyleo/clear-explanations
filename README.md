# Clear explanations

An agent skill that makes AI answers easier to read, check, and act on.

The idea comes from Andrej Karpathy: as models do more of the work, we spend more time understanding their output. He suggests asking for plain controlled writing (ASD-STE100), then diagrams, then HTML pages, then explainer videos.

## What it does

- Writes answers first, in plain short sentences inspired by ASD-STE100.
- Adds a diagram, page, or video only when it saves you effort.
- Marks what is sourced, assumed, or unchecked.
- Skips one-line answers, routine edits, and documents like papers, grants, and cover letters.

## Install

Clone once:

```sh
git clone https://github.com/Antimonyleo/clear-explanations.git
```

Then link or copy the folder into your tool's skills directory:

| Tool | Skills folder |
| --- | --- |
| Claude Code | `~/.claude/skills/clear-explanations` |
| Codex | `~/.agents/skills/clear-explanations` |
| Other Agent Skills tools | Their skills folder (see the [spec](https://agentskills.io/specification)) |

```sh
ln -s "$PWD/clear-explanations" ~/.claude/skills/clear-explanations
```

Update with `git pull`. If your tool has no skill support, paste `SKILL.md` into its custom instructions or system prompt.

## Make it apply everywhere (recommended)

Skills load only when the model judges them relevant, so short replies may skip it. Add this line to your global `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex and others). In chat apps, paste it into custom instructions.

```text
Write for a human reader: answer first, then limits and reasons; plain words, short active sentences (about 20-25 words), one word per meaning, no idioms; define terms on first use; paragraphs by default, lists for steps, tables for exact values; one concrete example for abstract ideas; no filler or closing recap. Match length to the question. Check what the request leaves out; never fill a gap with invented numbers, names, sources, or events. Say unknown, state an assumption, or ask one short question. For explanations, plans, comparisons, and overviews, also use the clear-explanations skill. Skip for one-line answers and for papers, grants, and other documents for submission.
```

## Use

Ask normally, or call it by name: `/clear-explanations` in Claude Code, `$clear-explanations` in Codex.

[Research and rationale](references/research.md)
