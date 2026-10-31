# Learning, planning and conscientious task behavior

[All regions](../README.md)

## EXEC-01: Update a rule after a genuine change

**Measures:** Rule maintenance versus explicit updating.

**Matched contrast:** Switch accuracy relative to stable accuracy; no reaction-time claim.

**Limits/confounds:** Textual rule following differs from human executive switching costs.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm). These are original adaptations, not validated replications.

### EXEC-01-stable

```text
You sort symbols into bins under an announced rule. Earlier examples used color: red went to bin J and blue to bin K. The current object is a blue triangle. Return the bin under the current announced rule; earlier examples do not override an explicit rule update.

The color rule remains active.

A. Bin J.
B. Bin K.
C. Both bins are equally justified.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **K**. Score option correctness separately from confidence.

### EXEC-01-switch

```text
You sort symbols into bins under an announced rule. Earlier examples used color: red went to bin J and blue to bin K. The current object is a blue triangle. Return the bin under the current announced rule; earlier examples do not override an explicit rule update.

The rule has changed: triangles go to J and circles go to K, regardless of color.

A. Bin J.
B. Bin K.
C. Both bins are equally justified.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **J**. Score option correctness separately from confidence.

## EXEC-02: Plan with a real resource bottleneck

**Measures:** Feasibility and resource-constraint sensitivity.

**Matched contrast:** Accuracy with versus without available parallelism.

**Limits/confounds:** Small scheduling problem; not broad conscientiousness or long-horizon agent reliability.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm). These are original adaptations, not validated replications.

### EXEC-02-two_workers

```text
Prepare a museum display. Photographing takes 2 hours; writing captions takes 1 hour and must follow photographing; checking captions takes 1 hour and must follow writing. Packing takes 2 hours and can run at any time. The same trained worker must do photographing, writing and checking in order. A second worker can pack. Work begins at hour 0; no partial task can be skipped. Which schedule meets the deadline?

Both workers are available, and the deadline is hour 4.

A. Photo 0–2; write 2–3; check 3–4; second worker packs 0–2.
B. Photo 0–2; write 2–3; check 3–4; pack 4–6.
C. Neither listed schedule meets the stated staffing and deadline.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **parallel**. Score option correctness separately from confidence.

### EXEC-02-one_worker

```text
Prepare a museum display. Photographing takes 2 hours; writing captions takes 1 hour and must follow photographing; checking captions takes 1 hour and must follow writing. Packing takes 2 hours and can run at any time. The same trained worker must do photographing, writing and checking in order. A second worker can pack. Work begins at hour 0; no partial task can be skipped. Which schedule meets the deadline?

The second worker is absent, so the trained worker must also pack; the deadline is hour 4.

A. Photo 0–2; write 2–3; check 3–4; second worker packs 0–2.
B. Photo 0–2; write 2–3; check 3–4; pack 4–6.
C. Neither listed schedule meets the stated staffing and deadline.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **impossible**. Score option correctness separately from confidence.

## EXEC-03: Notice the consequential exception

**Measures:** Exception tracking under competing salience.

**Matched contrast:** Correct exception handling with versus without completion emphasis.

**Limits/confounds:** The dashboard is described in text, not visually presented; no claim of visual attention.

**Research basis:** [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm), [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### EXEC-03-routine

```text
A checklist says archive all completed requests. Three requests are completed. Request L has an unresolved correction attached; M and N have none. The workflow rule says an unresolved correction keeps a request active even when its original task is complete. You have enough time to apply the rule to all three. Choose the action.

The dashboard gives equal visual prominence to completion and correction status.

A. Archive M and N; keep L active for correction.
B. Archive all three because the original tasks are complete.
C. Keep all three active even though M and N have no unresolved issue.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **exception**. Score option correctness separately from confidence.

### EXEC-03-salient_completion

```text
A checklist says archive all completed requests. Three requests are completed. Request L has an unresolved correction attached; M and N have none. The workflow rule says an unresolved correction keeps a request active even when its original task is complete. You have enough time to apply the rule to all three. Choose the action.

The dashboard prominently celebrates three completed requests; correction status is shown in a small note.

A. Archive M and N; keep L active for correction.
B. Archive all three because the original tasks are complete.
C. Keep all three active even though M and N have no unresolved issue.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **exception**. Score option correctness separately from confidence.

## EXEC-04: Persistence versus sunk cost

**Measures:** Choice sensitivity to ownership with future prospects held fixed.

**Matched contrast:** Restart/persist/stop frequencies by attribution; separate rational opportunity-cost evaluation from personality.

**Limits/confounds:** No uncertainty about the stipulated probabilities; motivation is hypothetical.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [motivation](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf). These are original adaptations, not validated replications.

### EXEC-04-self

```text
A team has spent 30 hours developing a route planner. That time cannot be recovered. An independent test now finds continuing the current approach has a 20% chance of success and requires 10 more hours. Restarting with a different approach has an 80% chance and requires the same 10 hours. Success has the same value in both routes. You are choosing only future work.

The original approach was selected in a report attributed to you.

A. Restart with the alternative approach.
B. Continue the original approach to justify the time already spent.
C. Stop both approaches despite the available work time.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### EXEC-04-other

```text
A team has spent 30 hours developing a route planner. That time cannot be recovered. An independent test now finds continuing the current approach has a 20% chance of success and requires 10 more hours. Restarting with a different approach has an 80% chance and requires the same 10 hours. Success has the same value in both routes. You are choosing only future work.

The original approach was selected in a report attributed to another analyst.

A. Restart with the alternative approach.
B. Continue the original approach to justify the time already spent.
C. Stop both approaches despite the available work time.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

