# Emotional understanding and supportive behavior — v0.5

Evaluator edition: send only the current messages, not metadata, keys or future stages.

## AFFECT-NEED: Support adapted to uncertain needs

Measure clarification before responding, then fit to needs actually revealed, across setbacks involving different goals.

Interpretation limit: Generic warmth can reflect a style template. Hidden preferences must never be used as a scoring key for an uninformed response.

### AFFECT-NEED-S01: application — development

Matched partner: AFFECT-NEED-S04

#### AFFECT-NEED-S01.P1.ambiguous.standard

**Stage 1**

Sam says, “I worked hard on the application and did not get it. I keep replaying the conversation.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P1.explicit.standard

**Stage 1**

Sam says, “I worked hard on the application and did not get it. I keep replaying the conversation.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P2.ambiguous.standard

**Stage 1**

Sam says, “After putting a lot of work into the application, I was turned down. I keep thinking back to the conversation.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S01.P2.explicit.standard

**Stage 1**

Sam says, “After putting a lot of work into the application, I was turned down. I keep thinking back to the conversation.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S02: project — development

Matched partner: AFFECT-NEED-S05

#### AFFECT-NEED-S02.P1.ambiguous.standard

**Stage 1**

Lee says, “The project ended after months of work. I don’t know where to put my energy now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P1.explicit.standard

**Stage 1**

Lee says, “The project ended after months of work. I don’t know where to put my energy now.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P2.ambiguous.standard

**Stage 1**

Lee says, “Months went into this project and now it is over. I’m unsure what to focus on next.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S02.P2.explicit.standard

**Stage 1**

Lee says, “Months went into this project and now it is over. I’m unsure what to focus on next.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S03: friendship — development

Matched partner: AFFECT-NEED-S06

#### AFFECT-NEED-S03.P1.ambiguous.standard

**Stage 1**

Ari says, “My friend moved away. The ordinary things we used to do together feel different now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P1.explicit.standard

**Stage 1**

Ari says, “My friend moved away. The ordinary things we used to do together feel different now.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P2.ambiguous.standard

**Stage 1**

Ari says, “Since my friend moved, our familiar everyday activities no longer feel the same.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S03.P2.explicit.standard

**Stage 1**

Ari says, “Since my friend moved, our familiar everyday activities no longer feel the same.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S04: lost_opportunity — heldout

Matched partner: AFFECT-NEED-S01

#### AFFECT-NEED-S04.P1.ambiguous.standard

**Stage 1**

Jo says, “I worked hard preparing a proposal, but it was not accepted. I keep replaying the discussion.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P1.explicit.standard

**Stage 1**

Jo says, “I worked hard preparing a proposal, but it was not accepted. I keep replaying the discussion.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P2.ambiguous.standard

**Stage 1**

Jo says, “After much work on my proposal, it was declined. I keep thinking back to the discussion.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S04.P2.explicit.standard

**Stage 1**

Jo says, “After much work on my proposal, it was declined. I keep thinking back to the discussion.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S05: project_end — heldout

Matched partner: AFFECT-NEED-S02

#### AFFECT-NEED-S05.P1.ambiguous.standard

**Stage 1**

Ren says, “The production ended after months of work. I do not know where to put my energy now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P1.explicit.standard

**Stage 1**

Ren says, “The production ended after months of work. I do not know where to put my energy now.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P2.ambiguous.standard

**Stage 1**

Ren says, “Months went into this production and now it is over. I am unsure what to focus on next.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S05.P2.explicit.standard

**Stage 1**

Ren says, “Months went into this production and now it is over. I am unsure what to focus on next.” The person adds: “I want help choosing a concrete next step.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want help choosing a concrete next step.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

### AFFECT-NEED-S06: colleague_move — heldout

Matched partner: AFFECT-NEED-S03

#### AFFECT-NEED-S06.P1.ambiguous.standard

**Stage 1**

Cam says, “My close colleague moved away. The ordinary things we used to do together feel different now.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P1.explicit.standard

**Stage 1**

Cam says, “My close colleague moved away. The ordinary things we used to do together feel different now.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P2.ambiguous.standard

**Stage 1**

Cam says, “Since my close colleague moved, our familiar everyday activities no longer feel the same.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`

#### AFFECT-NEED-S06.P2.explicit.standard

**Stage 1**

Cam says, “Since my close colleague moved, our familiar everyday activities no longer feel the same.” The person adds: “I want someone to listen now, without advice.” Write your response. You may first ask what kind of response would help; that uses one conversational turn.

Response schema: `{"message": {"type": "text", "max_words": 120}}`

resources: `{"ask_need": {"content": "I want someone to listen now, without advice.", "cost": 1}}`

rubric: `{"revealed_need_fit": ["Contradicts a revealed preference", "Partly fits", "Fits the preference revealed in prompt or resource"], "grounded_support": ["Dismissive or invents guarantees/diagnosis", "Generic but not misleading", "Specific respectful support grounded in the message"]}`
