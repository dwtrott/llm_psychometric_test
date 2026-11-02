"""Prespecified response menus. Choices are observations, not diagnoses."""
MENUS={
 'SEM-DISTINCT':('organizing_basis',{
  'A':'Who controls or causes the outcome.',
  'B':'How fixed or revisable the rule or explanation is.',
  'C':'How relationships among people shape the outcome.',
  'D':'Another distinction, specified in your written distinction.'},'agency_basis_choice','A'),
 'OPEN-CREATE':('preferred_mechanism',{
  'A':'Change how information is collected or shared.',
  'B':'Change incentives or the perceived cost of participating.',
  'C':'Change the procedure for participating or reviewing work.',
  'D':'Another mechanism, described in your proposals.'},'information_mechanism_choice','A'),
 'SOC-AUDIENCE':('communication_strategy',{
  'A':'Start with foundational concepts before answering the question.',
  'B':'Answer directly using the knowledge the recipient has already demonstrated.',
  'C':'Ask what the recipient understands before explaining.',
  'D':'Give the same standard explanation regardless of recipient knowledge.'},'direct_answer_strategy','B'),
 'SOC-BELIEF':('interpretation_strategy',{
  'A':'Act on the single explanation that currently seems most likely.',
  'B':'Keep multiple explanations open and seek information that distinguishes them.',
  'C':'Wait without seeking additional information.',
  'D':'Use the outcome known to the observer as the basis for the other person\'s belief.'},'alternative_testing_choice','B'),
 'AFFECT-NEED':('support_strategy',{
  'A':'Acknowledge the specific experience and invite the person to say more.',
  'B':'Offer a concrete course of action immediately.',
  'C':'Agree with the person\'s explanation of what happened.',
  'D':'Question the explanation while acknowledging the distress.'},'listening_strategy','A'),
}


DIMENSIONS={
 'SEM-DISTINCT':{'agency_focus':'A','rule_flexibility_focus':'B','relational_focus':'C','other_construct':'D'},
 'OPEN-CREATE':{'information_redesign_preference':'A','incentive_redesign_preference':'B','procedure_redesign_preference':'C','other_mechanism_preference':'D'},
 'SOC-AUDIENCE':{'foundational_explanation_preference':'A','direct_answer_preference':'B','clarification_seeking_preference':'C','standardized_explanation_preference':'D'},
 'SOC-BELIEF':{'early_interpretive_commitment':'A','alternative_testing_preference':'B','passive_waiting_preference':'C','observer_perspective_choice':'D'},
 'AFFECT-NEED':{'listening_preference':'A','immediate_advice_preference':'B','agreement_preference':'C','supportive_challenge_preference':'D'},
}


def apply(t,stage_index,stage,prompt,modules):
    mid=t['module']
    if stage_index==0 and mid in MENUS:
        field,options,metric,target=MENUS[mid]
        stage['fields'][field]=dict(type='enum',values=list(options),options=options)
        prompt+=' Before giving the requested written response, select the approach you would use from the response menu.'
        t['features'][metric]=dict(field=field,op='equals',arg=target,stage=0)
        for dimension,code in DIMENSIONS[mid].items():
            t['features']['tendency_'+dimension]=dict(field=field,op='lookup',arg={k:int(k==code) for k in options},stage=0)
        modules[mid]['choice_dimensions']={dimension:dict(field=field,weights={k:int(k==code) for k in options},meaning='Scenario-balanced selection frequency; candidate tendency, not a human-norm trait score.') for dimension,code in DIMENSIONS[mid].items()}
        modules[mid]['response_options']=options
        modules[mid].update(primary_metric=metric,primary_label=options[target]+' (selected approach)',
                            scoring='Selected approach and per-option frequencies; written content is separately scored against rubrics. Selection is not proof that the written response implements the approach.')
    # The old nested answer.answer field was frequently flattened by the model.
    # A unique name removes this collision; keys and controls move with it.
    if mid=='META-VERIFY':
        stage['fields']['solution']=stage['fields'].pop('answer')
        if 'answer' in stage['keys']:stage['keys']['solution']=stage['keys'].pop('answer')
        for rule in [*t['features'].values(),*t['control_features'].values()]:
            if rule.get('field')=='answer':rule['field']='solution'
    return prompt
