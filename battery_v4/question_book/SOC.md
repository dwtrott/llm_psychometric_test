# Social inference and communication — v0.4

Evaluator edition. Split and facet labels, later stages, resources and keys must not be sent to the tested model. Held-out means held out from analysis fitting, not secret or guaranteed absent from training data.

## SOC-AUDIENCE: Adaptation to recipient knowledge

Compare actual messages under recipient knowledge changes, with factuality separate from unnecessary repetition.

Alternative explanations: Brevity and policy repetition can masquerade as audience adaptation; there is no inference about social enjoyment.

Controls: SOC-02, SOC-04

Sources: [social](https://www.nature.com/articles/s41562-024-01882-z)

### SOC-AUDIENCE-S01: chart — development

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S01.P1.uninformed

**Stage 1**

A chart can be used internally today, but client sharing requires tomorrow’s audit. The recipient has not been told these conditions. They ask: “Can I use this chart today?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P1.informed

**Stage 1**

A chart can be used internally today, but client sharing requires tomorrow’s audit. The recipient has already read and accurately restated: Internal use is allowed; client sharing awaits the audit. They ask: “Can I use this chart today?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P2.uninformed

**Stage 1**

Today a chart is approved for internal use only; it may be shared with clients after tomorrow’s audit. The recipient has not been told these conditions. They ask: “Can I use this chart today?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P2.informed

**Stage 1**

Today a chart is approved for internal use only; it may be shared with clients after tomorrow’s audit. The recipient has already read and accurately restated: Internal use is allowed; client sharing awaits the audit. They ask: “Can I use this chart today?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S02: photo — development

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S02.P1.uninformed

**Stage 1**

A photograph may be displayed at a private club meeting, but public posting requires the photographer’s permission. The recipient has not been told these conditions. They ask: “Can I show this photograph?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P1.informed

**Stage 1**

A photograph may be displayed at a private club meeting, but public posting requires the photographer’s permission. The recipient has already read and accurately restated: Private club display is allowed; public posting needs permission. They ask: “Can I show this photograph?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P2.uninformed

**Stage 1**

Private club display of a photo is permitted; posting it publicly requires permission from its photographer. The recipient has not been told these conditions. They ask: “Can I show this photograph?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P2.informed

**Stage 1**

Private club display of a photo is permitted; posting it publicly requires permission from its photographer. The recipient has already read and accurately restated: Private club display is allowed; public posting needs permission. They ask: “Can I show this photograph?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S03: dataset — development

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S03.P1.uninformed

**Stage 1**

A dataset may be analyzed on the organization’s server, but it must not be copied to personal devices. The recipient has not been told these conditions. They ask: “Can I work with this dataset?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P1.informed

**Stage 1**

A dataset may be analyzed on the organization’s server, but it must not be copied to personal devices. The recipient has already read and accurately restated: Use on the organization server is permitted; personal-device copies are not. They ask: “Can I work with this dataset?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P2.uninformed

**Stage 1**

Analysis of this dataset is permitted on the organization’s server; copying it onto personal devices is prohibited. The recipient has not been told these conditions. They ask: “Can I work with this dataset?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P2.informed

**Stage 1**

Analysis of this dataset is permitted on the organization’s server; copying it onto personal devices is prohibited. The recipient has already read and accurately restated: Use on the organization server is permitted; personal-device copies are not. They ask: “Can I work with this dataset?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S04: prototype — development

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S04.P1.uninformed

**Stage 1**

A prototype may be demonstrated without passengers, but passenger trials require a completed safety inspection. The recipient has not been told these conditions. They ask: “Can we demonstrate the prototype?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P1.informed

**Stage 1**

A prototype may be demonstrated without passengers, but passenger trials require a completed safety inspection. The recipient has already read and accurately restated: A demonstration without passengers is allowed; passenger trials need inspection. They ask: “Can we demonstrate the prototype?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P2.uninformed

**Stage 1**

Demonstrations of the prototype are allowed when no passengers are aboard; passenger trials must await safety inspection. The recipient has not been told these conditions. They ask: “Can we demonstrate the prototype?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P2.informed

**Stage 1**

Demonstrations of the prototype are allowed when no passengers are aboard; passenger trials must await safety inspection. The recipient has already read and accurately restated: A demonstration without passengers is allowed; passenger trials need inspection. They ask: “Can we demonstrate the prototype?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S05: recording — heldout

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S05.P1.uninformed

**Stage 1**

A recording may be transcribed for the research team, but public quotations require the speaker’s approval. The recipient has not been told these conditions. They ask: “Can I use the recording?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P1.informed

**Stage 1**

A recording may be transcribed for the research team, but public quotations require the speaker’s approval. The recipient has already read and accurately restated: Research-team transcription is permitted; public quotations need approval. They ask: “Can I use the recording?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P2.uninformed

**Stage 1**

The research team may transcribe the recording; publishing quotations requires the speaker’s approval. The recipient has not been told these conditions. They ask: “Can I use the recording?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P2.informed

**Stage 1**

The research team may transcribe the recording; publishing quotations requires the speaker’s approval. The recipient has already read and accurately restated: Research-team transcription is permitted; public quotations need approval. They ask: “Can I use the recording?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S06: venue — heldout

Contrast: recipient knows restriction versus does not; broad question held fixed

#### SOC-AUDIENCE-S06.P1.uninformed

**Stage 1**

A room can host a seated meeting of 20, but moving furniture or serving food requires a separate booking. The recipient has not been told these conditions. They ask: “Can we hold our meeting there?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P1.informed

**Stage 1**

A room can host a seated meeting of 20, but moving furniture or serving food requires a separate booking. The recipient has already read and accurately restated: A seated meeting of 20 is covered; furniture changes or food need another booking. They ask: “Can we hold our meeting there?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P2.uninformed

**Stage 1**

The room booking permits 20 people seated for a meeting; rearranging furniture or providing food needs another booking. The recipient has not been told these conditions. They ask: “Can we hold our meeting there?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P2.informed

**Stage 1**

The room booking permits 20 people seated for a meeting; rearranging furniture or providing food needs another booking. The recipient has already read and accurately restated: A seated meeting of 20 is covered; furniture changes or food need another booking. They ask: “Can we hold our meeting there?” Write your reply.

Fields: `{"message": {"type": "text", "max_words": 80}}`

Rubric (evaluator edition): `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`
