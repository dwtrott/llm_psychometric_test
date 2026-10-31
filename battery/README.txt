LLM PSYCHOMETRIC BATTERY — CSV + PYTHON

READ THE CONTENT WITHOUT RUNNING CODE
Open QUESTIONS.md for the complete question book, organized by module.
Each page includes the actual questions/scenarios, answer options and response
instructions. complete_prompts.csv puts each full prompt in a single column.
Research references are background, not pointers to missing question text.
This is a pilot task set, not a complete psychological profile. Its 436 rows
include repeated scenario variants; many tasks are simple and require deeper
item review and empirical validation before psychological conclusions.

This is the measurement and data-processing component. The psychometric KG
visualizer is a separate tool consuming graph.json, or nodes.csv and edges.csv.
No rendering, layout, browser, or visualization dependencies are included.

FILES
questions.csv: canonical editable question list, 436 instances / 28 modules.
processor.py: Python 3.10+ standard-library preparation, scoring and KG export.
battery_metadata.json: version, system prompt, module definitions and sampling strata.
module_scoring.csv: readable module scoring rules and interpretation limits.
config.example.json: record actual model/provider settings here.
kg-contract.json: data interface for the separate visualizer.
sources.json and coverage.json: research basis and coverage limitations.

CSV FORMAT
One row per item. question is plain text. Columns ending _json store valid JSON
objects/arrays so options, conditions and scoring keys survive CSV round-trips.
Use a CSV-aware editor to preserve quoting, commas and line breaks. Encoding: UTF-8.
item_id must be unique. Edit scoring keys when factual premises change.
Changing the CSV or metadata changes the battery hash; old run plans are rejected.
The scoring implementation supports the existing 28 modules; adding a new module
also requires adding validation and scoring logic in processor.py.

PREPARE
From this folder, edit config.example.json, then run:
python processor.py prepare --config config.example.json --run-id modelA-session1 --repeats 4 --out runA

This writes plan.json, prompts.csv, prompts.jsonl and responses_template.csv.
Send each system_prompt/user_prompt pair as a fresh conversation, or send the
messages field from prompts.jsonl. Model API calls are external to this script.
Never send questions.csv, scoring keys, module labels or the full plan to a model.
4 repetitions = 1,744 trials. 12 repetitions balance all 2/3/4-option menus.
Repeats are exact wording with rotated options, not validated paraphrases.

COLLECT
Save responses as CSV using responses_template.csv, or as JSONL. Required fields:
trial_id, config_id, status, raw_response. timestamp is optional but recommended.
status is ok or api_error. raw_response is the unedited response text.
Leave uncollected CSV template rows blank; they are reported as missing.
An explicit model refusal {"declined": true} is retained separately from invalid,
missing, API-error and valid action-level abstention responses.

PROCESS
python processor.py process --plan runA/plan.json --responses responses.csv --out resultsA

OUTPUTS
graph.json: full provenance-rich property graph for the separate visualizer.
nodes.csv and edges.csv: equivalent node/edge tables; extra fields in properties_json.
scores.json: per-condition means, family means, quality counts, matched contrasts.
measurements.csv: long-format numerical scores, one metric per valid trial row.
trial_status.csv: every planned trial, including missing/invalid/refused/error trials.
trial_scores.jsonl: full per-trial scoring records.

SCORING AND INTERPRETATION
No total personality, Dark Triad, intelligence, morality or alignment score.
Construct edges are researcher hypotheses, not discovered personality traits.
Semantic edges keep cue/context/configuration separate; absence is not a zero.
Missing answers never become zero-risk answers. Reports after a selected repair
are compared against the post-repair truth defined by the fictional task.
Contrast values are explicitly B minus A; inspect the labels before interpreting.
The data export contains no automated confidence intervals or significance tests.
Open-ended GRID and CREATIVE responses remain pending human review; the provided
human-rating template is not imported by this automatic scorer.

This is a research-informed pilot. The broad profile includes meaning, cognition,
learning, uncertainty, decisions, social understanding, values and self-evaluation,
as well as integrity/conflict probes. It is not yet psychometrically validated.
No real model results are included, and no model was called during packaging.
