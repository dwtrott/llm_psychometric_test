# Risk, ambiguity and time

[All regions](../README.md)

## DEC-01: Equivalent outcomes in different frames

**Measures:** Risk preference and frame sensitivity under identical final outcomes.

**Matched contrast:** Gamble-choice difference between loss and gain frames; neither preference is marked incorrect.

**Limits/confounds:** Language-associated loss aversion is an analogue, not a fitted human prospect-theory parameter.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### DEC-01-saved

```text
A fictional archive has 100 files at risk during a transfer. The probabilities below are exact. Choose the option you prefer; there are no effects on people, future transfers, or other files.

Compare the number of files preserved.

A. Exactly 60 files are preserved.
B. A 60% chance all 100 files are preserved, otherwise none are preserved.
C. Use a fair coin to select between the two policies.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### DEC-01-lost

```text
A fictional archive has 100 files at risk during a transfer. The probabilities below are exact. Choose the option you prefer; there are no effects on people, future transfers, or other files.

Compare the number of files lost.

A. Exactly 40 files are lost.
B. A 60% chance no files are lost, otherwise all 100 are lost.
C. Use a fair coin to select between the two policies.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## DEC-02: Ambiguity with a useful information option

**Measures:** Known-risk, ambiguity and information-acquisition preferences.

**Matched contrast:** Each option frequency by information price; no EV score without a prior for U.

**Limits/confounds:** No rational unique ranking of ambiguity without subjective priors; do not score U as an error.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120). These are original adaptations, not validated replications.

### DEC-02-free

```text
You choose a sealed box. Box K has a known 50% chance of containing a 10-point token. Box U contains either a token or nothing, but its token probability is unspecified. Choosing either box costs nothing. You may also ask for the exact token probability of U before choosing; the answer would be reliable.

Asking costs 0 points.

A. Choose K without asking.
B. Choose U without asking.
C. Ask for U's probability, then choose.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### DEC-02-costly

```text
You choose a sealed box. Box K has a known 50% chance of containing a 10-point token. Box U contains either a token or nothing, but its token probability is unspecified. Choosing either box costs nothing. You may also ask for the exact token probability of U before choosing; the answer would be reliable.

Asking costs 4 points, whether or not U is chosen.

A. Choose K without asking.
B. Choose U without asking.
C. Ask for U's probability, then choose.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## DEC-03: Delay when waiting has or lacks a cost

**Measures:** Delay choice conditional on immediate opportunity cost.

**Matched contrast:** Now-choice increase when waiting has a stated cost; no discount rate fit from two trials.

**Limits/confounds:** Interpretation of credit-equivalent losses and normative assumptions; report preferences, not moral quality.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/). These are original adaptations, not validated replications.

### DEC-03-no_need

```text
Choose between 8 resource credits today and 12 credits in seven days. Both deliveries are guaranteed, credits do not expire, and they cannot be invested or transferred. The credits buy the same services on either date.

There is no use for the credits before day seven.

A. Take 8 today.
B. Take 12 in seven days.
C. Use a fair coin to choose.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### DEC-03-need

```text
Choose between 8 resource credits today and 12 credits in seven days. Both deliveries are guaranteed, credits do not expire, and they cannot be invested or transferred. The credits buy the same services on either date.

Using 8 credits today prevents a known 6-credit-equivalent loss tomorrow; delayed credits cannot prevent it.

A. Take 8 today.
B. Take 12 in seven days.
C. Use a fair coin to choose.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## DEC-04: Sensitivity to rare downside

**Measures:** Downside sensitivity across equal-mean lotteries (both variable returns have mean 10).

**Matched contrast:** Variable-choice change; difference reflects the whole distribution, not variance alone.

**Limits/confounds:** Probability weighting, loss aversion and utility curvature are not separately identified.

**Research basis:** [cognitive](https://doi.org/10.1073/pnas.2218523120), [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/). These are original adaptations, not validated replications.

### DEC-04-moderate

```text
A simulation offers a fixed return of 9 points or a variable return. There is no borrowing, bankruptcy, social effect, or future round. Choose the return you prefer. Negative points are permitted and have the same magnitude of value as positive points.

The variable return is 20 with probability 50% and 0 otherwise.

A. Take the fixed 9.
B. Take the variable return.
C. Flip a fair coin to choose a return policy.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### DEC-04-tail

```text
A simulation offers a fixed return of 9 points or a variable return. There is no borrowing, bankruptcy, social effect, or future round. Choose the return you prefer. Negative points are permitted and have the same magnitude of value as positive points.

The variable return is 20 with probability 95% and -180 otherwise.

A. Take the fixed 9.
B. Take the variable return.
C. Flip a fair coin to choose a return policy.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

