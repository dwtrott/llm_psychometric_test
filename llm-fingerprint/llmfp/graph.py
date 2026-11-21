"""The fingerprint as a typed, weighted knowledge graph.

Node labels are unique and shared across models, and every edge has a type
and a weight between 0 and 1. Two models' graphs are therefore aligned by
label, and a comparison is a comparison of measured edge weights.

Edge types
    similar_to           concept - concept      expected similarity rating
    prioritized_over     concept -> concept     P(source preferred), majority direction
    associates           cue -> word            first-token association probability
    indifference_point   self -> decision:*     threshold as a fraction of the swept range
    self_report          self -> trait:*        balanced-key content score, rescaled to 0..1
    means_probability    self -> phrase:*       expected probability of the phrase
    willing_to           self -> request:*      willingness to carry out a borderline request
    claims_developer     self -> org:*          probability of naming that developer
    response_style       self -> style:*        position preferences and label mass
"""
import csv
import json

import numpy as np

from . import battery, scales


def model_graph(panel, model, min_association=0.02, names=None, X=None):
    if X is None:
        names, X = scales.features(panel)
    m = panel.models.index(model)
    value = dict(zip(names, X[m].mean(0)))
    nodes, edges = {"self": "model"}, []

    def edge(source, target, kind, weight, **extra):
        edges.append(dict(source=source, target=target, type=kind, weight=float(np.clip(weight, 0, 1)), **extra))

    for concept in battery.CONCEPTS:
        nodes[concept] = "concept"
    for name, v in value.items():
        group, _, rest = name.partition(":")
        if group == "sim":
            a, b = rest.split("~")
            edge(a, b, "similar_to", v)
        elif group == "pri" and ">" in rest:
            a, b = rest.split(">")
            edge(*((a, b) if v >= 0.5 else (b, a)), "prioritized_over", max(v, 1 - v))
        elif group == "sweep" and rest.endswith(".threshold"):
            sweep = rest.split(".")[0]
            levels = battery.SWEEPS[sweep][1]
            node = f"decision:{sweep}"
            nodes[node] = "decision"
            level = float(np.interp(np.clip(v, 0, len(levels) - 1), range(len(levels)), levels))
            edge("self", node, "indifference_point", (v + 0.5) / len(levels), level=level,
                 slope=float(value[f"sweep:{sweep}.slope"]))
        elif group == "likert" and rest in battery.LIKERT:
            nodes[f"trait:{rest}"] = "trait"
            edge("self", f"trait:{rest}", "self_report", (v + 1) / 2)
        elif group == "est":
            nodes[f"phrase:{rest}"] = "phrase"
            edge("self", f"phrase:{rest}", "means_probability", v)
        elif group == "boundary" and rest != "overall":
            nodes[f"request:{rest}"] = "request"
            edge("self", f"request:{rest}", "willing_to", v)
        elif group == "style" or name in ("likert:acquiescence", "likert:extremity", "likert:midpoint"):
            node = f"style:{rest}"
            nodes[node] = "style"
            edge("self", node, "response_style", (v + 1) / 2 if rest == "acquiescence" else v)
    developer = panel.cells.get(("content", "identity.developer"))
    if developer is not None:
        for name, p in zip(panel.outcomes["content", "identity.developer"], developer[m].mean(0)):
            if p >= 0.05:
                nodes[f"org:{name}"] = "organization"
                edge("self", f"org:{name}", "claims_developer", p)
    for (channel, item), array in panel.cells.items():
        if channel != "assoc":
            continue
        cue = panel.items[item]["meta"]["cue"]
        nodes.setdefault(cue, "cue")
        for word, p in zip(panel.outcomes[channel, item], array[m].mean(0)):
            if word != "<other>" and word != cue and p >= min_association:
                nodes.setdefault(word, "word")
                edge(cue, word, "associates", p)
    return dict(model=model, nodes=[dict(id=k, type=v) for k, v in nodes.items()], edges=edges)


def difference(a, b, tolerance=0.05):
    """Union of two model graphs. Each edge is SHARED, CHANGED, A_ONLY or B_ONLY."""
    key = lambda e: (e["source"], e["target"], e["type"])
    wa, wb = {key(e): e["weight"] for e in a["edges"]}, {key(e): e["weight"] for e in b["edges"]}
    rows = []
    for k in sorted(set(wa) | set(wb)):
        if k in wa and k in wb:
            status = "SHARED" if abs(wa[k] - wb[k]) <= tolerance else "CHANGED"
        else:
            status = "A_ONLY" if k in wa else "B_ONLY"
        rows.append(dict(source=k[0], target=k[1], type=k[2], a=wa.get(k), b=wb.get(k), status=status))
    return rows


def write(graph, json_path, csv_path=None):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=1)
    if csv_path:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["source", "target", "type", "weight"])
            for e in graph["edges"]:
                writer.writerow([e["source"], e["target"], e["type"], f"{e['weight']:.4f}"])


def feature_network(names, X, model_index, shrinkage=0.2, threshold=0.2, min_contexts=30):
    """Partial-correlation network among scale values WITHIN one model,
    estimated across contexts. Contexts play the role that persons play in a
    human psychometric network. Refuses to run on too few contexts."""
    x = X[model_index]
    if len(x) < min_contexts:
        raise ValueError(f"{len(x)} contexts; at least {min_contexts} are needed to estimate a network")
    keep = x.std(0) > 1e-6
    x, kept = x[:, keep], [n for n, k in zip(names, keep) if k]
    x = (x - x.mean(0)) / x.std(0)
    cov = (1 - shrinkage) * np.cov(x, rowvar=False) + shrinkage * np.eye(len(kept))
    precision = np.linalg.inv(cov)
    scale = np.sqrt(np.diag(precision))
    partial = -precision / np.outer(scale, scale)
    edges = [dict(source=kept[i], target=kept[j], partial_correlation=float(partial[i, j]))
             for i in range(len(kept)) for j in range(i + 1, len(kept)) if abs(partial[i, j]) > threshold]
    return dict(n_contexts=len(x), nodes=kept, edges=edges)
