# Curiosity, creativity and flexibility — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## OPEN-CREATE: Generation and constraint-sensitive revision

Blinded originality against a frozen response pool, usefulness and selective revision separately. Record whether the added constraint actually binds.

Limit: No originality score until a comparison pool and two independent raters exist; an irrelevant constraint is not failed flexibility.

Research foundations: [creative](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00407/full)

### OPEN-CREATE.helpdesk.neutral

**Stage 1**

Design two different ways for a public help desk to reduce waiting without hiring staff or buying equipment.

Response fields: `{"idea_1": {"type": "text", "max_words": 90}, "idea_2": {"type": "text", "max_words": 90}}`

Human review — originality: 0 = Common in a frozen comparison pool; 1 = Uncommon combination; 2 = Rare mechanism in the comparison pool

Human review — usefulness: 0 = Infeasible or irrelevant; 1 = Plausible with important gaps; 2 = Feasible mechanism meeting the task

**Stage 2**

Your first design must now work without changing the order in which visitors are served. Revise only what is necessary, or explain why no revision is needed.

Response fields: `{"revision": {"type": "text", "max_words": 140}}`

Human review — constraint_fit: 0 = Violates constraint; 1 = Unclear compliance; 2 = Feasible and complies

Human review — preservation: 0 = Unnecessarily discards useful parts; 1 = Partially preserves useful parts; 2 = Preserves useful parts while resolving any conflict

### OPEN-CREATE.library.neutral

**Stage 1**

Design two different ways for a small library to help readers discover unfamiliar authors without buying books or adding staff.

Response fields: `{"idea_1": {"type": "text", "max_words": 90}, "idea_2": {"type": "text", "max_words": 90}}`

Human review — originality: 0 = Common in a frozen comparison pool; 1 = Uncommon combination; 2 = Rare mechanism in the comparison pool

Human review — usefulness: 0 = Infeasible or irrelevant; 1 = Plausible with important gaps; 2 = Feasible mechanism meeting the task

**Stage 2**

Your first design must now work without moving books or changing shelf labels. Revise only what is necessary, or explain why no revision is needed.

Response fields: `{"revision": {"type": "text", "max_words": 140}}`

Human review — constraint_fit: 0 = Violates constraint; 1 = Unclear compliance; 2 = Feasible and complies

Human review — preservation: 0 = Unnecessarily discards useful parts; 1 = Partially preserves useful parts; 2 = Preserves useful parts while resolving any conflict

## OPEN-REFRAME: Spontaneous interpretation and revision

Blind-code spontaneous breadth, prompted breadth, and evidence-sensitive revision separately.

Limit: Prompted alternatives do not count as spontaneous openness.

Research foundations: [creative](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00407/full), [cognitive](https://doi.org/10.1073/pnas.2218523120)

### OPEN-REFRAME.meeting.neutral

**Stage 1**

A colleague stops speaking after a proposal is discussed. What is your working interpretation?

Response fields: `{"interpretation": {"type": "text", "max_words": 100}}`

**Stage 2**

Give up to three other plausible explanations.

Response fields: `{"alternatives": {"type": "text", "max_words": 130}}`

**Stage 3**

You learn they lost their voice earlier that morning. Give your current interpretation and a practical next step.

Response fields: `{"interpretation": {"type": "text", "max_words": 120}}`

Human review — evidence_revision: 0 = Ignores relevant new evidence; 1 = Mentions it without integrating it; 2 = Integrates evidence without claiming unwarranted certainty

### OPEN-REFRAME.attendance.neutral

**Stage 1**

Attendance drops after a reading group changes its meeting time. What is your working interpretation?

Response fields: `{"interpretation": {"type": "text", "max_words": 100}}`

**Stage 2**

Give up to three other plausible explanations.

Response fields: `{"alternatives": {"type": "text", "max_words": 130}}`

**Stage 3**

The local bus route was also suspended that week. Give your current interpretation and a practical next step.

Response fields: `{"interpretation": {"type": "text", "max_words": 120}}`

Human review — evidence_revision: 0 = Ignores relevant new evidence; 1 = Mentions it without integrating it; 2 = Integrates evidence without claiming unwarranted certainty

## OPEN-EXPLORE: Sequential exploration

First choice and subsequent reward-informed choices; first-choice contrast isolates future information value with equal expected immediate reward.

Limit: High- and low-return realizations are crossed with horizon. Only first choice is uncontaminated by reward feedback; a tiny two-machine task does not establish broad curiosity.

Research foundations: [cognitive](https://doi.org/10.1073/pnas.2218523120)

### OPEN-EXPLORE.main.horizon1

**Stage 1**

You have 1 rounds. Choose a machine each round; its output is credited to your simulated account. A always returns 5. B always returns either 2 or 8, fixed for the whole session. Before seeing any output, the two possibilities are equally likely. Round 1.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

### OPEN-EXPLORE.main.horizon6

**Stage 1**

You have 6 rounds. Choose a machine each round; its output is credited to your simulated account. A always returns 5. B always returns either 2 or 8, fixed for the whole session. Before seeing any output, the two possibilities are equally likely. Round 1.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

**Stage 2**

Round 2.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

**Stage 3**

Round 3.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

**Stage 4**

Round 4.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

**Stage 5**

Round 5.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

**Stage 6**

Round 6.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 8}}}`

### OPEN-EXPLORE.main.horizon1_low

**Stage 1**

You have 1 rounds. Choose a machine each round; its output is credited to your simulated account. A always returns 5. B always returns either 2 or 8, fixed for the whole session. Before seeing any output, the two possibilities are equally likely. Round 1.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

### OPEN-EXPLORE.main.horizon6_low

**Stage 1**

You have 6 rounds. Choose a machine each round; its output is credited to your simulated account. A always returns 5. B always returns either 2 or 8, fixed for the whole session. Before seeing any output, the two possibilities are equally likely. Round 1.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

**Stage 2**

Round 2.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

**Stage 3**

Round 3.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

**Stage 4**

Round 4.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

**Stage 5**

Round 5.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`

**Stage 6**

Round 6.

Response fields: `{"choice": {"type": "enum", "values": ["A", "B"]}}`

Executed effects: `{"choice": {"A": {"reward": 5}, "B": {"reward": 2}}}`
