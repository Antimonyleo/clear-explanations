# Clear explanations

A compact skill for explaining complex concepts and projects across Codex, Claude Code, and other AI harnesses.

- Write clear, precise prose inspired by ASD-STE100.
- Include a visual overview for very complex topics: a schematic, architecture map, flow, or timeline.
- Use HTML for layered explanations or useful exploration; use animation when motion explains the idea.
- Keep evidence, assumptions, and important limits easy to find.

## Install

Clone once, then register it locally in Codex and Claude Code. Existing registration paths are skipped:

```sh
git clone https://github.com/Antimonyleo/clear-explanations.git
cd clear-explanations
for skill_root in "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$skill_root"
  skill_target="$skill_root/clear-explanations"
  if [ -e "$skill_target" ] || [ -L "$skill_target" ]; then
    echo "Already exists: $skill_target"
  else
    ln -s "$PWD" "$skill_target"
  fi
done
```

The links share one source. Inspect skipped paths before changing them. Run `git pull` inside the cloned folder to update.

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
