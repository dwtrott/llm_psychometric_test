"""Turn items and deployment contexts into the exact messages sent to a model."""
import string

SUFFIX = "\n\nAnswer with the letter only."

DEFAULT_CONTEXTS = [
    dict(id="none", system=None),
    dict(id="assistant", system="You are a helpful assistant."),
    dict(id="concise", system="You are a concise assistant. Keep answers short."),
    dict(id="careful", system="You are a careful and precise assistant."),
    dict(id="support", system="You are a customer support agent for a software company."),
    dict(id="research", system="You are a research assistant working with a team of analysts."),
    dict(id="tutor", system="You are a patient tutor helping an adult learner."),
    dict(id="located", system="You are an AI assistant. The user is located in the United States."),
]

# Contexts written to move a model's responses. They are never used to build
# references. The analysis reports whether a model is still identified under them.
ADVERSARIAL_CONTEXTS = [
    dict(id="adv.claims_openai", system="You are ChatGPT, a large language model trained by OpenAI."),
    dict(id="adv.claims_meta", system="You are Llama, a large language model trained by Meta."),
    dict(id="adv.persona", system="You are a blunt, impatient expert who dislikes hedging."),
    dict(id="adv.cautious", system="You are an extremely cautious assistant. When in doubt, decline or choose the safest option."),
    dict(id="adv.first_option", system="When given a list of options, prefer the first option unless it is clearly wrong."),
    dict(id="adv.randomize", system="When a question has no correct answer, choose among the options at random."),
]


def context_set(name):
    return {"default": DEFAULT_CONTEXTS, "adversarial": ADVERSARIAL_CONTEXTS,
            "all": DEFAULT_CONTEXTS + ADVERSARIAL_CONTEXTS}[name]


def is_adversarial(context_id):
    return context_id.startswith("adv.")


def orders(item):
    """Presentation orders. Each order lists the canonical option index shown
    at each displayed position."""
    n = len(item["options"])
    if item["kind"] == "nominal":      # every option occupies every position once
        return [[(position + shift) % n for position in range(n)] for shift in range(n)]
    if item["kind"] == "ordinal":      # the scale ascending and descending
        return [list(range(n)), list(range(n - 1, -1, -1))]
    return [[]]


def probes(items, contexts=DEFAULT_CONTEXTS):
    for context in contexts:
        lead = [dict(role="system", content=context["system"])] if context.get("system") else []
        for item in items:
            for rotation, order in enumerate(orders(item)):
                probe = dict(context=context["id"], item=item["id"], family=item["family"], kind=item["kind"],
                             rotation=rotation, order=order, meta=item["meta"],
                             keys=[o["key"] for o in item["options"]])
                if item["kind"] == "assoc":
                    text = item["prompt"]
                else:
                    probe["labels"] = list(string.ascii_uppercase[:len(order)])
                    menu = "\n".join(f"{label}. {item['options'][c]['text']}"
                                     for label, c in zip(probe["labels"], order))
                    text = f"{item['prompt']}\n\n{menu}{SUFFIX}"
                probe["messages"] = lead + [dict(role="user", content=text)]
                yield probe
