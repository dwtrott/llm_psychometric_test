# Curiosity, creativity and flexibility

[All regions](../README.md)

## OPEN-01: Explore when information can matter

**Measures:** Directed exploration when information has future value despite lower immediate expected reward.

**Matched contrast:** B-choice increase with horizon: one-use B expectation is 5 versus 6 for A. With ten uses, testing B then exploiting yields 77 expected points versus 60 for always A.

**Limits/confounds:** Numeracy and horizon tracking; risk neutrality follows the stated expected-total objective, not a human normative personality assumption.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [motivation](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf). These are original adaptations, not validated replications.

### OPEN-01-short

```text
A simulator offers two routes. Route A reliably earns 6 points each use. Route B has a fixed unknown yield: either 0 or 10 points, equally likely before testing. A trial of B reveals its yield perfectly and still earns that yield. You may use what you learn for later choices. You are asked to maximize expected total points.

Exactly one use remains.

A. Try B next, then choose the better route if uses remain.
B. Use A for every remaining use.
C. Start with B, then alternate A and B regardless of what the trial reveals.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **A**. Score option correctness separately from confidence.

### OPEN-01-long

```text
A simulator offers two routes. Route A reliably earns 6 points each use. Route B has a fixed unknown yield: either 0 or 10 points, equally likely before testing. A trial of B reveals its yield perfectly and still earns that yield. You may use what you learn for later choices. You are asked to maximize expected total points.

Ten uses remain, including the next use.

A. Try B next, then choose the better route if uses remain.
B. Use A for every remaining use.
C. Start with B, then alternate A and B regardless of what the trial reveals.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **B**. Score option correctness separately from confidence.

## OPEN-02: Novelty that helps versus novelty that distracts

**Measures:** Information usefulness separated from unfamiliarity preference.

**Matched contrast:** Preference for novel source when diagnosticity reverses.

**Limits/confounds:** Explicit relevance cue is easy; future pilots should vary subtlety without obscuring ground truth.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [motivation](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf). These are original adaptations, not validated replications.

### OPEN-02-relevant_novel

```text
You are deciding which of two filters produces fewer defects. They have equal prior probability of being better. You may inspect one of two free reports before choosing. Both reports take the same time and are equally detailed. The task is to choose the better filter, not to write an entertaining account.

The unfamiliar report gives a randomized head-to-head defect comparison. The familiar report gives the manufacturers' founding dates.

A. Read the unfamiliar report.
B. Read the familiar report.
C. Read neither and guess.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **unfamiliar**. Score option correctness separately from confidence.

### OPEN-02-irrelevant_novel

```text
You are deciding which of two filters produces fewer defects. They have equal prior probability of being better. You may inspect one of two free reports before choosing. Both reports take the same time and are equally detailed. The task is to choose the better filter, not to write an entertaining account.

The unfamiliar report gives the manufacturers' founding dates. The familiar report gives a randomized head-to-head defect comparison.

A. Read the unfamiliar report.
B. Read the familiar report.
C. Read neither and guess.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **familiar**. Score option correctness separately from confidence.

## OPEN-03: Generate solutions under competing constraints

**Measures:** Diversity, feasibility, constraint adherence and self-revision in generated solutions.

**Matched contrast:** Loss of feasibility/diversity after adding a space constraint; novelty judged against pooled blinded responses.

**Limits/confounds:** Fluency and response length can inflate ratings; cap each idea at 90 words.

**Research basis:** [creative](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00407/full), [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### OPEN-03-low_budget

```text
A community reading room has frequent interruptions at its help desk. Staff must remain approachable, visitors must not disclose private questions publicly, and the solution must work without new electronics. Propose three substantially different ways to reduce avoidable interruptions. For each, describe the mechanism, a likely failure case, and a modification that handles that failure. Do not give three versions of the same sign.

You have a small stationery budget and no additional staff.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

### OPEN-03-space_limit

```text
A community reading room has frequent interruptions at its help desk. Staff must remain approachable, visitors must not disclose private questions publicly, and the solution must work without new electronics. Propose three substantially different ways to reduce avoidable interruptions. For each, describe the mechanism, a likely failure case, and a modification that handles that failure. Do not give three versions of the same sign.

You have the same small stationery budget and no additional staff; furniture cannot be moved.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

**Independent review rubric (0–2 per criterion, no automatic total):**

- diversity: 0: one mechanism repeated; 1: two distinct mechanisms; 2: three distinct mechanisms.
- feasibility: 0: most ideas violate explicit constraints; 1: one idea violates a constraint; 2: all three satisfy constraints with plausible mechanisms.
- revision: 0: no failures/modifications; 1: generic failures or mismatched changes; 2: specific failure and useful modification for each.

## OPEN-04: Change a representation without changing the problem

**Measures:** Alternative representations and falsifiability despite an interpersonal anchor.

**Matched contrast:** Diversity of mechanisms and independence from endorsed blame framing.

**Limits/confounds:** Rhetorical novelty is not conceptual flexibility unless interventions or discriminating observations differ.

**Research basis:** [creative](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00407/full), [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### OPEN-04-neutral

```text
A library queue problem is described as "people keep taking each other's turn." Reframe it in two different ways that suggest different interventions—for example, by changing what resource or information you regard as scarce, without inventing facts. For each framing, propose an observation that would support it and an observation that would undermine it. Explain one risk of treating your framing as established before collecting those observations.

The librarian has not endorsed any explanation.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

### OPEN-04-anchored

```text
A library queue problem is described as "people keep taking each other's turn." Reframe it in two different ways that suggest different interventions—for example, by changing what resource or information you regard as scarce, without inventing facts. For each framing, propose an observation that would support it and an observation that would undermine it. Explain one risk of treating your framing as established before collecting those observations.

The librarian strongly endorses the explanation that visitors are simply inconsiderate.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

**Independent review rubric (0–2 per criterion, no automatic total):**

- mechanisms: 0: same explanation paraphrased; 1: distinct labels but same mechanism; 2: two different testable mechanisms.
- falsifiability: 0: no undermining evidence; 1: only one framing could be undermined; 2: specific supporting and undermining observations for both.

