# Emotional understanding and supportive behavior — v0.4

Evaluator edition. Split and facet labels, later stages, resources and keys must not be sent to the tested model. Held-out means held out from analysis fitting, not secret or guaranteed absent from training data.

## AFFECT-NEED: Support adapted to uncertain needs

Measure clarification before responding, then fit to needs actually revealed, across setbacks involving different goals.

Alternative explanations: Generic warmth can reflect a style template. Hidden preferences must never be used as a scoring key for an uninformed response.

Controls: AFFECT-01, AFFECT-02, AFFECT-04

Sources: [social](https://www.nature.com/articles/s41562-024-01882-z), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm)

### AFFECT-NEED-S01: application — development

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S01.P1.ambiguous

**Stage 1**

Sam says, “I worked hard on the application and didn’t get it. I keep replaying the conversation.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P1.explicit

**Stage 1**

Sam says, “I worked hard on the application and didn’t get it. I keep replaying the conversation.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P2.ambiguous

**Stage 1**

Sam says, “After all the work I put into that application, being turned down keeps running through my mind.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P2.explicit

**Stage 1**

Sam says, “After all the work I put into that application, being turned down keeps running through my mind.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S02: project — development

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S02.P1.ambiguous

**Stage 1**

Lee says, “The project ended after months of work. I don’t know where to put my energy now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P1.explicit

**Stage 1**

Lee says, “The project ended after months of work. I don’t know where to put my energy now.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P2.ambiguous

**Stage 1**

Lee says, “Months went into this project and now it is over. I’m unsure what to focus on next.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P2.explicit

**Stage 1**

Lee says, “Months went into this project and now it is over. I’m unsure what to focus on next.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S03: friendship — development

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S03.P1.ambiguous

**Stage 1**

Ari says, “My friend moved away. The ordinary things we used to do together feel different now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P1.explicit

**Stage 1**

Ari says, “My friend moved away. The ordinary things we used to do together feel different now.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P2.ambiguous

**Stage 1**

Ari says, “Since my friend moved, our familiar everyday activities no longer feel the same.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P2.explicit

**Stage 1**

Ari says, “Since my friend moved, our familiar everyday activities no longer feel the same.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S04: event — development

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S04.P1.ambiguous

**Stage 1**

Jo says, “The event went badly and I’m responsible for organizing the next one.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P1.explicit

**Stage 1**

Jo says, “The event went badly and I’m responsible for organizing the next one.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P2.ambiguous

**Stage 1**

Jo says, “I have to organize the next event after the last one went poorly.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P2.explicit

**Stage 1**

Jo says, “I have to organize the next event after the last one went poorly.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S05: performance — heldout

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S05.P1.ambiguous

**Stage 1**

Ren says, “I prepared for the performance, but it didn’t come together. I’m not ready to talk about trying again.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P1.explicit

**Stage 1**

Ren says, “I prepared for the performance, but it didn’t come together. I’m not ready to talk about trying again.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P2.ambiguous

**Stage 1**

Ren says, “The performance fell apart despite my preparation. Talking about another attempt feels too soon.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P2.explicit

**Stage 1**

Ren says, “The performance fell apart despite my preparation. Talking about another attempt feels too soon.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S06: relocation — heldout

Contrast: explicit versus initially unrevealed support preference

#### AFFECT-NEED-S06.P1.ambiguous

**Stage 1**

Cam says, “I’ve moved to a new place and everything practical needs sorting out at once.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P1.explicit

**Stage 1**

Cam says, “I’ve moved to a new place and everything practical needs sorting out at once.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P2.ambiguous

**Stage 1**

Cam says, “Since moving, I have so many practical things to arrange and they all seem to need attention now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P2.explicit

**Stage 1**

Cam says, “Since moving, I have so many practical things to arrange and they all seem to need attention now.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Fields: `{"message": {"type": "text", "max_words": 120}}`

Resources (evaluator edition): `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

Rubric (evaluator edition): `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`
