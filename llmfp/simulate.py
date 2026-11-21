"""Synthetic models for testing the statistics. NOT evidence about real models.

Each simulated model has latent parameters that match the battery's scoring
models: sweep thresholds and slopes, Bradley-Terry strengths, similarity
levels, trait scores with acquiescence, and a position bias. Every latent has
a component shared by all models and a component of its own. Contexts add
noise to the latents. A derived model is a perturbation of its parent.
"""
import hashlib
import math
import random

CANONICAL_PROBABILITY = [0.95, 0.85, 0.7, 0.7, 0.6, 0.5, 0.35, 0.35, 0.2, 0.25, 0.1, 0.03]


def _g(*parts):
    seed = int(hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:12], 16)
    return random.Random(seed).gauss(0, 1)


def _softmax(logits):
    top = max(logits)
    weights = [math.exp(v - top) for v in logits]
    total = sum(weights)
    return [w / total for w in weights]


class SimBackend:
    def __init__(self, seed, parent=None, drift=0.3, context_noise=0.25, shared=1.0, own=0.7):
        self.seed, self.parent, self.drift = seed, parent, drift
        self.context_noise, self.shared, self.own = context_noise, shared, own

    def latent(self, name):
        if self.parent is not None:
            return self.parent.latent(name) + self.drift * _g("drift", self.seed, name)
        return self.shared * _g("shared", name) + self.own * _g("own", self.seed, name)

    def _in_context(self, name, context):
        # Adversarial contexts move a simulated model three times as far as benign ones.
        scale = self.context_noise * (3 if context.startswith("adv.") else 1)
        return self.latent(name) + scale * _g("context", self.seed, context, name)

    def true_threshold(self, sweep):
        return 3 + 0.8 * self.latent(f"threshold.{sweep}") + 0.2 * self.latent(f"form.{sweep}.a")

    def _canonical_logits(self, probe):
        L = lambda name: self._in_context(name, probe["context"])
        meta, keys, family = probe["meta"], probe["keys"], probe["family"]
        ordered = lambda mu, sharpness: [-sharpness * (k - mu) ** 2 for k in range(len(keys))]
        if family == "similarity":
            return ordered(2 + L(probe["item"]), 1.5)
        if family == "priority":
            diff = 1.2 * (L("bt." + meta["a"]) - L("bt." + meta["b"])) + 0.3 * L(probe["item"])
            return [diff, 0.0]
        if family == "sweep":
            threshold = (3 + 0.8 * L(f"threshold.{meta['sweep']}")
                         + 0.2 * L(f"form.{meta['sweep']}.{meta.get('form', 'a')}"))   # wording effect
            slope = 1.5 * math.exp(0.3 * L(f"slope.{meta['sweep']}"))
            logit = slope * (meta["index"] - threshold)
            return [logit if k == meta["target"] else 0.0 for k in keys]
        if family == "likert":
            mu = 2 + meta["keyed"] * 0.9 * L("trait." + meta["dimension"]) + 0.5 * L("acquiescence") + 0.4 * L(probe["item"])
            return ordered(mu, 1.2)
        if family == "estimative":
            return ordered(10 * CANONICAL_PROBABILITY[meta["rank"]] + 0.8 * L(probe["item"]), 0.8)
        return [L(f"{probe['item']}.{k}") for k in keys]

    def label_probs(self, batch):
        out = []
        for probe in batch:
            canonical = self._canonical_logits(probe)
            n = len(probe["order"])
            primacy = 0.5 * self.latent("primacy")
            logits = [canonical[c] - primacy * position / (n - 1) for position, c in enumerate(probe["order"])]
            mass = 0.85 + 0.15 / (1 + math.exp(-self.latent("label_mass")))
            out.append([mass * p for p in _softmax(logits)])
        return out

    def top_tokens(self, batch, k):
        out = []
        for probe in batch:
            words = [f"{probe['meta'].get('cue', probe['item'])}_w{n}" for n in range(12)]
            probs = _softmax([1.5 * self._in_context(f"{probe['item']}.{w}", probe["context"]) for w in words])
            out.append(dict(sorted(zip(words, [0.95 * p for p in probs]), key=lambda kv: -kv[1])[:k]))
        return out


def panel(n_base=6, **kwargs):
    """Unrelated base models, two fine-tunes, a near-identical quantized copy,
    and an exact copy under another name as a negative control."""
    base = {f"base{n}": SimBackend(seed=n, **kwargs) for n in range(n_base)}
    models = dict(base)
    models["base0-finetune"] = SimBackend(seed=100, parent=base["base0"], drift=0.3, **kwargs)
    models["base3-finetune"] = SimBackend(seed=103, parent=base["base3"], drift=0.3, **kwargs)
    models["base2-quantized"] = SimBackend(seed=202, parent=base["base2"], drift=0.03, **kwargs)
    models["base1-copy"] = SimBackend(seed=1, **kwargs)
    return models
