"""Fingerprint statistics. The criterion is identification, not construct validity.

Every statistic is defined on a panel: several models, each observed under
several contexts. Models are the subjects and contexts are the occasions.
"""
import itertools

import numpy as np

from . import probes
from .battery import CONTROL_FAMILIES, DECLARED_FAMILIES
from .fingerprint import entropy, jsd


def _stack(panel, cells):
    return [panel.cells[k] for k in cells]


def item_information(panel, cells=None, contexts=None):
    """For each cell, the bits one response carries about model identity
    (between) and about the context within a model (within)."""
    rows = []
    index = slice(None) if contexts is None else [panel.contexts.index(c) for c in contexts]
    for key in cells or list(panel.cells):
        x = panel.cells[key][:, index]                      # (M, C, K)
        per_model = x.mean(1)                               # (M, K)
        between = float(entropy(per_model.mean(0)) - entropy(per_model).mean())
        within = float((entropy(per_model) - entropy(x).mean(1)).mean())
        between, within = max(between, 0.0), max(within, 0.0)
        rows.append(dict(channel=key[0], item=key[1], family=panel.items[key[1]]["family"],
                         between_bits=between, within_bits=within, net_bits=between - within,
                         stability=between / (between + within) if between + within > 0 else 0.0))
    return rows


def _loco_tensor(panel, cells=None):
    """Per-cell leave-one-context-out divergences, shape (cells, C, M, M)."""
    arrays = _stack(panel, cells or list(panel.cells))
    M, C = len(panel.models), len(panel.contexts)
    T = np.zeros((len(arrays), C, M, M))
    for n, x in enumerate(arrays):
        summed = x.sum(1)
        for c in range(C):
            refs = (summed - x[:, c]) / (C - 1)
            T[n, c] = jsd(x[:, c][:, None, :], refs[None, :, :])
    return T


def loco_distances(panel, cells=None):
    """Leave-one-context-out distances. Returns D[c, query model, reference model]:
    the distance from each model's fingerprint under context c to every model's
    reference built from all other contexts."""
    return np.sqrt(_loco_tensor(panel, cells).mean(0))


def identification_interval(panel, cells=None, draws=300, seed=0):
    """Bootstrap over items: how much does identification accuracy depend on
    which items happen to be in the battery? Returns a 95% interval."""
    T = _loco_tensor(panel, cells)
    rng = np.random.default_rng(seed)
    truth = np.arange(len(panel.models))
    accuracy = []
    for _ in range(draws):
        weights = np.bincount(rng.integers(0, len(T), len(T)), minlength=len(T))
        accuracy.append((np.tensordot(weights, T, 1).argmin(-1) == truth).mean())
    return [float(np.quantile(accuracy, 0.025)), float(np.quantile(accuracy, 0.975))]


def open_set(panel, cells=None, groups=None, accept_quantile=0.95):
    """What happens when the true model is NOT among the references?

    Each query is compared with every reference except its own lineage, as if
    its model had never been enrolled. The acceptance threshold is the stated
    quantile of genuine same-model distances. false_accept is the share of
    such unknown-model queries that would be accepted as some enrolled model.
    false_reject is the share of genuine queries that would be turned away."""
    D = loco_distances(panel, cells)
    M = len(panel.models)
    truth = np.arange(M)
    lineage_of = np.array([(groups or {}).get(m, m) for m in panel.models])
    related = lineage_of[:, None] == lineage_of[None, :]
    genuine = D[:, truth, truth]
    impostor = np.where(related[None], np.inf, D).min(-1)
    threshold = float(np.quantile(genuine, accept_quantile))
    return dict(threshold=threshold, false_accept=float((impostor <= threshold).mean()),
                false_reject=float((genuine > threshold).mean()),
                genuine_median=float(np.median(genuine)), impostor_median=float(np.median(impostor)))


def robustness(panel, reference_contexts, query_contexts, cells=None):
    """Identification of queries collected under query_contexts against
    references built only from reference_contexts. Used for adversarial
    contexts, which never contribute to a reference."""
    arrays = _stack(panel, cells or list(panel.cells))
    ri = [panel.contexts.index(c) for c in reference_contexts]
    truth = np.arange(len(panel.models))
    out = {}
    for context in query_contexts:
        c = panel.contexts.index(context)
        total = sum(jsd(x[:, c][:, None, :], x[:, ri].mean(1)[None, :, :]) for x in arrays)
        D = np.sqrt(total / len(arrays))
        out[context] = dict(accuracy=float((D.argmin(-1) == truth).mean()),
                            own_distance=float(D[truth, truth].mean()))
    return out


def identify_unknown(panel, query_model, cells=None):
    """Rank the enrolled models as candidates for an unlabeled query model.

    The query is excluded from every reference. For each candidate the result
    gives the query's mean distance over its contexts and the largest distance
    the candidate shows to itself across contexts. A query within that range
    is consistent with being the candidate."""
    cells = cells or list(panel.cells)
    q = panel.models.index(query_model)
    others = [m for m in panel.models if m != query_model]
    enrolled = panel.subset(others)
    own = loco_distances(enrolled, cells)
    rows = []
    for i, candidate in enumerate(others):
        total = sum(jsd(panel.cells[k][q], enrolled.cells[k][i].mean(0)[None, :]) for k in cells)
        per_context = np.sqrt(total / len(cells))
        null = own[:, i, i]
        rows.append(dict(candidate=candidate, distance=float(per_context.mean()),
                         candidate_self_distance_max=float(null.max()),
                         consistent=bool(per_context.mean() <= null.max())))
    return sorted(rows, key=lambda r: r["distance"])


def identification(panel, cells=None, groups=None):
    """Closed-set identification of every single-context fingerprint against
    references that never saw that context. With groups, a match to any model
    of the same lineage also counts toward lineage_accuracy."""
    D = loco_distances(panel, cells)
    M = len(panel.models)
    truth = np.arange(M)
    predicted = D.argmin(-1)
    hits = predicted == truth
    own = D[:, truth, truth]
    other = np.where(np.eye(M, dtype=bool), np.inf, D).min(-1)
    confusions = {}
    for c, q in zip(*np.where(~hits)):
        pair = (panel.models[q], panel.models[predicted[c, q]])
        confusions[pair] = confusions.get(pair, 0) + 1
    result = dict(accuracy=float(hits.mean()), n_queries=int(hits.size), chance=1 / M,
                  mean_margin=float((other - own).mean()), min_margin=float((other - own).min()),
                  confusions=[dict(true=a, predicted=b, count=n) for (a, b), n in sorted(confusions.items())])
    if groups:
        lineage_of = np.array([groups.get(m, m) for m in panel.models])
        result["lineage_accuracy"] = float((lineage_of[predicted] == lineage_of[truth][None, :]).mean())
    return result


def unit_distances(panel, cells=None, groups=None):
    """Distances between all single-context fingerprints, split into same-model
    pairs (different contexts) and different-model pairs. groups maps a model
    to a lineage label; pairs of different models in one lineage are known
    relatives and are left out of the different-model set."""
    arrays = _stack(panel, cells or list(panel.cells))
    M, C = len(panel.models), len(panel.contexts)
    total = np.zeros((M * C, M * C))
    for x in arrays:
        flat = x.reshape(M * C, -1)
        total += jsd(flat[:, None, :], flat[None, :, :])
    D = np.sqrt(total / len(arrays))
    model_of = np.repeat(np.arange(M), C)
    lineage_of = np.array([(groups or {}).get(m, m) for m in panel.models])[model_of]
    upper = np.triu(np.ones_like(D, dtype=bool), 1)
    same = D[upper & (model_of[:, None] == model_of[None, :])]
    different = D[upper & (lineage_of[:, None] != lineage_of[None, :])]
    return same, different


def auc(same, different):
    """Probability that a different-model pair is farther apart than a same-model pair."""
    order = np.concatenate([same, different]).argsort(kind="mergesort")
    ranks = np.empty(len(order))
    ranks[order] = np.arange(1, len(order) + 1)
    values = np.concatenate([same, different])
    for v in np.unique(values):                  # average ranks over ties
        tie = values == v
        ranks[tie] = ranks[tie].mean()
    u = ranks[len(same):].sum() - len(different) * (len(different) + 1) / 2
    return float(u / (len(same) * len(different)))


def separation(panel, cells=None, false_match_rate=0.01, groups=None):
    """Verification operating point. The threshold is set so that only
    false_match_rate of different-model pairs fall below it."""
    same, different = unit_distances(panel, cells, groups)
    threshold = float(np.quantile(different, false_match_rate))
    return dict(auc=auc(same, different), threshold=threshold, false_match_rate=false_match_rate,
                true_match_rate=float((same < threshold).mean()),
                same_model_max=float(same.max()), different_model_min=float(different.min()))


def model_distance_matrix(panel, cells=None):
    arrays = _stack(panel, cells or list(panel.cells))
    M = len(panel.models)
    total = np.zeros((M, M))
    for x in arrays:
        mean = x.mean(1)
        total += jsd(mean[:, None, :], mean[None, :, :])
    return np.sqrt(total / len(arrays))


def verify(panel, query, reference_model, cells=None):
    """Is a query fingerprint consistent with a reference model?

    query maps cell -> distribution array (one context of an unknown model).
    Returns its distance to the reference and the share of the reference's own
    leave-one-context-out distances that are at least as large."""
    cells = cells or list(panel.cells)
    m = panel.models.index(reference_model)
    D = loco_distances(panel, cells)
    null = D[:, m, m]
    total = sum(float(jsd(query[k], panel.cells[k][m].mean(0))) for k in cells)
    d = float(np.sqrt(total / len(cells)))
    return dict(distance=d, p_same_model=float((1 + (null >= d).sum()) / (1 + len(null))),
                same_model_null_max=float(null.max()))


def selection_curve(panel, cells=None, sizes=(10, 25, 50, 100, 200, 400)):
    """Rank cells on half of the contexts, test identification on the other half."""
    cells = cells or list(panel.cells)
    train, test = panel.contexts[::2], panel.contexts[1::2]
    ti = [panel.contexts.index(c) for c in train]
    si = [panel.contexts.index(c) for c in test]
    ranked = sorted(item_information(panel, cells, train), key=lambda r: -r["net_bits"])
    truth = np.arange(len(panel.models))
    curve = []
    for n in list(sizes) + [len(ranked)]:
        n = min(n, len(ranked))
        if curve and curve[-1]["n_cells"] == n:
            break
        total = np.zeros((len(si), len(truth), len(truth)))
        for r in ranked[:n]:
            x = panel.cells[r["channel"], r["item"]]
            refs = x[:, ti].mean(1)
            for j, c in enumerate(si):
                total[j] += jsd(x[:, c][:, None, :], refs[None, :, :])
        used = {r["item"] for r in ranked[:n]}
        n_probes = sum(len(probes.orders(panel.items[i])) for i in used) * len(panel.contexts)
        curve.append(dict(n_cells=n, n_items=len(used), probes_per_model=n_probes,
                          accuracy=float((total.argmin(-1) == truth).mean())))
    return dict(train_contexts=train, test_contexts=test, curve=curve)


def split_half_reliability(panel, cells=None, seeds=20):
    """Do two disjoint random halves of the items agree on which models are
    close? Mean correlation of the two model-by-model distance matrices."""
    if len(panel.models) < 4:
        return None
    cells = cells or panel.select(channels=("content",))
    items = sorted({i for _, i in cells})
    upper = np.triu_indices(len(panel.models), 1)
    values = []
    for seed in range(seeds):
        rng = np.random.default_rng(seed)
        half = set(rng.permutation(items)[: len(items) // 2])
        a = model_distance_matrix(panel, [k for k in cells if k[1] in half])[upper]
        b = model_distance_matrix(panel, [k for k in cells if k[1] not in half])[upper]
        values.append(np.corrcoef(a, b)[0, 1])
    return float(np.mean(values))


def by_group(panel, groups=None):
    """Identification and information for each family and channel, and for the
    psychometric families against the control families."""
    cell_groups = {}
    for family in panel.families():
        channel = "assoc" if family == "association" else "content"
        cell_groups[f"content:{family}"] = panel.select(channels=(channel,), families=(family,))
    cell_groups["position:all"] = panel.select(channels=("position",))
    cell_groups["format:all"] = panel.select(channels=("format",))
    cell_groups["content:psychometric"] = panel.select(channels=("content", "assoc"),
                                                   exclude_families=CONTROL_FAMILIES + DECLARED_FAMILIES)
    cell_groups["content:control"] = panel.select(channels=("content",), families=CONTROL_FAMILIES)
    out = {}
    for name, cells in cell_groups.items():
        if not cells:
            continue
        info = item_information(panel, cells)
        result = identification(panel, cells)
        n_probes = sum(len(probes.orders(panel.items[i])) for i in {i for _, i in cells})
        out[name] = dict(n_cells=len(cells), probes_per_context=n_probes,
                         between_bits_per_probe=sum(r["between_bits"] for r in info) / n_probes,
                         accuracy=result["accuracy"], mean_margin=result["mean_margin"],
                         auc=separation(panel, cells, groups=groups)["auc"],
                         between_bits=sum(r["between_bits"] for r in info),
                         within_bits=sum(r["within_bits"] for r in info),
                         between_bits_per_cell=float(np.mean([r["between_bits"] for r in info])))
    return out


def matched_control_test(panel, draws=200, seed=0):
    """Do psychometric items identify models better than control items when the
    number of items is equal? Draws random psychometric subsets the size of
    the control set and compares the same-versus-different AUC."""
    control = panel.select(channels=("content",), families=CONTROL_FAMILIES)
    psych = panel.select(channels=("content", "assoc"), exclude_families=CONTROL_FAMILIES + DECLARED_FAMILIES)
    if not control or len(psych) < len(control):
        return None
    control_margin = identification(panel, control)["mean_margin"]
    rng = np.random.default_rng(seed)
    margins = []
    for _ in range(draws):
        pick = [psych[i] for i in rng.choice(len(psych), len(control), replace=False)]
        margins.append(identification(panel, pick)["mean_margin"])
    margins = np.array(margins)
    return dict(n_cells=len(control), control_margin=control_margin,
                psychometric_margin_mean=float(margins.mean()),
                psychometric_margin_5th_95th=[float(np.quantile(margins, 0.05)), float(np.quantile(margins, 0.95))],
                share_of_psychometric_draws_beating_control=float((margins > control_margin).mean()))


def relatives(panel, groups, cells=None):
    """Distance between declared relatives, as a share of the median distance
    between unrelated models. Near 0 means behaviorally identical; near 1
    means the relative is as far from its base as an unrelated model."""
    D = model_distance_matrix(panel, cells)
    lineage_of = [groups.get(m, m) for m in panel.models]
    pairs = list(itertools.combinations(range(len(panel.models)), 2))
    unrelated = [D[i, j] for i, j in pairs if lineage_of[i] != lineage_of[j]]
    if not unrelated:
        return []
    median = float(np.median(unrelated))
    return [dict(a=panel.models[i], b=panel.models[j], distance=float(D[i, j]),
                 share_of_unrelated_median=float(D[i, j] / median))
            for i, j in pairs if lineage_of[i] == lineage_of[j]]


def lineage(panel, cells=None):
    """Models as nodes and behavioral distance as edge weight, with the minimum
    spanning tree marked. Derived models should attach to their parents."""
    D = model_distance_matrix(panel, cells)
    M = len(panel.models)
    in_tree, tree = {0}, set()
    while len(in_tree) < M:
        a, b = min(((a, b) for a in in_tree for b in range(M) if b not in in_tree), key=lambda e: D[e])
        tree.add((min(a, b), max(a, b)))
        in_tree.add(b)
    edges = [dict(source=panel.models[a], target=panel.models[b], distance=float(D[a, b]),
                  in_spanning_tree=(a, b) in tree) for a, b in itertools.combinations(range(M), 2)]
    masked = np.where(np.eye(M, dtype=bool), np.inf, D)
    nearest = {panel.models[m]: panel.models[int(masked[m].argmin())] for m in range(M)}
    return dict(nodes=[dict(id=m) for m in panel.models], edges=edges, nearest=nearest,
                matrix=D.tolist())
