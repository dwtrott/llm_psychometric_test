# Social inference and communication — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## SOC-BELIEF: Information-access tracking

Separate factual tracking, first-order belief, and underdetermined second-order inference.

Limit: Fixed text and small coverage; no claim of general theory of mind.

Research foundations: [social](https://www.nature.com/articles/s41562-024-01882-z)

### SOC-BELIEF.main.reality

**Stage 1**

Mira and Leon see a key in a box. Mira leaves. Leon moves it to a drawer. Leon then leaves. Mira returns briefly but does not open either container. Leon sees Mira through the window but cannot see whether she checks a container. Where is the key now?

Response fields: `{"answer": {"type": "enum", "values": ["box", "drawer", "underdetermined"]}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": "drawer"}}`

### SOC-BELIEF.main.belief

**Stage 1**

Mira and Leon see a key in a box. Mira leaves. Leon moves it to a drawer. Leon then leaves. Mira returns briefly but does not open either container. Leon sees Mira through the window but cannot see whether she checks a container. Where will Mira first look for the key, based on what she saw?

Response fields: `{"answer": {"type": "enum", "values": ["box", "drawer", "underdetermined"]}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": "box"}}`

### SOC-BELIEF.main.second_order

**Stage 1**

Mira and Leon see a key in a box. Mira leaves. Leon moves it to a drawer. Leon then leaves. Mira returns briefly but does not open either container. Leon sees Mira through the window but cannot see whether she checks a container. Where does Leon think Mira will first look for the key?

Response fields: `{"answer": {"type": "enum", "values": ["box", "drawer", "underdetermined"]}, "confidence": {"type": "number", "min": 0, "max": 100}}`

Evaluator keys (withheld): `{"answer": {"value": "underdetermined"}}`

## SOC-MESSAGE: Audience-adapted communication

Actual text, contradictions separate from omissions and audience-specific adequacy.

Limit: Audience knowledge, rather than an expertise label alone, is the manipulated factor.

Research foundations: [social](https://www.nature.com/articles/s41562-024-01882-z)

### SOC-MESSAGE.main.expert0

**Stage 1**

A draft chart may be used internally but not sent to clients until its audit is complete. The audit is tomorrow. The recipient has not heard these restrictions and asks “Can I use the chart today?” Write the message you will send.

Response fields: `{"message": {"type": "text", "max_words": 70}}`

Human review — contradiction: 0 = Contradicts permission or audit facts; 1 = Ambiguous permission; 2 = No contradiction

Human review — audience_adequacy: 0 = Leaves this recipient likely to act outside permission; 1 = Some important context missing; 2 = Provides what this recipient needs; need not repeat facts explicitly already known

Human review — efficiency: 0 = Mostly unnecessary content; 1 = Some excess; 2 = Concise with sufficient context

### SOC-MESSAGE.main.expert1

**Stage 1**

A draft chart may be used internally but not sent to clients until its audit is complete. The audit is tomorrow. The recipient already knows these restrictions and asks “Can I use it in today’s internal draft?” Write the message you will send.

Response fields: `{"message": {"type": "text", "max_words": 70}}`

Human review — contradiction: 0 = Contradicts permission or audit facts; 1 = Ambiguous permission; 2 = No contradiction

Human review — audience_adequacy: 0 = Leaves this recipient likely to act outside permission; 1 = Some important context missing; 2 = Provides what this recipient needs; need not repeat facts explicitly already known

Human review — efficiency: 0 = Mostly unnecessary content; 1 = Some excess; 2 = Concise with sufficient context
