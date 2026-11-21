"""Observations -> fingerprint panel.

A panel holds, for every cell (channel, item), an array of shape
(models, contexts, outcomes) whose last axis is a probability distribution.

Channels
    content   option probabilities with presentation order averaged out
    position  where on the displayed menu the response falls. For a nominal
              item this is the distribution over displayed positions, which is
              exactly uniform for a model that answers on content alone. For an
              ordinal item it is first half versus last half of the displayed
              scale, exactly 50/50 under the same condition.
    format    share of first-token probability that is a valid label
    assoc     leading first-token distribution for an association cue
"""
import collections
import json
from pathlib import Path

import numpy as np

from . import battery

CHANNELS = ("content", "position", "format", "assoc")
EPS = 1e-12


def entropy(p):
    return -(p * np.log2(np.clip(p, EPS, None))).sum(-1)


def jsd(p, q):
    """Jensen-Shannon divergence in bits along the last axis, with broadcasting."""
    return np.clip(entropy((p + q) / 2) - (entropy(p) + entropy(q)) / 2, 0, None)


class Panel:
    def __init__(self, models, contexts, items, cells, outcomes, dropped):
        self.models, self.contexts, self.items = models, contexts, items
        self.cells, self.outcomes, self.dropped = cells, outcomes, dropped

    def select(self, channels=None, families=None, exclude_families=None, items=None):
        keys = []
        for channel, item in self.cells:
            family = self.items[item]["family"]
            if channels and channel not in channels:
                continue
            if families and family not in families:
                continue
            if exclude_families and family in exclude_families:
                continue
            if items is not None and item not in items:
                continue
            keys.append((channel, item))
        return keys

    def subset(self, models):
        index = [self.models.index(m) for m in models]
        cells = {k: v[index] for k, v in self.cells.items()}
        return Panel(list(models), self.contexts, self.items, cells, self.outcomes, self.dropped)

    def with_contexts(self, contexts):
        index = [self.contexts.index(c) for c in contexts]
        cells = {k: v[:, index] for k, v in self.cells.items()}
        return Panel(self.models, list(contexts), self.items, cells, self.outcomes, self.dropped)

    def families(self):
        return list(dict.fromkeys(self.items[i]["family"] for _, i in self.cells))


def load(paths, items=None):
    items = items or battery.build()
    version = battery.battery_hash(items)
    by_id = {i["id"]: i for i in items}
    raw = collections.defaultdict(dict)
    for path in paths:
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r["battery"] != version:
                raise ValueError(f"{path} was collected with battery {r['battery']}, not {version}. "
                                 "Observations from different batteries cannot be pooled.")
            raw[r["model"], r["context"], r["item"]][r["rotation"]] = r
    models = sorted({k[0] for k in raw})
    contexts = sorted(set.intersection(*({k[1] for k in raw if k[0] == m} for m in models)))
    unit = {}   # (model, context, channel, item) -> {outcome: probability}
    for (model, context, item_id), rotations in raw.items():
        item = by_id[item_id]
        if item["kind"] == "assoc":
            tokens = rotations[0]["tokens"]
            unit[model, context, "assoc", item_id] = dict(tokens, **{"<other>": max(0.0, 1 - sum(tokens.values()))})
            continue
        n = len(item["options"])
        if len(rotations) != (n if item["kind"] == "nominal" else 2):
            continue   # incomplete presentation set: order cannot be separated from content
        content, position, masses = np.zeros(n), np.zeros(n), []
        for r in rotations.values():
            shown = np.array(r["position_probs"], dtype=float)
            mass = shown.sum()
            shown = shown / mass if mass > 1e-9 else np.full(n, 1 / n)
            content[r["order"]] += shown / len(rotations)
            position += shown / len(rotations)
            masses.append(min(1.0, mass))
        keys = [o["key"] for o in item["options"]]
        unit[model, context, "content", item_id] = dict(zip(keys, content))
        if item["kind"] == "nominal":
            unit[model, context, "position", item_id] = {f"pos{p + 1}": v for p, v in enumerate(position)}
        else:
            first, last = position[: n // 2].sum(), position[-(n // 2):].sum()
            total = first + last
            unit[model, context, "position", item_id] = (
                {"first": first / total, "last": last / total} if total > 1e-9 else {"first": 0.5, "last": 0.5})
        mass = float(np.mean(masses))
        unit[model, context, "format", item_id] = {"label": mass, "other": 1 - mass}
    cells, outcomes, dropped = {}, {}, []
    for channel in CHANNELS:
        for item in items:
            key = (channel, item["id"])
            got = [unit.get((m, c, channel, item["id"])) for m in models for c in contexts]
            if all(g is None for g in got):
                continue
            if any(g is None for g in got):
                dropped.append(key)
                continue
            names = list(dict.fromkeys(k for g in got for k in g))
            if channel == "assoc":
                names = [k for k in names if k != "<other>"] + ["<other>"]
            array = np.array([[g.get(k, 0.0) for k in names] for g in got], dtype=float)
            array = array / array.sum(-1, keepdims=True)
            cells[key] = array.reshape(len(models), len(contexts), len(names))
            outcomes[key] = names
    return Panel(models, contexts, by_id, cells, outcomes, dropped)
