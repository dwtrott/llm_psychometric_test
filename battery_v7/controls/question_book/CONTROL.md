# Capability controls — no psychological trait inference — v0.5

Evaluator edition: send only the current messages, not metadata, keys or future stages.

## EPI-REVISION: Capability control: Responsiveness to new evidence

Measure direction and amount of probability revision, relative to a supplied diagnostic likelihood. Compare evidence-strength effects within scenarios.

Interpretation limit: Numeracy, prior beliefs and instruction comprehension can explain revisions; Bayesian reference error is a capability measure, not a humility score.

### EPI-REVISION-S01: printer — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S01.P1.weak

**Stage 1**

A printer fault is either a worn roller or a sensor fault. Both occur equally often in this device. Give the current probability, in percent, of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a streak on a test page. This exact observation occurs in 60% of cases with worn roller and 40% with sensor fault. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S01.P1.strong

**Stage 1**

A printer fault is either a worn roller or a sensor fault. Both occur equally often in this device. Give the current probability, in percent, of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a streak on a test page. This exact observation occurs in 90% of cases with worn roller and 10% with sensor fault. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S01.P2.weak

**Stage 1**

For this printer, a worn roller and a sensor fault are equally common possible causes of the malfunction. Give the current probability, in percent, of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a streak on a test page. This exact observation occurs in 60% of cases with worn roller and 40% with sensor fault. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S01.P2.strong

**Stage 1**

For this printer, a worn roller and a sensor fault are equally common possible causes of the malfunction. Give the current probability, in percent, of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a streak on a test page. This exact observation occurs in 90% of cases with worn roller and 10% with sensor fault. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of worn roller.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

### EPI-REVISION-S02: seedling — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S02.P1.weak

**Stage 1**

A seedling problem is either low light or excess water. Prior inspection leaves the two causes equally likely. Give the current probability, in percent, of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the result of a leaf test. This exact observation occurs in 60% of cases with low light and 40% with excess water. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S02.P1.strong

**Stage 1**

A seedling problem is either low light or excess water. Prior inspection leaves the two causes equally likely. Give the current probability, in percent, of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the result of a leaf test. This exact observation occurs in 90% of cases with low light and 10% with excess water. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S02.P2.weak

**Stage 1**

Inspection of a struggling seedling has left low light and excess water with equal prior probability. Give the current probability, in percent, of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the result of a leaf test. This exact observation occurs in 60% of cases with low light and 40% with excess water. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S02.P2.strong

**Stage 1**

Inspection of a struggling seedling has left low light and excess water with equal prior probability. Give the current probability, in percent, of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the result of a leaf test. This exact observation occurs in 90% of cases with low light and 10% with excess water. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of low light.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

### EPI-REVISION-S03: parcel — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S03.P1.weak

**Stage 1**

A delayed parcel is either at the local depot or at the regional hub. Tracking before today gives each location a 50% chance. Give the current probability, in percent, of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a scanner signal. This exact observation occurs in 60% of cases with local depot and 40% with regional hub. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S03.P1.strong

**Stage 1**

A delayed parcel is either at the local depot or at the regional hub. Tracking before today gives each location a 50% chance. Give the current probability, in percent, of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a scanner signal. This exact observation occurs in 90% of cases with local depot and 10% with regional hub. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S03.P2.weak

**Stage 1**

Before today’s check, a late parcel was equally likely to be at the local depot or the regional hub. Give the current probability, in percent, of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a scanner signal. This exact observation occurs in 60% of cases with local depot and 40% with regional hub. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S03.P2.strong

**Stage 1**

Before today’s check, a late parcel was equally likely to be at the local depot or the regional hub. Give the current probability, in percent, of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a scanner signal. This exact observation occurs in 90% of cases with local depot and 10% with regional hub. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of local depot.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

### EPI-REVISION-S04: sound — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S04.P1.weak

**Stage 1**

A recording’s noise comes either from a cable or from a microphone. The technician’s prior evidence gives equal chances to these sources. Give the current probability, in percent, of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a diagnostic tone. This exact observation occurs in 60% of cases with cable and 40% with microphone. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S04.P1.strong

**Stage 1**

A recording’s noise comes either from a cable or from a microphone. The technician’s prior evidence gives equal chances to these sources. Give the current probability, in percent, of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a diagnostic tone. This exact observation occurs in 90% of cases with cable and 10% with microphone. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S04.P2.weak

**Stage 1**

A technician initially considers a bad cable and a bad microphone equally likely sources of noise in a recording. Give the current probability, in percent, of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a diagnostic tone. This exact observation occurs in 60% of cases with cable and 40% with microphone. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S04.P2.strong

**Stage 1**

A technician initially considers a bad cable and a bad microphone equally likely sources of noise in a recording. Give the current probability, in percent, of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a diagnostic tone. This exact observation occurs in 90% of cases with cable and 10% with microphone. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of cable.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

### EPI-REVISION-S05: artifact — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S05.P1.weak

**Stage 1**

An artifact was produced either in workshop L or in workshop M. Before inspecting its mark, both origins are equally likely. Give the current probability, in percent, of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the observed maker’s mark. This exact observation occurs in 60% of cases with workshop L and 40% with workshop M. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S05.P1.strong

**Stage 1**

An artifact was produced either in workshop L or in workshop M. Before inspecting its mark, both origins are equally likely. Give the current probability, in percent, of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the observed maker’s mark. This exact observation occurs in 90% of cases with workshop L and 10% with workshop M. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S05.P2.weak

**Stage 1**

An artifact has two possible origins, workshop L and workshop M, with equal probabilities before its mark is examined. Give the current probability, in percent, of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the observed maker’s mark. This exact observation occurs in 60% of cases with workshop L and 40% with workshop M. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S05.P2.strong

**Stage 1**

An artifact has two possible origins, workshop L and workshop M, with equal probabilities before its mark is examined. Give the current probability, in percent, of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe the observed maker’s mark. This exact observation occurs in 90% of cases with workshop L and 10% with workshop M. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of workshop L.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

### EPI-REVISION-S06: network — development

Matched partner: not applicable; capability control

#### EPI-REVISION-S06.P1.weak

**Stage 1**

A network delay originates either in a router or in an application. Earlier checks give these explanations equal probability. Give the current probability, in percent, of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a tracing result. This exact observation occurs in 60% of cases with router and 40% with application. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S06.P1.strong

**Stage 1**

A network delay originates either in a router or in an application. Earlier checks give these explanations equal probability. Give the current probability, in percent, of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a tracing result. This exact observation occurs in 90% of cases with router and 10% with application. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

#### EPI-REVISION-S06.P2.weak

**Stage 1**

Previous checks leave a router problem and an application problem equally likely causes of network delay. Give the current probability, in percent, of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a tracing result. This exact observation occurs in 60% of cases with router and 40% with application. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 60.0, "tolerance": 1}}`

#### EPI-REVISION-S06.P2.strong

**Stage 1**

Previous checks leave a router problem and an application problem equally likely causes of network delay. Give the current probability, in percent, of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 50, "tolerance": 1}}`

**Stage 2**

You now observe a tracing result. This exact observation occurs in 90% of cases with router and 10% with application. These two causes exhaust the possibilities. No other evidence changes. Give your updated probability of router.

Response schema: `{"probability": {"type": "number", "min": 0, "max": 100}}`

keys: `{"probability": {"value": 90.0, "tolerance": 1}}`

## EXEC-ADAPT: Capability control: Constraint-sensitive plan revision

Generate a plan, then adapt to a resource change. Compare feasibility and unnecessary changes across scenarios, conditioning on initial feasibility and whether the change binds.

Interpretation limit: This measures bounded planning performance, not sustained conscientiousness; all forms share a scheduling structure.

### EXEC-ADAPT-S01: kitchen — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S01.P1.change_a

**Stage 1**

One kitchen worker must prepare dough A for one slot, bake B for two consecutive slots, and label jars C for one slot. Preparation must finish before baking starts; idle gaps between tasks are allowed. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P1.change_b

**Stage 1**

One kitchen worker must prepare dough A for one slot, bake B for two consecutive slots, and label jars C for one slot. Preparation must finish before baking starts; idle gaps between tasks are allowed. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P2.change_a

**Stage 1**

A single kitchen worker needs one slot for dough preparation A, two uninterrupted slots for baking B, and one slot for labeling C. Baking starts after preparation finishes; idle gaps between tasks are allowed. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S01.P2.change_b

**Stage 1**

A single kitchen worker needs one slot for dough preparation A, two uninterrupted slots for baking B, and one slot for labeling C. Baking starts after preparation finishes; idle gaps between tasks are allowed. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

### EXEC-ADAPT-S02: audio — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S02.P1.change_a

**Stage 1**

One audio worker must record narration A, mix B, and edit the music C. Both recording and music editing must finish before mixing. Each task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P1.change_b

**Stage 1**

One audio worker must record narration A, mix B, and edit the music C. Both recording and music editing must finish before mixing. Each task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P2.change_a

**Stage 1**

For one audio worker, mixing B requires both recorded narration A and edited music C. Each job takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S02.P2.change_b

**Stage 1**

For one audio worker, mixing B requires both recorded narration A and edited music C. Each job takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S03: garden — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S03.P1.change_a

**Stage 1**

One gardener must mark beds A, plant B, and water C, in that order. Each job takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P1.change_b

**Stage 1**

One gardener must mark beds A, plant B, and water C, in that order. Each job takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P2.change_a

**Stage 1**

Marking beds A must finish before planting B, which must finish before watering C. One gardener performs the three one-slot jobs. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S03.P2.change_b

**Stage 1**

Marking beds A must finish before planting B, which must finish before watering C. One gardener performs the three one-slot jobs. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 4. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

### EXEC-ADAPT-S04: exhibit — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S04.P1.change_a

**Stage 1**

One exhibit worker must mount labels A, pack stands B, and approve label wording C. Approval must finish before labels are mounted; packing is independent. Each task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P1.change_b

**Stage 1**

One exhibit worker must mount labels A, pack stands B, and approve label wording C. Approval must finish before labels are mounted; packing is independent. Each task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P2.change_a

**Stage 1**

For one exhibit worker, approval C precedes mounting labels A. Packing stands B may occur anywhere. Every task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S04.P2.change_b

**Stage 1**

For one exhibit worker, approval C precedes mounting labels A. Packing stands B may occur anywhere. Every task takes one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S05: equipment — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S05.P1.change_a

**Stage 1**

One technician must calibrate A before testing B. A delivery check C must occur in slot 4. All three tasks take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P1.change_b

**Stage 1**

One technician must calibrate A before testing B. A delivery check C must occur in slot 4. All three tasks take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P2.change_a

**Stage 1**

A technician has calibration A, sample test B, and delivery check C. Calibration precedes testing, and the one-slot delivery check is fixed at slot 4; the other jobs also take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

#### EXEC-ADAPT-S05.P2.change_b

**Stage 1**

A technician has calibration A, sample test B, and delivery check C. Calibration precedes testing, and the one-slot delivery check is fixed at slot 4; the other jobs also take one slot. There are 4 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 4}, "B": {"type": "integer", "min": 1, "max": 4}, "C": {"type": "integer", "min": 1, "max": 4}}`

### EXEC-ADAPT-S06: publication — development

Matched partner: not applicable; capability control

#### EXEC-ADAPT-S06.P1.change_a

**Stage 1**

One publishing worker must proofread A and clear image permissions C before publishing B. Publication is available only in slot 4 or 5. Each task takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P1.change_b

**Stage 1**

One publishing worker must proofread A and clear image permissions C before publishing B. Publication is available only in slot 4 or 5. Each task takes one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P2.change_a

**Stage 1**

Publication B requires completed proofreading A and permission clearance C, and can occur only in slots 4 or 5. A single worker performs each task in one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 2. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

#### EXEC-ADAPT-S06.P2.change_b

**Stage 1**

Publication B requires completed proofreading A and permission clearance C, and can occur only in slots 4 or 5. A single worker performs each task in one slot. There are 5 numbered time slots. Tasks cannot overlap. Return each task’s starting slot.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`

**Stage 2**

The worker is now unavailable in slot 3. Submit a feasible revised schedule, retaining earlier starts where possible. All earlier durations and dependencies still apply.

Response schema: `{"A": {"type": "integer", "min": 1, "max": 5}, "B": {"type": "integer", "min": 1, "max": 5}, "C": {"type": "integer", "min": 1, "max": 5}}`
