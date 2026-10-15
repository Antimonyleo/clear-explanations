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
cd clear-explanations
```

Then link or copy the folder into your tool's skills directory:

| Tool | Skills folder |
| --- | --- |
| Claude Code | `~/.claude/skills/clear-explanations` |
| Codex | `~/.agents/skills/clear-explanations` |
| Other Agent Skills tools | Their skills folder (see the [spec](https://agentskills.io/specification)) |

```sh
mkdir -p ~/.claude/skills && ln -sn "$PWD" ~/.claude/skills/clear-explanations   # Codex: ~/.agents/skills
```

Update with `git pull`. If your tool has no skill support, paste `SKILL.md` into its custom instructions or system prompt.

## Always-on core (optional)

The skill loads only when the model picks it, which is not every time. To make the main rules apply every session, add one short core file to the instructions your tool always loads. Pick one language:

- English: `always-on/core.txt`
- Chinese explanations, English technical terms kept: `always-on/core.zh.txt`

```sh
cat always-on/core.txt >> ~/.claude/CLAUDE.md   # Codex: ~/.codex/AGENTS.md; chat apps: paste into custom instructions
```

Run this once, with only one language file. When updating, replace the existing core text instead of appending another copy. Do not paste the full skill or its references alongside the core when your tool already supports skills.

### Context cost

The core is a fixed instruction block: 119 words for English or 154 for Chinese explanations, both written in English. The skill entrypoint is 519 words including metadata. These are word counts, not tokenizer measurements. The skill does not install hooks, append reminders each turn, or automatically load the test results and terminal preview. Codex discovers a skill's name and description first and loads its full instructions when selected; see the [official skill documentation](https://learn.chatgpt.com/docs/build-skills). Codex builds its `AGENTS.md` instruction chain once per run; see [instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

This supports a small fixed instruction cost under normal loading, not a guarantee of zero context growth. Repeated skill invocations or reference reads can add copies to conversation history; host behavior and compaction determine what remains. Answers and tool output also accumulate normally. No controlled long-conversation token-growth test has been completed for the current version. Detailed findings and limits are in the [context review](tests/presentation/context-review.md).

Earlier evaluations and reader feedback do not establish a general readability or accuracy gain. The current presentation rules follow the reader's preferences and have not been re-evaluated across models. See the [evaluation summary](tests/SUMMARY.md) and [why the core is optional](references/always-on-enforcement.md).

## Use

Ask normally, or call it by name: `/clear-explanations` in Claude Code, `$clear-explanations` in Codex.

Switch the explanation language for the rest of a conversation: `/clear-explanations zh` or `/clear-explanations en` (Codex: `$clear-explanations zh` or `$clear-explanations en`).

[Research and rationale](references/research.md)

[Optional presentation tests and preview](tests/README.md) are for development; they are not needed to use the skill. Raw model transcripts, logs, and retired experimental variants are excluded from this release.
