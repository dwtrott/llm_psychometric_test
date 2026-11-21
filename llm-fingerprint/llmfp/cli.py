"""Command line interface: python -m llmfp <command>"""
import argparse
import glob
import json
import sys
from pathlib import Path

from . import battery, collect, probes, report


def _contexts(args):
    if args.contexts:
        return json.loads(Path(args.contexts).read_text(encoding="utf-8"))
    return probes.context_set(args.context_set)


def _expand(paths):
    """Expand wildcards and directories here, because the Windows shells do not."""
    out = []
    for p in paths:
        if any(ch in p for ch in "*?["):
            out += sorted(glob.glob(p))
        elif Path(p).is_dir():
            out += sorted(str(f) for f in Path(p).glob("*.jsonl"))
        else:
            out.append(p)
    if not out:
        raise SystemExit("No observation files found.")
    return out


def _preflight(backend):
    result = collect.preflight(backend)
    print(f"label mass on the check probes: mean {result['mean_label_mass']:.2f}, "
          f"min {result['min_label_mass']:.2f}")
    for example in result["first_tokens"]:
        top = sorted(example["tokens"].items(), key=lambda kv: -kv[1])[:5]
        print(f"  first tokens for {example['item']}: " + ", ".join(f"{t!r} {p:.2f}" for t, p in top))
    if result["mean_label_mass"] < 0.5:
        print("WARNING: the model mostly does not answer with a letter as its first token. Look at the first "
              "tokens above. Use --no-thinking for a model that opens with reasoning, or --prefill for a model "
              "that opens with a fixed character such as '(' or a space.")
    return result


def _progress(done, total):
    print(f"\r{done}/{total} probes", end="", file=sys.stderr, flush=True)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="llmfp", description="Behavioral fingerprints for language models.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("battery", help="write the battery as JSON and Markdown")
    p.add_argument("--out", default=".")

    p = sub.add_parser("run-hf", help="collect observations from a local Hugging Face model")
    p.add_argument("model")
    p.add_argument("--out", required=True)
    p.add_argument("--name")
    p.add_argument("--contexts", help="JSON file with a custom context list")
    p.add_argument("--context-set", choices=["default", "adversarial", "all"], default="default")
    p.add_argument("--revision")
    p.add_argument("--dtype", default="auto")
    p.add_argument("--batch-size", type=int, default=16)
    p.add_argument("--load-in-4bit", action="store_true")
    p.add_argument("--prefill", default="")
    p.add_argument("--template-kwargs", default="{}", help='JSON, for example \'{"enable_thinking": false}\'')
    p.add_argument("--no-thinking", action="store_true", help="pass enable_thinking=False to the chat template")
    p.add_argument("--check", action="store_true", help="run a short format check and stop")

    p = sub.add_parser("run-api", help="collect from an OpenAI-compatible endpoint that returns logprobs")
    p.add_argument("model")
    p.add_argument("--base-url", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--name")
    p.add_argument("--contexts", help="JSON file with a custom context list")
    p.add_argument("--context-set", choices=["default", "adversarial", "all"], default="default")
    p.add_argument("--api-key-env", default="OPENAI_API_KEY")
    p.add_argument("--samples", type=int, default=0,
                   help="for endpoints without logprobs: estimate each distribution from this many sampled replies")
    p.add_argument("--check", action="store_true", help="run a short format check and stop")

    p = sub.add_parser("simulate", help="write observations for a synthetic model panel")
    p.add_argument("--out", required=True)
    p.add_argument("--context-set", choices=["default", "adversarial", "all"], default="default")

    p = sub.add_parser("identify", help="rank enrolled models as candidates for an unlabeled model")
    p.add_argument("query", help="observation file of the unlabeled model")
    p.add_argument("enrolled", nargs="+", help="observation files of known models")

    p = sub.add_parser("diff", help="compare two model graphs written by analyze")
    p.add_argument("graph_a")
    p.add_argument("graph_b")
    p.add_argument("--tolerance", type=float, default=0.05)
    p.add_argument("--out", help="CSV file for the full edge table")

    p = sub.add_parser("analyze", help="analyze observation files and write a report")
    p.add_argument("observations", nargs="+")
    p.add_argument("--out", default="report")
    p.add_argument("--groups", help="JSON file mapping model name to lineage label for known relatives")

    args = parser.parse_args(argv)

    if args.command == "battery":
        items = battery.build()
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        (out / "battery.json").write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
        (out / "BATTERY.md").write_text(battery.markdown(items), encoding="utf-8")
        print(f"{len(items)} items, version {battery.battery_hash(items)}")

    elif args.command == "run-hf":
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from .backends import HFBackend
        kwargs = dict(revision=args.revision, device_map="auto")
        if args.load_in_4bit:
            from transformers import BitsAndBytesConfig
            kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)
        else:
            kwargs["torch_dtype"] = "auto" if args.dtype == "auto" else getattr(torch, args.dtype)
        tokenizer = AutoTokenizer.from_pretrained(args.model, revision=args.revision)
        model = AutoModelForCausalLM.from_pretrained(args.model, **kwargs)
        template_kwargs = json.loads(args.template_kwargs)
        if args.no_thinking:
            template_kwargs["enable_thinking"] = False
        backend = HFBackend(model, tokenizer, args.batch_size, template_kwargs, args.prefill)
        _preflight(backend)
        if args.check:
            return
        collect.collect(backend, args.name or args.model, args.out, contexts=_contexts(args), progress=_progress)
        print(f"\nwrote {args.out}")

    elif args.command == "run-api":
        import os
        from .backends import OpenAIBackend, OpenAISampler, SamplingBackend
        key = os.environ.get(args.api_key_env)
        if args.samples:
            backend = SamplingBackend(OpenAISampler(args.base_url, args.model, key), args.samples)
        else:
            backend = OpenAIBackend(args.base_url, args.model, key)
        _preflight(backend)
        if args.check:
            return
        collect.collect(backend, args.name or args.model, args.out, contexts=_contexts(args), progress=_progress)
        print(f"\nwrote {args.out}")

    elif args.command == "simulate":
        from . import simulate
        for name, backend in simulate.panel().items():
            collect.collect(backend, name, Path(args.out) / f"{name}.jsonl", contexts=probes.context_set(args.context_set))
        print(f"wrote synthetic observations to {args.out}")

    elif args.command == "identify":
        from . import analysis, fingerprint
        panel = fingerprint.load([args.query] + _expand(args.enrolled))
        panel = panel.with_contexts([c for c in panel.contexts if not probes.is_adversarial(c)])
        query = json.loads(Path(args.query).read_text(encoding="utf-8").splitlines()[0])["model"]
        for row in analysis.identify_unknown(panel, query):
            print(f"{row['candidate']:40s} distance {row['distance']:.4f}   candidate's own range {row['candidate_self_distance_max']:.4f}"
                  f"   {'CONSISTENT' if row['consistent'] else 'different'}")

    elif args.command == "diff":
        import collections
        import csv
        from . import graph
        a, b = (json.loads(Path(p).read_text(encoding="utf-8")) for p in (args.graph_a, args.graph_b))
        rows = graph.difference(a, b, args.tolerance)
        counts = collections.Counter((r["type"], r["status"]) for r in rows)
        for kind in dict.fromkeys(r["type"] for r in rows):
            print(f"{kind:20s} " + "  ".join(f"{status} {counts[kind, status]}" for status in ("SHARED", "CHANGED", "A_ONLY", "B_ONLY")))
        if args.out:
            with open(args.out, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)

    elif args.command == "analyze":
        groups = json.loads(Path(args.groups).read_text(encoding="utf-8")) if args.groups else None
        summary = report.analyze(_expand(args.observations), args.out, groups=groups)
        print(json.dumps({k: summary[k] for k in ("identification", "identification_interval_95", "open_set", "verification", "adversarial", "psychometric_vs_control", "scales", "alternate_forms", "self_report_alpha", "relatives")}, indent=1))
        print(f"report: {Path(args.out) / 'report.html'}")


if __name__ == "__main__":
    main()
