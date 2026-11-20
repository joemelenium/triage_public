# Review pack: Hip pain

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
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | 2026-11-19 |  | Page last reviewed: 23 January 2025 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Falls](https://www.nhs.uk/conditions/falls/) | 2026-11-19 |  | Page last reviewed: 06 March 2025 |
| [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | 2026-11-19 |  | Page last reviewed: 03 April 2024 |
| [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Hip fracture](https://www.nhs.uk/conditions/broken-hip/) | 2026-11-19 |  | Page last reviewed: 29 July 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | 2026-11-19 |  | Page last reviewed: 23 April 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/) | 2026-11-19 |  | Page last reviewed: 16 August 2023 |
| [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | 2026-11-19 |  | Page last reviewed: 22 May 2023 |

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

## Hip pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hip_severe_after_injury`<br>Severe hip pain after a fall or injury<br>**Note:** The Hip fracture page gives the same advice. | "Started after an injury, fall or accident" AND "Severe pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_cannot_bear_weight`<br>Hip pain and unable to walk or put weight on the leg<br>**Note:** For children, the Limping in children page says the same. The Irritable hip page says urgent GP or 111 for a child who cannot put weight on a leg. The more urgent is used. | "Cannot walk or put weight on the leg" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_numb_after_injury`<br>Tingling or loss of feeling in the hip or leg after an injury | "Numb, tingling or no feeling below the injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_misshapen`<br>Leg has changed shape or is at an odd angle, or after an injury looks shorter or turned outwards<br>**Note:** A leg that looks shorter and turned out after a fall is a classic sign of a broken hip. Adding it is AI judgement. | "Changed shape, or pointing at an odd angle" OR ("Started after an injury, fall or accident" AND "Leg looks shorter, or foot turned outwards") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_hip_cold_leg`<br>Leg or foot cold, pale, white, blue or grey<br>**Note:** Can mean the blood supply to the leg is blocked. Applying it without an injury is AI judgement. | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_hip_older_fall`<br>Hip pain after a fall in someone aged 65 or over<br>**Note:** The Falls page says call 999 if someone has fallen and may have injured their hip. A broken hip in an older person can still allow some walking. Marked soft because the Hip pain page only says 999 for severe pain or not being able to walk. A firm urgent rule below still applies. | "Had a fall" AND "Aged 65 or over" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_hip_child_unwell`<br>A child with hip pain who feels generally unwell, with a high temperature or feeling hot, cold or shivery<br>**Note:** Could be an infected hip joint, which can damage the joint within hours. The Irritable hip page says take the child back to a GP if they get a high temperature. The more urgent is used. | "Under 16 years old" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_hip_child_sudden`<br>A child with sudden pain in the hip, thigh or knee<br>**Note:** Source difference: the Limping in children page says 999 or A&E for sudden pain in the hip, knee or thigh. The Irritable hip page says urgent GP or 111. The more urgent is used, marked soft so a likely irritable hip in a well child can lower it to urgent. | "Under 16 years old" AND "Pain started suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_hip_child_tummy_pain`<br>A child with hip pain and severe pain in the lower tummy | "Under 16 years old" AND "Severe pain in the lower tummy" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |

## Hip pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hip_severe_sudden`<br>Severe hip pain that started suddenly, with no fall or injury | "Severe pain" AND "Pain started suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_hot_or_colour`<br>Hip swollen and hot, or the skin around the hip has changed colour | "Swollen area is red or hot to touch" OR "Skin over the painful area has changed colour" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_unwell`<br>Hip pain with feeling generally unwell and a high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| `rf_hip_child_limp`<br>A child with hip pain who is limping | "Under 16 years old" AND "Limping" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | |
| `rf_hip_older_fall_urgent`<br>Hip pain after a fall or injury in someone aged 65 or over, or with thin bones<br>**Note:** The Osteoporosis page says get urgent help after a recent fall or injury if the pain is not getting better. | "Started after an injury, fall or accident" AND ("Aged 65 or over" OR "Thin bones (osteoporosis), or long-term steroid tablets") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | |

## Hip pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_hip_child_checked`<br>Hip pain in a child, which should always be checked<br>**Note:** The Irritable hip page says hip pain in children should always be checked. Within a few days is AI judgement; sudden pain or a limp is urgent by the rules above. | "Under 16 years old" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within a few days, sooner if it gets worse* | [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | |
| `or_hip_gp`<br>Hip pain stopping usual activities or sleep, getting worse or coming back, not better after 2 weeks, or stiff for more than 30 minutes after waking | "Pain stopping usual activities or affecting sleep" OR "Pain getting worse, or keeps coming back" OR "Pain for 2 weeks or more, not getting better" OR "Stiff for more than 30 minutes after waking" OR "Pain and stiffness in both shoulders or both hips, worst in the morning" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |

## Default outcome

Used when no rule fires.

- **Hip pain in an adult with nothing that needs more help: ease it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *See a GP if it has not improved after 2 weeks*
- Source: [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Hip pain | Do you have pain in your hip? | 49218002 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Cannot walk or put weight on the leg | Are you unable to walk, or to put any weight on your leg? | 285674009 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Numb, tingling or no feeling below the injury | Since the injury, has the injured area, or the part below it, gone numb or tingly, or lost feeling? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Leg looks shorter, or foot turned outwards | Does the leg on the painful side look shorter than the other, or is the foot turned outwards? |  | [Hip fracture](https://www.nhs.uk/conditions/broken-hip/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Had a fall | Did you have a fall? | 1912002 | [Falls](https://www.nhs.uk/conditions/falls/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Severe pain in the lower tummy | Do you have severe pain in the lower part of your tummy? |  | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Skin over the painful area has changed colour | Has the skin over the painful area changed colour, for example gone red or purple? This may be harder to see on brown or black skin. |  | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Limping | Are you limping? | 16973004 | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| Thin bones (osteoporosis), or long-term steroid tablets | Do you have thin, weak bones (osteoporosis)? Or have you taken steroid tablets for 3 months or more? |  | [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain getting worse, or keeps coming back | Is the pain slowly getting worse, or does it keep coming back? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Stiff for more than 30 minutes after waking | Are you stiff for more than 30 minutes after you wake up in the morning? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain and stiffness in both shoulders or both hips, worst in the morning | Do you have pain and stiffness in both shoulders, or both hips, that is worst in the morning? |  | [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | |

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

### `advice_hip_pain_emergency`

**What to do:** Call 999 or go to A&E now. You may have a broken hip or another serious injury.

**Look out for:**
- The leg looking shorter or turned outwards
- Numbness or tingling in the leg
- Pain getting worse

**Get more help when:**
- Call 999 if you cannot move, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not try to walk on the leg
- Keep warm while you wait

Source: [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/), [Hip fracture](https://www.nhs.uk/conditions/broken-hip/)

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

### `advice_child_limp_emergency`

**What to do:** Call 999 or go to A&E now. Your child needs to be checked in hospital. It could be an infected joint or bone, a broken bone, or a hip problem that needs treatment quickly.

**Look out for:**
- Your child getting more unwell, sleepy or floppy
- A rash that does not fade when you press a glass against it
- Pain getting worse

**Get more help when:**
- Call 999 if your child is very unwell or you cannot get to A&E

**Where to go:** Go to A&E now, or call 999. Do not drive if you are upset. Bring any medicines your child takes.

**What you can do yourself:**
- Do not let your child walk on the painful leg
- Do not give them anything to eat until a doctor has checked them, in case they need an operation

Source: [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/), [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/), [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/)

### `advice_hip_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today.

**Look out for:**
- Not being able to walk or put weight on your leg
- The hip becoming hot, swollen or red
- Feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if you cannot walk or put weight on your leg, or have tingling or loss of feeling in your leg

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Try not to put strain on the hip
- Take paracetamol for the pain

Source: [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/), [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/)

### `advice_joint_infection_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A hot, swollen joint, or joint pain with a high temperature, can be an infection in the joint or bone that needs treatment quickly.

**Look out for:**
- The joint getting hotter, more swollen or harder to move
- Feeling more unwell, hot, cold or shivery
- Red skin spreading

**Get more help when:**
- Call 999 or go to A&E if you feel very unwell, confused, or your skin goes blotchy, pale or blue

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you cannot get an urgent appointment, call 111.

**What you can do yourself:**
- Rest the joint
- Take paracetamol for the pain while you wait

Source: [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/), [Joint pain](https://www.nhs.uk/symptoms/joint-pain/), [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/)

### `advice_child_hip_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Hip pain or a limp in a child needs to be checked the same day, as it could be a sign of something serious.

**Look out for:**
- A high temperature, or your child feeling hot, cold or shivery
- Not being able to put any weight on the leg
- The pain getting worse

**Get more help when:**
- Call 999 or go to A&E if your child gets a high temperature or seems very unwell. Do the same if they cannot put any weight on their leg.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Let your child rest their leg
- Give children's paracetamol or ibuprofen for the pain

Source: [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/), [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)

### `advice_child_hip_soon`

**What to do:** See a GP within a few days. Hip pain in children should always be checked.

**Look out for:**
- Sudden pain in the hip, thigh or knee
- Limping, or not wanting to walk
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Get an urgent GP appointment or help from 111 if your child starts limping or has sudden pain
- Call 999 or go to A&E if your child cannot put weight on their leg or seems unwell with a high temperature

**Where to go:** Ask your GP surgery for an appointment in the next few days.

**What you can do yourself:**
- Give children's paracetamol or ibuprofen for the pain
- Avoid sports and activities that put strain on the hip until it has been checked

Source: [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/)

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

### `advice_hip_pain_self_care`

**What to do:** You can ease hip pain yourself. See a GP if it has not improved after 2 weeks.

**Look out for:**
- The hip becoming hot, swollen or red
- Feeling hot, cold or shivery
- Stiffness for more than 30 minutes after waking up

**Get more help when:**
- Get help from 111 or an urgent GP appointment if the hip gets hot and swollen. Do the same if you feel unwell with a high temperature.
- See a GP if the pain is stopping you doing normal things or affecting your sleep

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers.

**What you can do yourself:**
- Keep moving if you can, but try not to overdo it
- Put an ice pack wrapped in a towel on it for up to 20 minutes every 2 to 3 hours
- Use paracetamol or ibuprofen gel
- Wear comfortable shoes with a soft sole, and try gentle hip stretches
- Do not carry heavy things or sit in low chairs

Source: [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hip_severe_after_injury`: The Hip fracture page gives the same advice.
- `rf_hip_cannot_bear_weight`: For children, the Limping in children page says the same. The Irritable hip page says urgent GP or 111 for a child who cannot put weight on a leg. The more urgent is used.
- `rf_hip_misshapen`: A leg that looks shorter and turned out after a fall is a classic sign of a broken hip. Adding it is AI judgement.
- `rf_hip_cold_leg`: Can mean the blood supply to the leg is blocked. Applying it without an injury is AI judgement.
- `rf_hip_older_fall`: The Falls page says call 999 if someone has fallen and may have injured their hip. A broken hip in an older person can still allow some walking. Marked soft because the Hip pain page only says 999 for severe pain or not being able to walk. A firm urgent rule below still applies.
- `rf_hip_child_unwell`: Could be an infected hip joint, which can damage the joint within hours. The Irritable hip page says take the child back to a GP if they get a high temperature. The more urgent is used.
- `rf_hip_child_sudden`: Source difference: the Limping in children page says 999 or A&E for sudden pain in the hip, knee or thigh. The Irritable hip page says urgent GP or 111. The more urgent is used, marked soft so a likely irritable hip in a well child can lower it to urgent.
- `rf_hip_older_fall_urgent`: The Osteoporosis page says get urgent help after a recent fall or injury if the pain is not getting better.
- `or_hip_child_checked`: The Irritable hip page says hip pain in children should always be checked. Within a few days is AI judgement; sudden pain or a limp is urgent by the rules above.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bursitis (a swollen, painful fluid-filled pad near a joint) | 84017003 | uncommon | Painful to kneel, lean on or lie on the area: strongly supports; Swelling of the painful area: supports; Started after more activity than usual, or doing the same movement many times: supports; Skin over the painful area has changed colour: supports |
| A broken hip | 5913000 | rare | Started after an injury, fall or accident: strongly supports; Cannot walk or put weight on the leg: strongly supports; Had a fall: supports; Severe pain: supports; Leg looks shorter, or foot turned outwards: supports |
| Irritable hip (a short-lived swelling of the hip joint in children) | 301864002 | rare | Limping: strongly supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Pain started suddenly: supports; Pain in the groin, thigh or knee: supports; Hip pain: supports |
| Osteoarthritis (painful, stiff joints from wear and repair over time) | 396275006 | uncommon | Pain on and off for more than 3 months: strongly supports; Pain worse when moving, easier when resting: strongly supports; Same joints painful on both sides of the body: supports; Grating or crackling when moving the joint: supports; Pain getting worse, or keeps coming back: supports |
| Perthes (a problem with the blood supply to the top of the thigh bone in children) | 111255008 | rare | Limping: strongly supports; Pain in the groin, thigh or knee: strongly supports; Pain for 2 weeks or more, not getting better: supports; Cannot move the painful joint or limb, or hold things: supports |
| Polymyalgia rheumatica (stiff, sore shoulders and hips) | 65323003 | rare | Pain and stiffness in both shoulders or both hips, worst in the morning: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Feels very tired: supports; Losing weight without trying: supports; Jaw pain when eating, or a sore or tender scalp or temple: supports |
| Septic arthritis (an infection in a joint) | 372939007 | rare | Swollen area is red or hot to touch: strongly supports; Swelling of the painful area: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Cannot move the painful joint or limb, or hold things: supports; Cannot walk or put weight on the leg: supports; Severe pain: supports; Skin over the painful area has changed colour: supports; Pain in just one joint: supports |
| A slipped growth plate at the top of the thigh bone (slipped upper femoral epiphysis) | 26460006 | rare | Pain in the groin, thigh or knee: strongly supports; Limping: strongly supports; Leg looks shorter, or foot turned outwards: supports; Pain for 2 weeks or more, not getting better: supports; Cannot walk or put weight on the leg: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |
| Tendonitis (a swollen, painful tendon), such as Achilles tendonitis | 34840004 | uncommon | Started after more activity than usual, or doing the same movement many times: strongly supports; Pain worse when moving, easier when resting: supports; Swelling of the painful area: supports; Grating or crackling when moving the joint: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
