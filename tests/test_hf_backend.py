"""Mechanical check of HFBackend on tiny randomly initialized models.

Run: python tests/test_hf_backend.py   (skips when torch is not installed)

Random weights say nothing about real model behavior. This verifies the code
path only: chat templating, the system-role fallback, label token discovery,
left-padded batching, and that two different networks get different
fingerprints while one network gets the same fingerprint twice.
"""
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from llmfp import analysis, backends, battery, collect, fingerprint, probes

CHATML = ("{% for m in messages %}<|im_start|>{{ m['role'] }}\n{{ m['content'] }}<|im_end|>\n{% endfor %}"
          "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")
NO_SYSTEM = ("{% for m in messages %}{% if m['role'] == 'system' %}{{ raise_exception('no system role') }}{% endif %}"
             "<|im_start|>{{ m['role'] }}\n{{ m['content'] }}<|im_end|>\n{% endfor %}"
             "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")


def tiny(seed, items, template=CHATML):
    import torch
    from tokenizers import ByteLevelBPETokenizer
    from transformers import GPT2Config, GPT2LMHeadModel, PreTrainedTokenizerFast
    corpus = [p["messages"][-1]["content"] for p in probes.probes(items, probes.DEFAULT_CONTEXTS[:1])]
    corpus += [c["system"] for c in probes.DEFAULT_CONTEXTS if c["system"]]
    corpus += [f"{sep}{letter}" for letter in "ABCDEFGHIJK" for sep in ("", " ", "\n")] * 5
    raw = ByteLevelBPETokenizer()
    raw.train_from_iterator(corpus, vocab_size=600, min_frequency=2,
                            special_tokens=["<|endoftext|>", "<|im_start|>", "<|im_end|>"])
    tokenizer = PreTrainedTokenizerFast(tokenizer_object=raw._tokenizer, eos_token="<|endoftext|>",
                                        pad_token="<|endoftext|>", chat_template=template)
    torch.manual_seed(seed)
    config = GPT2Config(vocab_size=len(tokenizer), n_positions=512, n_embd=48, n_layer=2, n_head=2,
                        bos_token_id=0, eos_token_id=0)
    return GPT2LMHeadModel(config), tokenizer


def main():
    try:
        import torch  # noqa: F401
    except ImportError:
        print("torch not installed; skipped")
        return
    items = [i for i in battery.build() if i["family"] in ("sweep", "estimative", "arbitrary", "association")][::3]
    contexts = probes.DEFAULT_CONTEXTS[:4]
    batch = list(probes.probes(items, contexts))
    choice = [p for p in batch if p["kind"] != "assoc"]

    model, tokenizer = tiny(0, items)
    single = backends.HFBackend(model, tokenizer, batch_size=1)
    batched = backends.HFBackend(model, tokenizer, batch_size=7)
    a, b = single.label_probs(choice[:20]), batched.label_probs(choice[:20])
    for x, y in zip(a, b):
        assert np.allclose(x, y, atol=1e-5), "padding changes the result"
        assert 0 < sum(x) <= 1 + 1e-6
    assert len(single._ids_for("A")) >= 1
    check = collect.preflight(batched, items=items, n=6)
    assert 0 < check["mean_label_mass"] <= 1 + 1e-6 and len(check["first_tokens"]) == 3
    tokens = batched.top_tokens([p for p in batch if p["kind"] == "assoc"][:3], 10)
    assert all(0 < sum(t.values()) <= 1 + 1e-6 for t in tokens)

    # A template that rejects the system role falls back to folding it into the user turn.
    model2, tokenizer2 = tiny(0, items, NO_SYSTEM)
    fallback = backends.HFBackend(model2, tokenizer2)
    with_system = [p for p in choice if p["messages"][0]["role"] == "system"][:2]
    assert len(fallback.label_probs(with_system)) == 2

    # Two different networks are told apart; the same network measured twice is identical.
    tmp = Path(tempfile.mkdtemp())
    paths = []
    for name, seed in (("net-a", 0), ("net-a-again", 0), ("net-b", 1), ("net-c", 2)):
        model, tokenizer = tiny(seed, items)
        paths.append(collect.collect(backends.HFBackend(model, tokenizer, batch_size=8), name,
                                     tmp / f"{name}.jsonl", items=items, contexts=contexts))
    panel = fingerprint.load(paths, items)
    D = analysis.model_distance_matrix(panel)
    i, j, k = (panel.models.index(m) for m in ("net-a", "net-a-again", "net-b"))
    assert D[i, j] < 1e-6 and D[i, k] > 10 * max(D[i, j], 1e-6)
    result = analysis.identification(panel.subset(["net-a", "net-b", "net-c"]))
    print("identification among three random networks:", result["accuracy"])
    print("HF backend checks passed")


if __name__ == "__main__":
    main()
