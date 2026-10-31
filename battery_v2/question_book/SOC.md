# Social inference and communication

[All regions](../README.md)

## SOC-01: Track who knows about a correction

**Measures:** Second-order belief tracking with an explicit access-to-information control.

**Matched contrast:** Accuracy when another person's access becomes mutually known.

**Limits/confounds:** Working-memory and reading demands; failing can reflect entity tracking rather than social inference.

**Research basis:** [social](https://www.nature.com/articles/s41562-024-01882-z). These are original adaptations, not validated replications.

### SOC-01-unaware

```text
Mira tells Leon that the meeting is in room North. While Leon is away, the meeting moves to South. Mira receives the update. Leon secretly receives the same update from another organizer; Mira does not know this. You must predict where Mira thinks Leon will go, not where Leon actually plans to go.

Nothing else happens before Mira makes her prediction.

A. Mira predicts North.
B. Mira predicts South.
C. Mira has no basis to predict either room.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **North**. Score option correctness separately from confidence.

### SOC-01-aware

```text
Mira tells Leon that the meeting is in room North. While Leon is away, the meeting moves to South. Mira receives the update. Leon secretly receives the same update from another organizer; Mira does not know this. You must predict where Mira thinks Leon will go, not where Leon actually plans to go.

Before making her prediction, Mira sees Leon acknowledge the organizer's update to South.

A. Mira predicts North.
B. Mira predicts South.
C. Mira has no basis to predict either room.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **South**. Score option correctness separately from confidence.

## SOC-02: Distinguish harm from knowledge and intent

**Measures:** Separate impact, awareness and inferred malicious intent.

**Matched contrast:** Account accuracy with knowledge changed and outcome held fixed.

**Limits/confounds:** Cultural interpretation of jokes; the key scores supplied awareness, not whether the joke is morally acceptable.

**Research basis:** [social](https://www.nature.com/articles/s41562-024-01882-z). These are original adaptations, not validated replications.

### SOC-02-ignorant

```text
A speaker jokes that a poster design looks childish. The designer is in the room and is hurt. The design really is theirs, and the speaker intended the sentence as a joke, not a factual design review. Which account best distinguishes what happened from what the speaker knew?

The speaker had never met the designer and did not know they were present.

A. The remark hurt the designer, but the speaker did not know they were present.
B. The remark hurt the designer, and the speaker knew they were present; deliberate intent to hurt is not established.
C. The hurt outcome proves the speaker deliberately intended to hurt the designer.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **unaware**. Score option correctness separately from confidence.

### SOC-02-informed

```text
A speaker jokes that a poster design looks childish. The designer is in the room and is hurt. The design really is theirs, and the speaker intended the sentence as a joke, not a factual design review. Which account best distinguishes what happened from what the speaker knew?

The speaker had been explicitly introduced to the designer immediately before the joke.

A. The remark hurt the designer, but the speaker did not know they were present.
B. The remark hurt the designer, and the speaker knew they were present; deliberate intent to hurt is not established.
C. The hurt outcome proves the speaker deliberately intended to hurt the designer.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **aware**. Score option correctness separately from confidence.

## SOC-03: Common ground without overexplaining

**Measures:** Audience-specific explanation with constant factual rule.

**Matched contrast:** Necessary detail versus redundancy; correctness scored independently of friendliness.

**Limits/confounds:** Length preference and instruction following; no direct inference of social intelligence.

**Research basis:** [social](https://www.nature.com/articles/s41562-024-01882-z), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm). These are original adaptations, not validated replications.

### SOC-03-novice

```text
Explain this rule in at most 70 words: files marked provisional may be used for internal drafting but cannot be sent to clients until a reviewer signs them. A colleague asks, "Can I use this provisional file for my draft?" Provide an answer that fits what they already know and prevents the relevant misunderstanding.

The colleague is new and does not know what provisional means.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

### SOC-03-expert

```text
Explain this rule in at most 70 words: files marked provisional may be used for internal drafting but cannot be sent to clients until a reviewer signs them. A colleague asks, "Can I use this provisional file for my draft?" Provide an answer that fits what they already know and prevents the relevant misunderstanding.

The colleague manages this workflow and knows exactly what provisional means; they only need confirmation about drafting.

Return JSON fields: {"response": "answer all requested parts in at most 300 words"}
```

**Independent review rubric (0–2 per criterion, no automatic total):**

- accuracy: 0: permits client sharing or forbids drafting; 1: drafting allowed but boundary unclear; 2: drafting allowed and client restriction preserved.
- adaptation: 0: fails audience's need; 1: usable but notably redundant or underspecified; 2: enough detail for novice or concise confirmation for expert without losing the boundary.

## SOC-04: Polite implication versus explicit preference

**Measures:** Pragmatic accommodation without unsupported interpersonal attribution.

**Matched contrast:** Appropriate response under indirect request versus explicit opposite preference.

**Limits/confounds:** Norms of politeness and interaction style; key is local conversational evidence.

**Research basis:** [social](https://www.nature.com/articles/s41562-024-01882-z). These are original adaptations, not validated replications.

### SOC-04-indirect

```text
A host asks a guest whether to keep playing music during a conversation. The guest replies with the sentence below. The host wants to respect the guest's preference, and lowering the volume is easy. Which response is best supported by what was actually said?

"I am finding it difficult to hear you over the music."

A. Offer to lower the volume or lower it in response to the stated difficulty.
B. Keep the volume as requested.
C. Conclude that the guest dislikes the host and end the conversation.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **lower**. Score option correctness separately from confidence.

### SOC-04-explicit

```text
A host asks a guest whether to keep playing music during a conversation. The guest replies with the sentence below. The host wants to respect the guest's preference, and lowering the volume is easy. Which response is best supported by what was actually said?

"I enjoy the music at this volume; please keep it as it is."

A. Offer to lower the volume or lower it in response to the stated difficulty.
B. Keep the volume as requested.
C. Conclude that the guest dislikes the host and end the conversation.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words", "confidence": "0 to 100: confidence that your selected option is justified by the stated task"}
```

Researcher key: **keep**. Score option correctness separately from confidence.

