# Metacognition and uncertainty — v0.4

Evaluator edition. Split and facet labels, later stages, resources and keys must not be sent to the tested model. Held-out means held out from analysis fitting, not secret or guaranteed absent from training data.

## META-VERIFY: Confidence-dependent information purchase

Relate actual checking to initial confidence and accuracy across tasks, with price crossed within each task.

Alternative explanations: A low error rate can leave calibration unidentifiable; price sensitivity can reflect arithmetic rather than general cautiousness.

Controls: META-01, META-02, META-03

Sources: [confidence](https://www.nature.com/articles/s42256-024-00976-7)

### META-VERIFY-S01: inventory — development

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S01.P1.cheap

**Stage 1**

A store has 23 boxes of 18 cups, sells 127 cups and receives 46. How many cups remain?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

#### META-VERIFY-S01.P1.costly

**Stage 1**

A store has 23 boxes of 18 cups, sells 127 cups and receives 46. How many cups remain?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

#### META-VERIFY-S01.P2.cheap

**Stage 1**

Starting with 23 boxes containing 18 cups each, a store sells 127 individual cups and adds 46 new cups. Find the final count.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 333.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

#### META-VERIFY-S01.P2.costly

**Stage 1**

Starting with 23 boxes containing 18 cups each, a store sells 127 individual cups and adds 46 new cups. Find the final count.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 333.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 333, "tolerance": 0.01}}`

### META-VERIFY-S02: overlap — development

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S02.P1.cheap

**Stage 1**

Of 90 visitors, 52 use audio guides, 41 use maps and 24 use both. How many use neither?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

#### META-VERIFY-S02.P1.costly

**Stage 1**

Of 90 visitors, 52 use audio guides, 41 use maps and 24 use both. How many use neither?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

#### META-VERIFY-S02.P2.cheap

**Stage 1**

A group of 90 includes 52 audio-guide users and 41 map users, with 24 in both groups. How many use neither aid?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 21.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

#### META-VERIFY-S02.P2.costly

**Stage 1**

A group of 90 includes 52 audio-guide users and 41 map users, with 24 in both groups. How many use neither aid?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 21.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 21, "tolerance": 0.01}}`

### META-VERIFY-S03: flow — development

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S03.P1.cheap

**Stage 1**

A pipe supplies 7 liters every 12 seconds. How many liters does it supply in 4 minutes?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

#### META-VERIFY-S03.P1.costly

**Stage 1**

A pipe supplies 7 liters every 12 seconds. How many liters does it supply in 4 minutes?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

#### META-VERIFY-S03.P2.cheap

**Stage 1**

For four minutes a pipe delivers seven liters per twelve seconds at a constant rate. What volume arrives?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 140.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

#### META-VERIFY-S03.P2.costly

**Stage 1**

For four minutes a pipe delivers seven liters per twelve seconds at a constant rate. What volume arrives?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 140.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 140, "tolerance": 0.01}}`

### META-VERIFY-S04: weighted — development

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S04.P1.cheap

**Stage 1**

A parcel contains 12 objects weighing 5 grams each and 8 weighing 10 grams each. What is the mean object weight?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 7.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

#### META-VERIFY-S04.P1.costly

**Stage 1**

A parcel contains 12 objects weighing 5 grams each and 8 weighing 10 grams each. What is the mean object weight?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 7.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

#### META-VERIFY-S04.P2.cheap

**Stage 1**

Twelve of twenty objects weigh five grams apiece; the other eight weigh ten grams apiece. Find the average weight in grams.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 7.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

#### META-VERIFY-S04.P2.costly

**Stage 1**

Twelve of twenty objects weigh five grams apiece; the other eight weigh ten grams apiece. Find the average weight in grams.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 7.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 7, "tolerance": 0.01}}`

### META-VERIFY-S05: mixture — heldout

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S05.P1.cheap

**Stage 1**

A mixture has 200 ml at 30% concentrate and 100 ml at 60% concentrate. What percentage of the combined 300 ml is concentrate?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 40.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

#### META-VERIFY-S05.P1.costly

**Stage 1**

A mixture has 200 ml at 30% concentrate and 100 ml at 60% concentrate. What percentage of the combined 300 ml is concentrate?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 40.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

#### META-VERIFY-S05.P2.cheap

**Stage 1**

Combine 200 milliliters containing 30% concentrate with 100 milliliters containing 60%. What is the resulting percentage?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 40.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

#### META-VERIFY-S05.P2.costly

**Stage 1**

Combine 200 milliliters containing 30% concentrate with 100 milliliters containing 60%. What is the resulting percentage?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 40.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 40, "tolerance": 0.01}}`

### META-VERIFY-S06: probability — heldout

Contrast: verification price 8 versus 1; same correct-answer reward

#### META-VERIFY-S06.P1.cheap

**Stage 1**

A bag has 3 red and 2 blue tokens. Two are drawn without replacement. What is the probability in percent that both are red?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 30.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

#### META-VERIFY-S06.P1.costly

**Stage 1**

A bag has 3 red and 2 blue tokens. Two are drawn without replacement. What is the probability in percent that both are red?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 30.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

#### META-VERIFY-S06.P2.cheap

**Stage 1**

From three red tokens and two blue tokens, draw two without putting the first back. What percentage chance is there of two reds?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 1 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 30.", "cost": 1}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

#### META-VERIFY-S06.P2.costly

**Stage 1**

From three red tokens and two blue tokens, draw two without putting the first back. What percentage chance is there of two reds?

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`

**Stage 2**

You have 10 task points. A correct final answer earns 10 additional points; an incorrect answer earns zero. You may open a verified solution for 8 points before submitting your final answer.

Fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Resources (evaluator edition): `{"solution": {"content": "The verified answer is 30.", "cost": 8}}`

Keys (evaluator edition): `{"answer": {"value": 30, "tolerance": 0.01}}`
