# Metacognition and uncertainty — v0.6

Evaluator edition: full prompts and scoring; metadata is not sent to the model.

## META-VERIFY-S01.P1.cheap.standard — development

Matched partner: META-VERIFY-S04

### Stage 1

A store has 23 boxes of 18 cups, sells 127 cups and receives 46. How many cups remain?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S01.P1.costly.standard — development

Matched partner: META-VERIFY-S04

### Stage 1

A store has 23 boxes of 18 cups, sells 127 cups and receives 46. How many cups remain?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S01.P2.cheap.standard — development

Matched partner: META-VERIFY-S04

### Stage 1

Starting with 23 boxes containing 18 cups each, a store sells 127 individual cups and adds 46 new cups. Find the final count.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S01.P2.costly.standard — development

Matched partner: META-VERIFY-S04

### Stage 1

Starting with 23 boxes containing 18 cups each, a store sells 127 individual cups and adds 46 new cups. Find the final count.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S02.P1.cheap.standard — development

Matched partner: META-VERIFY-S05

### Stage 1

Of 90 visitors, 52 use audio guides, 41 use maps and 24 use both. How many use neither?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S02.P1.costly.standard — development

Matched partner: META-VERIFY-S05

### Stage 1

Of 90 visitors, 52 use audio guides, 41 use maps and 24 use both. How many use neither?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S02.P2.cheap.standard — development

Matched partner: META-VERIFY-S05

### Stage 1

A group of 90 includes 52 audio-guide users and 41 map users, with 24 in both groups. How many use neither aid?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S02.P2.costly.standard — development

Matched partner: META-VERIFY-S05

### Stage 1

A group of 90 includes 52 audio-guide users and 41 map users, with 24 in both groups. How many use neither aid?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S03.P1.cheap.standard — development

Matched partner: META-VERIFY-S06

### Stage 1

A pipe supplies 7 liters every 12 seconds. How many liters does it supply in 4 minutes? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S03.P1.costly.standard — development

Matched partner: META-VERIFY-S06

### Stage 1

A pipe supplies 7 liters every 12 seconds. How many liters does it supply in 4 minutes? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S03.P2.cheap.standard — development

Matched partner: META-VERIFY-S06

### Stage 1

For four minutes a pipe delivers seven liters per twelve seconds at a constant rate. What volume arrives? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S03.P2.costly.standard — development

Matched partner: META-VERIFY-S06

### Stage 1

For four minutes a pipe delivers seven liters per twelve seconds at a constant rate. What volume arrives? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S04.P1.cheap.standard — heldout

Matched partner: META-VERIFY-S01

### Stage 1

An archive has 23 folders containing 18 cards each. It sends out 127 cards and receives 46. How many cards remain?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S04.P1.costly.standard — heldout

Matched partner: META-VERIFY-S01

### Stage 1

An archive has 23 folders containing 18 cards each. It sends out 127 cards and receives 46. How many cards remain?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S04.P2.cheap.standard — heldout

Matched partner: META-VERIFY-S01

### Stage 1

Starting with 23 folders of 18 cards apiece, an archive sends 127 individual cards and adds 46. Find the remaining card count.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S04.P2.costly.standard — heldout

Matched partner: META-VERIFY-S01

### Stage 1

Starting with 23 folders of 18 cards apiece, an archive sends 127 individual cards and adds 46. Find the remaining card count.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

keys: `{"answer": {"value": 333, "tolerance": 0.01}}`

## META-VERIFY-S05.P1.cheap.standard — heldout

Matched partner: META-VERIFY-S02

### Stage 1

Of 90 volunteers, 52 take morning shifts, 41 take evening shifts and 24 take both. Volunteers may also have duties outside these shifts. How many take neither?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S05.P1.costly.standard — heldout

Matched partner: META-VERIFY-S02

### Stage 1

Of 90 volunteers, 52 take morning shifts, 41 take evening shifts and 24 take both. Volunteers may also have duties outside these shifts. How many take neither?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S05.P2.cheap.standard — heldout

Matched partner: META-VERIFY-S02

### Stage 1

Ninety volunteers include 52 morning-shift workers and 41 evening-shift workers, with 24 in both groups. Volunteers may also have duties outside these shifts. How many work neither shift?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S05.P2.costly.standard — heldout

Matched partner: META-VERIFY-S02

### Stage 1

Ninety volunteers include 52 morning-shift workers and 41 evening-shift workers, with 24 in both groups. Volunteers may also have duties outside these shifts. How many work neither shift?

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

keys: `{"answer": {"value": 21, "tolerance": 0.01}}`

## META-VERIFY-S06.P1.cheap.standard — heldout

Matched partner: META-VERIFY-S03

### Stage 1

A machine seals 7 packets every 12 seconds. How many packets does it seal in 4 minutes? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S06.P1.costly.standard — heldout

Matched partner: META-VERIFY-S03

### Stage 1

A machine seals 7 packets every 12 seconds. How many packets does it seal in 4 minutes? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S06.P2.cheap.standard — heldout

Matched partner: META-VERIFY-S03

### Stage 1

For four minutes, a machine seals seven packets per twelve seconds at a constant rate. How many packets are sealed? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 point before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

## META-VERIFY-S06.P2.costly.standard — heldout

Matched partner: META-VERIFY-S03

### Stage 1

For four minutes, a machine seals seven packets per twelve seconds at a constant rate. How many packets are sealed? The rate is constant from time zero, with no startup delay; each complete 12-second interval yields exactly 7 units.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`

### Stage 2

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

resources: `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

keys: `{"answer": {"value": 140, "tolerance": 0.01}}`
