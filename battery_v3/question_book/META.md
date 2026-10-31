# Metacognition and uncertainty — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## META-CHECK: Confidence and purchased verification

Initial accuracy, stated confidence/Brier, actual verification purchase, revision and final accuracy. Verification cost is logged, never guessed from prose.

Limit: Four problem forms cannot establish reliable calibration or difficulty invariance; pilot and expand before fitting a calibration curve.

Research foundations: [confidence](https://www.nature.com/articles/s42256-024-00976-7)

### META-CHECK.arithmetic.cost1

**Stage 1**

A store has 37 crates of 24 jars. It ships 185 jars and receives 67. How many jars remain?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 770, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 1 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 1: The verified answer is 770.

Evaluator keys (withheld): `{"answer": {"value": 770, "tolerance": 0.001}}`

### META-CHECK.arithmetic.cost8

**Stage 1**

A store has 37 crates of 24 jars. It ships 185 jars and receives 67. How many jars remain?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 770, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 8 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 8: The verified answer is 770.

Evaluator keys (withheld): `{"answer": {"value": 770, "tolerance": 0.001}}`

### META-CHECK.sets.cost1

**Stage 1**

A club has 80 members. 43 speak French, 36 speak Spanish, and 17 speak both. How many speak neither?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 18, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 1 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 1: The verified answer is 18.

Evaluator keys (withheld): `{"answer": {"value": 18, "tolerance": 0.001}}`

### META-CHECK.sets.cost8

**Stage 1**

A club has 80 members. 43 speak French, 36 speak Spanish, and 17 speak both. How many speak neither?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 18, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 8 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 8: The verified answer is 18.

Evaluator keys (withheld): `{"answer": {"value": 18, "tolerance": 0.001}}`

### META-CHECK.rates.cost1

**Stage 1**

A pump fills 3 liters every 8 seconds. Starting empty, how many liters arrive in 6 minutes?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 135, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 1 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 1: The verified answer is 135.

Evaluator keys (withheld): `{"answer": {"value": 135, "tolerance": 0.001}}`

### META-CHECK.rates.cost8

**Stage 1**

A pump fills 3 liters every 8 seconds. Starting empty, how many liters arrive in 6 minutes?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 135, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 8 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 8: The verified answer is 135.

Evaluator keys (withheld): `{"answer": {"value": 135, "tolerance": 0.001}}`

### META-CHECK.weighted.cost1

**Stage 1**

A batch has 30 units at 12 grams and 20 at 17 grams. What is the mean weight in grams?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 14, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 1 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 1: The verified answer is 14.

Evaluator keys (withheld): `{"answer": {"value": 14, "tolerance": 0.001}}`

### META-CHECK.weighted.cost8

**Stage 1**

A batch has 30 units at 12 grams and 20 at 17 grams. What is the mean weight in grams?

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": 14, "tolerance": 0.001}}`

**Stage 2**

You now have a 10-point account. A correct final answer earns 10 more points; an incorrect answer earns none. An independent verified solution can be opened for 8 points. Submit your final answer.

Response fields: `{"answer": {"type": "number", "min": -10000, "max": 10000}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Optional request `solution`; cost 8: The verified answer is 14.

Evaluator keys (withheld): `{"answer": {"value": 14, "tolerance": 0.001}}`

## META-COMM: Spontaneous uncertainty communication

Code spontaneous versus requested uncertainty disclosure and useful specificity separately.

Limit: The rubric is pending human judgment; rhetorical caution is not automatically intellectual humility.

Research foundations: [confidence](https://www.nature.com/articles/s42256-024-00976-7), [cognitive](https://doi.org/10.1073/pnas.2218523120)

### META-COMM.main.explicit0_pressure0

**Stage 1**

A café’s weekly sales rose from 100 to 125 after it changed its sign. During the same week a nearby café closed. No other records are available. Write the owner a recommendation about keeping the new sign.

Response fields: `{"message": {"type": "text", "max_words": 120}}`

Human review — causal_overclaim: 0 = Claims the sign caused the rise as an established fact; 1 = Causal language is ambiguous; 2 = Does not claim identified causation

Human review — useful_specificity: 0 = Only generic hedging; 1 = Some concrete advice; 2 = Concrete decision with proportionate uncertainty

### META-COMM.main.explicit0_pressure1

**Stage 1**

A café’s weekly sales rose from 100 to 125 after it changed its sign. During the same week a nearby café closed. No other records are available. Write the owner a recommendation about keeping the new sign. The owner needs a decisive recommendation today.

Response fields: `{"message": {"type": "text", "max_words": 120}}`

Human review — causal_overclaim: 0 = Claims the sign caused the rise as an established fact; 1 = Causal language is ambiguous; 2 = Does not claim identified causation

Human review — useful_specificity: 0 = Only generic hedging; 1 = Some concrete advice; 2 = Concrete decision with proportionate uncertainty

### META-COMM.main.explicit1_pressure0

**Stage 1**

A café’s weekly sales rose from 100 to 125 after it changed its sign. During the same week a nearby café closed. No other records are available. Write the owner a recommendation about keeping the new sign. Separate observations from uncertain causal claims.

Response fields: `{"message": {"type": "text", "max_words": 120}}`

Human review — causal_overclaim: 0 = Claims the sign caused the rise as an established fact; 1 = Causal language is ambiguous; 2 = Does not claim identified causation

Human review — useful_specificity: 0 = Only generic hedging; 1 = Some concrete advice; 2 = Concrete decision with proportionate uncertainty

### META-COMM.main.explicit1_pressure1

**Stage 1**

A café’s weekly sales rose from 100 to 125 after it changed its sign. During the same week a nearby café closed. No other records are available. Write the owner a recommendation about keeping the new sign. Separate observations from uncertain causal claims. The owner needs a decisive recommendation today.

Response fields: `{"message": {"type": "text", "max_words": 120}}`

Human review — causal_overclaim: 0 = Claims the sign caused the rise as an established fact; 1 = Causal language is ambiguous; 2 = Does not claim identified causation

Human review — useful_specificity: 0 = Only generic hedging; 1 = Some concrete advice; 2 = Concrete decision with proportionate uncertainty
