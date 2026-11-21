"""Resumable collection of observations into a JSONL file, one line per probe."""
import json
from pathlib import Path

from . import battery, probes


def preflight(backend, items=None, n=12, top_k=8):
    """Probe a model briefly before a full run. Returns the label mass on a
    spread of choice probes and the leading first tokens for three of them, so
    that a format problem is found before thousands of probes are spent."""
    items = items or battery.build()
    choice = [p for p in probes.probes(items, probes.DEFAULT_CONTEXTS[:1]) if p["kind"] != "assoc"]
    sample = choice[:: max(1, len(choice) // n)][:n]
    masses = [sum(p) for p in backend.label_probs(sample)]
    tokens = backend.top_tokens(sample[:3], top_k)
    return dict(mean_label_mass=sum(masses) / len(masses), min_label_mass=min(masses),
                first_tokens=[dict(item=p["item"], tokens=t) for p, t in zip(sample, tokens)])


def collect(backend, model_name, out_path, items=None, contexts=None, top_k=20, chunk=64, progress=None):
    items = items or battery.build()
    contexts = contexts or probes.DEFAULT_CONTEXTS
    version = battery.battery_hash(items)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r["battery"] != version or r["model"] != model_name:
                raise ValueError(f"{out_path} holds a different battery or model. Use a new file.")
            done.add((r["context"], r["item"], r["rotation"]))
    pending = [p for p in probes.probes(items, contexts) if (p["context"], p["item"], p["rotation"]) not in done]
    total = len(pending)
    with out_path.open("a", encoding="utf-8") as f:
        for start in range(0, total, chunk):
            batch = pending[start:start + chunk]
            choice = [p for p in batch if p["kind"] != "assoc"]
            assoc = [p for p in batch if p["kind"] == "assoc"]
            results = dict(zip((id(p) for p in choice), backend.label_probs(choice) if choice else []))
            results.update(zip((id(p) for p in assoc), backend.top_tokens(assoc, top_k) if assoc else []))
            for p in batch:
                record = dict(model=model_name, battery=version, context=p["context"], item=p["item"],
                              family=p["family"], kind=p["kind"], rotation=p["rotation"])
                if p["kind"] == "assoc":
                    record["tokens"] = results[id(p)]
                else:
                    record.update(order=p["order"], position_probs=results[id(p)])
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
            f.flush()
            if progress:
                progress(min(start + chunk, total), total)
    return out_path
