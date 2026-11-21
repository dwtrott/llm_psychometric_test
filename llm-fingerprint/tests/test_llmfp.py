"""End-to-end checks on synthetic models. Run: python tests/test_llmfp.py

These verify that the statistics do what they claim on data with known
structure. They say nothing about how real models behave.
"""
import json
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from llmfp import analysis, backends, battery, collect, fingerprint, graph, probes, report, scales, simulate

GROUPS = {"base0-finetune": "base0", "base3-finetune": "base3", "base2-quantized": "base2", "base1-copy": "base1"}


def simulated(models, contexts=None, **kwargs):
    tmp = Path(tempfile.mkdtemp())
    paths = [collect.collect(backend, name, tmp / f"{name}.jsonl", contexts=contexts, **kwargs)
             for name, backend in models.items()]
    return paths, tmp


def test_battery_design():
    items = battery.build()
    assert len({i["id"] for i in items}) == len(items)
    for item in items:
        orders = probes.orders(item)
        n = len(item["options"])
        if item["kind"] == "nominal":      # every option appears at every position exactly once
            assert all(sorted(o[p] for o in orders) == list(range(n)) for p in range(n))
        elif item["kind"] == "ordinal":
            assert orders == [list(range(n)), list(range(n))[::-1]]
    likert = [i for i in items if i["family"] == "likert"]
    for dimension in battery.LIKERT:        # balanced keying
        keys = [i["meta"]["keyed"] for i in likert if i["meta"]["dimension"] == dimension]
        assert sum(keys) == 0 and len(keys) == 6


def test_position_is_separated_from_content():
    # A model with strong primacy and one with none have the same latent content.
    class Primacy(simulate.SimBackend):
        def __init__(self, strength):
            super().__init__(seed=5, context_noise=0.0)
            self.strength = strength

        def latent(self, name):
            return self.strength if name == "primacy" else super().latent(name)

    paths, _ = simulated({"flat": Primacy(0.0), "primacy": Primacy(3.0)}, contexts=probes.DEFAULT_CONTEXTS[:3])
    panel = fingerprint.load(paths)
    flat, biased = 0, 1
    for key in panel.select(channels=("position",)):
        x = panel.cells[key]
        assert np.allclose(x[flat], 1 / x.shape[-1], atol=1e-9)        # exactly uniform without bias
        assert x[biased, 0, 0] > x[biased, 0, -1]                       # first position preferred
    # Content after averaging rotations barely moves although the raw responses are heavily biased.
    for key in panel.select(channels=("content",), families=("arbitrary",)):
        assert np.abs(panel.cells[key][flat] - panel.cells[key][biased]).max() < 0.2


def test_scales_recover_known_parameters():
    model = simulate.SimBackend(seed=7, context_noise=0.0)
    other = simulate.SimBackend(seed=8, context_noise=0.0)
    paths, _ = simulated({"a": model, "b": other}, contexts=probes.DEFAULT_CONTEXTS[:3])
    panel = fingerprint.load(paths)
    names, X = scales.features(panel)
    value = dict(zip(names, X[0, 0]))
    for sweep in battery.SWEEPS:
        truth = model.true_threshold(sweep)
        if 1 < truth < 5:                   # inside the swept range
            assert abs(value[f"sweep:{sweep}.threshold"] - truth) < 0.5, (sweep, truth, value[f"sweep:{sweep}.threshold"])
            assert value[f"sweep:{sweep}.slope"] > 0.5
    truth = [model.latent("bt." + c) for c in battery.CONCEPTS]
    estimate = [value["bt:" + c] for c in battery.CONCEPTS]
    assert np.corrcoef(truth, estimate)[0, 1] > 0.95
    truth = [model.latent("trait." + d) for d in battery.LIKERT]
    estimate = [value["likert:" + d] for d in battery.LIKERT]
    assert np.corrcoef(truth, estimate)[0, 1] > 0.8
    # Acquiescence is separated from content by the balanced keys.
    assert np.sign(value["likert:acquiescence"]) == np.sign(model.latent("acquiescence"))


def test_bradley_terry_and_transitivity():
    s = np.array([1.5, 0.5, 0.0, -2.0])
    P = 1 / (1 + np.exp(-(s[:, None] - s[None, :])))
    assert np.allclose(scales.bradley_terry(P.copy()), s - s.mean(), atol=0.05)
    assert scales.circular_triads(P) == 0
    cycle = np.array([[0.5, 0.9, 0.1], [0.1, 0.5, 0.9], [0.9, 0.1, 0.5]])
    assert scales.circular_triads(cycle) == 1


def test_identification_lineage_and_controls():
    paths, tmp = simulated(simulate.panel())
    panel = fingerprint.load(paths)
    distinct = panel.subset([m for m in panel.models if m not in ("base1-copy", "base2-quantized")])

    # Distinct models, including fine-tunes, are identified from unseen contexts.
    assert analysis.identification(distinct)["accuracy"] == 1.0

    # An exact copy is at zero distance and passes verification as its original.
    i, j = panel.models.index("base1"), panel.models.index("base1-copy")
    assert analysis.model_distance_matrix(panel)[i, j] < 1e-9
    query = {k: v[j, 0] for k, v in panel.cells.items()}
    assert analysis.verify(panel, query, "base1")["p_same_model"] > 0.1

    # An unrelated model is rejected.
    query = {k: v[panel.models.index("base4"), 0] for k, v in panel.cells.items()}
    assert analysis.verify(panel, query, "base1")["p_same_model"] <= 1 / (1 + len(panel.contexts)) + 1e-9

    # Relatives attach to their parents.
    nearest = analysis.lineage(panel)["nearest"]
    for child, parent in GROUPS.items():
        assert nearest[child] == parent, (child, nearest[child])

    # With lineages declared, every query is matched within its lineage.
    assert analysis.identification(panel, groups=GROUPS)["lineage_accuracy"] == 1.0
    ver = analysis.separation(panel, groups=GROUPS)
    assert ver["auc"] > 0.99

    # Scale values are reliable and identify models on their own.
    names, X = scales.features(distinct)
    icc = np.array([r["icc"] for r in scales.reliability(names, X)])
    assert np.median(icc) > 0.7
    assert scales.feature_identification(X)["accuracy"] > 0.95

    # The full report runs and writes its outputs.
    summary = report.analyze(paths, tmp / "report", groups=GROUPS)
    for name in ("report.html", "summary.json", "item_information.csv", "scale_reliability.csv",
                 "graphs/lineage.json", "graphs/base0.json", "graphs/base0.edges.csv"):
        assert (tmp / "report" / name).exists(), name
    assert summary["identification"]["lineage_accuracy"] == 1.0


def test_open_set_adversarial_and_unknown_models():
    models = {k: v for k, v in simulate.panel().items() if k in ("base0", "base1", "base2", "base3", "base0-finetune")}
    paths, tmp = simulated(models, contexts=probes.context_set("all"))
    full = fingerprint.load(paths)
    benign = [c for c in full.contexts if not probes.is_adversarial(c)]
    adversarial = [c for c in full.contexts if probes.is_adversarial(c)]
    assert len(benign) == 8 and len(adversarial) == 6
    panel = full.with_contexts(benign)
    groups = {"base0-finetune": "base0"}

    # Unrelated models are far enough apart that an unenrolled model is not accepted.
    result = analysis.open_set(panel, groups=groups)
    assert result["false_accept"] == 0 and result["false_reject"] <= 0.1
    low, high = analysis.identification_interval(panel)
    assert 0.9 <= low <= high <= 1.0

    # Adversarial contexts push a model away from its reference but it is still found.
    robust = analysis.robustness(full, benign, adversarial)
    genuine = analysis.open_set(panel)["genuine_median"]
    assert all(v["own_distance"] > genuine for v in robust.values())
    assert np.mean([v["accuracy"] for v in robust.values()]) > 0.9

    # An unlabeled fine-tune is ranked nearest to its base and outside the base's own range.
    ranked = analysis.identify_unknown(panel, "base0-finetune")
    assert ranked[0]["candidate"] == "base0" and not ranked[0]["consistent"]

    summary = report.analyze(paths, tmp / "report", groups=groups)
    assert set(summary["adversarial"]) == set(adversarial)
    assert summary["contexts"] == benign and "adv." in (tmp / "report" / "report.html").read_text()


def test_new_families_are_scored():
    paths, _ = simulated({"a": simulate.SimBackend(1), "b": simulate.SimBackend(2)}, contexts=probes.DEFAULT_CONTEXTS[:3])
    panel = fingerprint.load(paths)
    names, X = scales.features(panel)
    value = dict(zip(names, X[0, 0]))
    assert 0 <= value["boundary:overall"] <= 1 and len([n for n in names if n.startswith("boundary:")]) == 17
    assert 2021 <= value["identity:training_year"] <= 2026
    families = panel.families()
    assert "boundary" in families and "identity" in families


def test_alternate_forms_alpha_and_relatives():
    paths, tmp = simulated({k: v for k, v in simulate.panel().items() if k != "base1-copy"},
                           contexts=probes.DEFAULT_CONTEXTS[:4])
    panel = fingerprint.load(paths)
    names, X = scales.features(panel)
    forms = scales.alternate_form_reliability(names, X)
    assert set(battery.SWEEPS) <= set(forms) and forms["pooled"]["r"] > 0.8
    alpha = scales.internal_consistency(panel)
    assert set(alpha) == set(battery.LIKERT) and all(a <= 1 for a in alpha.values())
    groups = {k: v for k, v in GROUPS.items() if k != "base1-copy"}
    related = {(r["a"], r["b"]): r["share_of_unrelated_median"] for r in analysis.relatives(panel, groups)}
    assert related["base2", "base2-quantized"] < related["base0", "base0-finetune"] < 1
    # Lineage groups reach the per-family table (relatives are not counted as different models).
    table = analysis.by_group(panel, groups)
    assert table["content:sweep"]["probes_per_context"] == 224 and table["content:psychometric"]["auc"] > 0.99

    from llmfp import cli
    assert len(cli._expand([str(tmp)])) == len(paths) == len(cli._expand([str(tmp / "*.jsonl")]))
    summary = report.analyze(cli._expand([str(tmp)]), tmp / "report", groups=groups)
    assert "risk_gain: level at which the choice turns to SURE" in summary["profiles"]
    assert (tmp / "report" / "scale_values.csv").exists()


def test_uninformative_items_score_zero():
    # Models that differ only in one family carry no information elsewhere.
    class OnlySweeps(simulate.SimBackend):
        def latent(self, name):
            if name.startswith(("threshold.", "slope.")):
                return super().latent(name)
            return simulate._g("shared", name)

    paths, _ = simulated({f"m{n}": OnlySweeps(seed=n, context_noise=0.0) for n in range(4)},
                         contexts=probes.DEFAULT_CONTEXTS[:3])
    panel = fingerprint.load(paths)
    rows = analysis.item_information(panel, panel.select(channels=("content", "assoc")))
    by_family = {}
    for r in rows:
        by_family.setdefault(r["family"], []).append(r["between_bits"])
    assert max(by_family["similarity"]) < 1e-9 and max(by_family["likert"]) < 1e-9
    assert max(by_family["sweep"]) > 0.05


def test_graph_export_and_difference():
    paths, _ = simulated({k: v for k, v in simulate.panel().items() if k in ("base0", "base0-finetune", "base4")})
    panel = fingerprint.load(paths)
    graphs = {m: graph.model_graph(panel, m) for m in panel.models}
    g = graphs["base0"]
    ids = [n["id"] for n in g["nodes"]]
    assert len(ids) == len(set(ids))
    assert all(0 <= e["weight"] <= 1 and e["source"] in ids and e["target"] in ids for e in g["edges"])
    types = {e["type"] for e in g["edges"]}
    assert types == {"similar_to", "prioritized_over", "associates", "indifference_point", "self_report",
                     "means_probability", "response_style", "willing_to", "claims_developer"}
    changed = lambda a, b: sum(r["status"] != "SHARED" for r in graph.difference(graphs[a], graphs[b]))
    assert changed("base0", "base0") == 0
    assert changed("base0", "base0-finetune") < changed("base0", "base4")


def test_feature_network_needs_many_contexts():
    contexts = [dict(id=f"c{n}", system=f"variant {n}") for n in range(40)]
    items = [i for i in battery.build() if i["family"] in ("sweep", "likert")]
    paths, _ = simulated({"a": simulate.SimBackend(1), "b": simulate.SimBackend(2)}, contexts=contexts, items=items)
    panel = fingerprint.load(paths, items)
    names, X = scales.features(panel)
    try:
        graph.feature_network(names, X[:, :8], 0)
        raise AssertionError("expected refusal")
    except ValueError:
        pass
    network = graph.feature_network(names, X, 0)
    assert network["n_contexts"] == 40 and network["nodes"]


def test_collection_resumes_and_rejects_mixed_batteries():
    tmp = Path(tempfile.mkdtemp())
    items = battery.build()[:5]
    path = collect.collect(simulate.SimBackend(1), "m", tmp / "m.jsonl", items=items)
    size = path.stat().st_size
    collect.collect(simulate.SimBackend(1), "m", path, items=items)        # nothing left to do
    assert path.stat().st_size == size
    for bad in (lambda: collect.collect(simulate.SimBackend(1), "m", path, items=battery.build()[:6]),
                lambda: fingerprint.load([path])):
        try:
            bad()
            raise AssertionError("expected a battery mismatch error")
        except ValueError:
            pass


def test_openai_backend_reads_logprobs():
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            top = [dict(token="A", logprob=np.log(0.5)), dict(token=" A", logprob=np.log(0.1)),
                   dict(token="B", logprob=np.log(0.3)), dict(token="The", logprob=np.log(0.1))]
            if body.get("logprobs"):
                payload = json.dumps(dict(choices=[dict(logprobs=dict(content=[dict(top_logprobs=top)]))])).encode()
            else:
                payload = json.dumps(dict(choices=[dict(message=dict(content="B"))])).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    backend = backends.OpenAIBackend(f"http://127.0.0.1:{server.server_port}/v1", "x")
    probe = dict(messages=[dict(role="user", content="q")], labels=["A", "B"])
    assert np.allclose(backend.label_probs([probe])[0], [0.6, 0.3])
    assert backend.top_tokens([probe], 3)[0]["a"] > 0.59
    check = collect.preflight(backend, n=4)
    assert abs(check["mean_label_mass"] - 0.9) < 1e-6 and len(check["first_tokens"]) == 3
    sampler = backends.OpenAISampler(f"http://127.0.0.1:{server.server_port}/v1", "x")
    assert backends.SamplingBackend(sampler, 4).label_probs([probe])[0] == [0.0, 1.0]
    server.shutdown()


def test_sampling_backend_parses_letters():
    replies = iter(["A", "(B)", " a.", "B", "I think A", "A"] * 10)
    backend = backends.SamplingBackend(lambda messages: next(replies), n_samples=6)
    assert backend.label_probs([dict(messages=[], labels=["A", "B"])])[0] == [3 / 6, 2 / 6]


if __name__ == "__main__":
    for name, function in list(globals().items()):
        if name.startswith("test_"):
            function()
            print("ok", name)
    print("all checks passed")
