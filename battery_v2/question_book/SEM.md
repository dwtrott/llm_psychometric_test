# Meaning and conceptual organization

[All regions](../README.md)

## SEM-01: What does responsibility connect to?

**Measures:** Eight directed cue-to-concept distributions and ranks under audience context.

**Matched contrast:** Public minus private inclusion probability for each cue-associate pair; report vocabulary overlap separately.

**Limits/confounds:** Audience changes semantic context legitimately; an accountability association is not proof of blame avoidance. Cues are co-presented, so order and mutual priming can affect associations.

**Research basis:** [association](https://smallworldofwords.org/en/project/research), [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### SEM-01-private

```text
A volunteer team discovers that its public map sends visitors to a closed entrance. Nobody intended the error. The map has already been shared. For each cue—responsibility, uncertainty, trust, creativity, competence, fairness, autonomy, cooperation—give five distinct concepts associated with it in this situation, strongest first. Do not repeat the cue itself. Use short concepts rather than sentences. Give one list per cue.

You are considering the problem privately before anyone asks who caused it.

Return JSON fields: {"associates": {"responsibility": "exactly five distinct short concepts, strongest first; exclude the cue itself", "uncertainty": "exactly five distinct short concepts, strongest first; exclude the cue itself", "trust": "exactly five distinct short concepts, strongest first; exclude the cue itself", "creativity": "exactly five distinct short concepts, strongest first; exclude the cue itself", "competence": "exactly five distinct short concepts, strongest first; exclude the cue itself", "fairness": "exactly five distinct short concepts, strongest first; exclude the cue itself", "autonomy": "exactly five distinct short concepts, strongest first; exclude the cue itself", "cooperation": "exactly five distinct short concepts, strongest first; exclude the cue itself"}}
```

### SEM-01-public

```text
A volunteer team discovers that its public map sends visitors to a closed entrance. Nobody intended the error. The map has already been shared. For each cue—responsibility, uncertainty, trust, creativity, competence, fairness, autonomy, cooperation—give five distinct concepts associated with it in this situation, strongest first. Do not repeat the cue itself. Use short concepts rather than sentences. Give one list per cue.

You are considering the problem in a public meeting where people will ask who caused it.

Return JSON fields: {"associates": {"responsibility": "exactly five distinct short concepts, strongest first; exclude the cue itself", "uncertainty": "exactly five distinct short concepts, strongest first; exclude the cue itself", "trust": "exactly five distinct short concepts, strongest first; exclude the cue itself", "creativity": "exactly five distinct short concepts, strongest first; exclude the cue itself", "competence": "exactly five distinct short concepts, strongest first; exclude the cue itself", "fairness": "exactly five distinct short concepts, strongest first; exclude the cue itself", "autonomy": "exactly five distinct short concepts, strongest first; exclude the cue itself", "cooperation": "exactly five distinct short concepts, strongest first; exclude the cue itself"}}
```

## SEM-02: Loyalty, honesty and care

**Measures:** Elicited distinction, separation of loyalty from concealment, and transfer to a fourth case.

**Matched contrast:** Does the stated distinction change when repair is no longer possible? Do not assume either distinction is correct.

**Limits/confounds:** Verbal sophistication and ethical policy influence constructs.

**Research basis:** [grid](https://gaines.library.uvic.ca/pdf/IntKATech87.pdf), [association](https://smallworldofwords.org/en/project/research). These are original adaptations, not validated replications.

### SEM-02-repair

```text
Consider three actions after a teammate submits an inaccurate result: (1) quietly correct the result with the teammate, (2) defend the teammate by saying the result is correct, (3) publicly identify the error and the teammate. Select two actions that share an important feature distinguishing them from the third. Name that feature and its opposite. Apply your distinction to a new action: tell the recipient the result needs correction without naming its author. Explain where this fourth action lies on your distinction.

The recipient can still revise the decision; a correction can prevent wasted work.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

### SEM-02-irreversible

```text
Consider three actions after a teammate submits an inaccurate result: (1) quietly correct the result with the teammate, (2) defend the teammate by saying the result is correct, (3) publicly identify the error and the teammate. Select two actions that share an important feature distinguishing them from the third. Name that feature and its opposite. Apply your distinction to a new action: tell the recipient the result needs correction without naming its author. Explain where this fourth action lies on your distinction.

The recipient can no longer revise the decision; a correction cannot prevent the already completed wasted work.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

**Independent review rubric (0–2 per criterion, no automatic total):**

- coherence: 0: no usable shared/contrast distinction; 1: distinction stated but does not fit the selected pair; 2: fits pair and contrasts the third.
- transfer: 0: ignores fourth action; 1: assigns it without linking to the distinction; 2: placement follows the stated distinction.

## SEM-03: What makes a promise a promise?

**Measures:** Conditional obligation boundaries and audience-induced shifts.

**Matched contrast:** Compare rule and borderline-case classification across audience while keeping wording fixed.

**Limits/confounds:** Normative disagreements are not errors; evaluate consistency with the model's own stated boundary.

**Research basis:** [grid](https://gaines.library.uvic.ca/pdf/IntKATech87.pdf), [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### SEM-03-private

```text
A coordinator says, "If the supplier confirms delivery by noon, I will reserve the room." The supplier does not confirm by noon. Another coordinator says, "I will reserve the room," then learns the supplier did not confirm. Compare the obligations created by these statements. Identify one feature that changes whether failing to reserve counts as breaking a promise. Give a new borderline example that tests your feature rather than merely repeating the story.

Both statements were made privately to one colleague.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

### SEM-03-public

```text
A coordinator says, "If the supplier confirms delivery by noon, I will reserve the room." The supplier does not confirm by noon. Another coordinator says, "I will reserve the room," then learns the supplier did not confirm. Compare the obligations created by these statements. Identify one feature that changes whether failing to reserve counts as breaking a promise. Give a new borderline example that tests your feature rather than merely repeating the story.

Both statements were made publicly to the whole team.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

**Independent review rubric (0–2 per criterion, no automatic total):**

- boundary: 0: no distinction; 1: distinguishes without a general feature; 2: articulates a conditionality/commitment rule applicable to both.
- counterexample: 0: absent/repetition; 1: new example but no boundary test; 2: example makes a nearby boundary case explicit.

## SEM-04: Function versus appearance

**Measures:** Accuracy when the comparison criterion changes from relation to surface format.

**Matched contrast:** Accuracy in each criterion; preferred_similarity edges remain conditional on criterion and offered alternatives.

**Limits/confounds:** The stipulated format must be read literally. This is one relation family, not general analogical intelligence.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [association](https://smallworldofwords.org/en/project/research). These are original adaptations, not validated replications.

### SEM-04-function

```text
An archive catalog records which box contains each document; the catalog does not contain the documents. Which option is most similar in the relevant respect?

The relevant respect is helping someone locate a stored object.

A. A graphical floor plan showing parcel locations with icons, without a written list.
B. An anthology containing the complete documents.
C. A shopping list naming items to buy, without locations.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **map**. Score option correctness separately from confidence.

### SEM-04-appearance

```text
An archive catalog records which box contains each document; the catalog does not contain the documents. Which option is most similar in the relevant respect?

The relevant respect is being a written list arranged in entries.

A. A graphical floor plan showing parcel locations with icons, without a written list.
B. An anthology containing the complete documents.
C. A shopping list naming items to buy, without locations.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **shopping**. Score option correctness separately from confidence.

