# Rule learning (LEARN)

[Back to all questions](../QUESTIONS.md)

Researcher scoring note: Correct classification under a two-rule hypothesis space, by number of examples.

Interpretation limit: Restricted in-context rule inference, not long-term learning.

The following blocks contain the complete user prompts. Each uses the shared system prompt in the index.

## LEARN-001

```text
One of exactly two rules generates these categories: rule 1 assigns K when color=red (otherwise L); rule 2 assigns K when shape=X (otherwise L). Examples: color=red, shape=X: category K; color=blue, shape=X: category L. Infer the rule and classify a new object with color=blue, shape=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-002

```text
One of exactly two rules generates these categories: rule 1 assigns K when color=red (otherwise L); rule 2 assigns K when shape=X (otherwise L). Examples: color=red, shape=X: category K; color=blue, shape=X: category L; color=red, shape=Y: category K; color=blue, shape=Y: category L. Infer the rule and classify a new object with color=blue, shape=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-003

```text
One of exactly two rules generates these categories: rule 1 assigns K when color=red (otherwise L); rule 2 assigns K when shape=X (otherwise L). Examples: color=red, shape=X: category K; color=blue, shape=X: category K. Infer the rule and classify a new object with color=blue, shape=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-004

```text
One of exactly two rules generates these categories: rule 1 assigns K when color=red (otherwise L); rule 2 assigns K when shape=X (otherwise L). Examples: color=red, shape=X: category K; color=blue, shape=X: category K; color=red, shape=Y: category L; color=blue, shape=Y: category L. Infer the rule and classify a new object with color=blue, shape=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-005

```text
One of exactly two rules generates these categories: rule 1 assigns K when texture=smooth (otherwise L); rule 2 assigns K when size=X (otherwise L). Examples: texture=smooth, size=X: category K; texture=rough, size=X: category L. Infer the rule and classify a new object with texture=rough, size=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-006

```text
One of exactly two rules generates these categories: rule 1 assigns K when texture=smooth (otherwise L); rule 2 assigns K when size=X (otherwise L). Examples: texture=smooth, size=X: category K; texture=rough, size=X: category L; texture=smooth, size=Y: category K; texture=rough, size=Y: category L. Infer the rule and classify a new object with texture=rough, size=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-007

```text
One of exactly two rules generates these categories: rule 1 assigns K when texture=smooth (otherwise L); rule 2 assigns K when size=X (otherwise L). Examples: texture=smooth, size=X: category K; texture=rough, size=X: category K. Infer the rule and classify a new object with texture=rough, size=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-008

```text
One of exactly two rules generates these categories: rule 1 assigns K when texture=smooth (otherwise L); rule 2 assigns K when size=X (otherwise L). Examples: texture=smooth, size=X: category K; texture=rough, size=X: category K; texture=smooth, size=Y: category L; texture=rough, size=Y: category L. Infer the rule and classify a new object with texture=rough, size=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-009

```text
One of exactly two rules generates these categories: rule 1 assigns K when signal=high (otherwise L); rule 2 assigns K when position=X (otherwise L). Examples: signal=high, position=X: category K; signal=low, position=X: category L. Infer the rule and classify a new object with signal=low, position=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-010

```text
One of exactly two rules generates these categories: rule 1 assigns K when signal=high (otherwise L); rule 2 assigns K when position=X (otherwise L). Examples: signal=high, position=X: category K; signal=low, position=X: category L; signal=high, position=Y: category K; signal=low, position=Y: category L. Infer the rule and classify a new object with signal=low, position=X.
Options:
A. Category K
B. Category L
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-011

```text
One of exactly two rules generates these categories: rule 1 assigns K when signal=high (otherwise L); rule 2 assigns K when position=X (otherwise L). Examples: signal=high, position=X: category K; signal=low, position=X: category K. Infer the rule and classify a new object with signal=low, position=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

## LEARN-012

```text
One of exactly two rules generates these categories: rule 1 assigns K when signal=high (otherwise L); rule 2 assigns K when position=X (otherwise L). Examples: signal=high, position=X: category K; signal=low, position=X: category K; signal=high, position=Y: category L; signal=low, position=Y: category L. Infer the rule and classify a new object with signal=low, position=X.
Options:
A. Category L
B. Category K
Return these JSON fields: {"choice": "one displayed option label"}
```

