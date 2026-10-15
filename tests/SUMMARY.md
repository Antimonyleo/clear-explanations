# Evaluation summary

Release summary, 2026-10-14. Raw transcripts, logs, historical prompt variants, old evaluation harnesses, and one-off comparison packets were removed during release cleanup. This file preserves the conclusions, not an independently reproducible archive of those historical runs. No new model calls were made during cleanup.

## Historical findings

- An earlier frozen snapshot was exercised through native Codex GPT-6 Sol and Claude Sonnet 5.5 loading paths: 128 main task runs, 32 extra task runs, and eight three-turn language sessions. GPT-6.1 Sol remained a separate partial lane after infrastructure failures.
- The recorded deterministic checks covered exact-output controls, independently checked code changes, read-only investigations, and language switching. Before cleanup, the saved-evidence audit passed 818 checks. This count is a historical evidence audit, not 818 behavioral tests of the current skill.
- Codex retained more supplied checklist facts with instructions; Claude showed no clear core benefit. Ease changes were small and inconsistent. These results do not establish general readability improvement and refer to an older snapshot.
- Later bilingual core experiments used Claude Sonnet and Opus with a Codex judge. Judge objections are not independently confirmed factual errors. Language changes confound some Chinese preferences. Failed shortening variants were rejected, and the reader-guided v6 core wording was retained.

## Reader decisions

One Chinese-native reader requested bold important messages, short bold labels, and bullets for parallel items at the same information level. These preferences are in the current skill and both optional cores. Important emphasis must include its negation, uncertainty, and decisive limits.

On a later Chinese CUDA editing comparison, the reader said “B is better.” B placed the first action and recommendation earlier, separated backup options, moved background later, and removed a closing offer. It also replaced long table cells that the Rich preview truncated. This was one unblinded, untimed preference on combined changes; it does not isolate color, bold, ordering, or length effects. The retired CUDA packet is not shipped as technical advice.

In a separate two-case terminology comparison, the reader preferred B: retain familiar English technical terms within natural Chinese sentences, avoiding routine bilingual duplicates. The reader specified that this affects explanations and reports only; new skills, code, projects, and scientific/general writing should default to English. The current skill and Chinese core reflect that scope, with explicit requests and existing project conventions taking precedence. This is reader preference, not a new cross-model result; the one-off comparison packet was retired after the decision.

## Current verification and limits

The retained presentation suite has eight highlighting safeguard tests and a 96-condition Chinese/English layout audit. It verifies selection application and renderer fidelity, not automatic importance selection by a model. D implements the reader's preferred combination of grouping, emphasis, and parallel bullets; A/B/C remain fixed-wording controls.

The current Chinese core was checked on 2026-10-15 against no core and the earlier v6 wording (Claude Sonnet and Opus, 12 prompts, 8 repeats; Codex checklist judge; 144 paired answers per comparison). Judge-rated plainness was +0.22 [+0.12, +0.31] on a 5-point scale versus no core, and equal to v6 (−0.04 [−0.11, +0.03]). Ease, wrong-claim counts, and facts kept did not change clearly. English-prompt replies came back in Chinese in 39 of 40 runs; exact JSON was correct 8 of 8, and no commit message contained Chinese. Restoring the "technical term only when needed" clause did not change plainness, and three one-sentence shortening variants (stop rule, section size, both) either cut under 15% or lowered quality, so none was adopted. The raw runs are in the local branch `archive/eval-history` (round 9 data was not saved); judge ratings are not confirmed factual errors, and no new human read was done.

The skill wording as a whole has not undergone a new multi-model evaluation. Native interface contrast, fonts, clipboard behavior, controlled reading performance, and long-conversation token growth remain unverified. The [context review](presentation/context-review.md) found no repository-driven per-turn reminder or loading loop; repeated host invocations or reference reads can still add context.
