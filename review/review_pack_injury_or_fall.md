# Review pack: Injury or fall

**Status: AI-drafted, not clinically reviewed. Not for clinical use.**

Knowledge base version 0.4.0. Generated from the knowledge base by `python triage.py review-pack`. Do not edit by hand: change the knowledge base files and generate it again.

## What we are asking you to check

This content was drafted by AI from the published pages listed below. Please check:

1. Is any red flag for this symptom **missing**?
2. Is each rule's **urgency and level of care** right?
3. Is each **question** clear, and does it mean what the source means?
4. Is the **advice** right, specific enough, and safe?
5. For each item under "AI judgement and open points": keep, change or remove?

Mark the "OK?" column, or write comments against the rule id.

## How the engine uses this

- Each rule says: when these findings are present, the outcome is **at least** this.
- The most urgent rule that fires wins. If none fires, the default outcome is used.
- Red flags are always all checked. After an emergency outcome, the engine only asks what could still raise it to the most urgent outcome (an ambulance), then stops.
- "Not sure" is never treated as "no". If a rule cannot be ruled out, the more urgent outcome is chosen.

## Sources

| Page | Accessed | Page last reviewed | Note |
| --- | --- | --- | --- |
| [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | 2026-11-18 | 2024-09-12 |  |
| [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | 2026-11-18 | 2026-03-31 |  |
| [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | 2026-11-18 | 2024-01-30 |  |
| [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | 2026-11-18 | 2026-04-02 |  |
| [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | 2026-11-18 | 2024-04-26 |  |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Falls](https://www.nhs.uk/conditions/falls/) | 2026-11-19 |  | Page last reviewed: 06 March 2025 |
| [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | 2026-11-19 |  | Page last reviewed: 11 June 2025 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | 2026-11-19 |  | Page last reviewed: 04 September 2026 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | 2026-11-19 |  | Page last reviewed: 5 November 2025 |
| [Ankle pain](https://www.nhs.uk/symptoms/foot-pain/ankle-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | 2026-11-19 |  | Page last reviewed: 27 April 2023 |
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | 2026-11-19 |  | Page last reviewed: 02 October 2026 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | 2026-11-19 |  | Page last reviewed: 22 May 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dislocated shoulder](https://www.nhs.uk/conditions/dislocated-shoulder/) | 2026-11-19 |  | Page last reviewed: 16 September 2026 |
| [Broken ankle](https://www.nhs.uk/conditions/broken-ankle/) | 2026-11-19 |  | Page last reviewed: 05 November 2025 |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |

Content adapted from these pages contains public sector information licensed under the Open Government Licence v3.0. Adapted text no longer carries the original clinical approval.

## Red flags checked for everyone

Asked as one question: *"First, do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_stroke_signs`<br>Signs of a stroke now or in the last 24 hours | "Signs of a stroke" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_severe_breathing_difficulty`<br>Severe difficulty breathing: gasping, choking or not able to get words out | "Severe difficulty breathing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_lips_or_skin_blue_grey`<br>Lips or skin pale, blue or grey | "Lips or skin pale, blue or grey" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_passed_out`<br>Passed out and not responding normally | "Passed out and not responding normally" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_sudden_confusion`<br>Suddenly confused<br>**Note:** The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review. | "Suddenly confused" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| `rf_heavy_bleeding`<br>Bleeding that cannot be stopped, or blood coming out in spurts | "Bleeding that cannot be stopped" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_serious_self_harm`<br>Has seriously self-harmed, or feels about to self-harm | "Serious self-harm or about to self-harm" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |

## Injury or fall red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_inj_head_serious`<br>Head injury with serious signs: knocked out, a fit, very sleepy, or problems seeing, hearing, walking or speaking | "Serious signs after a head injury" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_inj_could_not_get_up`<br>Fallen and cannot get up, or was on the floor for a long time<br>**Note:** Being on the floor for an hour or more can damage muscles and kidneys. Adding it is AI judgement. | "Could not get up after a fall" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_inj_serious_accident`<br>A serious accident, such as a car crash or a fall from a height<br>**Note:** The Head injury page says call 999 after a fall from a height of more than 1 metre or 5 stairs, or a head injury at high speed. The Back pain page says 999 or A&E for back pain after a serious accident. | "A serious accident, such as a car crash or a fall from a height" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E. Do not move if your neck or back may be hurt.* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_inj_shock`<br>After an injury: cold, pale, sweaty skin, fast breathing, or feeling very faint<br>**Note:** The Broken leg page says call 999 or go to A&E. These are signs of shock from bleeding, so an ambulance is AI judgement. | "Cold, pale, sweaty skin or fast breathing after an injury" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | |
| `rf_inj_older_fall_head_back_neck_hip`<br>A fall in someone aged 65 or over, who may have hurt their head, neck, back or hip<br>**Note:** The Falls page says call 999 if someone has fallen and may have injured the head, back, neck or hip. Limiting it to people aged 65 or over, and allowing A&E, is AI judgement, needs clinical review. | "Had a fall" AND "Aged 65 or over" AND ("Head injury in the last month" OR "Neck pain or stiff neck" OR "Back pain" OR "Hip pain") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_inj_misshapen_or_out_of_place`<br>Changed shape or pointing at an odd angle, a bone sticking out, or a joint out of place | "Changed shape, or pointing at an odd angle" OR "Bone sticking out, or a deep cut over the injury" OR "A joint has moved out of place" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_inj_numb`<br>The injured area, or the part below it, is numb, tingling or has lost feeling | "Numb, tingling or no feeling below the injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_inj_cold_limb`<br>The skin around the injury has changed colour, such as blue or grey, or is cold to touch | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_inj_compartment`<br>Very bad pain that keeps getting worse, even with painkillers | "Very bad pain that keeps getting worse, even with painkillers" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | |
| `rf_inj_cannot_bear_weight`<br>Unable to walk or put weight on the leg after an injury<br>**Note:** The Hip pain page gives the same advice. The Ankle pain page says contact 111 if you are not able to walk. The more urgent is used. | "Cannot walk or put weight on the leg" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_inj_severe`<br>Severe pain after a fall or injury<br>**Note:** The Joint pain and Hip pain pages give the same advice. The hand and foot pages say contact 111 for severe pain. The more urgent is used. | "Severe pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | |

## Injury or fall red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_inj_head_urgent`<br>Head injury with being sick or dizzy, or in someone who takes medicine that thins the blood | "Being sick or dizzy after a head injury" OR ("Head injury in the last month" AND "Takes medicine that thins the blood, or bleeds easily") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_inj_maybe_broken`<br>A snap, crack, pop or grinding at the time of injury, or thinks a bone may be broken<br>**Note:** Source difference: the Sprains and strains page says A&E if you heard a crack. The body-area pages (wrist, finger, ankle, heel) say contact 111. An urgent treatment centre can X-ray most simple breaks, so urgent is used. Needs clinical review. | "Heard or felt a snap, crack or pop at the time of injury" OR "Thinks a bone may be broken" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111, or go to an urgent treatment centre* | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| `rf_inj_swollen_or_cannot_move`<br>Badly swollen, or cannot move the injured part or hold things<br>**Note:** The Broken arm or wrist page gives the same advice. | "Badly swollen, or swelled up very quickly" OR "Cannot move the painful joint or limb, or hold things" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111, or go to an urgent treatment centre* | [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | |
| `rf_inj_faint_from_pain`<br>Feeling faint, dizzy or sick from the pain | "Feels faint, dizzy or sick from the pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact NHS 111* | [Ankle pain](https://www.nhs.uk/symptoms/foot-pain/ankle-pain/) | |
| `rf_inj_fall_blackout`<br>Blacked out or felt dizzy or faint just before falling<br>**Note:** The Falls page says get help from 111 if someone has fallen and may be unwell. A blackout before a fall can be a heart rhythm problem. Urgent is AI judgement; chest pain or palpitations bring in their own entry symptoms. | "Blacked out or felt dizzy or faint just before falling" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_inj_older_fall`<br>A fall in someone aged 65 or over who may be in pain, injured or unwell<br>**Note:** The Falls page says get help from 111 if someone has fallen and may be in pain, injured or unwell. Limiting it to older people and marking it soft is AI judgement. A firm GP rule below still applies. | "Had a fall" AND "Aged 65 or over" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_inj_cast`<br>A plaster cast that feels too tight, or fingers or toes numb, swollen, blue or white | "Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | |
| `rf_inj_child_arm`<br>A child who will not use their arm after it was pulled or injured<br>**Note:** A pulled elbow is common in young children and is quickly put right at an urgent treatment centre. AI judgement. | "Under 16 years old" AND ("Child not using an arm, holding it still" OR "Child's arm was pulled or yanked, and now not used") | Urgent (help today)<br>Urgent care<br>Today<br>*Go to an urgent treatment centre today* | **AI judgement, needs clinical review** | |

## Injury or fall: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_inj_falls_gp`<br>Has had a fall at 65 or over, falls more than once, or is worried about balance | "Has fallen more than once, or worried about balance" OR ("Had a fall" AND "Aged 65 or over") | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP about your fall* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `or_inj_not_improving`<br>An injury that is getting worse or not feeling better after treating it yourself | "Pain for 2 weeks or more, not getting better" OR "Pain getting worse, or keeps coming back" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |

## Default outcome

Used when no rule fires.

- **A minor injury with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most sprains and strains get better on their own*
- Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Serious signs after a head injury | Since hitting your head, have you been knocked out, had a fit, found it hard to stay awake, or had problems seeing, hearing, walking or speaking? Or new numbness or weakness, or fluid or blood coming from the ears or nose? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Could not get up after a fall | After the fall, can you not get up, or were you on the floor for an hour or more? |  | [Falls](https://www.nhs.uk/conditions/falls/) | |
| A serious accident, such as a car crash or a fall from a height | Was it a serious accident, such as a car crash, or a fall from higher than 1 metre or down 5 or more stairs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Cold, pale, sweaty skin or fast breathing after an injury | Is your skin cold, pale and sweaty, or are you breathing fast or feeling very faint? |  | [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | |
| Had a fall | Did you have a fall? | 1912002 | [Falls](https://www.nhs.uk/conditions/falls/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Neck pain or stiff neck | Do you have pain or stiffness in your neck? | 81680005 | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Back pain | Do you have back pain? | 161891005 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Hip pain | Do you have pain in your hip? | 49218002 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Bone sticking out, or a deep cut over the injury | Is a bone sticking out through the skin, or is there a deep cut over the injury? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| A joint has moved out of place | Do you think a joint has moved out of place (dislocated), even if it then went back by itself? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Numb, tingling or no feeling below the injury | Since the injury, has the injured area, or the part below it, gone numb or tingly, or lost feeling? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Very bad pain that keeps getting worse, even with painkillers | Is the pain very bad and getting worse, even with painkillers? For example, a muscle that feels very tight and hurts more when it is moved. |  | [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | |
| Cannot walk or put weight on the leg | Are you unable to walk, or to put any weight on your leg? | 285674009 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Being sick or dizzy after a head injury | Since hitting your head, have you been sick or felt dizzy? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Takes medicine that thins the blood, or bleeds easily | Do you take medicine that thins your blood, such as warfarin, apixaban or rivaroxaban? Or do you have a condition that makes you bleed more easily? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Heard or felt a snap, crack or pop at the time of injury | Did you hear or feel a snap, crack, pop or grinding at the time of the injury? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Thinks a bone may be broken | Do you think you might have broken a bone? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Badly swollen, or swelled up very quickly | Is it badly swollen, or did it swell up very quickly? |  | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| Cannot move the painful joint or limb, or hold things | Are you unable to move the painful joint, arm or leg, or unable to hold things? |  | [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | |
| Feels faint, dizzy or sick from the pain | Do you feel faint, dizzy or sick because of the pain? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Blacked out or felt dizzy or faint just before falling | Just before the fall, did you black out, or feel dizzy, faint or that your heart was racing? |  | [Falls](https://www.nhs.uk/conditions/falls/) | |
| Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured | Do you have a plaster cast or splint that feels too tight? Or have your fingers or toes gone numb, swollen, blue or white? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child not using an arm, holding it still | Is your child not using their arm, and holding it still by their side? |  | **AI judgement, needs clinical review** | |
| Child's arm was pulled or yanked, and now not used | Was your child's arm pulled or yanked, for example when lifted by the hand, and now they will not use it? |  | **AI judgement, needs clinical review** | |
| Has fallen more than once, or worried about balance | Have you fallen more than once in the last year, or are you worried about your balance or walking? |  | [Falls](https://www.nhs.uk/conditions/falls/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain getting worse, or keeps coming back | Is the pain slowly getting worse, or does it keep coming back? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |

## Advice given with each outcome

### `advice_stroke`

**What to do:** Call 999 now. You may be having a stroke, or may have had one.

**Look out for:**
- One side of the face drooping
- Not being able to lift both arms and keep them up
- Slurred or confused speech
- Signs of a stroke can stop after a short time. Get help straight away even if they have stopped.

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/)

### `advice_breathing_emergency`

**What to do:** Call 999 now.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes
- Call 999 again if you move to a different place

**Where to go:** Call 999. Do not drive yourself to A&E. Stay with the person until help arrives.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/)

### `advice_sudden_confusion`

**What to do:** Call 999 or go to A&E now.

**Look out for:**
- Severe difficulty breathing, such as gasping, choking or not being able to get words out
- Lips or skin turning very pale, blue or grey

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/)

### `advice_heavy_bleeding`

**What to do:** Call 999 or go to A&E now.

**Look out for:**
- Blood that comes out in spurts and is bright red and hard to control
- Blood coming through the bandage or cloth. If it does, put another one on top and keep pressing.

**Get more help when:**
- Call 999 if you cannot stop the bleeding or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Press firmly on the wound with a bandage or a clean, folded cloth
- If something is stuck in the wound, do not take it out. Press on either side of it.
- If the wound is on a hand or arm, raise it above your head. If it is on a leg, lie down and raise it above the level of your heart.

Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/)

### `advice_self_harm`

**What to do:** Call 999 for an ambulance or go straight to A&E. Or ask someone else to call 999 or take you to A&E.

**Look out for:**
- Feeling that you may be about to harm yourself

**Get more help when:**
- If your life is in danger, call 999 now
- If you need someone to talk to, call Samaritans on 116 123 at any time, or text SHOUT to 85258

**Where to go:** Call 999 or go straight to A&E. Try to be around other people and get yourself to a safe place.

Source: [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

### `advice_head_injury_999`

**What to do:** Call 999 now. These signs after a head injury need to be checked in hospital straight away.

**Look out for:**
- The person stops responding, or their breathing changes
- A fit (seizure)
- Being very hard to wake
- Being sick again and again

**Get more help when:**
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.
- Call 999 again if they get worse before help arrives

**Where to go:** Call 999. Do not drive them to A&E yourself. If they may have hurt their neck, do not move them unless they are in danger.

**What you can do yourself:**
- Do not move the person if they may have hurt their neck or back

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_fall_999`

**What to do:** Call 999 now. The person may have a serious injury, or has been on the floor too long.

**Look out for:**
- Pain in the head, neck, back or hip
- Being confused or very sleepy

**Get more help when:**
- Call 999 again if the person gets worse before help arrives

**Where to go:** Call 999. Do not try to lift the person yourself.

**What you can do yourself:**
- Keep the person warm and comfortable, for example with a blanket
- If they can get up safely, help them slowly onto a chair. Do not lift them yourself.

Source: [Falls](https://www.nhs.uk/conditions/falls/)

### `advice_spinal_injury_emergency`

**What to do:** Call 999 or go to A&E now. The spine may be injured after a serious accident.

**Look out for:**
- Numbness, tingling or weakness in the arms or legs
- Problems peeing or pooing
- Being sick, very sleepy or confused after hitting the head

**Get more help when:**
- Call 999 straight away if the neck or back may be hurt. Do not move the person unless they are in danger.

**Where to go:** Call 999 for an ambulance if the neck or back may be hurt. Otherwise go to A&E. Do not drive yourself.

**What you can do yourself:**
- Keep still and keep the head and neck in line with the body
- Do not try to sit up or walk if your neck or back hurts after a serious accident

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/), [Falls](https://www.nhs.uk/conditions/falls/), [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_injury_999`

**What to do:** Call 999 now. These can be signs of shock after a serious injury.

**Look out for:**
- Getting more pale, cold or sleepy
- Breathing getting faster, or the person stops responding

**Get more help when:**
- Call 999 again if the person gets worse before help arrives
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Stay with the person and keep them warm.

**What you can do yourself:**
- Lie the person down and raise their legs if you can, unless you think they have hurt their neck, back or legs
- Press firmly on any bleeding with a clean cloth
- Do not give them anything to eat or drink

Source: [Broken leg](https://www.nhs.uk/conditions/broken-leg/)

### `advice_msk_emergency_ae`

**What to do:** Go to A&E now. You may have a broken bone, a joint out of place, or damage to the nerves or blood vessels.

**Look out for:**
- The arm, hand, leg or foot going cold, pale, blue or grey
- Numbness or pins and needles getting worse
- Pain that keeps getting worse, even with painkillers

**Get more help when:**
- Call 999 if you cannot get to A&E, or you cannot move because of the pain
- Call 999 if a bone is sticking out, or there is heavy bleeding

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you, or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not try to push a bone or joint back into place
- Keep the injured part still. Support it with a cushion or a sling if you can.
- Do not eat or drink in case you need an operation
- Take off any rings or watches near the injury before it swells

Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/), [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/), [Dislocated shoulder](https://www.nhs.uk/conditions/dislocated-shoulder/), [Broken ankle](https://www.nhs.uk/conditions/broken-ankle/)

### `advice_limb_blood_supply_emergency`

**What to do:** Call 999 or go to A&E now. A cold, pale, blue or grey arm or leg can mean its blood supply is blocked. It needs treatment within hours.

**Look out for:**
- The arm or leg getting colder or more pale
- Numbness or weakness getting worse
- Pain getting much worse

**Get more help when:**
- Call 999 if you cannot get to A&E quickly

**Where to go:** Go to A&E now, or call 999. Do not drive yourself.

**What you can do yourself:**
- Do not rub the arm or leg or put heat on it
- Take off anything tight, such as rings or a tight bandage

Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/), [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/)

### `advice_compartment_emergency`

**What to do:** Call 999 or go to A&E now. Pain that keeps getting worse after an injury can be pressure building up inside the muscles (compartment syndrome). This may need an operation quickly.

**Look out for:**
- The muscle feeling very tight or hard
- Numbness or pins and needles
- A plaster cast feeling tighter

**Get more help when:**
- Call 999 if you cannot get to A&E quickly

**Where to go:** Go to A&E now, or call 999. Do not drive yourself.

**What you can do yourself:**
- Do not raise the arm or leg high above your heart. Keep it level.
- Loosen any tight bandage. Do not take off a plaster cast yourself.

Source: [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/), [Broken leg](https://www.nhs.uk/conditions/broken-leg/), [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/)

### `advice_head_injury_urgent`

**What to do:** Get help from NHS 111 now. After a head injury, these symptoms need to be checked today.

**Look out for:**
- Getting drowsy or hard to wake
- A fit (seizure)
- Problems with vision, hearing, walking, balance or speaking
- Clear fluid or blood coming from the ears or nose
- A headache that will not go away

**Get more help when:**
- Call 999 if you get any of the signs above
- Call 999 if the person is knocked out, has a fit, or cannot stay awake

**Where to go:** Call 111 or use 111 online. Call 111 for a child under 5. If you are told to go to A&E, do not drive yourself.

**What you can do yourself:**
- Make sure an adult stays with you for at least the first 24 hours
- Rest, and do not drink alcohol

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_injury_urgent`

**What to do:** Get help from NHS 111 or go to an urgent treatment centre today. You may have a broken bone or a torn ligament or tendon, and may need an X-ray.

**Look out for:**
- The injured part changing shape, or going numb, cold, pale or blue
- Pain or swelling getting much worse

**Get more help when:**
- Go to A&E or call 999 if the injured part changes shape, goes numb, cold, pale or blue, or a bone is sticking out

**Where to go:** Call 111 or use 111 online. You can also go to an urgent treatment centre (also called a walk-in centre or minor injuries unit).

**What you can do yourself:**
- Rest the injured part and keep it still
- Put an ice pack (or frozen peas) wrapped in a towel on it for up to 20 minutes every 2 to 3 hours
- Raise it on a pillow if you can
- Take off any rings or jewellery near the injury

Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/), [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/), [Broken leg](https://www.nhs.uk/conditions/broken-leg/)

### `advice_fall_urgent`

**What to do:** Get help from NHS 111 today. A fall in an older person, or a fall after blacking out or feeling dizzy, needs checking.

**Look out for:**
- Pain in the hip, back or neck
- Being confused or very sleepy
- Chest pain, or your heart racing

**Get more help when:**
- Call 999 if the person cannot get up, hit their head and is confused or very sleepy, or has chest pain

**Where to go:** Call 111 or use 111 online.

**What you can do yourself:**
- Get up slowly. Sit for a while before you stand.

Source: [Falls](https://www.nhs.uk/conditions/falls/)

### `advice_fall_gp`

**What to do:** See a GP about your fall. They can check why you fell and help stop it happening again.

**Look out for:**
- Pain that gets worse after the fall
- Feeling dizzy or faint

**Get more help when:**
- Get help from 111 if you fall again, are in pain, or feel unwell
- Call 999 if you fall and cannot get up, or may have hurt your head, neck, back or hip

**Where to go:** Contact your GP surgery.

**What you can do yourself:**
- Remove things you could trip over at home, and use good lighting
- Wear shoes that fit well and grip

Source: [Falls](https://www.nhs.uk/conditions/falls/)

### `advice_msk_gp`

**What to do:** See a GP. In many areas you can also refer yourself to a physiotherapist or an NHS service for muscle and joint problems without seeing a GP first.

**Look out for:**
- The pain getting worse, or new swelling, heat or redness
- Numbness, tingling or weakness
- Feeling unwell with a high temperature

**Get more help when:**
- Get help from NHS 111 if the pain gets very bad, or the area gets hot and swollen. Do the same if you feel hot, cold or shivery.

**Where to go:** Contact your GP surgery, or look for an NHS service for back and joint problems you can refer yourself to.

**What you can do yourself:**
- Keep moving gently. Do not stop using the painful part completely.
- Use painkillers such as paracetamol or ibuprofen gel. Ask a pharmacist which is right for you.
- Use an ice pack or heat pack wrapped in a towel

Source: [Joint pain](https://www.nhs.uk/symptoms/joint-pain/), [Back pain](https://www.nhs.uk/conditions/back-pain/), [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/)

### `advice_injury_self_care`

**What to do:** You can treat most sprains, strains and minor injuries yourself. They usually start to feel better within a few days.

**Look out for:**
- Not being able to put weight on it or use it
- Numbness, or the skin going cold, pale or blue
- Pain or swelling getting worse

**Get more help when:**
- Get help from 111 or an urgent treatment centre if you think a bone may be broken
- See a GP if it is not feeling better after treating it yourself

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers and supports.

**What you can do yourself:**
- Rest it for the first 2 to 3 days
- Put an ice pack wrapped in a towel on it for up to 20 minutes every 2 to 3 hours
- Raise it on a pillow when you can
- Start moving it gently once the pain eases
- Do not use heat or have hot baths for the first 2 to 3 days

Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_inj_could_not_get_up`: Being on the floor for an hour or more can damage muscles and kidneys. Adding it is AI judgement.
- `rf_inj_serious_accident`: The Head injury page says call 999 after a fall from a height of more than 1 metre or 5 stairs, or a head injury at high speed. The Back pain page says 999 or A&E for back pain after a serious accident.
- `rf_inj_shock`: The Broken leg page says call 999 or go to A&E. These are signs of shock from bleeding, so an ambulance is AI judgement.
- `rf_inj_older_fall_head_back_neck_hip`: The Falls page says call 999 if someone has fallen and may have injured the head, back, neck or hip. Limiting it to people aged 65 or over, and allowing A&E, is AI judgement, needs clinical review.
- `rf_inj_cannot_bear_weight`: The Hip pain page gives the same advice. The Ankle pain page says contact 111 if you are not able to walk. The more urgent is used.
- `rf_inj_severe`: The Joint pain and Hip pain pages give the same advice. The hand and foot pages say contact 111 for severe pain. The more urgent is used.
- `rf_inj_maybe_broken`: Source difference: the Sprains and strains page says A&E if you heard a crack. The body-area pages (wrist, finger, ankle, heel) say contact 111. An urgent treatment centre can X-ray most simple breaks, so urgent is used. Needs clinical review.
- `rf_inj_swollen_or_cannot_move`: The Broken arm or wrist page gives the same advice.
- `rf_inj_fall_blackout`: The Falls page says get help from 111 if someone has fallen and may be unwell. A blackout before a fall can be a heart rhythm problem. Urgent is AI judgement; chest pain or palpitations bring in their own entry symptoms.
- `rf_inj_older_fall`: The Falls page says get help from 111 if someone has fallen and may be in pain, injured or unwell. Limiting it to older people and marking it soft is AI judgement. A firm GP rule below still applies.
- `rf_inj_child_arm`: A pulled elbow is common in young children and is quickly put right at an urgent treatment centre. AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A torn Achilles tendon (the tendon at the back of the heel) | 429513001 | rare | Felt a snap, or like being kicked, in the back of the ankle or heel: strongly supports; Cannot stand or walk on tiptoe, or walk up stairs: strongly supports; Pain in the heel: supports; Swelling and bruising in the calf and ankle: supports; Started after an injury, fall or accident: supports |
| A broken bone (fracture), such as a broken wrist, ankle, finger, toe or collarbone | 125605004 | uncommon | Started after an injury, fall or accident: strongly supports; Very painful to press on the bone: strongly supports; Heard or felt a snap, crack or pop at the time of injury: supports; Swelling of the painful area: supports; Bruising: supports; Cannot walk or put weight on the leg: supports; Cannot move the painful joint or limb, or hold things: supports; Thinks a bone may be broken: supports; Feels faint, dizzy or sick from the pain: supports |
| A bruise or minor knock | 125667009 | common | Bruising: strongly supports; Swelling of the painful area: supports |
| Compartment syndrome (pressure building up inside the muscles) | 111245009 | rare | Very bad pain that keeps getting worse, even with painkillers: strongly supports; Started after an injury, fall or accident: supports; Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured: supports; Numb, tingling or no feeling below the injury: supports; Swelling of the painful area: supports; Severe pain: supports |
| A dislocated joint (a bone pushed out of its usual place), such as a shoulder, kneecap or finger | 108367008 | rare | A joint has moved out of place: strongly supports; Changed shape, or pointing at an odd angle: strongly supports; Cannot move the painful joint or limb, or hold things: strongly supports; Started after an injury, fall or accident: strongly supports; Severe pain: supports |
| A broken hip | 5913000 | rare | Started after an injury, fall or accident: strongly supports; Cannot walk or put weight on the leg: strongly supports; Had a fall: supports; Severe pain: supports; Leg looks shorter, or foot turned outwards: supports |
| A serious injury to the spine or spinal cord, such as a broken neck or back |  | very rare | A serious accident, such as a car crash or a fall from a height: strongly supports; Started after an injury, fall or accident: strongly supports; Numb, tingling or no feeling below the injury: supports; Pain, tingling, weakness or numbness in both legs: supports; Severe pain: supports; Electric shock feeling in the neck or back, into the arms or legs: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
