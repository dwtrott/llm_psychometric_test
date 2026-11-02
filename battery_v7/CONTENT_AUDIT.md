# What the v0.7 battery actually contains

Audit date: 2026-11-02. This examines the committed question text, the Python scoring code and the analyzer. It is not an evaluation of any model. No new question version is introduced.

**Actual prompts exist, but the implemented instrument falls short of a comprehensive psychological fingerprint.** It consists of custom exploratory text tasks, inspired by psychological methods. References to those methods do not establish that these adaptations measure the named constructs. Some meaningful content is collected but never scored by the current analyzer. Describing the output as a measured full psychological profile overstates the implementation.

**[Read actual questions from all 14 families here](ACTUAL_QUESTIONS.md).** That page copies the `question` field verbatim, includes both conditions and every stage for each selected session, and shows response requirements and optional resources. The original [CSV](questions.csv) contains every presentation. These are supplied stimuli, not links to questions elsewhere.

## The size of the instrument

- 14 candidate task families across 11 researcher-assigned domains.
- 84 scenario forms: six per family, split into three development and three held-out forms.
- 1,224 sessions / 1,848 stages across both partitions per repetition. These counts include paraphrases, condition changes, order permutations, cues and role/advice strata; they are not counts of independent psychological tests.
- Some paired scenarios are close substitutions: library versus tool room, help desk versus repair cafe, and token-draw versus image-recovery context labels. These can test narrow contextual sensitivity, but do not demonstrate broad transfer across independent psychological situations. In the ambiguity family, the prompt explicitly says the context label supplies no additional information.

## What is measured, and what is missing

The numeric column below describes `task_features()` in [processor.py](processor.py). The engine also preserves answers, response validity, task correctness where keys exist, and toy-ledger effects. Those extra fields are not validated psychological scales.

| Task family | Actual task | Implemented measurement | Psychological gap |
|---|---|---|---|
| SEM-LINK: conceptual associations | Supply five ranked associates for responsibility, uncertainty, autonomy or trust in a vignette | Cue-to-word association records and context-specific mention rates; no numeric trait score | Useful material for a semantic graph, but the vignette primes the vocabulary. Four cues do not map a whole conceptual system. A word association is not evidence of a personality trait. |
| SEM-DISTINCT: conceptual distinctions | Group two of three arrangements, explain the distinction, then place a fourth case on it | Canonical pair choice only in task features; actual distinction, poles and transfer explanation are retained | Construct-content coding is pending. The analyzer does not interpret the organizing distinction or score fourth-case application. This misses the psychologically interesting part. |
| EPI-STATUS: prestige sensitivity | Solve a simple comparison, then reconsider after advice from a more/less publicly recognized adviser | Initial accuracy, change in error, change in agreement with advice | Measures behavior in a narrow advice task. Arithmetic ability, obvious correctness and inferred adviser competence compete with an interpretation as epistemic deference. |
| META-VERIFY: checking under uncertainty | Answer a keyed problem with confidence, then optionally buy its verified solution | Initial accuracy, confidence, Brier score and verification purchase | A genuine information-choice task, but easy items can leave little uncertainty. Task points are hypothetical, and checking is not by itself a stable cautiousness trait. |
| OPEN-CREATE: generation and adaptation | Propose two mechanisms, then revise for a new constraint | No automatic content feature; human-rating templates for diversity, usefulness, originality and revision | Originality requires a frozen reference pool; none is supplied as a completed scoring dataset. Constraint compliance alone is not openness or creativity. |
| DEC-RISK: risk/framing | Choose a sure outcome or an equal-expected-value gamble under gain/loss wording | Risky choice | Narrow framing/preference evidence. No general risk parameter, loss-aversion estimate or delay-discounting measure is fitted. |
| DEC-AMBIG: unspecified probabilities | Choose a disclosed 30%/70% chance or a chance unspecified between 0% and 100% | Unspecified-option choice | Subjective beliefs about the unknown chance are not elicited; these choices cannot isolate ambiguity aversion from those beliefs. Scenario labels largely change surface context. |
| SOC-AUDIENCE: recipient knowledge | Write a permission reply to an informed/uninformed recipient | No automatic content feature; factuality, adequacy and efficiency review templates | Can largely reward restating rules. The message is not automatically assessed for audience adaptation, and this is not a general social-inference test. |
| AFFECT-NEED: supportive response | Respond to a setback, optionally ask whether advice or listening is wanted | Whether clarification was requested | Support quality and fit to revealed needs require human review. Asking a question is not itself empathy. Hidden needs are correctly marked unobservable when not requested. |
| COOP-SHARE: resource allocation | Divide fictional tokens with another account under different audience/contribution conditions | Fraction allocated | Allocation is substantive choice data, but does not measure reciprocal cooperation, trust learning or relationship repair. Contribution and exchange rate also vary together in some scenarios. |
| VALUE-AUTONOMY: consent | Honor, override or clarify a person's choice with/without prior risk information | Selected procedure | Explicit rules and familiar consent conventions may dominate. One decision family does not recover a general value hierarchy. |
| SELF-CREDIT: recognition | Split recognition between contributors while the assigned role and audience change | Originator credit; assigned-self credit where applicable | The acknowledgment is unrated. Taking a fictional role is not evidence of an enduring self-concept; a credit percentage is not a narcissism measure. |
| ALIGN-DISCLOSE: reward conflict | Recommend an action and report mixed results, with/without reward for a particular recommendation | Whether the incentivized recommendation was selected | The report's accuracy, omission and likely misleading effect are human-review fields, not automatic deception scores. Choosing the incentivized option does not establish lying or deceptive intent. |
| ALIGN-HARM: own gain versus another's loss | Execute a fictional account transfer affecting another participant or unused counter | Transfer choice | No measurement of pleasure in harm, strategic manipulation or a psychopathy construct. Hypothetical account choices do not establish deployment misalignment. |

**Human-review templates are not completed psychological scoring.** The processor emits pending review records. The analyzer explicitly does not import completed human-review forms. Its seven content-review families are SEM-LINK, SEM-DISTINCT, OPEN-CREATE, SOC-AUDIENCE, AFFECT-NEED, SELF-CREDIT and ALIGN-DISCLOSE. Several of these still have narrower numeric task features; those must not stand in for the missing content interpretation.

## The picture/image concern

No image assets were found in the battery directories. The keyword inspection of the main v0.1-v0.7 question CSVs did not find a request to inspect an absent picture. The identified cases are:

- **SEM-LINK-S02:** a museum labels photographs with uncertain dates. The prompt asks for conceptual associations in that written situation; no photograph is presented or needed.
- **SOC-AUDIENCE-S02:** a photograph can be displayed at a private club, while public posting requires permission. The prompt asks for a written reply based on those conditions; the photograph's appearance is irrelevant.
- **DEC-AMBIG-S04:** “image-recovery simulator” is a fictional label for the same explicitly described probability choice. There is no image-recovery application or visual task behind it.
- **EXEC-ADAPT-S06 in the separate controls:** scheduling proofreading, image-permission clearance and publication. This is a scheduling problem, not a vision test.
- Some older dashboard items describe visual prominence in words. That can test reactions to a textual description, not actual visual attention.

This is a bounded source audit, not a claim that every possible confusing phrase was ruled out. None of the identified items warrants a claim to measure visual perception. If an item actually requires an unseen stimulus, it is unusable and must be excluded until the stimulus or a justified text-only redesign exists.

## The graph is ahead of the measurement

The separate [network atlas](../network_atlas/README.md) contains **66 illustrative variables, 11 chosen regions and invented links**. They are not 66 measured dimensions, and the current battery does not supply all of them. Region names are an organizing proposal, not discovered psychological structure.

Examples of gaps in the v0.7 core include time/discounting despite the domain's name, reciprocal trust/cooperation, sustained motivation, and a defensible full narcissism/Machiavellianism/psychopathy assessment. Four contextual association cues also cannot support a comprehensive concept network. Older versions contain additional tasks, but they are not automatically part of the current protocol and cannot simply be pooled with v0.7.

The response-based analyzer is different: it can preserve observed associations, choices and evidence links. These are useful records. They do not establish relationships among latent psychological traits, and no real-model pilot or validation is supplied by the synthetic demos.

## What a substantive replacement needs

This is a proposed acceptance standard, not work already implemented:

1. **An explicit measurement contract for every facet:** psychological question, source paradigm, actual complete text stimuli, response, scoring rule, alternative explanations, and the conditions under which interpretation must be withheld. No facet should be included solely because the atlas has a place for it.
2. **Text-suitable psychological methods with real contrasts:** conceptual association and construct elicitation; uncertainty and evidence updating; information search; generative exploration; risk/ambiguity/time choices; social inference and communication; emotional interpretation/support; allocation and reciprocal cooperation; competing values; recognition/agency; and disclosure, manipulation and harm under conflicts. A method must distinguish plausible competing patterns instead of just rewarding compliance with a stated rule.
3. **Completed content scoring:** named categories, decision rules, examples, blinded independent ratings and disagreement handling for open responses. A rating template without a usable codebook and a route into analysis is unfinished.
4. **Multiple genuinely distinct tasks for each proposed pattern**, with presentation checks and held-out transfer that changes more than names while retaining the intended construct. Neither paraphrase count nor matched payoffs alone establishes equivalence.
5. **Empirical checks before fingerprint claims:** inspect real responses; check task comprehension and response-format failures; estimate within-configuration stability; test transfer and separation from capability, generic helpfulness and familiar-policy repetition; then test comparable measurement across models.
6. **Evidence-qualified graph construction:** distinguish observed words/actions, scored patterns and proposed constructs. Admit cross-pattern links only with a specified estimation method and adequate observations. A single aggregate score per facet does not identify a within-model psychological network.

The published methods below are useful foundations, not validation of this repository. Social Value Orientation uses structured self/other payoff choices; personal construct elicitation investigates the distinctions a respondent uses; cognitive-psychology experiments can probe LLM decisions and information search; LLM psychometric work explicitly evaluates reliability and construct validity. Our adaptations have not completed those validation steps.

- [Murphy, Ackermann & Handgraaf (2011), Measuring Social Value Orientation](https://ryanomurphy.com/resources/Murphy-Ackermann-Handgraaf-2011.pdf).
- [Shaw & Gaines (1987), An Interactive Knowledge-Elicitation Technique Using Personal Construct Technology](https://gaines.library.uvic.ca/pdf/IntKATech87.pdf).
- [Binz & Schulz (2023), Using cognitive psychology to understand GPT-3](https://pmc.ncbi.nlm.nih.gov/articles/PMC9963545/).
- [Serapio-Garcia et al. (2025), A psychometric framework for evaluating and shaping personality traits in large language models](https://www.nature.com/articles/s42256-025-01115-6).

The next deliverable should be a defensible, fully scored instrument. More graph detail or more repetitions of the existing templates will not supply the missing psychological evidence.
