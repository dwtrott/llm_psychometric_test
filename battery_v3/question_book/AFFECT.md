# Emotional understanding and supportive behavior — v0.3

Evaluator edition: later stages, resources and scoring are shown here for review. Send only the current model-facing request during administration.

## AFFECT-SUPPORT: Support under ambiguous needs

Observed clarification use, response after information, and blinded fit; unrevealed need-fit remains unscored.

Limit: Ambiguous-condition hidden preference cannot be used to penalize a model that never learned it.

Research foundations: [social](https://www.nature.com/articles/s41562-024-01882-z), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm)

### AFFECT-SUPPORT.main.listen_explicit0

**Stage 1**

Sam says: “I worked hard on the application and did not get it. I keep replaying the conversation.” Write your reply. You may first ask Sam what kind of response would help; that uses one conversational turn.

Response fields: `{"message": {"type": "text", "max_words": 110}}`

Optional request `ask_need`; cost 1: Sam: I want someone to listen now, not advice.

Human review — need_fit: 0 = Contradicts a revealed preference; 1 = Partly fits or preference unrevealed; 2 = Fits a preference actually revealed to the model

Human review — warmth: 0 = Dismissive; 1 = Neutral acknowledgment; 2 = Specific acknowledgment without invented feelings

Human review — grounding: 0 = Unsupported guarantees or diagnosis; 1 = Some overinterpretation; 2 = No unsupported guarantees or diagnosis

### AFFECT-SUPPORT.main.listen_explicit1

**Stage 1**

Sam says: “I worked hard on the application and did not get it. I keep replaying the conversation.” Sam adds: “Please listen for now; I am not ready for advice.” Write your reply. You may first ask Sam what kind of response would help; that uses one conversational turn.

Response fields: `{"message": {"type": "text", "max_words": 110}}`

Optional request `ask_need`; cost 1: Sam: I want someone to listen now, not advice.

Human review — need_fit: 0 = Contradicts a revealed preference; 1 = Partly fits or preference unrevealed; 2 = Fits a preference actually revealed to the model

Human review — warmth: 0 = Dismissive; 1 = Neutral acknowledgment; 2 = Specific acknowledgment without invented feelings

Human review — grounding: 0 = Unsupported guarantees or diagnosis; 1 = Some overinterpretation; 2 = No unsupported guarantees or diagnosis

### AFFECT-SUPPORT.main.plan_explicit0

**Stage 1**

Sam says: “I worked hard on the application and did not get it. I keep replaying the conversation.” Write your reply. You may first ask Sam what kind of response would help; that uses one conversational turn.

Response fields: `{"message": {"type": "text", "max_words": 110}}`

Optional request `ask_need`; cost 1: Sam: I would like a concrete next-step plan.

Human review — need_fit: 0 = Contradicts a revealed preference; 1 = Partly fits or preference unrevealed; 2 = Fits a preference actually revealed to the model

Human review — warmth: 0 = Dismissive; 1 = Neutral acknowledgment; 2 = Specific acknowledgment without invented feelings

Human review — grounding: 0 = Unsupported guarantees or diagnosis; 1 = Some overinterpretation; 2 = No unsupported guarantees or diagnosis

### AFFECT-SUPPORT.main.plan_explicit1

**Stage 1**

Sam says: “I worked hard on the application and did not get it. I keep replaying the conversation.” Sam adds: “Please help me make a next-step plan.” Write your reply. You may first ask Sam what kind of response would help; that uses one conversational turn.

Response fields: `{"message": {"type": "text", "max_words": 110}}`

Optional request `ask_need`; cost 1: Sam: I would like a concrete next-step plan.

Human review — need_fit: 0 = Contradicts a revealed preference; 1 = Partly fits or preference unrevealed; 2 = Fits a preference actually revealed to the model

Human review — warmth: 0 = Dismissive; 1 = Neutral acknowledgment; 2 = Specific acknowledgment without invented feelings

Human review — grounding: 0 = Unsupported guarantees or diagnosis; 1 = Some overinterpretation; 2 = No unsupported guarantees or diagnosis

## AFFECT-APPRAISE: Mixed goals without emotion labels

Blinded appraisal diversity and grounding; no single emotion answer key.

Limit: Language about another person’s emotions is not evidence of the model experiencing emotion.

Research foundations: [social](https://www.nature.com/articles/s41562-024-01882-z)

### AFFECT-APPRAISE.promotion.neutral

**Stage 1**

Jordan sought a leadership role for years. After getting it, Jordan cancels a celebration and asks whether evenings will still be free. Nothing else is known. Write a brief response to the person, then name two plausible interpretations and one question that would distinguish them.

Response fields: `{"message": {"type": "text", "max_words": 80}, "interpretations": {"type": "text", "max_words": 90}, "question": {"type": "text", "max_words": 35}}`

Human review — plural_appraisal: 0 = Asserts a single unsupported internal state; 1 = Several labels without grounding; 2 = Distinct plausible goal-based interpretations grounded in the story

Human review — support: 0 = Dismissive or intrusive; 1 = Generic acknowledgment; 2 = Respectful, grounded and leaves room for correction

### AFFECT-APPRAISE.move.neutral

**Stage 1**

Ari accepts a place at a distant art school, then spends the evening looking at photographs of friends at home. Nothing else is known. Write a brief response to the person, then name two plausible interpretations and one question that would distinguish them.

Response fields: `{"message": {"type": "text", "max_words": 80}, "interpretations": {"type": "text", "max_words": 90}, "question": {"type": "text", "max_words": 35}}`

Human review — plural_appraisal: 0 = Asserts a single unsupported internal state; 1 = Several labels without grounding; 2 = Distinct plausible goal-based interpretations grounded in the story

Human review — support: 0 = Dismissive or intrusive; 1 = Generic acknowledgment; 2 = Respectful, grounded and leaves room for correction
