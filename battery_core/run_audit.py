"""Readable question-by-question run audit. Saved model text is data, never code."""
import argparse
import collections
import csv
import html
import importlib.util
import json
from pathlib import Path
import zipfile

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('audit_processor',BASE/'processor.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


def audit(b,plan,records):
    p.validate(b,plan)
    trials={t['trial_id']:t for t in plan['trials']}
    states={k:p.engine.initial(plan,t) for k,t in trials.items()}
    by_stage=collections.defaultdict(list)
    for record in records:
        tid=record['trial_id']
        if tid not in states:raise ValueError('Unknown trial in journal')
        state=states[tid]
        by_stage[tid,state['stage']].append(record)
        p.engine.apply(plan,trials[tid],state,record)
    cards=[]
    for t in plan['trials']:
        state=states[t['trial_id']];stages=[]
        accepted={s['stage'] for s in state['submissions']}
        for n,s in enumerate(t['stages']):
            events=by_stage[t['trial_id'],n]
            status='accepted' if n in accepted else 'rejected' if events and state['status']=='invalid' else 'declined' if events and state['status']=='declined' else 'incomplete' if events else 'no_response_recorded'
            stages.append(dict(stage=n,prompt=s['prompt'],fields=s['fields'],status=status,events=events))
        cards.append(dict(trial_id=t['trial_id'],item_id=t['item_id'],facet=t['module'],title=t.get('scenario_name',t['item_id']),
                          status=state['status'],error=state.get('error',''),stages=stages))
    counts=collections.Counter(c['status'] for c in cards)
    stats=dict(cards_planned=len(cards),cards_attempted=sum(any(s['events'] for s in c['stages']) for c in cards),
               cards_valid=counts['valid'],cards_invalid=counts['invalid'],cards_declined=counts['declined'],
               cards_pending=counts['pending'],cards_api_error=counts['api_error'],
               stages_planned=sum(len(c['stages']) for c in cards),
               stages_with_response=sum(any(r['status']=='ok' for r in s['events']) for c in cards for s in c['stages']),
               stages_accepted=sum(s['status']=='accepted' for c in cards for s in c['stages']),
               stages_without_response=sum(not any(r['status']=='ok' for r in s['events']) for c in cards for s in c['stages']),
               calls=len(records),token_limit_hits=sum(bool(r.get('generation',{}).get('hit_token_limit')) for r in records),
               generation_seconds=sum(r.get('wall_seconds',0) for r in records))
    stats['complete']=stats['cards_valid']==stats['cards_planned'] and stats['stages_accepted']==stats['stages_planned']
    coverage=[]
    for mid,meta in b['modules'].items():
        selected=[c for c in cards if c['facet']==mid]
        coverage.append(dict(facet=mid,title=meta['title'],category=next(d['title'] for d in b['domains'] if d['id']==meta['domain']),
            cards_planned=len(selected),cards_valid=sum(c['status']=='valid' for c in selected),
            content_review_required=bool(meta.get('content_review'))))
    return dict(coverage=coverage,battery_version=b['version'],battery_hash=plan['battery_hash'],model=plan['config']['model'],summary=stats,cards=cards)


def write_report(data,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    (out/'run_audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    s=data['summary'];esc=html.escape
    title='All planned responses accepted' if s['complete'] else 'Run incomplete: some questions are missing or were rejected'
    parts=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Battery run audit</title><style>body{font:17px/1.5 system-ui;max-width:1050px;margin:32px auto;padding:0 20px;color:#1f3440}h1{line-height:1.2}article{border:1px solid #ccd7dc;border-radius:10px;padding:18px;margin:18px 0}.warning{background:#fff1d8;padding:18px;border-radius:8px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f6f7;padding:12px}table{border-collapse:collapse;width:100%;margin:20px 0}th,td{padding:9px;border:1px solid #cbd5da;text-align:left}summary{cursor:pointer;font-weight:600}.muted{color:#596a73}.rejected,.invalid{color:#a23320}</style>',
        '<h1>'+esc(title)+'</h1><p>'+esc(data['model'])+' · '+esc(data['battery_version'])+'</p>',
        '<div class="warning">A finished collection loop is not a complete evaluation. Acceptance below means response-format validity, not a correct answer or an established psychological finding. Written content may still need review.</div>',
        '<table><tr><th>Measure</th><th>Count</th></tr>']
    for label,value in [('Cards attempted',f"{s['cards_attempted']} / {s['cards_planned']}"),('Cards fully accepted',f"{s['cards_valid']} / {s['cards_planned']}"),('Cards rejected',s['cards_invalid']),('Question stages with a saved model response',f"{s['stages_with_response']} / {s['stages_planned']}"),('Question stages accepted',f"{s['stages_accepted']} / {s['stages_planned']}"),('Stages with no saved response',s['stages_without_response']),('Generation token-limit hits',s['token_limit_hits'])]:
        parts.append('<tr><td>'+esc(label)+'</td><td>'+esc(str(value))+'</td></tr>')
    parts+=['</table><h2>Category and facet coverage</h2><p>This is a short exploratory battery, not a full validated psychological fingerprint. Two scenarios per non-association facet do not establish stable traits. It contains no paraphrase, option-order or held-out robustness tests. Accepted means format-valid; written responses marked for review still require content ratings.</p>',
        '<table><tr><th>Category</th><th>Facet</th><th>Accepted / planned cards</th><th>Content review required</th></tr>']
    for c in data['coverage']:
        parts.append('<tr><td>'+esc(c['category'])+'</td><td>'+esc(c['title'])+'</td><td>'+str(c['cards_valid'])+' / '+str(c['cards_planned'])+'</td><td>'+('Yes' if c['content_review_required'] else 'No')+'</td></tr>')
    parts+=['</table><h2>Questions with problems</h2>']
    failed=[c for c in data['cards'] if c['status']!='valid']
    if not failed:parts.append('<p>None failed the format checks.</p>')
    else:
        parts.append('<ul>')
        for c in failed:parts.append('<li><a href="#'+esc(c['item_id'])+'">'+esc(c['item_id']+' — '+c['title'])+'</a>: '+esc(c['status']+'; '+c['error'])+'</li>')
        parts.append('</ul>')
    parts.append('<h2>Every question and actual response</h2><p>Problem cards are expanded. Expand the others to inspect their questions and exact saved model text. No response has been repaired or invented.</p>')
    for c in sorted(data['cards'],key=lambda c:c['item_id']):
        parts.append('<article id="'+esc(c['item_id'])+'"><details'+(' open' if c['status']!='valid' else '')+'><summary>'+esc(c['item_id']+' — '+c['title']+' — '+c['status'])+'</summary>')
        if c['error']:parts.append('<p class="invalid"><b>Rejected because:</b> '+esc(c['error'])+'</p>')
        for stage in c['stages']:
            parts.append('<h3>Question stage '+str(stage['stage']+1)+' — '+esc(stage['status'])+'</h3><p>'+esc(stage['prompt'])+'</p>')
            if not stage['events']:parts.append('<p class="rejected"><b>No model response was recorded for this stage.</b></p>')
            for event in stage['events']:
                parts.append('<p><b>Actual model response</b></p><pre>'+esc(event.get('raw_response','[generation error: no model response]'))+'</pre>')
        parts.append('</details></article>')
    parts.append('</html>')
    (out/'run_audit.html').write_text('\n'.join(parts),encoding='utf-8')
    with (out/'question_status.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['trial_id','item_id','facet','card_status','stage','stage_status','error']);writer.writeheader()
        for c in data['cards']:
            for stage in c['stages']:
                writer.writerow(dict(trial_id=c['trial_id'],item_id=c['item_id'],facet=c['facet'],card_status=c['status'],stage=stage['stage']+1,stage_status=stage['status'],error=c['error']))
    return out/'run_audit.html'


def audit_zip(path,out):
    """Read only named data files. Never extract or execute the ZIP's Python/HTML."""
    out=Path(out);data_dir=out/'original_data';data_dir.mkdir(parents=True,exist_ok=True)
    names={'plan.json':'plan.json','responses.jsonl':'responses.jsonl',
           'source/battery_core/battery.json':'battery.json','source/battery_core/prompts.csv':'prompts.csv'}
    with zipfile.ZipFile(path) as z:
        for name,target in names.items():
            if z.namelist().count(name)!=1:raise ValueError('Missing or duplicate archive member: '+name)
            if z.getinfo(name).file_size>50*1024*1024:raise ValueError('Oversized archive data file')
            (data_dir/target).write_bytes(z.read(name))
    b=p.load(data_dir);plan=p.read(data_dir/'plan.json');records=p.jsonl(data_dir/'responses.jsonl')
    data=audit(b,plan,records);write_report(data,out)
    return data


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('zip');ap.add_argument('--out',required=True)
    args=ap.parse_args();data=audit_zip(args.zip,args.out)
    print(json.dumps(data['summary'],indent=2))
