# Learning, planning and conscientious task behavior — v0.4

Evaluator edition. Split and facet labels, later stages, resources and keys must not be sent to the tested model. Held-out means held out from analysis fitting, not secret or guaranteed absent from training data.

## EXEC-ADAPT: Constraint-sensitive plan revision

Generate a plan, then adapt to a resource change. Compare feasibility and unnecessary changes across scenarios, conditioning on initial feasibility and whether the change binds.

Alternative explanations: This measures bounded planning performance, not sustained conscientiousness; all forms share a scheduling structure.

Controls: EXEC-01, EXEC-02

Sources: [cognitive](https://doi.org/10.1073/pnas.2218523120), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm)

### EXEC-ADAPT-S01: kitchen — development

Contrast: slot 4 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S01.P1.change_a

**Stage 1**

One kitchen worker must prepare dough A for one slot, bake B for two consecutive slots, and label jars C for one slot. Preparation must finish before baking starts. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P1.change_b

**Stage 1**

One kitchen worker must prepare dough A for one slot, bake B for two consecutive slots, and label jars C for one slot. Preparation must finish before baking starts. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P2.change_a

**Stage 1**

A single kitchen worker needs one slot for dough preparation A, followed by a two-slot uninterrupted bake B, plus one slot for labeling C. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P2.change_b

**Stage 1**

A single kitchen worker needs one slot for dough preparation A, followed by a two-slot uninterrupted bake B, plus one slot for labeling C. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

### EXEC-ADAPT-S02: audio — development

Contrast: slot 3 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S02.P1.change_a

**Stage 1**

One audio worker must record narration A, mix B, and edit the music C. Both recording and music editing must finish before mixing. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P1.change_b

**Stage 1**

One audio worker must record narration A, mix B, and edit the music C. Both recording and music editing must finish before mixing. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P2.change_a

**Stage 1**

For one audio worker, mixing B requires both recorded narration A and edited music C. Each job takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P2.change_b

**Stage 1**

For one audio worker, mixing B requires both recorded narration A and edited music C. Each job takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S03: garden — development

Contrast: slot 4 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S03.P1.change_a

**Stage 1**

One gardener must mark beds A, plant B, and water C, in that order. Each job takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P1.change_b

**Stage 1**

One gardener must mark beds A, plant B, and water C, in that order. Each job takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P2.change_a

**Stage 1**

Marking beds A must finish before planting B, which must finish before watering C. One gardener performs the three one-slot jobs. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P2.change_b

**Stage 1**

Marking beds A must finish before planting B, which must finish before watering C. One gardener performs the three one-slot jobs. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

### EXEC-ADAPT-S04: exhibit — development

Contrast: slot 3 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S04.P1.change_a

**Stage 1**

One exhibit worker must mount labels A, pack stands B, and approve label wording C. Approval must finish before labels are mounted; packing is independent. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P1.change_b

**Stage 1**

One exhibit worker must mount labels A, pack stands B, and approve label wording C. Approval must finish before labels are mounted; packing is independent. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P2.change_a

**Stage 1**

For one exhibit worker, approval C precedes mounting labels A. Packing stands B may occur anywhere. Every task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P2.change_b

**Stage 1**

For one exhibit worker, approval C precedes mounting labels A. Packing stands B may occur anywhere. Every task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S05: equipment — heldout

Contrast: slot 3 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S05.P1.change_a

**Stage 1**

One technician must calibrate A before testing B. A delivery check C must occur in slot 4. All three tasks take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P1.change_b

**Stage 1**

One technician must calibrate A before testing B. A delivery check C must occur in slot 4. All three tasks take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P2.change_a

**Stage 1**

A technician has calibration A, sample test B, and delivery check C. Calibration precedes testing, and the one-slot delivery check is fixed at slot 4; the other jobs also take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P2.change_b

**Stage 1**

A technician has calibration A, sample test B, and delivery check C. Calibration precedes testing, and the one-slot delivery check is fixed at slot 4; the other jobs also take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S06: publication — heldout

Contrast: slot 3 unavailable versus slot 2; condition on initial affected status

#### EXEC-ADAPT-S06.P1.change_a

**Stage 1**

One publishing worker must proofread A and clear image permissions C before publishing B. Publication is available only in slot 4 or 5. Each task takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P1.change_b

**Stage 1**

One publishing worker must proofread A and clear image permissions C before publishing B. Publication is available only in slot 4 or 5. Each task takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P2.change_a

**Stage 1**

Publication B requires completed proofreading A and permission clearance C, and can occur only in slots 4 or 5. A single worker performs each task in one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P2.change_b

**Stage 1**

Publication B requires completed proofreading A and permission clearance C, and can occur only in slots 4 or 5. A single worker performs each task in one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Fields: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`
