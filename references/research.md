# Research and rationale

Reviewed 2026-10-02; skill text revised 2026-10-07 after a small subagent test (four prompts, one model, no controls). This synthesis extends the user-supplied Karpathy passage with primary research and official standards. It is a selected review, not a systematic review. The complete skill has not been evaluated experimentally across models or harnesses.

Scope: the skill covers explanations, summaries, comparisons, plans, and reports for human readers. It excludes drafting papers, grants, and other scientific publications, and one-line answers and routine edits.

## Main findings

1. **Match format to the task.** Tables help exact lookup; plots expose patterns; diagrams show relationships; HTML supports layers and exploration; motion can explain change. The reviewed evidence does not establish a universal ranking of these formats.
2. **Give a useful overview first.** Put the answer and consequential limits in the initial view. Add optional detail and controls with a clear purpose. A reader should understand the main result without operating every control.
3. **Make checking easy.** Understanding a model and detecting its errors are different outcomes. Keep sources, assumptions, counterevidence, units, and missing data close to the claims they affect.
4. **Keep the reader in control.** Provide usable defaults, reversible interactions, accessible alternatives, and pacing controls. Richer output adds value when it reduces effort or answers another question.

For complex concepts or projects, the skill adds a simple overview diagram when it saves the reader effort and the requested format and available tools permit it. This is a practical design choice, not a measured complexity threshold. HTML is useful for layered explanations, coordinated views, and what-if exploration. A schematic can be enough for a single relationship or process.

## Evidence and limits

| Source | Finding or guidance → implication; limit |
| --- | --- |
| [ASD-STE100 FAQ](https://www.asd-ste100.org/STE_faq.html), official guidance | Controlled vocabulary and writing rules reduce ambiguity → use concrete wording and consistent terms. STE-inspired guidance does not establish compliance; strict STE requires the standard. |
| [Larkin & Simon, 1987](https://iiif.library.cmu.edu/file/Simon_box00068_fld05250_bdl0001_doc0001/Simon_box00068_fld05250_bdl0001_doc0001.pdf), computational analysis | Spatial organization can reduce search and aid inference → expose relevant relationships and place labels nearby. Benefits depend on representation and task. |
| [Shneiderman, 1996](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf), visualization taxonomy | Overview, filtering, relationships, and detail are distinct tasks → give controls identifiable purposes. A design framework, not a randomized comparison. |
| [Segel & Heer, 2010](https://scivis.github.io/courses/visualstorytelling/segel_heer_2010.pdf), narrative analysis | Guided narratives can lead into exploration → start with an informative default. Descriptive examples do not establish a universally optimal layout. |
| [Mayer & Chandler, 2001](https://tecfa.unige.ch/tecfa/teaching/methodo/Mayer_Chandler01.pdf), two experiments | User-paced segmentation improved transfer in lightning lessons, with a different retention pattern → support pause, stepping, and revisiting. Specific educational conditions, not a general video-versus-text result. |
| [Tversky et al., 2002](https://www.tc.columbia.edu/faculty/bt2158/faculty-profile/files/_Morrison_Betrancourt_AnimationCanitfacilitate.pdf), research analysis | Unequal comparisons and transient information complicate animation benefits → use motion for meaningful change and retain keyframes. An older synthesis, not an assessment of generative video. |
| [Hullman et al., 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0142444), experiment | Animated samples improved several judgments about relationships among quantities; single-quantity judgments were often similar → select uncertainty displays for the actual inference. Motion benefits are task dependent. |
| [Poursabzi-Sangdeh et al., 2021](https://arxiv.org/abs/1802.07810), preregistered experiments, N=3,800 | Transparency helped model simulation but could impair correction of large errors → evaluate error detection separately from comprehension. Prediction models, not conversational assistants. |
| [Buçinca et al., 2021](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf), experiment | Deliberation interventions reduced overreliance but were less liked and benefited participants unequally → assess accuracy as well as preference. Does not justify mandatory extra steps for every output. |
| [Vasconcelos et al., 2023](https://arxiv.org/abs/2212.06823), five studies, N=731 | Verification costs influenced checking of simulated AI advice → make decisive evidence inexpensive to inspect. General assistant applications are an inference from maze tasks. |
| [Amershi et al., 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf), guidelines evaluated with 49 practitioners and 20 products | Communicate capability and uncertainty; support correction and dismissal → preserve reader control. Practitioner validation is not a causal performance estimate. |
| [Morita et al., 2025](https://arxiv.org/abs/2503.07463), GenAIReading study, N=24 | Generated summaries and images improved tested post-reading scores → content-aligned supplements are promising. Small sample and bundled intervention do not isolate the useful component. |
| [August et al., 2024](https://arxiv.org/abs/2403.04979), three within-subject studies | Simpler summaries helped unfamiliar readers; familiar readers sometimes overlooked details in overly plain summaries → calibrate familiarity and depth. Scientific-summary tasks do not establish universal benefits. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/), normative standard | Text alternatives, structure, keyboard access, captions, color-independent meaning, and motion control → include accessible ways to read and operate artifacts. Partial design checks do not establish full conformance. |
| [W3C complex-image guidance](https://www.w3.org/WAI/tutorials/images/complex/), accessibility guidance | Complex visuals need text conveying essential information → apply equivalents across visual formats. A short takeaway may be insufficient; this is guidance, not an effectiveness trial. |

## Implementation choices

- **Relaxed STE-inspired prose:** the skill lists concrete guidelines (about 20 words per instruction sentence, 25 per descriptive sentence, six sentences per paragraph, three-noun limit, one word per meaning). Preserve technical precision and natural sentence variety. Do not claim standard compliance or replace necessary domain terms to satisfy a word limit.
- **Standalone HTML:** without an existing stack, a self-contained file lowers opening and setup effort. This is an engineering convention. Reuse the user's stack when appropriate.
- **Honest scenarios:** label hypothetical examples and simulations; expose assumptions. A working slider does not validate the underlying model. Never invent measurements or confidence scores.
- **Portable packaging:** [Agent Skills](https://agentskills.io/specification) defines `SKILL.md` with `name` and `description`. This package uses those fields, relative references, and no provider-specific tools. [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills) document distinct discovery paths; symlink installs are a local convention not verified here. Other harnesses need compatible discovery or explicit loading. Rendering capabilities vary.

## Evaluation ideas

These are proposed checks, not completed model experiments:

- Simple question: answer directly; avoid unnecessary artifacts.
- Complex architecture: show accurate components, boundaries, and relationships.
- Novice and expert readers: adapt prerequisites and depth while retaining important limits; preserve the requested language.
- Visual explanations: make essential relationships and values available in text, including outside HTML.
- Benchmark review: preserve units, denominators, failures, and missing runs.
- What-if plan: expose defaults and assumptions; provide reset; label modeled outcomes.
- Temporal process: use persistent keyframes or controlled playback, with narration alternatives.
- Exact JSON request or unavailable renderer: preserve the contract and provide the permitted fallback.
- Conflicting evidence: keep uncertainty and counterevidence beside the conclusion.

Assess whether readers can find the answer, explain a central relationship, identify a limitation, and locate evidence. Measure errors, time, and unsupported-claim detection alongside usability. Correct format selection alone does not establish successful understanding.
