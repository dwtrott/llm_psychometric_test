# Social inference and communication — v0.5

Evaluator edition: send only the current messages, not metadata, keys or future stages.

## SOC-AUDIENCE: Adaptation to recipient knowledge

Compare actual messages under recipient knowledge changes, with factuality separate from unnecessary repetition.

Interpretation limit: Brevity and policy repetition can masquerade as audience adaptation; there is no inference about social enjoyment.

### SOC-AUDIENCE-S01: chart — development

Matched partner: SOC-AUDIENCE-S04

#### SOC-AUDIENCE-S01.P1.uninformed.standard

**Stage 1**

A chart can be used internally today, but client sharing requires tomorrow’s audit. The recipient has not been told these conditions. They ask: “Can I use this chart today?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P1.informed.standard

**Stage 1**

A chart can be used internally today, but client sharing requires tomorrow’s audit. The recipient has already read and accurately restated: Internal use is allowed; client sharing awaits the audit. They ask: “Can I use this chart today?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P2.uninformed.standard

**Stage 1**

Today a chart is approved for internal use only; it may be shared with clients after tomorrow’s audit. The recipient has not been told these conditions. They ask: “Can I use this chart today?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S01.P2.informed.standard

**Stage 1**

Today a chart is approved for internal use only; it may be shared with clients after tomorrow’s audit. The recipient has already read and accurately restated: Internal use is allowed; client sharing awaits the audit. They ask: “Can I use this chart today?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S02: photo — development

Matched partner: SOC-AUDIENCE-S05

#### SOC-AUDIENCE-S02.P1.uninformed.standard

**Stage 1**

A photograph may be displayed at a private club meeting, but public posting requires the photographer’s permission. The recipient has not been told these conditions. They ask: “Can I show this photograph?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P1.informed.standard

**Stage 1**

A photograph may be displayed at a private club meeting, but public posting requires the photographer’s permission. The recipient has already read and accurately restated: Private club display is allowed; public posting needs permission. They ask: “Can I show this photograph?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P2.uninformed.standard

**Stage 1**

Private club display of a photo is permitted; posting it publicly requires permission from its photographer. The recipient has not been told these conditions. They ask: “Can I show this photograph?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S02.P2.informed.standard

**Stage 1**

Private club display of a photo is permitted; posting it publicly requires permission from its photographer. The recipient has already read and accurately restated: Private club display is allowed; public posting needs permission. They ask: “Can I show this photograph?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S03: dataset — development

Matched partner: SOC-AUDIENCE-S06

#### SOC-AUDIENCE-S03.P1.uninformed.standard

**Stage 1**

A dataset may be analyzed on the organization’s server, but it must not be copied to personal devices. The recipient has not been told these conditions. They ask: “Can I work with this dataset?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P1.informed.standard

**Stage 1**

A dataset may be analyzed on the organization’s server, but it must not be copied to personal devices. The recipient has already read and accurately restated: Use on the organization server is permitted; personal-device copies are not. They ask: “Can I work with this dataset?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P2.uninformed.standard

**Stage 1**

Analysis of this dataset is permitted on the organization’s server; copying it onto personal devices is prohibited. The recipient has not been told these conditions. They ask: “Can I work with this dataset?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S03.P2.informed.standard

**Stage 1**

Analysis of this dataset is permitted on the organization’s server; copying it onto personal devices is prohibited. The recipient has already read and accurately restated: Use on the organization server is permitted; personal-device copies are not. They ask: “Can I work with this dataset?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S04: prototype — heldout

Matched partner: SOC-AUDIENCE-S01

#### SOC-AUDIENCE-S04.P1.uninformed.standard

**Stage 1**

A prototype may be demonstrated without passengers, but passenger trials require a completed safety inspection. The recipient has not been told these conditions. They ask: “Can we demonstrate the prototype?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P1.informed.standard

**Stage 1**

A prototype may be demonstrated without passengers, but passenger trials require a completed safety inspection. The recipient has already read and accurately restated: A demonstration without passengers is allowed; passenger trials need inspection. They ask: “Can we demonstrate the prototype?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P2.uninformed.standard

**Stage 1**

Demonstrations of the prototype are allowed when no passengers are aboard; passenger trials must await safety inspection. The recipient has not been told these conditions. They ask: “Can we demonstrate the prototype?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S04.P2.informed.standard

**Stage 1**

Demonstrations of the prototype are allowed when no passengers are aboard; passenger trials must await safety inspection. The recipient has already read and accurately restated: A demonstration without passengers is allowed; passenger trials need inspection. They ask: “Can we demonstrate the prototype?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S05: recording — heldout

Matched partner: SOC-AUDIENCE-S02

#### SOC-AUDIENCE-S05.P1.uninformed.standard

**Stage 1**

A recording may be transcribed for the research team, but public quotations require the speaker’s approval. The recipient has not been told these conditions. They ask: “Can I use the recording?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P1.informed.standard

**Stage 1**

A recording may be transcribed for the research team, but public quotations require the speaker’s approval. The recipient has already read and accurately restated: Research-team transcription is permitted; public quotations need approval. They ask: “Can I use the recording?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P2.uninformed.standard

**Stage 1**

The research team may transcribe the recording; publishing quotations requires the speaker’s approval. The recipient has not been told these conditions. They ask: “Can I use the recording?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S05.P2.informed.standard

**Stage 1**

The research team may transcribe the recording; publishing quotations requires the speaker’s approval. The recipient has already read and accurately restated: Research-team transcription is permitted; public quotations need approval. They ask: “Can I use the recording?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

### SOC-AUDIENCE-S06: venue — heldout

Matched partner: SOC-AUDIENCE-S03

#### SOC-AUDIENCE-S06.P1.uninformed.standard

**Stage 1**

A room can host a seated meeting of 20, but moving furniture or serving food requires a separate booking. The recipient has not been told these conditions. They ask: “Can we hold our meeting there?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P1.informed.standard

**Stage 1**

A room can host a seated meeting of 20, but moving furniture or serving food requires a separate booking. The recipient has already read and accurately restated: A seated meeting of 20 is covered; furniture changes or food need another booking. They ask: “Can we hold our meeting there?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P2.uninformed.standard

**Stage 1**

The room booking permits 20 people seated for a meeting; rearranging furniture or providing food needs another booking. The recipient has not been told these conditions. They ask: “Can we hold our meeting there?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`

#### SOC-AUDIENCE-S06.P2.informed.standard

**Stage 1**

The room booking permits 20 people seated for a meeting; rearranging furniture or providing food needs another booking. The recipient has already read and accurately restated: A seated meeting of 20 is covered; furniture changes or food need another booking. They ask: “Can we hold our meeting there?” Write your reply.

Response schema: `{"message": {"type": "text", "max_words": 80}}`

rubric: `{"factuality": ["Contradicts conditions", "Ambiguous claims", "No contradiction"], "audience_adequacy": ["Likely to enable a prohibited use", "Some necessary context missing", "Sufficient for this recipient; known conditions need not be repeated"], "efficiency": ["Mostly unnecessary material", "Some unnecessary material", "Concise and sufficient"]}`
