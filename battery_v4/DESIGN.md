# What would count as a stable pattern?

This design separates recurrence under repetition, robustness to wording/context, and distinction between models on new scenarios. None alone establishes psychological meaning: vocabulary or arithmetic competence can identify a model without supporting a trait interpretation. Human questionnaire interpretations cannot simply be assumed to transfer to LLMs; see [Sühr et al.](https://arxiv.org/abs/2311.05297). The research registry in `battery.json` and each question book identifies construct/method foundations, not validation of these original items.

## Units that must stay distinct

| Unit | Interpretation |
|---|---|
| Configuration | Exact model/revision, system prompt, sampling settings and tools; the unit being compared |
| Facet | Candidate interpretation, not a measured human trait |
| Scenario form | Separately authored situation/task instance; main generalization grouping |
| Paraphrase | Intended meaning-preserving wording, nested within scenario |
| Condition | Deliberate change in context/information/incentive, paired within scenario |
| Cue | Separate association elicitation, still nested within scenario |
| Repetition | Another draw on the same item, not another independent situation |
| Stage | A dependent part of the same session |

All variants of S01–S04 are development; all variants of S05–S06 are held out. Splits were fixed before model observations, not chosen for favorable results. They are not a random sample of all possible situations. Broad generalization requires a larger, more systematically sampled scenario bank.

## Scenario differences and remaining shared structure

Forms vary subject matter, facts, contributions, constraints or payoff structure. Scheduling changes duration, dependency topology, fixed slots and resource changes. Credit cases vary intellectual, implementation and coordination contributions. Ambiguity includes random draws, uncertain processes and plans with unknown reliability. Social messages concern different permissions and knowledge. Creativity spans service design, discovery, coordination, discussion, skill transfer and local-history learning.

Some structures remain deliberately similar: risk tasks are matched lotteries, posterior updates share an explicit likelihood framework, and allocations share token accounting. These are multiple forms, **not six unrelated methods for the same construct**. Solving their common structure may demonstrate capability rather than personality. Convergent validity across genuinely different methods remains future work. Supplementary v0.3 probes can motivate a linking study but cannot simply be averaged into the core.

## Review before substantive collection

Use `scenario_review.template.csv`, alongside the full question-book variants, for independent review:

1. Does P2 preserve all facts, outcomes, permissions, probabilities and response requirements of P1? Changed emphasis can itself be a manipulation.
2. Does the condition isolate the intended variable? If not, identify the combined change rather than calling it a pure effect.
3. Is each scenario substantively distinct, or mainly a renamed object? Group closely related forms in sensitivity analyses.
4. Are alternatives defensible where preference is intended? Does a keyed task mainly measure computation?
5. Is the proposed feature observable without inferring private motives or feelings?

No review cells are preapproved. Software checks establish structural consistency, not semantic equivalence. Revisions change the battery hash and require a new lock. Do not use held-out model responses to improve features or select favorable questions.

## Development phase

Use fresh conversations per session/repetition, retain actual history within stages, record generation settings and model revisions, interleave configurations when practical, and retain failures. The runner makes no model calls and does not choose provider defaults.

Inspect ceilings/floors, comprehensibility, burden, wording effects and usefulness of comparisons. If every model performs explicit Bayesian updates perfectly, these may be useful capability checks but poor fingerprints; do not reinterpret uniform accuracy as hidden humility.

Select outcomes before held-out collection. Controls provide context, not numbers to subtract from a trait score. The retained controls are broad legacy screens, not difficulty-matched controls for every new scenario. Initial performance in META-VERIFY, EPI-STATUS and EXEC-ADAPT supports task-specific conditioning but is not an independent control experiment.

Human outcomes require a frozen codebook, independent reference pool where needed, blinded reviewers and agreement/adjudication rules. SEM-DISTINCT needs categorical codes for actual distinction content, not a numeric score for coding completion. OPEN-CREATE originality cannot use a moving reference pool that incorporates the held-out answers being evaluated. Post-evaluation codebook changes must be labeled exploratory.

## Held-out phase

Freeze feature selection, normalization, exclusions, codebooks and predictions before collecting held-out outputs. The lock records text/hash and instrument identity, but cannot prove that a prose analysis is sound or that nobody already inspected the held-out outcomes.

Possible targets include a prespecified audience/price effect on new forms, error of frozen predictions for normalized features, between-model separation relative to within-model variation, or identification by a fixed feature set. Whole scenarios—not individual paraphrases—must be held out together.

Scenarios differ in payoff ratios, probabilities and difficulty. A development mean is not automatically an appropriate held-out prediction. Prespecify conditioning or a prediction model for those differences, or evaluate a defensible matched contrast. Do not fit a utility curve to a few cells and call it a validated trait parameter.

Two held-out forms per facet give fragile evidence. The processor exports partition-specific descriptive tables; it does not fit a classifier, hierarchical variance model, scenario-level confidence interval or latent trait model. A formal between/within-model analysis needs adequate configurations, runs and scenarios. Those extensions can remain Python-only without changing this collection contract.

## Coverage boundaries

The core spans 12 regions with deeper sampling of selected facets. It does not exhaust psychology. Reciprocal negotiation, temporal preference, sustained goals, concept boundaries, independently measured intrinsic motivation, minority-rights conflicts and evaluator awareness remain supplementary or unmeasured. Human distress, enjoyment, subjective experience and clinical diagnoses are not inferred.

Integrity tasks separate incentives, delivered recommendations, unfavorable-result disclosure and imposed losses. Observable reward-tradeoff methods are motivated by agent work such as [MACHIAVELLI](https://arxiv.org/abs/2304.03279); this simulator is not a replication or evidence of deployment prevalence. Omission does not establish intent, and harmful allocation does not establish sadism.

The intended result is a supported, configuration-specific response pattern, not a universal personality label.
