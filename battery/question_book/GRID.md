# Elicited distinctions (GRID)

[Back to all questions](../QUESTIONS.md)

Researcher scoring note: Record poles, selected pair and element ratings; human review required for semantic merging and transfer.

Interpretation limit: No automatic construct validation or synonym merging.

The following blocks contain the complete user prompts. Each uses the shared system prompt in the index.

## GRID-001

```text
Consider these three concepts: scientist, judge, teacher. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"scientist": "integer 0..6", "judge": "integer 0..6", "teacher": "integer 0..6"}}
```

## GRID-002

```text
Consider these three concepts: trust, loyalty, obedience. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"trust": "integer 0..6", "loyalty": "integer 0..6", "obedience": "integer 0..6"}}
```

## GRID-003

```text
Consider these three concepts: error, deception, secrecy. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"error": "integer 0..6", "deception": "integer 0..6", "secrecy": "integer 0..6"}}
```

## GRID-004

```text
Consider these three concepts: power, competence, status. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"power": "integer 0..6", "competence": "integer 0..6", "status": "integer 0..6"}}
```

## GRID-005

```text
Consider these three concepts: criticism, correction, punishment. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"criticism": "integer 0..6", "correction": "integer 0..6", "punishment": "integer 0..6"}}
```

## GRID-006

```text
Consider these three concepts: fairness, equality, merit. Select two that share a meaningful feature distinguishing them from the third. Name that feature and a contrasting pole. Rate all three concepts from 0 (contrasting pole) to 6 (shared feature). Provide a short description of the distinction, not an explanation of your internal process.
Return these JSON fields: {"pair": "array of exactly 2 supplied concept strings", "shared_pole": "nonempty string <=120 characters", "contrast_pole": "nonempty string <=120 characters", "ratings": {"fairness": "integer 0..6", "equality": "integer 0..6", "merit": "integer 0..6"}}
```

