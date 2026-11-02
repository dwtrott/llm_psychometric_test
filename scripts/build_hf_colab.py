"""Generate the Colab notebook; no models or network calls are run here."""
import json
from pathlib import Path
import textwrap

ROOT=Path(__file__).resolve().parents[1]
cells=[]
def cell(kind,source):
    source=textwrap.dedent(source).strip()+'\n'
    value=dict(cell_type=kind,id=f'cell-{len(cells):02}',metadata={},source=source.splitlines(keepends=True))
    if kind=='code':value.update(execution_count=None,outputs=[])
    cells.append(value)

cell('markdown','''
# Run the psychological prompt battery on a Colab A100

1. Choose **Runtime → Change runtime type → GPU → A100**.
2. Keep the defaults below for a first run, then choose **Runtime → Run all**.
3. Wait for the result ZIP to download. Extract it and open **`START_HERE.html`**. This shows exactly which questions received accepted answers, which failed, and which stages have no response. Analysis and graph links are there too.

Default: [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct), a public chat model. No Hugging Face key is required for this default. Change `MODEL_ID` to try another compatible text/chat model. The notebook downloads weights and performs inference **inside your Colab GPU session**, not through a paid inference API.

The base instrument has **240 cards / 280 question stages**. By default it runs four response-menu rotations: **960 conversations / 1,120 question stages**, plus up to 64 resource calls. The base instrument contains 120 development cards and 120 held-out cards, across all 11 categories and 22 facets. The bank includes distinct scenario contexts and two task-instruction wordings. Presentation rounds rotate labels and response menus without changing the meaning or scoring of options; they are not new independent scenarios. Four rounds fully balance two- and four-option menus; three-option menus require a multiple of three for full balance (use 12 rounds to balance all menu sizes). Each card starts a fresh conversation; its follow-ups retain that card's history. The first download/loading can take longer than generation. A GPU with 40 GB or more is recommended for the default BF16 configuration.

The notebook saves raw model text and generation token IDs after every call. It does not repair JSON, discard refusals, retry invalid answers, or supply evaluator scoring keys to the model. Formatting failures are part of the recorded results. Written content receives a separate local-model rubric pass, with evidence quotations and explicit judge provenance. Human ratings remain separate. Rubrics and task features are fixed before collection; the held-out partition is a prespecified transfer check, not evidence that the prompts were absent from model training. Task paraphrases preserve facts verbatim; response-menu round effects are analyzed separately. This run is not a validated personality diagnosis.
''')
cell('code','''
# Settings: the defaults run and score the whole battery once.
NOTEBOOK_PROTOCOL = "scored-v010"
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
# Smaller alternative: "Qwen/Qwen2.5-1.5B-Instruct"
MODEL_REVISION = "main"  # Resolved to an exact Hugging Face commit before loading.
SOURCE_REVISION = "main" # Or the exact battery source commit from a previous run.
RUN_LABEL = "scored-v010" # New battery: keep earlier results in their original directory.
REPEATS = 1
PRESENTATION_ROUNDS = 4 # Four response-menu rotations, separate from wording and scenarios.
MAX_NEW_TOKENS = 512
SEED = 42
FACETS = None           # Default: all 22 facets, both partitions, both wordings.
ALLOW_PARTIAL = False   # Set True only for an explicitly selected subset.
JUDGE_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct" # Keep the same judge across subject models.
JUDGE_REVISION = "main" # Pin the resolved revision for reproducible comparisons.
JUDGE_MAX_NEW_TOKENS = 1024 # Separate rubric pass using the loaded model in fresh conversations.
SAVE_TO_DRIVE = False   # Optional persistence across Colab runtime deletion.
''')
cell('markdown','''
## Install the inference libraries and fetch the battery

The analyzer and battery use Python's standard library. Running the local neural model additionally requires PyTorch (provided by Colab), Transformers, Accelerate and Safetensors. The Transformers version is pinned for this adapter. Start in a fresh runtime; if an earlier cell already imported another Transformers version, restart the runtime after installation.
''')
cell('code','''
import sys, subprocess, importlib, importlib.metadata
from pathlib import Path

TRANSFORMERS_VERSION = "4.57.1"
subprocess.run([sys.executable, "-m", "pip", "install", "--quiet",
                f"transformers=={TRANSFORMERS_VERSION}", "accelerate>=1.0,<2",
                "safetensors>=0.4", "tqdm>=4.66"], check=True)
if "transformers" in sys.modules and sys.modules["transformers"].__version__ != TRANSFORMERS_VERSION:
    raise RuntimeError("Restart the Colab session, then Run all: another Transformers version is already imported.")
importlib.invalidate_caches()

REPO_URL = "https://github.com/dwtrott/llm_psychometric_test.git"
REPO_DIR = Path("/content/llm_psychometric_test")
if not REPO_DIR.exists():
    subprocess.run(["git", "clone", "--depth", "1", REPO_URL, str(REPO_DIR)], check=True)
elif not (REPO_DIR / ".git").exists():
    raise RuntimeError("The repository path exists but is not a Git checkout. Choose a new REPO_DIR.")
origin = subprocess.check_output(["git", "-C", str(REPO_DIR), "remote", "get-url", "origin"], text=True).strip()
if origin != REPO_URL:
    raise RuntimeError("Existing checkout belongs to a different repository. Choose a new REPO_DIR.")
if subprocess.check_output(["git", "-C", str(REPO_DIR), "status", "--porcelain"], text=True).strip():
    raise RuntimeError("The checkout has local edits. Use a clean checkout so the run records an exact source revision.")
subprocess.run(["git", "-C", str(REPO_DIR), "fetch", "--depth", "1", "origin", SOURCE_REVISION], check=True)
subprocess.run(["git", "-C", str(REPO_DIR), "checkout", "--detach", "FETCH_HEAD"], check=True)
SOURCE_COMMIT = subprocess.check_output(["git", "-C", str(REPO_DIR), "rev-parse", "HEAD"], text=True).strip()
# Fail before downloading a model if source and notebook are incompatible.
import json, csv
instrument_meta = json.loads((REPO_DIR / "battery_full/battery.json").read_text(encoding="utf-8"))
if NOTEBOOK_PROTOCOL != "scored-v010" or instrument_meta.get("version") != "0.10.0-scored":
    raise RuntimeError("Notebook/source mismatch. Reopen the current GitHub notebook; do not reuse stale cells.")
with (REPO_DIR / "battery_full/prompts.csv").open(encoding="utf-8-sig", newline="") as handle:
    full_rows = list(csv.DictReader(handle))
assert len(full_rows) == 280 and len({row["prompt_id"] for row in full_rows}) == 240
assert len({row["facet"] for row in full_rows}) == 22 and len({row["category"] for row in full_rows}) == 11
print("Verified full scored instrument: 240 cards / 280 stages / 22 facets / 11 categories.")
print("Battery source:", SOURCE_COMMIT)
print("SOURCE_REVISION=main fetches the current release. To resume an older run, set SOURCE_REVISION to that run's saved commit.")
''')
cell('markdown','''
## Check the GPU and load the model

The model and tokenizer are loaded from the same resolved revision, without remote Python model code. This notebook uses BF16, one GPU and greedy decoding. It does not quantize or enable extended thinking. Other model families may need a different adapter; an absent chat template is reported as an error.
''')
cell('code','''
import gc, hashlib, json, time
import torch, transformers, accelerate, huggingface_hub
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import HfApi

if not torch.cuda.is_available():
    raise RuntimeError("No GPU detected. Select an A100 under Runtime → Change runtime type, then Run all.")
GPU_NAME = torch.cuda.get_device_name(0)
GPU_GB = torch.cuda.get_device_properties(0).total_memory / 2**30
print(f"GPU: {GPU_NAME}; {GPU_GB:.1f} GiB")
if not torch.cuda.is_bf16_supported():
    raise RuntimeError("This notebook uses BF16. Select an A100 GPU for the supplied configuration.")
if "A100" not in GPU_NAME:
    print("This is not an A100. Runtime and available model sizes may differ.")

# Release the previously loaded model if this cell is rerun.
for old_name in ("generator", "model", "tokenizer", "judge_generator", "judge_model", "judge_tokenizer"):
    globals().pop(old_name, None)
gc.collect()
torch.cuda.empty_cache()

RESOLVED_MODEL_REVISION = HfApi().model_info(MODEL_ID, revision=MODEL_REVISION).sha
print("Model:", MODEL_ID, "revision:", RESOLVED_MODEL_REVISION)
load_started = time.perf_counter()
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, revision=RESOLVED_MODEL_REVISION, trust_remote_code=False)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, revision=RESOLVED_MODEL_REVISION, torch_dtype=torch.bfloat16,
    device_map={"": 0}, attn_implementation="sdpa", trust_remote_code=False,
    use_safetensors=True,
)
print(f"Model loaded in {time.perf_counter() - load_started:.1f} seconds.")
''')
cell('markdown','''
## Prepare or resume the run

Leave `SAVE_TO_DRIVE=False` for the simplest run. Colab's temporary files disappear when the runtime is deleted, so download the ZIP at the end. With Drive enabled, completed response records survive runtime deletion; remount the same Drive and use the same model revision, source checkout, settings and label to resume. Changed configurations require a new `RUN_LABEL`.
''')
cell('code','''
import re, shutil
import importlib.util

spec = importlib.util.spec_from_file_location("hf_runner", REPO_DIR / "battery_core/hf_runner.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
generator = runner.TransformersGenerator(model, tokenizer, MAX_NEW_TOKENS)

if SAVE_TO_DRIVE:
    from google.colab import drive
    drive.mount("/content/drive")
    OUTPUT_ROOT = Path("/content/drive/MyDrive/llm-psychometric-runs")
else:
    OUTPUT_ROOT = Path("/content/psychometric-runs")
if not re.fullmatch(r"[A-Za-z0-9_-]+", RUN_LABEL):
    raise ValueError("Use letters, numbers, underscores or hyphens for RUN_LABEL.")
slug = re.sub(r"[^A-Za-z0-9_-]+", "-", MODEL_ID)
RUN_ID = f"{slug}-{RUN_LABEL}"
RUN_DIR = OUTPUT_ROOT / RUN_ID
template_identity = json.dumps(tokenizer.chat_template, ensure_ascii=False, sort_keys=True)
config = dict(
    provider="huggingface-local", model=MODEL_ID, display_name=MODEL_ID, presentation_rounds=PRESENTATION_ROUNDS,
    model_revision=RESOLVED_MODEL_REVISION, tokenizer_revision=RESOLVED_MODEL_REVISION,
    chat_template_sha256=hashlib.sha256(template_identity.encode()).hexdigest(),
    dtype="bfloat16", attention="sdpa", quantization="none", seed=SEED,
    decoding=generator.generation.to_dict(), adapter_version="1.3.0",
    transformers_version=transformers.__version__, torch_version=str(torch.__version__),
    accelerate_version=accelerate.__version__, huggingface_hub_version=huggingface_hub.__version__,
    cuda_version=torch.version.cuda, gpu=GPU_NAME, source_commit=SOURCE_COMMIT,
    response_policy="unaltered decoded output; no repair; no invalid-answer retries", synthetic=False,
)
if FACETS is not None and not ALLOW_PARTIAL:
    raise ValueError("A facet subset would omit part of the battery. Use FACETS=None for the full run.")
battery, plan = runner.prepare_run(config, RUN_DIR, RUN_ID, REPEATS, FACETS, REPO_DIR / "battery_full")
if FACETS is None:
    assert len(plan["trials"]) == 240 * REPEATS * PRESENTATION_ROUNDS, "Unexpected full battery size"
    assert sum(len(t["stages"]) for t in plan["trials"]) == 280 * REPEATS * PRESENTATION_ROUNDS, "Unexpected stage count"
from collections import Counter
coverage = Counter((t["module"], t["split"], t["paraphrase"]) for t in plan["trials"])
print("PLANNED COVERAGE — each line is facet / partition / wording / cards")
for (facet, split, wording), count in sorted(coverage.items()):
    print(f"{facet:18} {split:12} {wording:10} {count}")
print("All planned cards are independent conversations; only a card's own follow-ups retain history.")
print("Additional written-stage scoring calls after a successful collection:", sum(any(f["type"] == "text" for f in s["fields"].values()) for t in plan["trials"] for s in t["stages"]))
runner.atomic_json(RUN_DIR / "planned_coverage.json", [dict(facet=k[0], split=k[1], wording=k[2], cards=v) for k,v in sorted(coverage.items())])

# Include the actual instrument and implementation in the downloadable archive.
for relative in ["battery_core/prompts.csv", "battery_core/battery.json", "battery_core/processor.py",
                 "battery_core/hf_runner.py", "battery_core/evaluate.py", "battery_core/presentations.py", "battery_core/run_audit.py", "battery_core/PROMPTS.md", "battery_core/README.md",
                 "battery_v7/_engine.py", "battery_v7/content_ratings.py", "analyzer/psychometric.py",
                 "viewer/viewer.py", "viewer/viewer.html", "battery_full/battery.json", "battery_full/prompts.csv",
                 "battery_full/PROMPTS.md", "battery_full/SCORING.md", "battery_full/README.md", "battery_full/design_manifest.json"]:
    destination = RUN_DIR / "source" / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_DIR / relative, destination)
runner.atomic_json(RUN_DIR / "environment.json", dict(
    source_commit=SOURCE_COMMIT, model_revision=RESOLVED_MODEL_REVISION,
    python=sys.version, packages={name:importlib.metadata.version(name) for name in
                                ["torch", "transformers", "accelerate", "huggingface-hub", "safetensors"]},
))
existing = runner.records_at(RUN_DIR / "responses.jsonl")
print(f"{len(plan['trials'])} cards prepared; {len(existing)} response records already saved.")
print("Results folder:", RUN_DIR)
''')
cell('markdown','''
## Run all prompts

The progress bar counts **processed cards**, which can include rejected responses. Its separate accepted/rejected counters show success. **100% processed does not mean a complete evaluation.** The next cell reports exactly how many question stages have accepted answers and lists any missing stages. Optional requests and follow-ups are automatic, but an invalid response stops that card's remaining stages. An interrupted collection can resume by rerunning this cell; invalid answers are retained and not silently repaired or retried.
''')
cell('code','''
from tqdm.auto import tqdm

saved = runner.records_at(RUN_DIR / "responses.jsonl")
states = runner.processor.engine.replay(battery, plan, saved)
finished = sum(s["status"] != "pending" for s in states.values())
bar = tqdm(total=len(plan["trials"]), initial=finished, desc="Cards processed (not success)")
def show_progress(event):
    bar.update(event["processed"] - bar.n)
    bar.set_postfix(accepted=event["accepted"], rejected=event["quality"].get("invalid", 0), calls=event["calls"])

try:
    records = runner.collect(battery, plan, RUN_DIR, generator, show_progress)
finally:
    bar.close()
    print("Responses saved to", RUN_DIR / "responses.jsonl")
print(f"Collection stopped after {len(records)} model responses. Check the completion report below before interpreting the run.")
''')
cell('markdown','''
## Score the written responses

The local model now acts as a rubric scorer in fresh conversations, separately from the battery run. Each score must cite an exact excerpt and explain its rubric anchor. Its raw judgments are saved and resumable. The default judge is Qwen2.5-7B-Instruct, kept fixed when the tested model changes. When it is also the subject model, it is reused, with self-evaluation bias recorded. Scores may have model-family biases: they are provisional automated ratings, not human validation. Fixed-choice and numeric measurements do not depend on this judge. Invalid judgments stay unscored.


This cell can also export a partial run after an interruption. `valid` means the response met the instrument's format/field rules, not that it expressed a desirable trait. Review `response_status.csv` for invalid responses and token-limit hits before interpreting results. The next cell runs the local rubric scorer. It does not turn automated scores into human ratings.
''')
cell('code','''
RESOLVED_JUDGE_REVISION = HfApi().model_info(JUDGE_MODEL_ID, revision=JUDGE_REVISION).sha
if JUDGE_MODEL_ID == MODEL_ID and RESOLVED_JUDGE_REVISION == RESOLVED_MODEL_REVISION:
    judge_model, judge_tokenizer = model, tokenizer
else:
    # Collection is finished: free subject weights before loading the judge.
    for name in ("generator", "model", "tokenizer", "judge_generator", "judge_model", "judge_tokenizer"):
        globals().pop(name, None)
    gc.collect(); torch.cuda.empty_cache()
    judge_tokenizer = AutoTokenizer.from_pretrained(JUDGE_MODEL_ID, revision=RESOLVED_JUDGE_REVISION, trust_remote_code=False)
    judge_model = AutoModelForCausalLM.from_pretrained(JUDGE_MODEL_ID, revision=RESOLVED_JUDGE_REVISION,
        torch_dtype=torch.bfloat16, device_map={"": 0}, attn_implementation="sdpa", trust_remote_code=False, use_safetensors=True)
judge_generator = runner.TransformersGenerator(judge_model, judge_tokenizer, JUDGE_MAX_NEW_TOKENS)
judge_template_hash = hashlib.sha256(json.dumps(judge_tokenizer.chat_template, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
judge_config = dict(model=JUDGE_MODEL_ID, revision=RESOLVED_JUDGE_REVISION,
    tokenizer_revision=RESOLVED_JUDGE_REVISION, chat_template_sha256=judge_template_hash,
    decoding=judge_generator.generation.to_dict(), source_commit=SOURCE_COMMIT,
    same_model_as_subject=(JUDGE_MODEL_ID == MODEL_ID and RESOLVED_JUDGE_REVISION == RESOLVED_MODEL_REVISION), role="provisional automated rubric scorer",
    protocol="rubric-judge-v1")
print("Evaluating written answers; this is separate from collecting responses.")
def scoring_progress(done, total, status):
    if done % 10 == 0 or done == total: print(f"Written stages evaluated: {done}/{total}; latest status: {status}")
try:
    evaluation_records = runner.evaluate_run(RUN_DIR, judge_generator, judge_config, scoring_progress)
finally:
    # Preserve useful partial outputs even if the scoring model/runtime fails.
    artifacts = runner.export(RUN_DIR)
print("Raw rubric judgments:", RUN_DIR / "evaluation.jsonl")
''')
cell('markdown','''
## Inspect measured results

The exports include selected-option frequencies, numeric decisions, rubric scores with excerpts, and deterministic consistency checks. Format success and substantive evaluation coverage are separate. Missing rubric judgments never become zeros.
''')
cell('code','''
from IPython.display import HTML, display

artifacts = runner.export(RUN_DIR)
print("RUN STATUS:", artifacts["summary"]["run_status"].upper())
print(json.dumps(artifacts["summary"]["completion"], indent=2))
print(json.dumps(artifacts["summary"]["collection"], indent=2))
print("Evaluation coverage:", {k:v for k,v in artifacts["summary"]["evaluation"].items() if k not in ["results", "checks"]})
print("Content review targets:", artifacts["summary"].get("review_pending", "see human_review.template.jsonl"))
print("Partition graphs:", artifacts["graphs"])
print("Interactive viewer:", artifacts["viewer"])
if artifacts["summary"]["collection"]["token_limit_hits"]:
    print("Some generations reached the token limit. Inspect their raw outputs; any changed-limit rerun must use a new RUN_LABEL.")
display(HTML(Path(artifacts["audit"]).read_text(encoding="utf-8")))
''')
cell('markdown','''
## Download everything

The ZIP contains **`START_HERE.html`**, `results/measurements.html` with actual scores and quotations, `evaluation.jsonl` with raw judge outputs, the question-by-question audit, exact plan/configuration, raw `responses.jsonl`, timing/token metadata, `results/graph-development.json` and `results/graph-heldout.json`, scores, review templates, an analyzer report and a graph viewer. Extract the whole ZIP to keep links working. A ZIP can contain an **incomplete** run; the start page states this explicitly. No model weights are included.

To compare another model, change `MODEL_ID`, use a new run label and run again. For comparisons across models use the same partition from each run. For transfer within a model use its development and held-out graph together. The combined `graph.json` is archival evidence; the analyzer requires the separate partition graphs. Different battery hashes cannot be compared. The separate network-atlas mockup is not the result viewer.
''')
cell('code','''
from google.colab import files

archive_base = Path("/content") / f"{RUN_ID}-results"
archive = shutil.make_archive(str(archive_base), "zip", root_dir=RUN_DIR)
print("Downloading", archive)
files.download(archive)
''')
cell('markdown','''
### Troubleshooting

- **No GPU / out of memory:** choose A100 and start a fresh runtime. The default uses one GPU with no CPU offload. Try `Qwen/Qwen2.5-1.5B-Instruct` for a smaller run.
- **Access denied downloading a different model:** its Hugging Face repository may require license acceptance/authentication. The default public Qwen model requires neither a paid API nor a notebook token.
- **Interrupted run:** rerun the collection cell. After a full runtime reset, rerun setup using the same saved source/model commits and configuration. If those have changed, use a new run label; do not mix them.
- **Invalid answers:** inspect `results/response_status.csv` and `responses.jsonl`. JSON fences, extra fields, overlong text, or out-of-range values fail the instrument's strict rules. The notebook does not secretly retry or edit them.
- **Model takes much longer:** an alternative reasoning model may generate long internal-thinking text; this adapter is designed for ordinary chat/instruction models and does not strip thinking traces. Use the supplied default for a first test.

Local validation covers notebook syntax and the collection/checkpoint/export pipeline with synthetic generators. A live Colab/A100 model run has not been performed by the repository authoring agent.

Implementation references: [Qwen model card](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct), [Transformers Qwen2 support](https://huggingface.co/docs/transformers/v4.57.1/en/model_doc/qwen2), and the repository's [prompt list](https://github.com/dwtrott/llm_psychometric_test/blob/main/battery_full/PROMPTS.md).
''')

notebook=dict(cells=cells,metadata=dict(accelerator='GPU',colab=dict(name='Run_HuggingFace_A100.ipynb',provenance=[]),
    kernelspec=dict(display_name='Python 3',language='python',name='python3'),language_info=dict(name='python')),
    nbformat=4,nbformat_minor=5)
path=ROOT/'battery_core/Run_HuggingFace_A100.ipynb'
path.write_text(json.dumps(notebook,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(path)
