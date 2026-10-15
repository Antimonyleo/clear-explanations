# Context review and release decision

Reviewed 2026-10-14. This is a source/mechanism review, not a long-conversation benchmark.

## What can enter context

| Component | Current size | Loading path |
| --- | --- | --- |
| Skill discovery metadata | Name, description, and host-supplied path | Available for skill selection; host controls representation. |
| `SKILL.md` | 535 whitespace-separated words, 3,846 UTF-8 bytes | Full instructions when selected. |
| English core | 119 words, 769 bytes | Optional manual installation in persistent instructions. |
| Chinese-explanation core | 160 words, 1,123 bytes | Alternative to English core; its instructions are also written in English. |
| Highlighting reference | 544 words, 3,520 bytes | Linked for emphasis/color decisions, not supplied by a runtime hook. |
| Other references | Conditional background/artifact guidance | Enter context if the agent reads them. |
| `tests/`, including preview and evaluation data | No automatic loading path in this skill | Agent may inspect them when explicitly working on this repository. |

Counts include file metadata/headings where present and are not token counts. Repository size is separate from loaded context size.

## Mechanism findings

- The shipped skill is instruction-only. `always-on/` contains two alternative text files. There is no installed hook, daemon, per-turn reminder, or recursive loader in this delivery. Historical hook experiments were removed during release cleanup.
- [Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) describes progressive disclosure: discovery metadata first, full instructions when selected. It does not establish a universal guarantee that a selected skill can appear only once throughout a conversation.
- [Official Codex instruction documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) says the `AGENTS.md` instruction chain is built once per run. A core installed once adds a fixed block to that chain. This is different from a new transcript reminder on every turn; it can still contribute input tokens on requests that include those instructions.
- Reinvoking a skill or rereading a reference can add context. The repository cannot enforce host-side deduplication or compaction behavior. Installing both cores, duplicate skill installations, or rerunning an append command also creates avoidable duplication. The README now warns against repeated appends and full-skill duplication.
- The color preview uses Rich only when run explicitly. It makes no model calls and does not become a permanent conversation renderer or prompt layer.

## Evidence boundary and decision

The historical portability evaluation covered bounded tasks and three-turn language sessions on an earlier snapshot. It did not validate long conversations or compaction. Older notes mentioned a small Claude compaction experiment without retained raw evidence; it is not treated as a passing current-version test. Historical raw outputs and retired harnesses were removed during release cleanup; the [evaluation summary](../SUMMARY.md) records their limits.

The current emphasis and hierarchy reflect reader preferences. Failed shortening experiments did not replace v6. No new model behavior was measured during cleanup.

The mechanism review found no repository-driven per-turn growth path; it does not promise zero context cost or zero host-driven repetition. Long-conversation token tracing and fresh Chinese/English multi-model comparisons remain optional follow-up work.
