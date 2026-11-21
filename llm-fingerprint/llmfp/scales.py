"""Classical scoring models for each battery family.

Each function turns content distributions into named scale values. All values
are computed for every (model, context), so their reliability can be measured
instead of assumed.

    similarity   expected rating, rescaled to 0..1
    priority     P(a over b), Bradley-Terry strengths, share of circular triads
    sweep        Spearman-Karber threshold, logistic slope, mean response
    likert       content score per dimension from balanced keys, acquiescence,
                 extremity and midpoint use
    estimative   expected probability per phrase
    boundary     willingness per borderline request and overall
    response style   position preference and label mass
"""
import itertools

import numpy as np

from . import battery


def expected(dist, values):
    return (dist * np.asarray(values, dtype=float)).sum(-1)


def bradley_terry(P, iterations=200):
    """Strengths from a matrix of preference probabilities P[i, j] = P(i over j).
    Returns centered log strengths. Probabilities are clipped so that a
    unanimous preference does not produce an infinite strength."""
    n = len(P)
    P = np.clip(P, 0.02, 0.98)
    np.fill_diagonal(P, 0)
    wins = P.sum(1)
    s = np.ones(n)
    for _ in range(iterations):
        denom = np.array([sum(1 / (s[i] + s[j]) for j in range(n) if j != i) for i in range(n)])
        s = wins / denom
        s /= np.exp(np.log(s).mean())
    return np.log(s)


def circular_triads(P):
    """Share of triads whose majority preferences form a cycle."""
    n = len(P)
    cycles = total = 0
    for i, j, k in itertools.combinations(range(n), 3):
        a, b, c = P[i, j] > 0.5, P[j, k] > 0.5, P[k, i] > 0.5
        cycles += (a and b and c) or (not a and not b and not c)
        total += 1
    return cycles / total


def spearman_karber(p):
    """Threshold of a response curve in level-index units, without assuming a
    functional form. p[j] is the probability of the target response at level
    j. The curve is treated as 0 below the first level and 1 above the last."""
    return len(p) - 0.5 - float(np.sum(p))


def logistic_slope(p, ridge=0.05, iterations=30):
    """Slope of logit P(target) on level index, by penalized Newton iterations.
    A negative slope means the response moves against the expected direction."""
    x = np.arange(len(p)) - (len(p) - 1) / 2
    X = np.stack([np.ones_like(x), x], 1)
    beta = np.zeros(2)
    penalty = np.diag([0.0, ridge])
    for _ in range(iterations):
        mu = 1 / (1 + np.exp(-X @ beta))
        gradient = X.T @ (p - mu) - penalty @ beta
        hessian = X.T @ (X * (mu * (1 - mu))[:, None]) + penalty + 1e-6 * np.eye(2)
        beta = beta + np.linalg.solve(hessian, gradient)
    return float(np.clip(beta[1], -6, 6))


def features(panel):
    """Returns (names, array of shape (models, contexts, features))."""
    M, C = len(panel.models), len(panel.contexts)
    names, columns = [], []

    def add(name, values):
        names.append(name)
        columns.append(np.asarray(values, dtype=float).reshape(M, C))

    def content(item_id):
        return panel.cells.get(("content", item_id))

    def per_unit(function):
        return [[function(m, c) for c in range(C)] for m in range(M)]

    by_family = {}
    for item in panel.items.values():
        by_family.setdefault(item["family"], []).append(item)

    for item in by_family.get("similarity", []):
        x = content(item["id"])
        if x is not None:
            add(f"sim:{item['meta']['a']}~{item['meta']['b']}", (expected(x, range(5))) / 4)

    concepts = battery.CONCEPTS
    pairs = {(i["meta"]["a"], i["meta"]["b"]): content(i["id"]) for i in by_family.get("priority", [])}
    if pairs and all(v is not None for v in pairs.values()):
        P = np.full((M, C, len(concepts), len(concepts)), 0.5)
        for (a, b), x in pairs.items():
            i, j = concepts.index(a), concepts.index(b)
            P[:, :, i, j], P[:, :, j, i] = x[:, :, 0], x[:, :, 1]
            add(f"pri:{a}>{b}", x[:, :, 0])
        strengths = np.array(per_unit(lambda m, c: bradley_terry(P[m, c].copy())))
        for i, concept in enumerate(concepts):
            add(f"bt:{concept}", strengths[:, :, i])
        add("pri:circular_triads", per_unit(lambda m, c: circular_triads(P[m, c])))

    sweeps = {}
    for item in by_family.get("sweep", []):
        sweeps.setdefault((item["meta"]["sweep"], item["meta"].get("form", "a")), []).append(item)
    for (name, form), group in sweeps.items():
        prefix = "sweep" if form == "a" else "sweep_b"
        group.sort(key=lambda i: i["meta"]["index"])
        if any(content(i["id"]) is None for i in group):
            continue
        target = [o["key"] for o in group[0]["options"]].index(group[0]["meta"]["target"])
        curve = np.stack([content(i["id"])[:, :, target] for i in group], -1)     # (M, C, levels)
        add(f"{prefix}:{name}.threshold", per_unit(lambda m, c: spearman_karber(curve[m, c])))
        add(f"{prefix}:{name}.slope", per_unit(lambda m, c: logistic_slope(curve[m, c])))
        add(f"{prefix}:{name}.reversals", (np.diff(curve, axis=-1) < -0.05).sum(-1))

    likert = by_family.get("likert", [])
    ratings = {i["id"]: (expected(content(i["id"]), range(5)) - 2) / 2 for i in likert if content(i["id"]) is not None}
    if likert and len(ratings) == len(likert):
        for dimension in dict.fromkeys(i["meta"]["dimension"] for i in likert):
            pos = [ratings[i["id"]] for i in likert if i["meta"]["dimension"] == dimension and i["meta"]["keyed"] > 0]
            neg = [ratings[i["id"]] for i in likert if i["meta"]["dimension"] == dimension and i["meta"]["keyed"] < 0]
            add(f"likert:{dimension}", (np.mean(pos, 0) - np.mean(neg, 0)) / 2)
        stack = np.stack([content(i["id"]) for i in likert])
        add("likert:acquiescence", np.mean(list(ratings.values()), 0))    # balanced keys: content cancels
        add("likert:extremity", (stack[..., 0] + stack[..., 4]).mean(0))
        add("likert:midpoint", stack[..., 2].mean(0))

    for item in by_family.get("estimative", []):
        x = content(item["id"])
        if x is not None:
            add(f"est:{item['meta']['phrase']}", expected(x, np.arange(11) / 10))

    boundary = [(i, content(i["id"])) for i in by_family.get("boundary", [])]
    if boundary and all(x is not None for _, x in boundary):
        willing = [x[:, :, 0] + 0.5 * x[:, :, 1] for _, x in boundary]     # HELP, PARTIAL, DECLINE
        for (item, _), value in zip(boundary, willing):
            add(f"boundary:{item['meta']['request']}", value)
        add("boundary:overall", np.mean(willing, 0))

    x = content("identity.training_year")
    if x is not None:
        add("identity:training_year", expected(x, [int(y) for y in battery.TRAINING_YEARS]))

    def mean_cell(channel, predicate, column):
        arrays = [panel.cells[channel, i["id"]][:, :, column] for i in panel.items.values()
                  if (channel, i["id"]) in panel.cells and predicate(i)]
        return np.mean(arrays, 0) if arrays else None

    for name, predicate in (("style:first_of_two", lambda i: i["kind"] == "nominal" and len(i["options"]) == 2),
                            ("style:first_of_four", lambda i: i["kind"] == "nominal" and len(i["options"]) == 4),
                            ("style:scale_start", lambda i: i["kind"] == "ordinal")):
        value = mean_cell("position", predicate, 0)
        if value is not None:
            add(name, value)
    value = mean_cell("format", lambda i: True, 0)
    if value is not None:
        add("style:label_mass", value)

    return names, np.stack(columns, -1)


def alternate_form_reliability(names, X):
    """Across models, do the two wordings of each sweep give the same threshold?
    A threshold that changes with wording is a property of the wording."""
    if X.shape[0] < 4:
        return None
    mean = dict(zip(names, X.mean(1).T))
    out, a_all, b_all = {}, [], []
    for name in battery.SWEEPS:
        a, b = mean.get(f"sweep:{name}.threshold"), mean.get(f"sweep_b:{name}.threshold")
        if a is None or b is None:
            continue
        out[name] = dict(r=float(np.corrcoef(a, b)[0, 1]) if a.std() > 0 and b.std() > 0 else None,
                         mean_abs_difference=float(np.abs(a - b).mean()))
        a_all.append(a - a.mean())
        b_all.append(b - b.mean())
    if a_all:
        a, b = np.concatenate(a_all), np.concatenate(b_all)
        out["pooled"] = dict(r=float(np.corrcoef(a, b)[0, 1]), mean_abs_difference=float(np.abs(a - b).mean()))
    return out


def internal_consistency(panel):
    """Cronbach's alpha of each self-report dimension, with models as subjects
    and reverse-keyed statements aligned."""
    if len(panel.models) < 4:
        return None
    out = {}
    for dimension in battery.LIKERT:
        columns = [item["meta"]["keyed"] * expected(panel.cells["content", item["id"]].mean(1), range(5))
                   for item in panel.items.values()
                   if item["family"] == "likert" and item["meta"]["dimension"] == dimension
                   and ("content", item["id"]) in panel.cells]
        if len(columns) < 2:
            continue
        S = np.stack(columns, 1)
        k, total = S.shape[1], S.sum(1).var(ddof=1)
        out[dimension] = float(k / (k - 1) * (1 - S.var(0, ddof=1).sum() / total)) if total > 0 else None
    return out


def reliability(names, X):
    """Intraclass correlation ICC(1) of each feature, with models as subjects
    and contexts as repeated occasions. 1 means the feature depends only on
    the model; 0 means it varies as much within a model as between models."""
    M, C, _ = X.shape
    model_mean = X.mean(1)
    grand = model_mean.mean(0)
    msb = C * ((model_mean - grand) ** 2).sum(0) / (M - 1)
    msw = ((X - model_mean[:, None]) ** 2).sum((0, 1)) / (M * (C - 1))
    icc = (msb - msw) / (msb + (C - 1) * msw + 1e-15)
    return [dict(feature=n, icc=float(i), between_sd=float(model_mean[:, k].std(ddof=1)),
                 within_sd=float(np.sqrt(msw[k]))) for k, (n, i) in enumerate(zip(names, icc))]


def feature_identification(X, floor=0.05):
    """Leave-one-context-out identification from scale values alone. Each
    feature is divided by its pooled within-model standard deviation, which
    is estimated from the reference contexts only."""
    M, C, _ = X.shape
    hits = 0
    for c in range(C):
        ref = np.delete(X, c, axis=1)
        centroid = ref.mean(1)
        within = np.sqrt(((ref - centroid[:, None]) ** 2).sum((0, 1)) / (M * (C - 2)))
        scale = np.maximum(within, floor * ref.reshape(-1, X.shape[-1]).std(0) + 1e-9)
        d = (((X[:, c][:, None, :] - centroid[None, :, :]) / scale) ** 2).sum(-1)
        hits += (d.argmin(-1) == np.arange(M)).sum()
    return dict(accuracy=float(hits / (M * C)), chance=1 / M, n_features=X.shape[-1])
