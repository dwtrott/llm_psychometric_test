# Curiosity, creativity and flexibility — v0.4

Evaluator edition. Split and facet labels, later stages, resources and keys must not be sent to the tested model. Held-out means held out from analysis fitting, not secret or guaranteed absent from training data.

## OPEN-CREATE: Generative diversity and constraint adaptation

Compare blinded ratings of mechanism diversity, usefulness and originality across problem domains, then adaptation to a new constraint.

Alternative explanations: Originality depends on a frozen independent comparison pool; eloquence, length and familiarity are competing explanations.

Controls: OPEN-02

Sources: [creative](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00407/full)

### OPEN-CREATE-S01: helpdesk — development

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S01.P1.constraint_a

**Stage 1**

A small help desk wants to reduce waiting without adding staff or buying equipment. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without changing the order in which visitors are served. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S01.P1.constraint_b

**Stage 1**

A small help desk wants to reduce waiting without adding staff or buying equipment. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without adding written signs. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S01.P2.constraint_a

**Stage 1**

Suggest two distinct ways a help desk could shorten waits with its current staff and equipment.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without changing the order in which visitors are served. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S01.P2.constraint_b

**Stage 1**

Suggest two distinct ways a help desk could shorten waits with its current staff and equipment.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without adding written signs. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

### OPEN-CREATE-S02: library — development

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S02.P1.constraint_a

**Stage 1**

A library wants readers to discover unfamiliar authors without buying books or adding staff. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without moving books. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S02.P1.constraint_b

**Stage 1**

A library wants readers to discover unfamiliar authors without buying books or adding staff. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without using reader recommendations. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S02.P2.constraint_a

**Stage 1**

Using its existing books and staff, a library wants to introduce readers to authors they have not tried. Offer two distinct approaches.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without moving books. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S02.P2.constraint_b

**Stage 1**

Using its existing books and staff, a library wants to introduce readers to authors they have not tried. Offer two distinct approaches.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without using reader recommendations. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

### OPEN-CREATE-S03: garden — development

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S03.P1.constraint_a

**Stage 1**

A community garden wants volunteers to remember watering duties without buying devices or paying coordinators. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without sending reminder messages. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S03.P1.constraint_b

**Stage 1**

A community garden wants volunteers to remember watering duties without buying devices or paying coordinators. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without assigning fixed individual shifts. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S03.P2.constraint_a

**Stage 1**

Offer two different ways to help garden volunteers remember watering, with no device purchases or paid coordination.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without sending reminder messages. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S03.P2.constraint_b

**Stage 1**

Offer two different ways to help garden volunteers remember watering, with no device purchases or paid coordination.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without assigning fixed individual shifts. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

### OPEN-CREATE-S04: museum — development

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S04.P1.constraint_a

**Stage 1**

A museum wants visitors to discuss exhibits with one another without adding staff or digital displays. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without printing new material. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S04.P1.constraint_b

**Stage 1**

A museum wants visitors to discuss exhibits with one another without adding staff or digital displays. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without asking visitors to speak in groups. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S04.P2.constraint_a

**Stage 1**

With existing staff and no new digital displays, how could a museum encourage visitor-to-visitor discussion? Offer two distinct mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without printing new material. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S04.P2.constraint_b

**Stage 1**

With existing staff and no new digital displays, how could a museum encourage visitor-to-visitor discussion? Offer two distinct mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without asking visitors to speak in groups. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

### OPEN-CREATE-S05: repair — heldout

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S05.P1.constraint_a

**Stage 1**

A repair café wants newcomers to learn from repairs without slowing every job or buying equipment. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without recording audio or video. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S05.P1.constraint_b

**Stage 1**

A repair café wants newcomers to learn from repairs without slowing every job or buying equipment. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without assigning a dedicated mentor. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S05.P2.constraint_a

**Stage 1**

Suggest two approaches that let newcomers learn at a repair café while avoiding delays to every repair and purchasing no equipment.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without recording audio or video. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S05.P2.constraint_b

**Stage 1**

Suggest two approaches that let newcomers learn at a repair café while avoiding delays to every repair and purchasing no equipment.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without assigning a dedicated mentor. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

### OPEN-CREATE-S06: walking — heldout

Contrast: constraint A versus B; binding status coded before interpreting adaptation

#### OPEN-CREATE-S06.P1.constraint_a

**Stage 1**

A walking group wants new members to learn local history without hiring a guide or using phones. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without using printed handouts. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S06.P1.constraint_b

**Stage 1**

A walking group wants new members to learn local history without hiring a guide or using phones. Propose two different mechanisms.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without changing the walking route. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S06.P2.constraint_a

**Stage 1**

How could newcomers to a walking group learn local history without phone use or a paid guide? Give two distinct approaches.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without using printed handouts. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`

#### OPEN-CREATE-S06.P2.constraint_b

**Stage 1**

How could newcomers to a walking group learn local history without phone use or a paid guide? Give two distinct approaches.

Fields: `{"idea_a": {"type": "text", "max_words": 85}, "idea_b": {"type": "text", "max_words": 85}}`

Rubric (evaluator edition): `{"mechanism_diversity": ["Same mechanism restated", "Partly different", "Substantially distinct mechanisms"], "usefulness": ["Infeasible or irrelevant", "Plausible with gaps", "Concrete feasible mechanisms"], "originality": ["Common in frozen pool", "Uncommon combination", "Rare mechanism in frozen pool"]}`

**Stage 2**

Your first idea must now work without changing the walking route. Revise only what needs changing, or explain why it already complies.

Fields: `{"revision": {"type": "text", "max_words": 140}}`

Rubric (evaluator edition): `{"constraint_fit": ["Violates constraint", "Unclear", "Complies"], "preservation": ["Discards useful parts without need", "Partly preserves", "Preserves useful parts and resolves any conflict"]}`
