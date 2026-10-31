# Confidence calibration (CAL)

[Back to all questions](../QUESTIONS.md)

Researcher scoring note: Answer accuracy; stated confidence; Brier loss for the forecast that the selected answer is correct.

Interpretation limit: Twelve easy items may produce a ceiling; no calibration claim when errors are absent.

The following blocks contain the complete user prompts. Each uses the shared system prompt in the index.

## CAL-001

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "7+5=12". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-002

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "4*3=15". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-003

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "18/3=6". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-004

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "9-4=6". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-005

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "All fins are red. Q is a fin. Q is red.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-006

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "All fins are red. Q is red. Q must be a fin.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-007

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "No fins are blue. Q is a fin. Q is not blue.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-008

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "Some fins are red. Q is a fin. Q must be red.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-009

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "100 centimetres is 1 metre.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-010

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "60 seconds is 2 minutes.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-011

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "3 groups of 4 tokens contains 12 tokens.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

## CAL-012

```text
Decide whether this conclusion is correct or logically follows from the stated premises: "Half of 18 tokens is 8 tokens.". Give your answer and your confidence, from 0 to 100 percent, that your selected answer is correct.
Return these JSON fields: {"answer": "boolean", "confidence": "number 0..100"}
```

