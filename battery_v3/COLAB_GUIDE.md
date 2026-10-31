# Run v0.3 in Colab and open the results

This walkthrough prepares the questions, records actual model responses, scores them, and creates a portable KG viewer. Use a normal CPU runtime; the battery and viewer do not require a GPU or package installation.

**One important prerequisite:** this repository does not include a provider-specific model API adapter. You need access to the LLM you want to test. The guide below works one response at a time using a provider playground/API that accepts messages with system/user/assistant roles. For an automated run, your adapter performs the same send-and-record steps. Colab itself does not supply model access, and preparing or scoring a run does not call an LLM.

For a first check, complete just a few sessions and inspect the partial results. One complete repetition of the profile is 194 sessions / at least 278 model responses, plus optional information requests. One repetition is a workflow check, not a reliable psychological assessment.

## 1. Open Colab and download the code

Open [a new Colab notebook](https://colab.research.google.com/), then paste each code block below into a separate code cell. Run them in order. Save the notebook to your Drive.

```python
from pathlib import Path
import subprocess, sys, json, importlib.util

repo = Path('/content/llm_psychometric_test')
if not repo.exists():
    subprocess.run(['git', 'clone',
                    'https://github.com/dwtrott/llm_psychometric_test.git',
                    str(repo)], check=True)
print('Code revision:', subprocess.check_output(
    ['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip())

spec = importlib.util.spec_from_file_location('battery_v3_processor',
                                             repo / 'battery_v3/processor.py')
processor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(processor)
battery = processor.load()
```

Keep this code revision fixed throughout a comparison. Rerunning this cell reuses the checkout; it does not update it underneath an existing run.

## 2. Name the model and prepare a run

Change the provider/model placeholders to the actual provider and exact model identifier. Record the settings you actually use, rather than assuming the values below apply to every model. Do not put API keys in this configuration.

```python
RUN_ID = 'model-a-first-check'  # Use a different name for the second model.
config = {
    'provider': 'REPLACE',
    'model': 'REPLACE_WITH_EXACT_MODEL_ID',
    'temperature': 0.7,         # Change to the actual setting, or omit if unsupported.
    'max_output_length': 1200,  # Record the actual output limit.
    'language': 'English',
    'external_tools': 'none',
    'collection_method': 'role-preserving playground/API; manual response upload',
    'synthetic': False,
}
assert not any('REPLACE' in str(v) for v in config.values()), 'Fill in your model details first.'

run_dir = repo / 'runs' / RUN_ID
run_dir.mkdir(parents=True, exist_ok=True)
plan_path = run_dir / 'plan.json'
responses_path = run_dir / 'responses.jsonl'
if plan_path.exists():
    plan = processor.read(plan_path)
    expected_config = dict(config, system_prompt=battery['system_prompt'])
    assert plan['config'] == expected_config, 'Settings changed: use a new RUN_ID.'
    processor.validate_plan(battery, plan)
    print('Resuming existing run; previous responses are retained.')
else:
    assert not responses_path.exists(), 'A response file already exists without its plan.'
    plan = processor.prepare(battery, config, RUN_ID, repeats=1, seed=1729)
    processor.write(plan_path, plan)
    print('Prepared', len(plan['trials']), 'sessions. No model calls made.')

def records():
    return processor.jsonl(responses_path) if responses_path.exists() else []
```

Use a fresh conversation for each session. Later stages within that session must retain the exact earlier messages. Do not add a persona or tell the model the psychological trait being tested. If using a consumer chat interface that cannot preserve the requested roles/system message, record that protocol deviation and keep those results separate from API results.

## 3. Collect a response, then advance the session

Run this cell to get the next model request. For a quick first example, keep the filter shown; it selects one association session. After completing it, try `META-CHECK.arithmetic.cost1` to exercise a multi-stage task and optional verification. Clear the filter to work through the entire prepared run.

```python
ITEM_FILTER = 'SEM-ASSOC.trust.neutral'  # Empty string selects any unfinished session.
pending = processor.next_requests(battery, plan, records())
selected = [r for r in pending if ITEM_FILTER in r['trial_id']]
request = selected[0] if selected else None
print('Total unfinished sessions:', len(pending))
if request is None:
    print('No unfinished session matches this filter. Change the filter or score the run.')
else:
    print('Session:', request['trial_id'], 'Event:', request['event_index'])
    print(json.dumps(request['messages'], ensure_ascii=False, indent=2))
```

**Send only `request['messages']` to the model**, preserving message roles and content. Do not send the routing fields, plan, question CSV, answer keys, or this guide. At later stages, the returned message list already contains the history: replace the provider's history with this list rather than appending it to a second copy.

Save the model's complete, unedited text response to a UTF-8 file, for example `response.txt`. Do not remove code fences, repair JSON, rewrite answers, or select a preferred alternative. Upload that text file using the next cell. Upload one file only; it must contain the model's response text, not the provider's outer HTTP response envelope.

```python
from google.colab import files
from datetime import datetime, timezone

assert request is not None, 'Select a pending request first.'
uploaded = files.upload()
assert len(uploaded) == 1, 'Upload exactly one response text file.'
raw_response = next(iter(uploaded.values())).decode('utf-8-sig')
record = {k: request[k] for k in
          ['trial_id', 'config_id', 'plan_hash', 'event_index', 'request_hash']}
record.update(status='ok', raw_response=raw_response,
              timestamp=datetime.now(timezone.utc).isoformat())

# Check routing integrity before appending. Malformed model answers are retained
# as invalid outcomes, rather than edited or silently retried.
updated = records() + [record]
states = processor.replay(battery, plan, updated)
with responses_path.open('a', encoding='utf-8') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print('Recorded status:', states[request['trial_id']]['status'])
request = None  # Prevent accidental reuse; select the next request again.
```

Repeat the two cells in this section. A model action requesting a resource is a real intermediate response: record it, then let the runner reveal the resource in the next request. Do not supply the hidden information yourself. When the selected session finishes, change the filter or proceed to scoring.

For automated collection, replace the upload with your adapter's unedited returned text, keep the same record fields, and regenerate pending requests after each batch. Preserve transport failures as `status: 'api_error'` records. Provider credentials belong in your private API setup, not in the notebook output, run metadata or repository. API calls may incur your provider's charges.

## 4. Score what you have collected

You can run this cell at any time. Unfinished sessions remain pending; they are not converted into zero scores. A graph from a few completed sessions is a **partial profile**, even though its catalog names all 12 regions.

```python
result_dir = repo / 'results' / RUN_ID
result_dir.mkdir(parents=True, exist_ok=True)
rows, summary, graph, review = processor.score(battery, plan, records())
processor.write(result_dir / 'scores.json', summary)
processor.write(result_dir / 'graph.json', graph)
processor.lines(result_dir / 'trial_scores.jsonl', rows)
processor.lines(result_dir / 'human_review.template.jsonl', review)
print(json.dumps(summary['quality'], indent=2))
print('Human-review criteria awaiting ratings:', summary['review_pending'])
```

`graph.json` is the visualizer input. `scores.json` contains summary estimates; `trial_scores.jsonl` contains individual scores. The human-review file is a template, not completed ratings. Open-ended psychological judgments and originality are not automatically validated or scored. See the [scoring protocol](PROTOCOL.md) before interpreting differences.

## 5. Create and download the KG viewer

```python
viewer_path = result_dir / 'psychometric-viewer.html'
subprocess.run([sys.executable, str(repo / 'viewer/viewer.py'),
                str(result_dir / 'graph.json'), '--out', str(viewer_path)], check=True)
files.download(str(viewer_path))
```

Open the downloaded HTML file in your desktop browser. It already contains this run's graph and works offline. No server is needed. Alternatively, open the repository's `viewer/viewer.html` locally and use **Load graph files** to select the scored `graph.json`.

Start with **Trial evidence** to inspect the actual prompts, responses, status and metrics. Then use **Full profile** for the tested modules and **Concept graph** for observed associations. An empty region means you have not collected its evidence; it is not evidence that the model lacks that characteristic.

### Compare two models

Repeat sections 2–4 with a different `RUN_ID` and actual model configuration, using the same code, questions, session selection and repetition count. Then run:

```python
model_a = repo / 'results/model-a-first-check/graph.json'
model_b = repo / 'results/model-b-first-check/graph.json'
comparison = repo / 'results/two-model-comparison.html'
subprocess.run([sys.executable, str(repo / 'viewer/viewer.py'),
                str(model_a), str(model_b), '--out', str(comparison)], check=True)
files.download(str(comparison))
```

Choose **Primary profile** and **Compare with**. **Graph comparison** shows synchronized side-by-side graphs and the difference graph; **Measurement comparison** shows matched numeric evidence. Teal means stronger in A, orange stronger in B, gray within the chosen descriptive tolerance. One-sided links are observed on only one side, not proven absent from the other. Comparisons require matching battery hashes; do not mix battery versions or interpret sparse one-response graphs as stable fingerprints.

## 6. Save your work before closing Colab

Colab runtimes are temporary; saving the notebook does not preserve all runtime files. Download a backup after collecting responses, not just at the end. [Google's Colab FAQ](https://research.google.com/colaboratory/faq.html) explains runtime lifetimes.

```python
import zipfile
from google.colab import files
backup = Path('/content') / f'{RUN_ID}-backup.zip'
with zipfile.ZipFile(backup, 'w', zipfile.ZIP_DEFLATED) as archive:
    for folder in [run_dir, repo / 'results' / RUN_ID]:
        if folder.exists():
            for path in folder.rglob('*'):
                if path.is_file():
                    archive.write(path, path.relative_to(repo))
    revision = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    archive.writestr('code_revision.txt', revision + '\n')
files.download(str(backup))
```

To resume later, clone the repo, check out the revision recorded in the backup **before importing the processor**, and restore the backup's `runs/<RUN_ID>/` folder into the checkout using Colab's file browser. Rerun sections 1–2 with the original run name and settings. Both `plan.json` and `responses.jsonl` are needed to resume; `graph.json` alone is enough only for viewing. Restore `results/` too if you want the previous exports.

The 18 capability-control families are a separate bank with the earlier `prepare/process` interface. Do not use this staged collection loop for them or merge their graph into a profile. See [controls/README.md](controls/README.md) and the [v0.2 collection protocol](../battery_v2/PROTOCOL.md).

**Verification:** preparation, staged response recording, partial scoring and HTML generation were smoke-tested locally with synthetic data. The Colab-specific upload/download dialogs were checked against [Google's file-helper implementation](https://github.com/googlecolab/colabtools/blob/main/google/colab/files.py), but this guide has not been executed in a live Colab session. No model runs are included.
