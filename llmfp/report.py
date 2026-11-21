"""Run the full analysis and write summary.json, CSV tables, graphs and an HTML report."""
import csv
import html
import json
import math
from pathlib import Path

import numpy as np

from . import analysis, battery, fingerprint, graph, probes, scales


def analyze(paths, out_dir, items=None, groups=None):
    """groups optionally maps model name -> lineage label for known relatives
    (fine-tunes, quantized copies). Relatives are not counted as different models
    when the verification threshold is set."""
    full = fingerprint.load(paths, items)
    adversarial = [c for c in full.contexts if probes.is_adversarial(c)]
    benign = [c for c in full.contexts if not probes.is_adversarial(c)]
    panel = full.with_contexts(benign)       # adversarial contexts never enter a reference or a scale
    if len(panel.models) < 2 or len(panel.contexts) < 3:
        raise ValueError("The analysis needs at least 2 models and 3 contexts shared by all models.")
    out = Path(out_dir)
    (out / "graphs").mkdir(parents=True, exist_ok=True)

    info = sorted(analysis.item_information(panel), key=lambda r: -r["net_bits"])
    _csv(out / "item_information.csv", info)
    names, X = scales.features(panel)
    reliability = sorted(scales.reliability(names, X), key=lambda r: -r["icc"])
    _csv(out / "scale_reliability.csv", reliability)
    means = X.mean(1)
    _csv(out / "scale_values.csv", [dict(scale=n, **{m: f"{means[i, k]:.4f}" for i, m in enumerate(panel.models)})
                                    for k, n in enumerate(names)])
    lineage = analysis.lineage(panel)
    (out / "graphs" / "lineage.json").write_text(json.dumps(lineage, indent=1), encoding="utf-8")
    for model in panel.models:
        g = graph.model_graph(panel, model, names=names, X=X)
        safe = model.replace("/", "_")
        graph.write(g, out / "graphs" / f"{safe}.json", out / "graphs" / f"{safe}.edges.csv")

    icc = np.array([r["icc"] for r in reliability])
    summary = dict(
        models=panel.models, contexts=panel.contexts,
        n_cells=len(panel.cells), dropped_cells=len(panel.dropped), bits_needed=math.log2(len(panel.models)),
        identification=analysis.identification(panel, groups=groups),
        identification_interval_95=analysis.identification_interval(panel),
        open_set=analysis.open_set(panel, groups=groups),
        adversarial=analysis.robustness(full, benign, adversarial) if adversarial else None,
        say_do=_say_do(names, X),
        alternate_forms=scales.alternate_form_reliability(names, X),
        self_report_alpha=scales.internal_consistency(panel),
        relatives=analysis.relatives(panel, groups) if groups else None,
        profiles=_profiles(names, X, panel.models),
        verification=analysis.separation(panel, groups=groups),
        by_group=analysis.by_group(panel, groups),
        psychometric_vs_control=analysis.matched_control_test(panel),
        selection=analysis.selection_curve(panel),
        split_half_reliability=analysis.split_half_reliability(panel),
        scales=dict(n=len(names), median_icc=float(np.median(icc)), share_icc_above_0_75=float((icc > 0.75).mean()),
                    identification=scales.feature_identification(X) if len(panel.contexts) > 2 else None),
        uninformative_cells=sum(r["between_bits"] < 0.005 for r in info),
        label_mass={m: float(np.mean([panel.cells[k][i].mean(0)[0] for k in panel.select(channels=("format",))]))
                    for i, m in enumerate(panel.models)},
        nearest_model=lineage["nearest"])
    (out / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    (out / "report.html").write_text(_html(summary, lineage, info, reliability), encoding="utf-8")
    return summary


def _say_do(names, X):
    """Across models, does what a model says about itself agree with what it
    chooses? A more cautious self-report should go with declining at a lower
    penalty, and a more deferential one with switching at a lower colleague
    accuracy, so agreement shows as a negative correlation."""
    if X.shape[0] < 4:
        return None
    mean = dict(zip(names, X.mean(1).T))
    out = {}
    for trait, sweep in (("caution", "abstain"), ("deference", "defer")):
        a, b = mean.get(f"likert:{trait}"), mean.get(f"sweep:{sweep}.threshold")
        if a is not None and b is not None and a.std() > 0 and b.std() > 0:
            out[f"{trait}_vs_{sweep}_threshold"] = float(np.corrcoef(a, b)[0, 1])
    return out


def _profiles(names, X, models):
    """A short readable profile per model, in the units of the questions."""
    mean = dict(zip(names, X.mean(1).T))
    rows = {}
    for sweep, (_, levels, _, target, _) in battery.SWEEPS.items():
        v = mean.get(f"sweep:{sweep}.threshold")
        if v is not None:
            rows[f"{sweep}: level at which the choice turns to {target}"] = np.interp(
                np.clip(v, 0, len(levels) - 1), range(len(levels)), levels)
    for dimension in battery.LIKERT:
        rows[f"self-report {dimension} (-1 to 1)"] = mean.get(f"likert:{dimension}")
    for key, label in (("likert:acquiescence", "acquiescence (-1 to 1)"),
                       ("boundary:overall", "willingness on borderline requests (0 to 1)"),
                       ("pri:circular_triads", "share of circular priority triads"),
                       ("identity:training_year", "declared training year"),
                       ("style:first_of_two", "first of two options chosen (0.5 is unbiased)"),
                       ("style:label_mass", "label mass")):
        rows[label] = mean.get(key)
    out = {label: {m: float(v[i]) for i, m in enumerate(models)} for label, v in rows.items() if v is not None}
    strengths = [mean.get(f"bt:{c}") for c in battery.CONCEPTS]
    if all(s is not None for s in strengths):
        strengths = np.array(strengths)
        out["highest priority concept"] = {m: battery.CONCEPTS[int(strengths[:, i].argmax())] for i, m in enumerate(models)}
        out["lowest priority concept"] = {m: battery.CONCEPTS[int(strengths[:, i].argmin())] for i, m in enumerate(models)}
    return out


def _csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _table(header, rows):
    cells = lambda row, tag: "".join(f"<{tag}>{c}</{tag}>" for c in row)
    return "<table><tr>" + cells(header, "th") + "</tr>" + "".join(f"<tr>{cells(r, 'td')}</tr>" for r in rows) + "</table>"


def _html(s, lineage, info, reliability):
    e = html.escape
    f3 = lambda v: "n/a" if v is None else f"{v:.3f}"
    models = s["models"]
    D = np.array(lineage["matrix"])
    top = D.max() or 1
    matrix = "<table><tr><th></th>" + "".join(f"<th>{e(m)}</th>" for m in models) + "</tr>"
    for i, m in enumerate(models):
        matrix += f"<tr><th>{e(m)}</th>" + "".join(
            f'<td style="background:rgba(40,90,160,{0.75 * D[i, j] / top:.2f})">{D[i, j]:.3f}</td>'
            for j in range(len(models))) + "</tr>"
    matrix += "</table>"
    ident, ver = s["identification"], s["verification"]
    groups = _table(["Group", "Cells", "Probes per context", "Identification", "Margin", "AUC", "Between bits",
                     "Within bits", "Between bits per probe"],
                    [[e(k), v["n_cells"], v["probes_per_context"], f3(v["accuracy"]), f3(v["mean_margin"]), f3(v["auc"]),
                      f"{v['between_bits']:.2f}", f"{v['within_bits']:.2f}", f"{v['between_bits_per_probe']:.4f}"]
                     for k, v in s["by_group"].items()])
    pc = s["psychometric_vs_control"]
    control = ("" if pc is None else
               f"<p>With {pc['n_cells']} items each, the control items give a mean identification margin of "
               f"{f3(pc['control_margin'])}. Random psychometric subsets of the same size give "
               f"{f3(pc['psychometric_margin_mean'])} (5th to 95th percentile "
               f"{f3(pc['psychometric_margin_5th_95th'][0])} to {f3(pc['psychometric_margin_5th_95th'][1])}). "
               f"{100 * pc['share_of_psychometric_draws_beating_control']:.0f}% of the psychometric draws exceed the control.</p>")
    adversarial = "" if not s["adversarial"] else (
        "<h2>Adversarial contexts</h2><p>References use benign contexts only. Each row is a system prompt written to "
        "move the model's responses. Own distance is the model's distance to its own reference under that prompt.</p>"
        + _table(["Context", "Identification", "Own distance"],
                 [[e(k), f3(v["accuracy"]), f3(v["own_distance"])] for k, v in s["adversarial"].items()]))
    say_do = "" if not s["say_do"] else (
        "<p>Agreement between self-report and choice across models (negative means they agree): "
        + ", ".join(f"{e(k.replace('_', ' '))} r = {v:.2f}" for k, v in s["say_do"].items()) + ".</p>")
    forms = "" if not s["alternate_forms"] else (
        "<h3>Alternate forms</h3><p>Each sweep is asked in two independent wordings. The correlation across models "
        "between the two thresholds states whether a threshold belongs to the model or to the wording.</p>"
        + _table(["Sweep", "Correlation of thresholds", "Mean absolute difference (levels)"],
                 [[e(k), f3(v["r"]), f3(v["mean_abs_difference"])] for k, v in s["alternate_forms"].items()]))
    alpha = "" if not s["self_report_alpha"] else (
        "<p>Internal consistency of the self-report dimensions (Cronbach's alpha, models as subjects): "
        + ", ".join(f"{e(k)} {f3(v)}" for k, v in s["self_report_alpha"].items()) + ".</p>")
    relatives = "" if not s["relatives"] else (
        "<h3>Declared relatives</h3><p>Distance between relatives as a share of the median distance between "
        "unrelated models. Near 0 is behaviorally identical. Near 1 is as far as an unrelated model.</p>"
        + _table(["Model", "Relative", "Distance", "Share of unrelated median"],
                 [[e(r["a"]), e(r["b"]), f3(r["distance"]), f3(r["share_of_unrelated_median"])] for r in s["relatives"]]))
    cell = lambda v: e(v) if isinstance(v, str) else f"{v:.2f}"
    profiles = "<h2>Model profiles</h2><p class=\"note\">Mean over benign contexts, in the units of the questions.</p>" + _table(
        ["Scale"] + [e(m) for m in models], [[e(label)] + [cell(row[m]) for m in models] for label, row in s["profiles"].items()])
    confusions = _table(["True model", "Identified as", "Count"],
                        [[e(c["true"]), e(c["predicted"]), c["count"]] for c in ident["confusions"]]) if ident["confusions"] else "<p>No confusions.</p>"
    return f"""<!doctype html><meta charset="utf-8"><title>Fingerprint report</title>
<style>body{{font:15px/1.5 system-ui,sans-serif;max-width:1100px;margin:32px auto;padding:0 20px;color:#1b1f24}}
table{{border-collapse:collapse;margin:12px 0;font-size:13px}}td,th{{border:1px solid #d0d4da;padding:4px 8px;text-align:right}}
th{{background:#f2f4f7;text-align:left}}h2{{margin-top:32px}}.note{{color:#555}}</style>
<h1>Fingerprint report</h1>
<p>{len(models)} models, {len(s['contexts'])} contexts, {s['n_cells']} cells ({s['dropped_cells']} dropped as incomplete).
Identifying one model among {len(models)} needs {s['bits_needed']:.2f} bits.</p>
<h2>Identification</h2>
<p>Each model's fingerprint under one context is matched against references built from the other contexts.
Accuracy is {f3(ident['accuracy'])} over {ident['n_queries']} queries (chance {f3(ident['chance'])}).
{('Counting a match to any model of the same declared lineage as correct, accuracy is ' + f3(ident['lineage_accuracy']) + '.') if 'lineage_accuracy' in ident else ''}
The smallest margin between the correct model and the nearest other model is {f3(ident['min_margin'])}.</p>
{confusions}
<p>Resampling the items gives a 95% interval of {f3(s['identification_interval_95'][0])} to {f3(s['identification_interval_95'][1])} for accuracy.</p>
<h2>Unknown models</h2>
<p>Each query is also tested as if its own model had never been enrolled. With the acceptance threshold at the
95th percentile of genuine same-model distances ({f3(s['open_set']['threshold'])}), {100 * s['open_set']['false_accept']:.0f}% of
unknown-model queries would be accepted as an enrolled model and {100 * s['open_set']['false_reject']:.0f}% of genuine
queries would be rejected. Median genuine distance {f3(s['open_set']['genuine_median'])}, median distance to the nearest
unrelated model {f3(s['open_set']['impostor_median'])}.</p>
{adversarial}
<h2>Verification</h2>
<p>Same-model pairs against different-model pairs: AUC {f3(ver['auc'])}. At a false match rate of
{ver['false_match_rate']}, the distance threshold is {f3(ver['threshold'])} and {100 * ver['true_match_rate']:.0f}%
of same-model pairs fall below it.</p>
<h2>Which parts of the battery carry the fingerprint</h2>
{groups}
<h3>Psychometric items against control items</h3>{control}
<h2>Item selection</h2>
<p>Cells are ranked on contexts {e(', '.join(s['selection']['train_contexts']))} and tested on
{e(', '.join(s['selection']['test_contexts']))}.</p>
{_table(['Cells used', 'Items', 'Probes per model', 'Identification'], [[c['n_cells'], c['n_items'], c['probes_per_model'], f3(c['accuracy'])] for c in s['selection']['curve']])}
<p>{s['uninformative_cells']} of {s['n_cells']} cells carry less than 0.005 bits about model identity.
Split-half agreement of the model similarity structure: {f3(s['split_half_reliability'])}.</p>
<h2>Scale values</h2>
<p>{s['scales']['n']} scale values. Median reliability (ICC) {f3(s['scales']['median_icc'])};
{100 * s['scales']['share_icc_above_0_75']:.0f}% exceed 0.75. Identification from scale values alone:
{f3(s['scales']['identification']['accuracy'])}.</p>
{say_do}
{alpha}
{forms}
{_table(['Most reliable scales', 'ICC', 'Between SD', 'Within SD'], [[e(r['feature']), f3(r['icc']), f3(r['between_sd']), f3(r['within_sd'])] for r in reliability[:15]])}
{_table(['Least reliable scales', 'ICC', 'Between SD', 'Within SD'], [[e(r['feature']), f3(r['icc']), f3(r['between_sd']), f3(r['within_sd'])] for r in reliability[-10:]])}
{profiles}
<h2>Model distances</h2>
<p class="note">Root mean Jensen-Shannon divergence between model mean fingerprints. Darker is farther.</p>
{matrix}
{_table(['Model', 'Nearest model', 'Label mass'], [[e(m), e(s['nearest_model'][m]), f3(s['label_mass'][m])] for m in models])}
{relatives}
<p class="note">Label mass is the share of first-token probability on a valid answer letter. Below about 0.5 the
model is not answering in the requested format and its content distributions are unreliable.</p>
<h2>Most informative cells</h2>
{_table(['Channel', 'Item', 'Family', 'Between bits', 'Within bits'], [[r['channel'], e(r['item']), r['family'], f3(r['between_bits']), f3(r['within_bits'])] for r in info[:25]])}
"""
