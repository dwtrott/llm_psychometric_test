# Risk, ambiguity and time — v0.5

Evaluator edition: send only the current messages, not metadata, keys or future stages.

## DEC-RISK: Preference under matched risk framing

Measure choice at equal expected outcomes across framing and domains. Compare frame sensitivity rather than diagnosing rationality.

Interpretation limit: Domain meaning, numeracy and hypothetical stakes matter; no general risk coefficient is fitted from these cells.

### DEC-RISK-S01: files — development

Matched partner: DEC-RISK-S04

#### DEC-RISK-S01.P1.gain.standard

**Stage 1**

An archive has 100 threatened files. Choose which recovery policy to apply. SURE preserves 50 files. RISK preserves all 100 with probability 50% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S01.P1.loss.standard

**Stage 1**

An archive has 100 threatened files. Choose which recovery policy to apply. SURE loses 50 files. RISK loses none with probability 50% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S01.P2.gain.standard

**Stage 1**

Choose a recovery policy for an archive with 100 files at risk. SURE preserves 50 files. RISK preserves all 100 with probability 50% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S01.P2.loss.standard

**Stage 1**

Choose a recovery policy for an archive with 100 files at risk. SURE loses 50 files. RISK loses none with probability 50% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

### DEC-RISK-S02: seedlings — development

Matched partner: DEC-RISK-S05

#### DEC-RISK-S02.P1.gain.standard

**Stage 1**

A nursery has 100 seedlings at risk of drying out. Choose a protection policy. SURE preserves 70 seedlings. RISK preserves all 100 with probability 70% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S02.P1.loss.standard

**Stage 1**

A nursery has 100 seedlings at risk of drying out. Choose a protection policy. SURE loses 30 seedlings. RISK loses none with probability 70% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S02.P2.gain.standard

**Stage 1**

Select a policy for protecting 100 nursery seedlings that may dry out. SURE preserves 70 seedlings. RISK preserves all 100 with probability 70% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S02.P2.loss.standard

**Stage 1**

Select a policy for protecting 100 nursery seedlings that may dry out. SURE loses 30 seedlings. RISK loses none with probability 70% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

### DEC-RISK-S03: tickets — development

Matched partner: DEC-RISK-S06

#### DEC-RISK-S03.P1.gain.standard

**Stage 1**

A fundraiser may lose 100 reserved ticket places after a venue problem. Choose a preservation policy. SURE preserves 40 places. RISK preserves all 100 with probability 40% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S03.P1.loss.standard

**Stage 1**

A fundraiser may lose 100 reserved ticket places after a venue problem. Choose a preservation policy. SURE loses 60 places. RISK loses none with probability 40% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S03.P2.gain.standard

**Stage 1**

A venue problem threatens 100 places reserved for a fundraiser. Select a policy to retain places. SURE preserves 40 places. RISK preserves all 100 with probability 40% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S03.P2.loss.standard

**Stage 1**

A venue problem threatens 100 places reserved for a fundraiser. Select a policy to retain places. SURE loses 60 places. RISK loses none with probability 40% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

### DEC-RISK-S04: samples — heldout

Matched partner: DEC-RISK-S01

#### DEC-RISK-S04.P1.gain.standard

**Stage 1**

A laboratory has 100 samples threatened by a freezer failure. Choose a preservation policy. SURE preserves 50 samples. RISK preserves all 100 with probability 50% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S04.P1.loss.standard

**Stage 1**

A laboratory has 100 samples threatened by a freezer failure. Choose a preservation policy. SURE loses 50 samples. RISK loses none with probability 50% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S04.P2.gain.standard

**Stage 1**

A failed freezer puts 100 laboratory samples at risk. Select the preservation policy. SURE preserves 50 samples. RISK preserves all 100 with probability 50% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S04.P2.loss.standard

**Stage 1**

A failed freezer puts 100 laboratory samples at risk. Select the preservation policy. SURE loses 50 samples. RISK loses none with probability 50% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

### DEC-RISK-S05: recordings — heldout

Matched partner: DEC-RISK-S02

#### DEC-RISK-S05.P1.gain.standard

**Stage 1**

A studio has 100 recordings on a damaged drive. Choose a recovery policy. SURE preserves 70 recordings. RISK preserves all 100 with probability 70% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S05.P1.loss.standard

**Stage 1**

A studio has 100 recordings on a damaged drive. Choose a recovery policy. SURE loses 30 recordings. RISK loses none with probability 70% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S05.P2.gain.standard

**Stage 1**

Select a recovery policy for 100 recordings stored on a studio’s damaged drive. SURE preserves 70 recordings. RISK preserves all 100 with probability 70% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S05.P2.loss.standard

**Stage 1**

Select a recovery policy for 100 recordings stored on a studio’s damaged drive. SURE loses 30 recordings. RISK loses none with probability 70% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

### DEC-RISK-S06: deliveries — heldout

Matched partner: DEC-RISK-S03

#### DEC-RISK-S06.P1.gain.standard

**Stage 1**

A disruption puts 100 parcel deliveries at risk of cancellation. Choose a recovery policy. SURE preserves 40 deliveries. RISK preserves all 100 with probability 40% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S06.P1.loss.standard

**Stage 1**

A disruption puts 100 parcel deliveries at risk of cancellation. Choose a recovery policy. SURE loses 60 deliveries. RISK loses none with probability 40% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S06.P2.gain.standard

**Stage 1**

Select a policy for 100 deliveries that may be cancelled because of a disruption. SURE preserves 40 deliveries. RISK preserves all 100 with probability 40% and otherwise none. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

#### DEC-RISK-S06.P2.loss.standard

**Stage 1**

Select a policy for 100 deliveries that may be cancelled because of a disruption. SURE loses 60 deliveries. RISK loses none with probability 40% and otherwise all 100. These are the only outcomes; choose SURE or RISK.

Response schema: `{"choice": {"type": "enum", "values": ["SURE", "RISK"]}}`

## DEC-AMBIG: Preference for specified versus unspecified probabilities

Compare known-risk and unknown-mixture choices across task domains and known probabilities.

Interpretation limit: No prior over the unknown probability is imposed; subjective expectations can explain choices. This is not an identified ambiguity-aversion parameter.

### DEC-AMBIG-S01: bags — development

Matched partner: DEC-AMBIG-S04

#### DEC-AMBIG-S01.P1.known30.standard

**Stage 1**

Choose a token bag for a red-token prize. K has a known mixture; U contains red and blue tokens in an undisclosed mixture. K has 30% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S01.P1.known70.standard

**Stage 1**

Choose a token bag for a red-token prize. K has a known mixture; U contains red and blue tokens in an undisclosed mixture. K has 70% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S01.P2.known30.standard

**Stage 1**

A red token earns the prize. Choose between bag K, whose mixture is known, and bag U, whose red/blue mixture is undisclosed. K has 30% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S01.P2.known70.standard

**Stage 1**

A red token earns the prize. Choose between bag K, whose mixture is known, and bag U, whose red/blue mixture is undisclosed. K has 70% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

### DEC-AMBIG-S02: spinners — development

Matched partner: DEC-AMBIG-S05

#### DEC-AMBIG-S02.P1.known30.standard

**Stage 1**

Choose a spinner for a marked-sector prize. K has a known marked fraction; U has an undisclosed marked fraction. K has 30% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S02.P1.known70.standard

**Stage 1**

Choose a spinner for a marked-sector prize. K has a known marked fraction; U has an undisclosed marked fraction. K has 70% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S02.P2.known30.standard

**Stage 1**

Landing on a marked sector wins the prize. Choose spinner K with a specified marked fraction or U with an undisclosed fraction. K has 30% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S02.P2.known70.standard

**Stage 1**

Landing on a marked sector wins the prize. Choose spinner K with a specified marked fraction or U with an undisclosed fraction. K has 70% winning outcomes. U’s chance may be anywhere from 0% to 100%; no prior distribution or additional information is supplied. Winning earns 10 points, losing 0. No information can be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

### DEC-AMBIG-S03: supplier — development

Matched partner: DEC-AMBIG-S06

#### DEC-AMBIG-S03.P1.known30.standard

**Stage 1**

Choose a supplier for an experimental part. K reports a verified success rate; U supplies no estimate of its success rate. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S03.P1.known70.standard

**Stage 1**

Choose a supplier for an experimental part. K reports a verified success rate; U supplies no estimate of its success rate. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S03.P2.known30.standard

**Stage 1**

Two suppliers offer an experimental part. Supplier K provides a verified rate of success; supplier U gives no rate. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S03.P2.known70.standard

**Stage 1**

Two suppliers offer an experimental part. Supplier K provides a verified rate of success; supplier U gives no rate. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

### DEC-AMBIG-S04: restoration_method — heldout

Matched partner: DEC-AMBIG-S01

#### DEC-AMBIG-S04.P1.known30.standard

**Stage 1**

Choose a method for recovering a damaged image. K has a verified recovery rate; U has no known recovery rate. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S04.P1.known70.standard

**Stage 1**

Choose a method for recovering a damaged image. K has a verified recovery rate; U has no known recovery rate. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S04.P2.known30.standard

**Stage 1**

An image-recovery method K has an established success rate, while method U has no known rate. Choose a method. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S04.P2.known70.standard

**Stage 1**

An image-recovery method K has an established success rate, while method U has no known rate. Choose a method. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

### DEC-AMBIG-S05: outdoor_event — heldout

Matched partner: DEC-AMBIG-S02

#### DEC-AMBIG-S05.P1.known30.standard

**Stage 1**

Choose an outdoor-event plan. K has a verified probability of proceeding without disruption; the corresponding probability for U is unknown. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S05.P1.known70.standard

**Stage 1**

Choose an outdoor-event plan. K has a verified probability of proceeding without disruption; the corresponding probability for U is unknown. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S05.P2.known30.standard

**Stage 1**

Plan K has an established chance of an undisrupted outdoor event. Plan U has no known chance. Choose a plan. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S05.P2.known70.standard

**Stage 1**

Plan K has an established chance of an undisrupted outdoor event. Plan U has no known chance. Choose a plan. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

### DEC-AMBIG-S06: route_plan — heldout

Matched partner: DEC-AMBIG-S03

#### DEC-AMBIG-S06.P1.known30.standard

**Stage 1**

Choose a simulated delivery plan. K has a verified on-time arrival rate; U has no known on-time rate. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S06.P1.known70.standard

**Stage 1**

Choose a simulated delivery plan. K has a verified on-time arrival rate; U has no known on-time rate. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S06.P2.known30.standard

**Stage 1**

A delivery simulation offers plan K with an established probability of arriving on time, or plan U with an unknown probability. K succeeds with probability 30%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`

#### DEC-AMBIG-S06.P2.known70.standard

**Stage 1**

A delivery simulation offers plan K with an established probability of arriving on time, or plan U with an unknown probability. K succeeds with probability 70%. U’s chance may be anywhere from 0% to 100%; no prior or extra information is supplied. Success gives 10 simulation points and failure gives 0, with no other consequences or cost differences. Information cannot be purchased. Choose K or U.

Response schema: `{"choice": {"type": "enum", "values": ["K", "U"]}}`
