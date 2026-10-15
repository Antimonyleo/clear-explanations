# Choose emphasis by meaning

The model or author selects the important text while writing. A renderer applies those choices; it should not infer importance or status from warning words, numbers, or every existing bold span.

## Select the span

1. Find what answers the reader's question or changes their decision: the outcome, a decisive limitation, or an action they must take.
2. Select the shortest complete phrase expressing that point. A word is enough only when it carries the whole meaning; a full sentence is appropriate when its condition cannot be separated safely.
3. Keep negation, uncertainty, scope, and decisive conditions with the claim. Keep the denominator or threshold when a highlighted number needs it to mean anything.
4. Leave supporting explanations, routine details, and repeated versions of the same warning plain. Begin with one central takeaway, adding another highlight only when it changes what the reader should understand or do. Do not fill a highlighting quota.
5. Read just the emphasized text, then read it in context. It should give a faithful account of the answer and its decisive limits, without implying greater certainty or a different outcome.

## Choose the treatment

| Role | Portable treatment | Optional client-supported color |
| --- | --- | --- |
| Short navigation label | Bold | Cyan |
| Central takeaway | Bold complete phrase | Cyan, unless its role is an unresolved limitation |
| Important evidence or a useful secondary fact | Bold only when it affects the decision | Default foreground |
| Unresolved blocker or uncertainty that changes the decision | Bold complete limiting phrase | Amber/yellow |
| A necessary reader action or dependency | Bold action and target | Amber/yellow |
| Explanation, background, routine steps, repeated reminders | Plain | Default foreground |

Color has a role; it is not an automatic decoration for bold. A routine next step need not look like a warning. Keep ordinary prose readable without color, and do not insert raw ANSI escapes into a reply whose client does not support them. No additional green or red is needed for these roles.

## Examples

- `代码修好了，但**验证还没有全部通过**。` Emphasize the decision-limiting result, rather than giving the successful part equal visual weight. The limiting phrase can be amber; the rest stays plain.
- `**测试结果** — **4 passed、1 error**。` The label can be cyan, while the complete count stays bold in the normal foreground. A nearby explanation of the error can remain plain if the unresolved status is already clear.
- `**Next step** — **Configure the test service**, then rerun the command below.` The label can be cyan and the required action amber. The verb and target are selected together.
- `**Only under matched conditions can these runtimes be compared.**` Keep the condition with the comparison; highlighting only “runtimes can be compared” would change the claim.
- `旧日志写着“全部通过”；**本次未运行测试，结果未知**。` The quoted success is background. The current unknown status deserves attention. A word-matching rule cannot establish which statement governs this answer.

These are selection guidelines, not evidence that a model reliably follows them. Test with fresh Chinese and English answers before claiming improved reading or model generality. The optional terminal preview uses explicit, document-scoped annotations to demonstrate the treatments; it is not an automatic semantic classifier.
