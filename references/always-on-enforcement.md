# Optional always-on core

The skill and the core serve different loading paths. The skill adds guidance when selected. A core pasted once into persistent instructions makes a short set of rules available even when the model does not select the skill. Use only one core and replace its existing text when updating.

The core is optional because earlier evaluations did not show a general readability gain. Some Chinese preferences also compared Chinese with English, so they cannot isolate a writing-rule effect. Model-judge error flags are not confirmed factual errors. The current emphasis and hierarchy rules reflect one reader's preferences rather than a new multi-model validation.

No hook, output style, per-turn reminder, or automatic rewrite pass is shipped. Colors are an optional renderer feature; the skill asks for meaningful emphasis without promising a particular client's appearance. The core does not enforce model compliance.

See the [evaluation summary](../tests/SUMMARY.md) for retained conclusions and the [context review](../tests/presentation/context-review.md) for measured file sizes, loading paths, and limits. Historical experiments and raw outputs were removed from the public release; they are not required to use the skill.
