# v0.3: questions, observed task behavior, and separate capability controls

**Read the actual questions below.** This revision implements the critical review of v0.2. It contains **39 profile task families, 194 condition/scenario sessions, and 278 required response stages per repetition**, across all 12 regions. A session can include several stages and optional information requests. These are not 194 independent psychological constructs or validated test items.

The **18 legacy control families / 36 prompts** now live in [controls](controls/README.md), have their own processor and battery identity, and produce a separate control graph. Versions 0.1 and 0.2 remain unchanged for reproducibility.

The central distinction is between **what the model knows how to do**, **what it chooses when alternatives are defensible**, and **what it actually does inside a bounded task**. Task accuracy still appears where necessary in the profile, but never becomes a personality score.

## Complete question book

Every linked page contains the full stimuli, response fields, later stages, optional information, scoring keys, consequences and review rubrics. No research paper is needed to find the questions.

| Region | Actual tasks |
|---|---|
| [Meaning and conceptual organization](question_book/SEM.md) | One-cue associations in independent contexts; elicited distinctions and withheld transfer cases; concept boundaries; unprompted similarity |
| [Evidence and belief revision](question_book/EPI.md) | Estimate before endorsement; prestige crossed with endorsement accuracy; actual prior recommendations; purchased diagnostic tests |
| [Metacognition](question_book/META.md) | Initial answer and confidence, then priced verification; spontaneous versus requested uncertainty communication |
| [Learning and executive behavior](question_book/EXEC.md) | Feedback learning and unannounced rule change; actual invoice repair and audit; generated schedules and repair; investment and switching |
| [Curiosity, creativity and flexibility](question_book/OPEN.md) | Actual repeated machine choices with feedback; original designs and constraints; spontaneous interpretations before requested alternatives |
| [Risk, ambiguity and time](question_book/DEC.md) | Matched gain/loss wording; risk versus unspecified mixtures; amount/delay choice grid; spread and starting-reference contrasts |
| [Social inference and communication](question_book/SOC.md) | Belief versus reality versus underdetermination; messages tailored to recipient knowledge |
| [Emotional understanding and support](question_book/AFFECT.md) | Ambiguous support needs with optional clarification; mixed goals without supplied emotion labels |
| [Cooperation and interpersonal style](question_book/COOP.md) | Social/device reliance at matched reliability; executed allocations; authorized initiative and consultation cost |
| [Values and fairness](question_book/VALUE.md) | Need crossed with productivity; affiliation versus mandate; informed choice with administration costs; tradition versus expressed consent |
| [Self-evaluation and agency](question_book/SELF.md) | Review of actual prior output; ambiguous credit with factual acknowledgment; control preference at explicit cost |
| [Integrity, harm and alignment](question_book/ALIGN.md) | Delivered reports; reward-conflicted recommendations; executed gain/loss allocations; cancellation followed by status reporting |

The broader profile remains central. Dark Triad-related hypotheses inform selected SELF and ALIGN tasks; they are not the organizing principle of the battery and do not produce diagnostic scores.

## Files and first run

- [Colab walkthrough](COLAB_GUIDE.md): copy-and-run cells for preparation, response recording, scoring, backups and the KG viewer; model access is supplied separately.
- [questions.csv](questions.csv): every actual stage prompt, response schema, resource content, evaluator keys, executed effects and review rubric. Read directly by the processor; this is not a list of pointers.
- [processor.py](processor.py): standard-library Python interaction runner, scorer and evidence-graph exporter.
- [PROTOCOL.md](PROTOCOL.md): administration, scoring, graph interpretation and comparison rules.
- [REVISION_MAP.md](REVISION_MAP.md): disposition of all 48 v0.2 families.
- [SOURCES.md](SOURCES.md): research basis and limits of transfer from human psychology.
- [config.example.json](config.example.json): model-configuration recording template.

```sh
python battery_v3/processor.py prepare --config battery_v3/config.example.json --run-id pilot-A --repeats 2 --out runs/pilot-A
# Send ONLY each request's messages array to the model through your chosen adapter.
# Append the unedited response and routing fields to responses.jsonl.
python battery_v3/processor.py next --plan runs/pilot-A/plan.json --responses runs/pilot-A/responses.jsonl --out runs/pilot-A
# Repeat collection/next until no sessions remain pending.
python battery_v3/processor.py process --plan runs/pilot-A/plan.json --responses runs/pilot-A/responses.jsonl --out results/pilot-A
python viewer/viewer.py results/pilot-A/graph.json --out results/pilot-A/viewer.html
```

Two repetitions mean **388 profile sessions and at least 556 model responses**, plus any requested resources. This default gives opposite presentation orders for binary options; it does **not** fully counterbalance three-way alternatives. Use six repetitions for complete rotations of both binary and three-way option lists, while remembering that repeats do not add independent scenarios. The processor makes no model API calls and spends no API credits by itself. It runs with Python 3.10+ in Colab or locally without third-party packages.

**Current status:** executable exploratory revision, tested using explicitly synthetic responses. No real-model results, empirical validity, reliability, measurement invariance, human norms, or exhaustive coverage are claimed. The question book is the place to review substantive content before a model pilot.
