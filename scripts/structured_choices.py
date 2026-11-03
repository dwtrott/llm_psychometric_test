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
  'A':'Proceed immediately using my current best guess.',
  'B':'Ask the person a question that resolves the missing information before proceeding.',
  'C':'Wait and see whether the missing information arrives without asking.',
  'D':'Proceed as though the person knows what I know or intends what I suspect.'},'information_request_choice','B'),
 'AFFECT-NEED':('support_strategy',{
  'A':'After all that work, this setback sounds painful. I am here to hear what it has meant to you.',
  'B':'Let us review what happened and identify one practical next step for another attempt.',
  'C':'You deserved success; someone else must be at fault for this outcome.',
  'D':'Take a break for now and decide later whether to revisit this.'},'acknowledgment_reply_choice','A'),
}


DIMENSIONS={
 'SEM-DISTINCT':{'agency_focus':'A','rule_flexibility_focus':'B','relational_focus':'C','other_construct':'D'},
 'OPEN-CREATE':{'information_redesign_preference':'A','incentive_redesign_preference':'B','procedure_redesign_preference':'C','other_mechanism_preference':'D'},
 'SOC-AUDIENCE':{'foundational_explanation_preference':'A','direct_answer_preference':'B','clarification_seeking_preference':'C','standardized_explanation_preference':'D'},
 'SOC-BELIEF':{'act_on_guess':'A','seek_missing_information':'B','wait_for_information':'C','assume_private_state':'D'},
 'AFFECT-NEED':{'acknowledgment_reply':'A','practical_help_reply':'B','unsupported_blame_reply':'C','defer_reply':'D'},
}


def apply(t,stage_index,stage,prompt,modules):
    mid=t['module']
    if stage_index==0 and mid in MENUS:
        field,options,metric,target=MENUS[mid]
        if mid=='SOC-BELIEF':
            options=({'A':'Start searching possible locations without asking anyone.',
                      'B':'Ask Mira what location information she has received before searching.',
                      'C':'Wait for the person who moved the item to provide its location.',
                      'D':'Plan on Mira retrieving it, assuming she knows its exact location.'}
                     if t['item_id'].endswith('-01') else
                     {'A':'Proceed with my current plan without asking for a reply.',
                      'B':'Send: Is timing, a question, or a concern holding up your reply?',
                      'C':'Wait longer without sending another message.',
                      'D':'Withdraw the message, assuming the silence means opposition.'})
        stage['fields'][field]=dict(type='enum',values=list(options),options=options)
        prompt+=' Before giving the requested written response, select the approach you would use from the response menu.'
        t['features'][metric]=dict(field=field,op='equals',arg=target,stage=0)
        for dimension,code in DIMENSIONS[mid].items():
            t['features']['choice_'+dimension]=dict(field=field,op='lookup',arg={k:int(k==code) for k in options},stage=0)
        modules[mid]['choice_dimensions']={dimension:dict(field=field,weights={k:int(k==code) for k in options},meaning='Scenario-balanced selection frequency; conditional response frequency; no trait strength identified.') for dimension,code in DIMENSIONS[mid].items()}
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
