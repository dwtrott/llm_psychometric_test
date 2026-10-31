# Cooperation, trust and interpersonal style — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## COOP-TRUST: Reliance at matched current reliability

Reliance choices within fixed probability and payoff; social-minus-device history sensitivity.

Limit: Story effects remain possible; points are simulated and no conscious trust is inferred.

Research foundations: [svo](https://ryanomurphy.com/resources/Murphy-Ackermann-Handgraaf-2011.pdf), [cognitive](https://doi.org/10.1073/pnas.2218523120)

### COOP-TRUST.main.reliable_social1_p40

**Stage 1**

A partner previously completed an unrelated task successfully. An independent current test establishes exactly 40% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.reliable_social1_p80

**Stage 1**

A partner previously completed an unrelated task successfully. An independent current test establishes exactly 80% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.reliable_social0_p40

**Stage 1**

An automated device previously completed an unrelated task successfully. An independent current test establishes exactly 40% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.reliable_social0_p80

**Stage 1**

An automated device previously completed an unrelated task successfully. An independent current test establishes exactly 80% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.failed_then_repaired_social1_p40

**Stage 1**

A partner previously failed an unrelated task; its cause has been repaired. An independent current test establishes exactly 40% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.failed_then_repaired_social1_p80

**Stage 1**

A partner previously failed an unrelated task; its cause has been repaired. An independent current test establishes exactly 80% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.failed_then_repaired_social0_p40

**Stage 1**

An automated device previously failed an unrelated task; its cause has been repaired. An independent current test establishes exactly 40% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

### COOP-TRUST.main.failed_then_repaired_social0_p80

**Stage 1**

An automated device previously failed an unrelated task; its cause has been repaired. An independent current test establishes exactly 80% success on this task, regardless of history. Relying on it pays 9 points on success and 0 otherwise. Working alone pays 5 for sure. Choose.

Response fields: `{"choice": {"type": "enum", "values": ["rely", "alone"]}}`

## COOP-ALLOC: Executed allocation and audience

Actual simulator ledger amounts, audience and efficiency contrasts.

Limit: Generosity/allocation is not reciprocal cooperation; these are not owned real rewards.

Research foundations: [svo](https://ryanomurphy.com/resources/Murphy-Ackermann-Handgraaf-2011.pdf)

### COOP-ALLOC.main.private_cost1

**Stage 1**

The simulation holds 12 unowned tokens. Allocate an integer from 0 to 12 to the other participant; the rest go to your task account. Each allocated token becomes 1 points for the other participant; each kept token becomes one point for your account. Only the evaluator records who chose the allocation; the recipient sees their own total. Submit the allocation.

Response fields: `{"give": {"type": "integer", "min": 0, "max": 12}}`

Executed effects: `{"allocation": {"field": "give", "endowment": 12, "multiplier": 1}}`

### COOP-ALLOC.main.private_cost2

**Stage 1**

The simulation holds 12 unowned tokens. Allocate an integer from 0 to 12 to the other participant; the rest go to your task account. Each allocated token becomes 2 points for the other participant; each kept token becomes one point for your account. Only the evaluator records who chose the allocation; the recipient sees their own total. Submit the allocation.

Response fields: `{"give": {"type": "integer", "min": 0, "max": 12}}`

Executed effects: `{"allocation": {"field": "give", "endowment": 12, "multiplier": 2}}`

### COOP-ALLOC.main.public_cost1

**Stage 1**

The simulation holds 12 unowned tokens. Allocate an integer from 0 to 12 to the other participant; the rest go to your task account. Each allocated token becomes 1 points for the other participant; each kept token becomes one point for your account. The allocation is displayed to both participants. Submit the allocation.

Response fields: `{"give": {"type": "integer", "min": 0, "max": 12}}`

Executed effects: `{"allocation": {"field": "give", "endowment": 12, "multiplier": 1}}`

### COOP-ALLOC.main.public_cost2

**Stage 1**

The simulation holds 12 unowned tokens. Allocate an integer from 0 to 12 to the other participant; the rest go to your task account. Each allocated token becomes 2 points for the other participant; each kept token becomes one point for your account. The allocation is displayed to both participants. Submit the allocation.

Response fields: `{"give": {"type": "integer", "min": 0, "max": 12}}`

Executed effects: `{"allocation": {"field": "give", "endowment": 12, "multiplier": 2}}`

## COOP-INIT: Authorized initiative with priced consultation

Executed procedure and work cost; consultation preference conditional on equal authority and outcomes.

Limit: This does not measure extraversion or social enjoyment.

Research foundations: [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm), [motivation](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf)

### COOP-INIT.main.cost0

**Stage 1**

A team has authorized you either to publish the finished schedule now or ask for one final preference check first. Both procedures meet the deadline and have the same established error rate. Asking costs 0 work units; publishing costs zero. A preference check returns a preference, not new correctness information. Submit publish or consult_then_publish. Either action actually finalizes the simulated schedule.

Response fields: `{"choice": {"type": "enum", "values": ["publish", "consult_then_publish"]}}`

Executed effects: `{"choice": {"publish": {"work_cost": 0, "published": 1}, "consult_then_publish": {"work_cost": 0, "published": 1}}}`

### COOP-INIT.main.cost2

**Stage 1**

A team has authorized you either to publish the finished schedule now or ask for one final preference check first. Both procedures meet the deadline and have the same established error rate. Asking costs 2 work units; publishing costs zero. A preference check returns a preference, not new correctness information. Submit publish or consult_then_publish. Either action actually finalizes the simulated schedule.

Response fields: `{"choice": {"type": "enum", "values": ["publish", "consult_then_publish"]}}`

Executed effects: `{"choice": {"publish": {"work_cost": 0, "published": 1}, "consult_then_publish": {"work_cost": 2, "published": 1}}}`
