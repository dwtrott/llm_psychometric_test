"""Import independently coded content into an evidence KG; standard library only.

Requires two agreeing named raters, exact response quotations and matching rubric
identity. Disagreement and missing ratings remain visible, never zero-filled.
This is content measurement infrastructure, not a validated psychological scale.
"""
import argparse
import collections
import copy
import hashlib
import html
import json
from pathlib import Path


def identity(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode()).hexdigest()


def readlines(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def merge(graph, templates, ratings):
    graph = copy.deepcopy(graph)
    if 'review_contract' in graph and templates != graph['review_contract']:
        raise ValueError('Review templates differ from the source graph contract')
    nodes = {n['id']: n for n in graph['nodes']}
    if len(nodes) != len(graph['nodes']):
        raise ValueError('Duplicate graph nodes')
    expected = {}
    for row in templates:
        if row['status'] == 'not_observable':
            continue
        key = (row['trial_id'], row['stage'], row['criterion'])
        if key in expected:
            raise ValueError('Duplicate review target')
        expected[key] = row
    grouped = collections.defaultdict(dict)
    for r in ratings:
        key = (r['trial_id'], r['stage'], r['criterion'])
        if key not in expected:
            raise ValueError('Unknown or unobservable review target')
        template = expected[key]
        anchors = template.get('anchors')
        if not anchors:
            raise ValueError('Categorical construct content needs a frozen categorical codebook; ordinal ratings cannot substitute')
        if len(anchors)<2:
            raise ValueError('Rating rubric needs at least two anchors')
        if r.get('rubric_hash') != identity(anchors):
            raise ValueError('Rubric identity mismatch')
        if r.get('graph_hash') != identity(graph):
            raise ValueError('Rating is not bound to this exact source graph')
        who = r.get('rater_id', '').strip()
        if not who or who in grouped[key]:
            raise ValueError('Missing or duplicate rater')
        value = r.get('score')
        if type(value) is not int or not 0 <= value < len(anchors):
            raise ValueError('Rating outside rubric')
        trial = nodes.get('trial:' + r['trial_id'])
        if not trial or trial['status'] != 'valid':
            raise ValueError('Only completed valid trials can be rated')
        answer = trial['answer'][r['stage']]
        quote = r.get('evidence_quote', '')
        if not isinstance(quote, str) or not quote.strip() or not any(
                isinstance(v, str) and quote in v for v in answer.values()):
            raise ValueError('Evidence must quote the actual stage response verbatim')
        if not r.get('rationale', '').strip():
            raise ValueError('Explain how evidence satisfies the chosen anchor')
        grouped[key][who] = r
    results = []
    for key, template in expected.items():
        rr = list(grouped[key].values())
        values = {r['score'] for r in rr}
        status = ('codebook_required' if not template.get('anchors') else
                  'missing' if not rr else 'single_rater' if len(rr) < 2 else
                  'agreed' if len(values) == 1 else 'disagreement')
        result = dict(trial_id=key[0], stage=key[1], criterion=key[2], status=status,
                      score=rr[0]['score'] if status == 'agreed' else None,
                      ratings=rr, anchors=template.get('anchors'))
        results.append(result)
        if status == 'agreed':
            nid = 'content:' + identity(key)
            if nid in nodes:
                raise ValueError('Content measurements already imported')
            graph['nodes'].append(dict(id=nid, kind='measurement', label=key[2],
                value=result['score'], stage=key[1], measurement_level='human_content_rating',
                rubric=template['anchors'], ratings=rr, stability_status='not_established'))
            graph['edges'].append(dict(id='rated:' + identity(key), source='trial:' + key[0],
                target=nid, type='has_content_rating', origin='independent_rater_agreement'))
            # Keep ordinal content measurements separate from automatic choice features.
            metric = 'rating_' + key[2]
            trial = nodes['trial:' + key[0]]
            if metric in trial.get('features', {}):
                raise ValueError('Ambiguous repeated criterion; use distinct stage criterion names')
            trial.setdefault('features', {})[metric] = result['score'] / (len(template['anchors']) - 1)
            trial.setdefault('metrics', {})['feature_'+metric] = trial['features'][metric]
    graph['content_review'] = dict(results=results, policy='All supplied raters must agree; minimum two. No inferred trait scores.')
    return graph, results


def export_tasks(graph, templates):
    nodes = {n['id']: n for n in graph['nodes']}
    gh = identity(graph)
    out = []
    for t in templates:
        if t['status'] == 'not_observable' or not t.get('anchors'):
            continue
        trial = nodes.get('trial:' + t['trial_id'])
        if not trial or trial['status'] != 'valid':
            continue
        out.append(dict(trial_id=t['trial_id'], stage=t['stage'], criterion=t['criterion'],
            anchors=t['anchors'], rubric_hash=identity(t['anchors']), graph_hash=gh,
            answer=trial['answer'][t['stage']], context=trial.get('rendered_messages', []), rater_id='', score=None,
            evidence_quote='', rationale=''))
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph', required=True)
    p.add_argument('--templates', required=True)
    p.add_argument('--ratings', help='JSONL; omit to export rating tasks')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    graph = json.loads(Path(a.graph).read_text(encoding='utf-8-sig'))
    templates = readlines(a.templates)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    if not a.ratings:
        tasks = export_tasks(graph, templates)
        (out / 'rating_tasks.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in tasks), encoding='utf-8')
        return
    enriched, rows = merge(graph, templates, readlines(a.ratings))
    (out / 'rated_graph.json').write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'content_scores.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    esc = html.escape
    sections = ['<!doctype html><meta charset="utf-8"><title>Content evidence</title><style>body{font:17px system-ui;max-width:950px;margin:40px auto;padding:20px}article{border-top:1px solid #ccc;padding:20px 0}pre{white-space:pre-wrap}</style>',
                '<h1>Content evidence</h1><p>Agreed human ratings, not validated personality scores. Missing and disputed ratings remain unscored.</p>']
    for row in rows:
        sections.append('<article><h2>' + esc(row['criterion']) + '</h2><p>' + esc(row['trial_id']) +
                        '</p><p>Status: ' + row['status'] + '; score: ' + str(row['score']) + '</p><pre>' +
                        esc(json.dumps(row, ensure_ascii=False, indent=2)) + '</pre></article>')
    (out / 'content_report.html').write_text('\n'.join(sections), encoding='utf-8')


if __name__ == '__main__':
    main()
