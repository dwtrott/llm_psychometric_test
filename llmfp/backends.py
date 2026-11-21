"""Backends return first-token probabilities for a batch of probes.

    label_probs(batch)  -> for each probe, the probability of each label in
                           probe["labels"]. NOT renormalized: the sum is the
                           share of the model's mass that is a valid label.
    top_tokens(batch,k) -> for each probe, {word: probability} for the leading
                           first tokens.

HFBackend      local Hugging Face model, exact probabilities from logits
OpenAIBackend  any OpenAI-compatible chat endpoint that returns logprobs
               (vLLM, llama.cpp server, hosted APIs)
SamplingBackend any text-only generator; probabilities estimated from samples
"""
import collections
import inspect
import json
import math
import re
import urllib.request


class HFBackend:
    def __init__(self, model, tokenizer, batch_size=16, template_kwargs=None, prefill=""):
        """template_kwargs is passed to the chat template, for example
        {"enable_thinking": False} for models that otherwise open with a
        reasoning block. prefill is appended after the generation prompt, for
        example "(" when a model habitually answers "(A)"."""
        import torch
        self.torch, self.model, self.tokenizer = torch, model.eval(), tokenizer
        self.batch_size, self.template_kwargs, self.prefill = batch_size, template_kwargs or {}, prefill
        self.tokenizer.padding_side = "left"
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self._label_ids = {}
        self._takes_positions = "position_ids" in inspect.signature(self.model.forward).parameters

    def _text(self, messages):
        try:
            text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True,
                                                      **self.template_kwargs)
        except Exception:
            # Some templates reject a system role. Fold it into the user turn.
            system = "\n\n".join(m["content"] for m in messages if m["role"] == "system")
            rest = [dict(m) for m in messages if m["role"] != "system"]
            if not system:
                raise
            rest[0]["content"] = f"{system}\n\n{rest[0]['content']}"
            text = self.tokenizer.apply_chat_template(rest, tokenize=False, add_generation_prompt=True,
                                                      **self.template_kwargs)
        return text + self.prefill

    def _next_token_probs(self, batch):
        out = []
        for start in range(0, len(batch), self.batch_size):
            texts = [self._text(p["messages"]) for p in batch[start:start + self.batch_size]]
            inputs = self.tokenizer(texts, return_tensors="pt", padding=True,
                                    add_special_tokens=False).to(self.model.device)
            if self._takes_positions:
                # Number real tokens from zero so that padding does not shift positions.
                inputs["position_ids"] = (inputs["attention_mask"].cumsum(-1) - 1).clamp(min=0)
            with self.torch.inference_mode():
                logits = self.model(**inputs).logits[:, -1]     # left padding: last position is real
            out.extend(self.torch.softmax(logits.float(), dim=-1).cpu())
        return out

    def _ids_for(self, label):
        """Every single token that decodes to the bare label, such as 'A' and ' A'."""
        if label not in self._label_ids:
            ids = set()
            for variant in (label, " " + label, "\n" + label):
                encoded = self.tokenizer.encode(variant, add_special_tokens=False)
                if len(encoded) == 1 and self.tokenizer.decode(encoded).strip() == label:
                    ids.add(encoded[0])
            if not ids:
                raise ValueError(f"No single token encodes label {label!r} for this tokenizer")
            self._label_ids[label] = sorted(ids)
        return self._label_ids[label]

    def label_probs(self, batch):
        return [[float(probs[self._ids_for(label)].sum()) for label in probe["labels"]]
                for probe, probs in zip(batch, self._next_token_probs(batch))]

    def top_tokens(self, batch, k):
        out = []
        for probs in self._next_token_probs(batch):
            values, ids = self.torch.topk(probs, k)
            merged = collections.Counter()
            for value, token_id in zip(values.tolist(), ids.tolist()):
                word = self.tokenizer.decode([token_id]).strip().lower()
                if word:
                    merged[word] += value
            out.append(dict(merged))
        return out


class OpenAIBackend:
    """Reads the first token's top logprobs from /v1/chat/completions. Labels
    outside the returned top tokens are recorded as probability zero, so use
    the largest top_logprobs the server allows."""

    def __init__(self, base_url, model, api_key=None, top_logprobs=20, extra_body=None, timeout=120):
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.model, self.api_key, self.top, self.extra, self.timeout = model, api_key, top_logprobs, extra_body or {}, timeout

    def _first_token(self, messages):
        body = dict(model=self.model, messages=messages, max_tokens=1, temperature=0,
                    logprobs=True, top_logprobs=self.top, **self.extra)
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = urllib.request.Request(self.url, json.dumps(body).encode(), headers)
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.load(response)
        merged = collections.Counter()
        for entry in data["choices"][0]["logprobs"]["content"][0]["top_logprobs"]:
            merged[entry["token"].strip()] += math.exp(entry["logprob"])
        return merged

    def label_probs(self, batch):
        out = []
        for probe in batch:
            tokens = self._first_token(probe["messages"])
            out.append([tokens.get(label, 0.0) for label in probe["labels"]])
        return out

    def top_tokens(self, batch, k):
        out = []
        for probe in batch:
            merged = collections.Counter()
            for token, p in self._first_token(probe["messages"]).items():
                if token:
                    merged[token.lower()] += p
            out.append(dict(merged.most_common(k)))
        return out


class OpenAISampler:
    """generate(messages) for SamplingBackend, for a chat endpoint that returns
    text only. Sampling uses the stated temperature."""

    def __init__(self, base_url, model, api_key=None, max_tokens=8, temperature=1.0, timeout=120):
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.model, self.api_key, self.max_tokens = model, api_key, max_tokens
        self.temperature, self.timeout = temperature, timeout

    def __call__(self, messages):
        body = dict(model=self.model, messages=messages, max_tokens=self.max_tokens, temperature=self.temperature)
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = urllib.request.Request(self.url, json.dumps(body).encode(), headers)
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            return json.load(response)["choices"][0]["message"]["content"] or ""


class SamplingBackend:
    """generate(messages) returns one sampled completion. The standard error
    of a probability near 0.5 is about 0.5 / sqrt(n_samples)."""

    def __init__(self, generate, n_samples=20):
        self.generate, self.n = generate, n_samples

    def label_probs(self, batch):
        out = []
        for probe in batch:
            counts = collections.Counter()
            for _ in range(self.n):
                match = re.match(r"\W*([A-Za-z])\b", self.generate(probe["messages"]))
                if match:
                    counts[match.group(1).upper()] += 1
            out.append([counts[label] / self.n for label in probe["labels"]])
        return out

    def top_tokens(self, batch, k):
        out = []
        for probe in batch:
            counts = collections.Counter()
            for _ in range(self.n):
                words = re.findall(r"[^\W\d_]+", self.generate(probe["messages"]).lower())
                if words:
                    counts[words[0]] += 1
            out.append({word: c / self.n for word, c in counts.most_common(k)})
        return out
