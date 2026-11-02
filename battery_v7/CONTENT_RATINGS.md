# Evidence-linked content rating import

Ordinal human-review ratings become evidence-linked graph measurements and separate `rating_*` features in the main analyzer. The [compact core](../battery_core/README.md) supplies a new readable prompt list, including additional coverage and explicit ordinal content rubrics. This importer does not infer arbitrary conceptual categories: the older v0.7 categorical construct-content field still requires a frozen codebook and is not accepted as an ordinal rating.

After running the v0.7 processor:

```sh
python battery_v7/content_ratings.py --graph results/model/graph.json --templates results/model/human_review.template.jsonl --out results/model/review
```

Give separate copies of `rating_tasks.jsonl` to two independent raters. Each fills `rater_id`, integer `score`, exact `evidence_quote` and `rationale`. Keep the hashes unchanged. The task includes the response, transcript and existing anchors. These exports include original trial identifiers and transcripts; they are not automatically blinded to model identity. A study requiring blinding needs an evaluator-maintained anonymous identifier mapping and transcript inspection before distribution. No ratings are generated automatically.

Combine the completed JSONL files and run:

```sh
python battery_v7/content_ratings.py --graph results/model/graph.json --templates results/model/human_review.template.jsonl --ratings completed-ratings.jsonl --out results/model/rated
```

Outputs are `rated_graph.json`, `content_scores.json` and a portable `content_report.html`. The importer requires at least two distinct raters, all supplied ratings agreeing, exact response evidence, a rationale, and matching graph/rubric hashes. Distinct names alone cannot prove independent judgments; that is a study-design responsibility. Disagreement, missing ratings and single-rater records remain unscored. Hidden needs and other unobservable targets are excluded. Categorical conceptual content is explicitly rejected until a frozen categorical codebook is supplied; ordinal scores cannot replace it.

Open the content report to inspect ratings and their evidence, or load `rated_graph.json` into the main analyzer or viewer. The graph preserves the original task-choice measurements and adds separate `human_content_rating` nodes. The analyzer compares imported `rating_*` features on matching items; the compact-core catalog selects the appropriate content metrics for its region summaries. Legacy v0.7 headline definitions are preserved, while imported ratings remain available in the detailed feature tables. Do not interpret these ratings as human personality norms, a deception-intent diagnosis, or validated trait scores.
