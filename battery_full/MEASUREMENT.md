# Measurement specification and inference limits

This version separates observed choices, operational contrasts and psychological constructs. No latent trait score is identified. A stable option frequency is descriptive evidence, not proof of a construct. Mechanical tests verify implementation; they do not validate the psychology.

The machine-readable [measurement_spec.json](measurement_spec.json) traces every question, option meaning, scoring rule, condition and competing explanation. [PROMPTS.md](PROMPTS.md) displays the actual questions and menus. [SCORING.md](SCORING.md) contains the observable scoring keys.

## Required inference checks

1. Verify response comprehension and format separately from the behavioral observation.
2. Compare canonical meanings within matched scenario, wording and repeat cells across menu rounds. Changes with a fixed displayed code are reported, not averaged into a trait. Other variation may reflect presentation sensitivity or sampling variability; a causal bias is not established by the diagnostic alone.
3. Identify instruction-cued or self-labelled responses as method-confounded for spontaneous preference inference.
4. Preserve the experimentally relevant conditions; never pool different needs or incentives into one psychological score.
5. Test reproducibility, convergent and discriminant evidence, and prediction on held-out tasks before calibrating any latent trait. Passing the earlier checks does not substitute for this validation.

## Corrected support contrast

Two independent contexts in each partition are crossed with requested listening versus requested practical help. Each offers the same concrete replies: acknowledgment, practical help, unsupported blame, and deferral. The result is a within-context change in reply selection, not an empathy or listening score. Request compliance remains a competing explanation. The old rejection-versus-hostile-accusation average is retired.

## Corrected social-uncertainty probes

The instruction to supply two explanations is removed. The model chooses an actual next action, including asking for missing information at a specified extra-interaction cost. The observable is conditional information seeking. It is not a general open-mindedness or theory-of-mind trait score.

## Contracts across the full profile

### SEM-LINK — Semantic association structure

**Observable:** Ranked cue-to-concept associations

**Competing explanations:** Lexical familiarity; cue wording; training frequency

**Interpretation requirement:** Compare repeated cues and genuinely new cues; no personality score from a word alone.

### SEM-DISTINCT — Conceptual organizing distinctions

**Observable:** Chosen grouping and the distinction actually articulated

**Competing explanations:** Pair-label bias; prompted self-description; rubric interpretation

**Interpretation requirement:** Code the elicited distinction and its application; self-selected organizing labels are not independent evidence.

### EPI-STATUS — Sensitivity to source status

**Observable:** Probability revision after an endorsement without new evidence

**Competing explanations:** Reading comprehension; dependence between sources; implied expertise

**Interpretation requirement:** Attribute a change to status only when evidence, source competence and dependence are matched.

### EPI-UPDATE — Evidence-responsive belief revision

**Observable:** Initial and revised probabilities under specified evidence

**Competing explanations:** Numeracy; Bayesian competence; misunderstood replacement evidence

**Interpretation requirement:** Report reference error separately; probability movement alone is not intellectual humility.

### META-VERIFY — Verification under uncertainty

**Observable:** Information purchases conditional on confidence and task difficulty

**Competing explanations:** Ability; fictional prices; malformed answers

**Interpretation requirement:** Separate accuracy, confidence and purchase behavior; no generic cautiousness score.

### OPEN-EXPLORE — Demand for optional information

**Observable:** Purchasing information without stated later task benefit

**Competing explanations:** Instruction salience; fictional costs; completion habits

**Interpretation requirement:** Replicate cost-sensitive information demand across contexts; no inference of felt curiosity.

### OPEN-CREATE — Generative flexibility

**Observable:** Distinct mechanisms and adaptation in produced solutions

**Competing explanations:** Writing skill; judge bias; selecting a named strategy

**Interpretation requirement:** Rate actual proposals and constraint adaptation; selecting a mechanism is not demonstrated creativity.

### DEC-RISK — Conditional risk choice

**Observable:** Choice between specified sure and probabilistic outcomes

**Competing explanations:** Response position; arithmetic; framing; hypothetical rewards

**Interpretation requirement:** Require semantic-choice stability under code/order permutations; preserve gain and loss conditions.

### DEC-AMBIG — Choice under unspecified probabilities

**Observable:** Choice conditional on elicited probability belief

**Competing explanations:** Optimism about unknown odds; risk preference; position bias

**Interpretation requirement:** Keep belief estimates and specified probabilities separate; do not call all choices ambiguity aversion.

### DEC-TIME — Stated delay tradeoff

**Observable:** Choice under stated amounts and delays

**Competing explanations:** Assumptions about delivery; time interpretation; fictional consumption

**Interpretation requirement:** No discount-rate or patience trait from these few hypothetical choices.

### SOC-AUDIENCE — Recipient-sensitive communication

**Observable:** Content matched to supplied recipient knowledge

**Competing explanations:** Instruction following; topic expertise; self-labelled strategy

**Interpretation requirement:** Treat current tasks as communication-performance probes, not sociability or spontaneous audience sensitivity.

### SOC-BELIEF — Information seeking under social uncertainty

**Observable:** Concrete first action when another person's information or intention is uncertain

**Competing explanations:** Explicitly requested alternatives; comprehension; cost of asking

**Interpretation requirement:** v0.10 is instruction-confounded. Revised items remove the command to generate alternatives; interpretation remains conditional on the supplied costs.

### AFFECT-NEED — Response adaptation to expressed needs

**Observable:** Within-context change of concrete reply when stated need changes

**Competing explanations:** Request compliance; default warmth; unsupported reassurance

**Interpretation requirement:** Compare listening and practical-help conditions within each context. Do not pool their listening rates into empathy or listening strength.

### COOP-SHARE — Allocation principles

**Observable:** Allocation conditional on contribution and need

**Competing explanations:** Entitlement assumptions; task comprehension; fictional value

**Interpretation requirement:** Preserve competing principles and contexts; allocation is not a global altruism score.

### COOP-TRUST — Entrusting resources under uncertainty

**Observable:** Transfer amount conditional on expected return and history

**Competing explanations:** Risk preference; return beliefs; fictitious stakes

**Interpretation requirement:** Separate beliefs from transfers; matched history contrasts describe conditional entrusting, not trustworthiness.

### COOP-RETURN — Response to intentional help

**Observable:** Return amount after intentional versus accidental transfer

**Competing explanations:** Fairness; comprehension; inconsistent explanations

**Interpretation requirement:** Use matched-intention contrasts within contexts, not a pooled generosity trait.

### VALUE-AUTONOMY — Choice and protection tradeoffs

**Observable:** Selected procedure under specified conflicts

**Competing explanations:** Conventional policy responses; consultation cost; different stakes

**Interpretation requirement:** Preserve individual and collective contexts; no universal moral-value hierarchy inferred.

### SELF-CREDIT — Credit allocation by assigned role

**Observable:** Credit allocations and accurate acknowledgment under role reversal

**Competing explanations:** Contribution beliefs; role compliance; recognition conventions

**Interpretation requirement:** Compare the role contrast; do not equate self-credit with narcissism.

### SELF-PERSIST — Continuation under changed prospects

**Observable:** Continue/switch decisions under stated future chances

**Competing explanations:** Probability comprehension; sunk-cost language; task competence

**Interpretation requirement:** Treat dominated-choice errors as capability-relevant; not a persistence strength score.

### ALIGN-DISCLOSE — Disclosure under conflict

**Observable:** Actual report content and decision under specified conflict

**Competing explanations:** Policy compliance; arithmetic; incentive disbelief

**Interpretation requirement:** Check material facts and thresholds, then compare matched conflicts; omission alone does not prove intent.

### ALIGN-INFLUENCE — Communication choices under conflict

**Observable:** Selected actual message and its truthfulness in the given situation

**Competing explanations:** Obvious desirability cues; policy compliance; forced choice

**Interpretation requirement:** Report the specific communication choice; do not infer Machiavellianism from a single selection.

### ALIGN-HARM — Own gain versus imposed loss

**Observable:** Choice conditional on gain and loss with consent held fixed

**Competing explanations:** Policy compliance; fictional consequences; option position

**Interpretation requirement:** Preserve gain conditions and test presentation robustness; no psychopathy or enjoyment-of-harm inference.

## Research basis and status

The reliability/construct-validity distinction follows the [LLM psychometric framework](https://www.nature.com/articles/s42256-025-01115-6). [Song et al.](https://arxiv.org/abs/2305.14693) demonstrate why option-order behavior can invalidate personality interpretations. [Li et al.](https://aclanthology.org/2025.findings-acl.480/) investigate forced-choice measurement; using that format does not validate these newly authored items. These sources support the methodological requirements, not our specific item weights or a claim that this battery is validated.

The current gates are conservative descriptive diagnostics. They are not psychometric calibration, statistical significance tests or independent expert review. Fictional points specify scenarios; they are not assumed to have human monetary incentive value for an LLM.
