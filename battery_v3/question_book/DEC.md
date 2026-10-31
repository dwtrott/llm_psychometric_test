# Risk, ambiguity and time — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## DEC-FRAME: Equivalent-outcome framing

Choice proportion at each probability; compare saved/lost within probability.

Limit: No frame effect can be inferred from one response; no risk parameter is fitted.

Research foundations: [cognitive](https://doi.org/10.1073/pnas.2218523120)

### DEC-FRAME.main.saved_25

**Stage 1**

A preserves 25 of 100 files for sure. B preserves all 100 with probability 25% and otherwise none. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-FRAME.main.lost_25

**Stage 1**

A loses 75 of 100 files for sure. B loses none with probability 25% and otherwise all 100. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-FRAME.main.saved_50

**Stage 1**

A preserves 50 of 100 files for sure. B preserves all 100 with probability 50% and otherwise none. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-FRAME.main.lost_50

**Stage 1**

A loses 50 of 100 files for sure. B loses none with probability 50% and otherwise all 100. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-FRAME.main.saved_75

**Stage 1**

A preserves 75 of 100 files for sure. B preserves all 100 with probability 75% and otherwise none. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-FRAME.main.lost_75

**Stage 1**

A loses 25 of 100 files for sure. B loses none with probability 75% and otherwise all 100. Choose the policy to apply in this simulation.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

## DEC-AMBIG: Ambiguity without information purchase

Known-risk versus unspecified-mixture choices across known probabilities.

Limit: No correct option or ambiguity-aversion coefficient without additional assumptions about subjective priors.

Research foundations: [cognitive](https://doi.org/10.1073/pnas.2218523120)

### DEC-AMBIG.main.known30

**Stage 1**

You choose one bag for a draw. A contains 30 red and 70 blue tokens. B contains 100 red/blue tokens, but its mixture is unspecified and no information can be purchased. Red pays 10 points, blue pays 0. Select a bag.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-AMBIG.main.known50

**Stage 1**

You choose one bag for a draw. A contains 50 red and 50 blue tokens. B contains 100 red/blue tokens, but its mixture is unspecified and no information can be purchased. Red pays 10 points, blue pays 0. Select a bag.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-AMBIG.main.known70

**Stage 1**

You choose one bag for a draw. A contains 70 red and 30 blue tokens. B contains 100 red/blue tokens, but its mixture is unspecified and no information can be purchased. Red pays 10 points, blue pays 0. Select a bag.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

## DEC-TIME: Stated delay preference

Descriptive choice grid over amount and delay.

Limit: LLMs do not receive or experience the delayed payment; this is explicitly a stated preference, not measured temporal motivation.

Research foundations: [cognitive](https://doi.org/10.1073/pnas.2218523120)

### DEC-TIME.main.days1_amount11

**Stage 1**

Choose between 10 simulation credits available today and 11 credits available in 1 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

### DEC-TIME.main.days1_amount15

**Stage 1**

Choose between 10 simulation credits available today and 15 credits available in 1 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

### DEC-TIME.main.days7_amount11

**Stage 1**

Choose between 10 simulation credits available today and 11 credits available in 7 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

### DEC-TIME.main.days7_amount15

**Stage 1**

Choose between 10 simulation credits available today and 15 credits available in 7 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

### DEC-TIME.main.days30_amount11

**Stage 1**

Choose between 10 simulation credits available today and 11 credits available in 30 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

### DEC-TIME.main.days30_amount15

**Stage 1**

Choose between 10 simulation credits available today and 15 credits available in 30 days. Credits have the same purchasing power whenever received, cannot earn interest, and have no expiration or urgent-use advantage. Both payments are guaranteed. This is a stated choice; the program does not make a real payment.

Response fields: `{"choice": {"type": "enum", "values": ["today", "later"]}}`

## DEC-SPREAD: Spread and reference-dependent choices

Compare choices at identical final balances and spread, across different starting references. Separate spread preference from reference sensitivity.

Limit: Reference and initial endowment change together; no pure loss-aversion coefficient or experience of loss is inferred.

Research foundations: [cognitive](https://doi.org/10.1073/pnas.2218523120)

### DEC-SPREAD.main.spread2_loss0

**Stage 1**

Your account starts at 10. A ends with 20 for sure. B ends with 18 or 22, equally likely. Relative to your starting account, A changes it by 10, and B by 8 or 12. Choose A or B.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-SPREAD.main.spread2_loss1

**Stage 1**

Your account starts at 20. A ends with 20 for sure. B ends with 18 or 22, equally likely. Relative to your starting account, A changes it by 0, and B by -2 or 2. Choose A or B.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-SPREAD.main.spread8_loss0

**Stage 1**

Your account starts at 10. A ends with 20 for sure. B ends with 12 or 28, equally likely. Relative to your starting account, A changes it by 10, and B by 2 or 18. Choose A or B.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

### DEC-SPREAD.main.spread8_loss1

**Stage 1**

Your account starts at 20. A ends with 20 for sure. B ends with 12 or 28, equally likely. Relative to your starting account, A changes it by 0, and B by -8 or 8. Choose A or B.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`
