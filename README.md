# Clear explanations

A compact skill for explaining complex concepts and projects across Codex, Claude Code, and other AI harnesses.

- Write clear, precise prose inspired by ASD-STE100.
- Include a visual overview for very complex topics: a schematic, architecture map, flow, or timeline.
- Use HTML for layered explanations or useful exploration; use animation when motion explains the idea.
- Keep evidence, assumptions, and important limits easy to find.

## Install

Clone once, then register it in either or both tools:

```sh
git clone https://github.com/Antimonyleo/clear-explanations.git
cd clear-explanations
mkdir -p "$HOME/.agents/skills" "$HOME/.claude/skills"
ln -s "$PWD" "$HOME/.agents/skills/clear-explanations"
ln -s "$PWD" "$HOME/.claude/skills/clear-explanations"
```

The links share one source. If a target already exists, inspect it before replacing it. Run `git pull` inside the cloned folder to update.

## Use

| Tool | Prompt |
| --- | --- |
| Codex | `$clear-explanations Explain this project's architecture.` |
| Claude Code | `/clear-explanations Explain this project's architecture.` |

Both tools can also select installed skills automatically. Other [Agent Skills](https://agentskills.io/specification) harnesses can load this folder from their skills directory. Without skill support, supply [SKILL.md](SKILL.md) as task instructions.

No dependencies are required. Available tools determine rendering options; the skill includes a text/static fallback.

For consistent selection across projects, add this optional line to your global `AGENTS.md` or `CLAUDE.md`:

```text
Use clear-explanations for complex explanations and project overviews.
```

[Research and rationale](references/research.md) · [Codex setup](https://learn.chatgpt.com/docs/build-skills) · [Claude Code setup](https://code.claude.com/docs/en/skills)
