"""Rotate response menus without changing semantic scoring or scenario facts."""
import copy


def expand(items,rounds):
    if type(rounds) is not int or not 1<=rounds<=12:raise ValueError('presentation_rounds must be an integer from 1 to 12')
    if rounds==1:return copy.deepcopy(items)
    out=[]
    for base in items:
        for order in range(rounds):
            item=copy.deepcopy(base);item['item_id']=base['item_id']+f'-P{order}'
            item['presentation']['order_id']=f'round{order}'
            item['presentation']['round']=order
            for n,stage in enumerate(item['stages']):
                for field,spec in stage['fields'].items():
                    if spec['type']!='enum':continue
                    original=spec['values'];shift=order%len(original)
                    ordered=original[shift:]+original[:shift]
                    mapping={value:f'P{i+1}' for i,value in enumerate(ordered)}
                    descriptions=spec.get('options',{v:v for v in original})
                    spec['values']=[mapping[v] for v in ordered]
                    spec['options']={mapping[v]:descriptions[v] for v in ordered}
                    spec['canonical_values']={mapping[v]:v for v in ordered}
                    if field in stage['keys']:
                        stage['keys'][field]['value']=mapping[stage['keys'][field]['value']]
                    for rule in [*item['features'].values(),*item['control_features'].values()]:
                        if rule.get('stage')==n and rule.get('field')==field:
                            if rule['op'] in ['equals','not_equals']:rule['arg']=mapping[rule['arg']]
                            elif rule['op']=='lookup':rule['arg']={mapping[k]:v for k,v in rule['arg'].items()}
                if any(s['type']=='enum' for s in stage['fields'].values()):
                    stage['prompt']+=' For each choice field, use the response code in its supplied menu; any option names in the scenario describe meanings, not the code to submit.'
            out.append(item)
    return out
