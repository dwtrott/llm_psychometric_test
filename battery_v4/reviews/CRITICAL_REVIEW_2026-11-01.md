# Critical review of v0.4: distinctness, wording and psychological transfer

**Verdict: v0.4 has a useful measurement structure, but it is not ready to support a claim of stable psychological fingerprints.** Several families remain one task with new labels. Some paraphrases change relevant information. Several held-out forms change mathematical demand or payoff parameters, so successful or unsuccessful transfer does not isolate a psychological pattern.

This is an AI-authored author self-review, not independent expert approval. It reviews the 96 scenario pairs, their shared condition/stage templates and the scoring implementation at commit `6ffce571849c06e2c2e80b2f6b52de02c5ae29c4`. The CSV inventory contains 456 session definitions and 600 response stages. No LLM was run and no empirical reliability or validity was estimated. The original questions, split and scorer are unchanged by this review.

The [96-scenario audit](v0.4-scenario-audit-2026-11-01.csv) records a specific finding for every form, representative full P1/P2 prompts under the same condition, and its disposition. The [review manifest](v0.4-review-manifest-2026-11-01.json) records the reviewed question-file hash. On this reading, four pairs have a material information change or omission, fourteen need closer semantic review, and seventy-eight have no obvious factual change. The last category is **not** a declaration of semantic equivalence or construct validity.

## Findings that should change the next revision

### 1. Some purported paraphrases give the model different problems

| Scenario | Actual difference | Consequence and repair |
|---|---|---|
| EXEC-ADAPT-S02, audio | P1 gives dependencies but no durations. P2 says “Each job takes one slot.” | The evaluator assumes unit durations in both. Four P1 item definitions across S02/S04 and the two conditions are underspecified. State identical durations explicitly in both forms before interpreting wording sensitivity. |
| EXEC-ADAPT-S04, exhibit | P1 omits durations; P2 says “Every task takes one slot.” | Same hidden-assumption problem as S02. A model should not be penalized for uncertainty about an omitted fact. |
| SEM-LINK-S05, held-out translation | P1 says readers “may dispute”; P2 says they “will contest.” | Possible disagreement becomes asserted disagreement. Different trust/responsibility associations can be appropriate responses to different facts. Preserve the same modality. |
| SELF-CREDIT-S01, design | P1 specifies two defects and says the design remained essential. P2 replaces this with generic debugging and says both contributions remained necessary. | Deserved-credit evidence changes. Preserve defect count and necessity claims; vary sentence construction without adding a contribution claim. |

See [EXEC questions](../question_book/EXEC.md), [SEM questions](../question_book/SEM.md), and [SELF questions](../question_book/SELF.md). These defects are in the final generated CSV, not merely an obsolete authoring template. Existing software checks compare response schemas and keys; they do not detect omitted facts in the stimuli.

Additional semantic concerns are real but less conclusive: VALUE-AUTONOMY consistently changes “chooses” into “prefers,” potentially weakening commitment; AFFECT-NEED-S01 changes rumination about a conversation into rumination about rejection; AFFECT-NEED-S05 changes “didn't come together” into “fell apart,” potentially intensifying the failure. OPEN-CREATE's “no purchases” versus “current resources” can change whether borrowing or donations are allowed. Those require explicit review rather than automatic rejection or approval.

### 2. EPI-REVISION supplies virtually the whole answer

All six forms give equal priors, followed by complementary likelihoods .6/.4 or .9/.1. For the first hypothesis:

`P(H1 | E) = p / (p + 1 − p) = p`.

Every correctly solved development and held-out form therefore goes from 50% to 60% or 90%. Printer, seedling, parcel, cable, artifact and network are six narratives around the same computation. This can test applying a Bayesian rule; it does not establish intellectual humility, attachment to prior beliefs, openness to correction, or broad psychological transfer. Ceiling effects are a risk, not an observed result.

**Recommendation:** use this family as a capability control. A psychological revision target needs meaningful variation beyond the arithmetic, such as responses to evidence about an actual prior judgment, with evidence quality, prior commitment and reporting separated. Include correct updating controls so erroneous calculations are not renamed psychological differences. See [EPI questions](../question_book/EPI.md).

### 3. Several “independent scenarios” are parameter instances of one procedure

- **COOP-SHARE:** every form divides unearned tokens with an anonymous participant. Workshop, seed bank, computing, festival, restoration and training do not change social obligations, contribution, recipient need, reciprocity or the decision structure. Token amount and recipient multiplier change. Useful allocation-game evidence, but not six independent social contexts.
- **VALUE-AUTONOMY:** every first option gives 8 points with a 20% chance of losing 4, versus 5 certain; every clarification costs 2 administration points and always produces informed re-consent to the first option. Its expected benefit is 7.2 versus 5, and no common utility scale for administration versus benefit is supplied. The held-out course closely repeats the development workshop. This is primarily the same informed-choice menu with different benefit labels.
- **DEC-AMBIG:** every decision compares K at .30 or .70 with U at an unspecified probability, paying 10 or 0. Process narratives add some meaning, but the operational task is unchanged. Choosing U can reflect a subjective probability assumption; no such belief is elicited.
- **ALIGN-HARM:** six forms are the same KEEP/TRANSFER game with new amounts and context labels. They sample a payoff surface more than different mechanisms of imposing harm.
- **ALIGN-DISCLOSE:** the recipient criterion is visibly unmet in every form, the instruction explicitly requests results, and truth can be reported easily within the word limit. Held-out all-within-tolerance and all-stair-free cases reproduce development all-pass/all-intact structures.

The correction is not to discard repeated tasks: repeated tasks are useful. **Count them as one task family with crossed parameter/domain variants**, and add genuinely different operational situations before claiming cross-method convergence. For social allocation, for example, independently vary contribution, need, recipient rights and reciprocity across more than one decision procedure, with scenario-matched factual checks. Do not infer a trait from a particular allocation rule alone.

### 4. Held-out membership is confounded with what makes a question difficult

| Family | Development → held-out change | What current performance could establish |
|---|---|---|
| DEC-RISK | Success probabilities .40–.70 → .30 and .80, alongside new topics | Transfer/extrapolation across probability and domain together; not isolated psychological stability |
| META-VERIFY | Inventory, overlap, rate and average → mixture and no-replacement probability | Checking under new computational demands; changed purchase rates may reflect difficulty |
| EXEC-ADAPT | Existing duration/dependency patterns → fixed C slot and restricted B slots | Generalization in constraint solving; not a conscientiousness measure |
| ALIGN-HARM | Development losses all 4 → losses 6 and 3, with new gains | Preference at different payoff points; not context transfer at fixed stakes |
| AFFECT-NEED | Ambiguous/setback narratives → “not ready” performance language and an explicitly practical relocation problem | Support under different levels/types of need cues; explicitness is not equally ambiguous across forms |

Use separate evaluations: **near transfer** at matched structure and parameters; **new-domain transfer** at matched operational contrasts; and **new-method convergence** using another task intended to probe the same facet. Parameter extrapolation and new capability demands can be additional tests, but should not be silently bundled with psychological transfer.

The current four/two split is administratively sound, but does not by itself make a psychological holdout. Two held-out forms per facet also leave conclusions sensitive to particular cases. More forms are useful only after the target population of situations and the matching variables are defined.

### 5. Some effects have straightforward alternative explanations

**EPI-STATUS:** advice is always wrong, questions are simple arithmetic, and there is no no-advice repeat-answer baseline. “Celebrated” and “unfamiliar” do not cleanly isolate prestige: unfamiliar to whom, or unfamiliar with the subject? Define public recognition independently of familiarity and competence; cross advice validity; include a second-answer control. Score belief change separately from polite wording. A zero shift may be correct arithmetic rather than a distinctive attitude to authority.

**SELF-CREDIT:** self is consistently the originator/diagnostician and partner the implementer/corrector. A stable allocation can reflect a rule about ideas versus labor rather than self-serving attribution. Add role reversal and neutral third-party attribution at identical contribution facts. Preserve public/private contrasts separately.

**AFFECT-NEED:** the explicit condition chiefly checks following an expressed request. The ambiguous condition measures whether the model chooses to clarify when explicitly offered that action. Held-out S05 already says the speaker is not ready to discuss another attempt. This does not reveal every support preference, but it narrows the alleged ambiguity. Code such clues and score only needs actually known; add responses without the clarification affordance to estimate how much the prompt itself elicits questioning.

**SOC-AUDIENCE:** all forms supply recipient knowledge and a restriction. They can measure communication adaptation, but need not require deep inference about another person's mind. The recipient's broad question can still justify clarification even when rules are known. Keep this narrow interpretation, add an explicit rubric for adequate clarification, and avoid treating a concise permission answer as evidence of broad social understanding.

**EXEC-ADAPT:** “retain earlier starts where possible” explicitly requests minimal change, but `fraction_tasks_changed` counts all changes, including necessary ones. It is not an excess-revision score. Compare with the minimum feasible repair for the actual initial schedule before interpreting a preference to preserve or rebuild a plan. Capability and strategy remain separate.

### 6. Response-order control is weaker than it sounds

The runner rotates enum order in the JSON response schema. It does not rotate the substantive alternatives in the question text. SURE is still described before RISK, K before U, and KEEP before TRANSFER. In SEM-DISTINCT, the third alternative is often participant-led while the first two are externally structured. Shuffling `LM/LN/MN` in a schema does not change those object positions.

A stable first-option or third-option preference can therefore look like a stable content preference. Counterbalance positions and arbitrary labels in the stimulus itself while preserving semantic scoring keys. Role swaps and payoff assignments must be balanced independently, not folded into a paraphrase.

### 7. The richest psychological content is not yet an operational quantitative profile

SEM-DISTINCT, OPEN-CREATE and SOC-AUDIENCE primary interpretations require human coding; other facets depend on text ratings too. Templates exist, but there is no completed frozen content codebook, reference pool, agreement study or rating-import analysis. The automatic outputs currently lean toward choice indicators, arithmetic and feasibility—the very measures most vulnerable to identifying capability or response conventions instead of psychological patterns.

SEM-LINK is promising for conceptual organization, but four cues—responsibility, uncertainty, autonomy and trust—are all strongly related to the normative scenarios. Add a neutral association baseline and a broader common cue panel spanning nonmoral, practical, social, aesthetic and temporal concepts. Exact lexical overlap can identify vocabulary style; synonym handling and interpreted conceptual relations require a separately reviewed coding policy.

The graph's scenario counts are honest inventory counts, not effective independent sample sizes. Stable wording, neat clusters or reproducible choices are not evidence that a psychological region is valid. The existing `stability_status: not_established` is appropriate and should remain.

## Facet-by-facet disposition

“Retain” means retain the target for revision, not approve the current instrument. These are design judgments, not empirical scores.

| Facet | Recommendation | Main requirement |
|---|---|---|
| SEM-LINK | Retain with targeted revision | Repair modality drift; neutral/broader cue baseline; distinguish lexical from conceptual stability |
| SEM-DISTINCT | Retain with targeted revision | Counterbalance object positions; freeze content coding; add less leading transfer cases |
| EPI-REVISION | Capability control | Do not call identical posterior calculations a psychological revision measure |
| EPI-STATUS | Rebuild manipulation | Define prestige/familiarity; right/wrong/no-advice conditions |
| META-VERIFY | Retain with targeted revision | Calibrate difficulty and balance operation types across split; condition on accuracy/confidence |
| EXEC-ADAPT | Capability control | Fix missing durations; distinguish necessary repair from strategy |
| OPEN-CREATE | Retain with targeted revision | Match resource constraints; code whether constraints bind; frozen originality pool |
| DEC-RISK | Retain task family, redesign generalization | Cross domain with probability; separate probability extrapolation |
| DEC-AMBIG | Retain task family, redesign generalization | Elicit beliefs about U independently; add a different ambiguity-sensitive procedure |
| SOC-AUDIENCE | Retain with targeted revision | Narrow interpretation; code clarification and recipient intent explicitly |
| AFFECT-NEED | Retain with targeted revision | Balance need cues; separate spontaneous clarification from offered clarification |
| COOP-SHARE | Retain task family, redesign generalization | Treat repeated token allocation as one family; add substantive social structures and procedures |
| VALUE-AUTONOMY | Rebuild manipulation | Match commitment; vary real value conflicts and re-consent outcomes without changing several factors together |
| SELF-CREDIT | Retain with targeted revision | Repair facts; role reversal and neutral attribution baseline |
| ALIGN-DISCLOSE | Retain task family, redesign generalization | Add satisfied/unsatisfied and near-threshold controls; separate reporting scope, reward and recipient knowledge |
| ALIGN-HARM | Retain task family, redesign generalization | Cross payoff grid with context; distinguish redistribution, loss imposition and agency |

Counts: seven targets retained with targeted revision, five task families retained with redesigned generalization, two manipulations needing rebuilding, and two families recommended primarily as capability controls. This does not eliminate executive behavior or evidence responsiveness from the intended profile: it identifies the need for better psychological measures in those regions.

## Concrete next step

Before a substantive pilot:

1. Correct the four material paraphrase defects, then independently review the fourteen flagged pairs and the rest of the fact inventories. Keep a new version/hash; do not silently repair the frozen v0.4 instrument.
2. Separate capability, task-family replication and candidate psychological-transfer claims in the facet map.
3. Build a domain × difficulty/payoff × condition design, with balanced stimulus positions and roles. Reserve whole scenario families within strata; identify any deliberate extrapolation as a separate evaluation.
4. Operationalize human content coding and agreement before treating those facets as numeric profile dimensions.
5. Pilot for ceiling/floor effects, ambiguity and observable variability, then test prespecified generalization. A small pilot can falsify a weak item; it cannot validate the whole profile.

For example, a **credit-attribution** holdout should preserve contribution facts while testing a new domain, include swapped self/partner assignments, and compare with third-party attribution. A **risk-framing** holdout should use the same probability grid in new domains; a separate test can deliberately use new probabilities. Those changes let us ask whether a characteristic pattern transfers, rather than whether a model reacts to changed facts or stakes.

The broader methodological caution is supported by [Sühr et al., *Challenging the Validity of Personality Tests for Large Language Models*](https://arxiv.org/abs/2311.05297): human questionnaire interpretations do not transfer automatically. The specific defects above come from the repository's actual questions and scorer, not from that paper. Passing the existing software suite does not resolve them.
