# Review pack: Knee pain

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
| [Dislocated kneecap](https://www.nhs.uk/conditions/dislocated-kneecap/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | 2026-11-19 |  | Page last reviewed: 30 April 2026 |
| [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | 2026-11-19 |  | Page last reviewed: 23 January 2025 |
| [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | 2026-11-19 |  | Page last reviewed: 02 October 2026 |
| [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | 2026-11-19 |  | Page last reviewed: 5 November 2025 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | 2026-11-19 |  | Page last reviewed: 22 May 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dislocated shoulder](https://www.nhs.uk/conditions/dislocated-shoulder/) | 2026-11-19 |  | Page last reviewed: 16 September 2026 |
| [Broken ankle](https://www.nhs.uk/conditions/broken-ankle/) | 2026-11-19 |  | Page last reviewed: 05 November 2025 |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | 2026-11-19 |  | Page last reviewed: 03 April 2024 |
| [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/) | 2026-11-19 |  | Page last reviewed: 16 August 2023 |

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

## Knee pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_knee_injury_misshapen`<br>Knee injury where the knee has changed shape or became very swollen very quickly, or a bone is sticking out<br>**Note:** The Knee pain page says get advice from 111 if the knee is badly swollen or has changed shape. The Dislocated kneecap page says A&E after an injury. The more urgent is used after an injury. | "Bone sticking out, or a deep cut over the injury" OR ("Started after an injury, fall or accident" AND ("Changed shape, or pointing at an odd angle" OR "Badly swollen, or swelled up very quickly")) | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E. Call 999 if you cannot move your leg because of the pain.* | [Dislocated kneecap](https://www.nhs.uk/conditions/dislocated-kneecap/) | |
| `rf_knee_injury_pop`<br>Knee injury with a pop or snap felt at the time<br>**Note:** Source difference: the Dislocated kneecap page says A&E if you felt a pop or snap in your knee. The Knee pain page links a pop during injury to a torn ligament or cartilage, and says 111 only if the knee is unstable. The more urgent is used, marked soft so a likely torn ligament can lower it. | "Heard or felt a snap, crack or pop at the time of injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E* | [Dislocated kneecap](https://www.nhs.uk/conditions/dislocated-kneecap/) | |
| `rf_knee_numb_after_injury`<br>Numbness, tingling or no feeling in the leg or foot after a knee injury | "Numb, tingling or no feeling below the injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_knee_cold_leg`<br>Leg or foot cold, pale, white, blue or grey<br>**Note:** A dislocated knee can damage the main blood vessel behind it. Applying the rule without an injury is AI judgement. | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_knee_dvt_breathless`<br>Signs of a blood clot in the leg with shortness of breath or chest pain | "One leg swollen, warm and painful, often in the calf" AND ("Short of breath" OR "Chest pain") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |
| `rf_knee_child_unwell`<br>A child with knee pain who feels generally unwell, with a high temperature or feeling hot, cold or shivery | "Under 16 years old" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_knee_child_no_weight`<br>A child with knee pain who cannot put any weight on the leg<br>**Note:** The Limping in children page says 999 or A&E for a child who cannot put any weight on their leg. Split from the soft rule below, so the likely conditions cannot lower it. | "Under 16 years old" AND "Cannot walk or put weight on the leg" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_knee_child_sudden_or_no_weight`<br>A child with sudden knee or thigh pain<br>**Note:** The Limping in children page says 999 or A&E, as hip problems can be felt in the knee. The Irritable hip page says urgent GP or 111. The more urgent is used, marked soft. | "Under 16 years old" AND "Pain started suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |

## Knee pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_knee_severe`<br>Very painful knee | "Severe pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 now, or go to an urgent treatment centre* | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| `rf_knee_cannot_move_or_weight`<br>Cannot move the knee or put any weight on it | "Cannot move the painful joint or limb, or hold things" OR "Cannot walk or put weight on the leg" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 now, or go to an urgent treatment centre* | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| `rf_knee_swollen_or_misshapen`<br>Knee badly swollen or changed shape | "Badly swollen, or swelled up very quickly" OR "Changed shape, or pointing at an odd angle" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 now* | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| `rf_knee_locks`<br>Knee locks, gives way or painfully clicks | "Knee locks, gives way or painfully clicks" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 now* | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| `rf_knee_infection_signs`<br>Knee hot and swollen, red, or with a high temperature or feeling hot, cold or shivery<br>**Note:** The Knee pain page lists a high temperature with redness or heat around the knee. The Septic arthritis and Joint pain pages say urgent help for any one of these. The more urgent reading is used. | "Swollen area is red or hot to touch" OR "Skin over the painful area has changed colour" OR "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 now* | [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | |
| `rf_knee_kneecap_went_back`<br>Thinks the kneecap moved out of place, even if it went back by itself | "A joint has moved out of place" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Dislocated kneecap](https://www.nhs.uk/conditions/dislocated-kneecap/) | |
| `rf_knee_blood_thinners_swelling`<br>A swollen knee in someone who takes medicine that thins the blood<br>**Note:** The Knee pain page says bleeding into the joint is more likely on medicine that thins the blood. Making it urgent is AI judgement, needs clinical review. | "Takes medicine that thins the blood, or bleeds easily" AND "Swelling of the painful area" | Urgent (help today)<br>Urgent care<br>Today<br>*Get advice from NHS 111 today* | **AI judgement, needs clinical review** | |
| `rf_knee_dvt`<br>Signs of a blood clot in the leg: one leg swollen, warm and painful, usually in the calf | "One leg swollen, warm and painful, often in the calf" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |

## Knee pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_knee_gp`<br>Knee pain that has not improved within a few weeks, is getting worse, or is stopping usual activities | "Pain for 2 weeks or more, not getting better" OR "Pain getting worse, or keeps coming back" OR "Pain stopping usual activities or affecting sleep" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |

## Default outcome

Used when no rule fires.

- **Knee pain with nothing that needs more help: treat it at home and it should start to feel better in a few days**
- Outcome: Self-manageable, Self-care, No appointment needed. *You should start to feel better in a few days*
- Source: [Knee pain](https://www.nhs.uk/symptoms/knee-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Knee pain | Do you have pain in your knee? | 1003722009 | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Bone sticking out, or a deep cut over the injury | Is a bone sticking out through the skin, or is there a deep cut over the injury? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Badly swollen, or swelled up very quickly | Is it badly swollen, or did it swell up very quickly? |  | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| Heard or felt a snap, crack or pop at the time of injury | Did you hear or feel a snap, crack, pop or grinding at the time of the injury? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Numb, tingling or no feeling below the injury | Since the injury, has the injured area, or the part below it, gone numb or tingly, or lost feeling? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| One leg swollen, warm and painful, often in the calf | Is one of your legs swollen, warm and painful, usually in the calf? The skin may look red or darker, and the veins may look swollen. |  | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Cannot walk or put weight on the leg | Are you unable to walk, or to put any weight on your leg? | 285674009 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Cannot move the painful joint or limb, or hold things | Are you unable to move the painful joint, arm or leg, or unable to hold things? |  | [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | |
| Knee locks, gives way or painfully clicks | Does your knee lock, give way, or click painfully? Clicking that does not hurt is usual. |  | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Skin over the painful area has changed colour | Has the skin over the painful area changed colour, for example gone red or purple? This may be harder to see on brown or black skin. |  | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| A joint has moved out of place | Do you think a joint has moved out of place (dislocated), even if it then went back by itself? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Takes medicine that thins the blood, or bleeds easily | Do you take medicine that thins your blood, such as warfarin, apixaban or rivaroxaban? Or do you have a condition that makes you bleed more easily? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Swelling of the painful area | Is the painful area swollen? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain getting worse, or keeps coming back | Is the pain slowly getting worse, or does it keep coming back? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |

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

### `advice_dvt_emergency`

**What to do:** Call 999 or go to A&E now. A blood clot in the leg may have moved to your lungs. This can be life-threatening.

**Look out for:**
- Breathing getting harder
- Chest pain getting worse
- Coughing up blood, or feeling faint

**Get more help when:**
- Call 999 if you collapse, or your breathing gets much worse

**Where to go:** Go to A&E now, or call 999. Do not drive yourself. Bring any medicines you take.

Source: [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/)

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

### `advice_knee_pain_urgent`

**What to do:** Get advice from NHS 111 now, or go to an urgent treatment centre. You may have a torn ligament or cartilage, a dislocated kneecap, or an infection.

**Look out for:**
- The knee changing shape, or swelling very quickly
- Your leg or foot going numb, cold, pale or blue
- Feeling hot, cold or shivery

**Get more help when:**
- Go to A&E if your knee changes shape, swells up very quickly after an injury, or a bone is sticking out

**Where to go:** Call 111 or use 111 online, or go to an urgent treatment centre. You may be seen quicker than at A&E.

**What you can do yourself:**
- Put as little weight as possible on your knee
- Put an ice pack wrapped in a tea towel on it for up to 20 minutes every 2 to 3 hours

Source: [Knee pain](https://www.nhs.uk/symptoms/knee-pain/), [Dislocated kneecap](https://www.nhs.uk/conditions/dislocated-kneecap/)

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

### `advice_dvt_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A swollen, warm, painful leg can be a blood clot in a vein (DVT). It needs treatment to stop it moving to the lungs.

**Look out for:**
- Feeling short of breath
- Chest pain, especially when breathing in
- Coughing up blood

**Get more help when:**
- Call 999 or go to A&E if you get short of breath or have chest pain

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you are pregnant, you can also call your maternity unit.

**What you can do yourself:**
- Do not rub or massage the leg

Source: [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/)

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

### `advice_knee_pain_self_care`

**What to do:** Knee pain can often be treated at home. You should start to feel better in a few days.

**Look out for:**
- The knee locking, giving way or clicking painfully
- The knee becoming hot and red, or you feeling hot, cold or shivery
- A swollen, painful calf

**Get more help when:**
- Get help from 111 if the pain gets very bad or you get a high temperature. Do the same if the knee swells a lot, locks or gives way.
- See a GP if it does not improve within a few weeks

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers.

**What you can do yourself:**
- Put as little weight as possible on your knee, for example avoid standing for a long time
- Put an ice pack or frozen peas wrapped in a tea towel on it for up to 20 minutes every 2 to 3 hours
- Use paracetamol, or ibuprofen gel or tablets

Source: [Knee pain](https://www.nhs.uk/symptoms/knee-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_knee_injury_misshapen`: The Knee pain page says get advice from 111 if the knee is badly swollen or has changed shape. The Dislocated kneecap page says A&E after an injury. The more urgent is used after an injury.
- `rf_knee_injury_pop`: Source difference: the Dislocated kneecap page says A&E if you felt a pop or snap in your knee. The Knee pain page links a pop during injury to a torn ligament or cartilage, and says 111 only if the knee is unstable. The more urgent is used, marked soft so a likely torn ligament can lower it.
- `rf_knee_cold_leg`: A dislocated knee can damage the main blood vessel behind it. Applying the rule without an injury is AI judgement.
- `rf_knee_child_no_weight`: The Limping in children page says 999 or A&E for a child who cannot put any weight on their leg. Split from the soft rule below, so the likely conditions cannot lower it.
- `rf_knee_child_sudden_or_no_weight`: The Limping in children page says 999 or A&E, as hip problems can be felt in the knee. The Irritable hip page says urgent GP or 111. The more urgent is used, marked soft.
- `rf_knee_infection_signs`: The Knee pain page lists a high temperature with redness or heat around the knee. The Septic arthritis and Joint pain pages say urgent help for any one of these. The more urgent reading is used.
- `rf_knee_blood_thinners_swelling`: The Knee pain page says bleeding into the joint is more likely on medicine that thins the blood. Making it urgent is AI judgement, needs clinical review.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A sudden loss of blood supply to an arm or leg |  | rare | Arm, hand, leg or foot cold, pale, blue or grey: strongly supports; Pain started suddenly: supports; Severe pain: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Weakness in one or both legs, or a foot that drags: supports; An arm or leg suddenly cold, pale or blue and painful: strongly supports; Only the fingers, toes, hands or feet are blue or grey: supports; Pain or swelling in one leg: supports |
| Bleeding into a joint | 81808003 | rare | Badly swollen, or swelled up very quickly: strongly supports; Bruising: supports; Swollen area is red or hot to touch: supports; Started after an injury, fall or accident: supports |
| A rare cancer affecting the bones or blood, such as leukaemia (a cancer of the blood) |  | rare | Pain worse at night, or not better with rest: strongly supports; A lump or swelling on a bone: supports; Losing weight without trying: supports; Feels very tired: supports; Feels very unwell: supports |
| A broken bone (fracture), such as a broken wrist, ankle, finger, toe or collarbone | 125605004 | uncommon | Started after an injury, fall or accident: strongly supports; Very painful to press on the bone: strongly supports; Heard or felt a snap, crack or pop at the time of injury: supports; Swelling of the painful area: supports; Bruising: supports; Cannot walk or put weight on the leg: supports; Cannot move the painful joint or limb, or hold things: supports; Thinks a bone may be broken: supports; Feels faint, dizzy or sick from the pain: supports |
| Bursitis (a swollen, painful fluid-filled pad near a joint) | 84017003 | uncommon | Painful to kneel, lean on or lie on the area: strongly supports; Swelling of the painful area: supports; Started after more activity than usual, or doing the same movement many times: supports; Skin over the painful area has changed colour: supports |
| A dislocated joint (a bone pushed out of its usual place), such as a shoulder, kneecap or finger | 108367008 | rare | A joint has moved out of place: strongly supports; Changed shape, or pointing at an odd angle: strongly supports; Cannot move the painful joint or limb, or hold things: strongly supports; Started after an injury, fall or accident: strongly supports; Severe pain: supports |
| Gout (sudden, very painful swelling in a joint, often the big toe) | 90560007 | uncommon | Swollen area is red or hot to touch: strongly supports; Pain started suddenly: strongly supports; Pain in a toe, or the joint at the base of the big toe: strongly supports; Skin over the painful area has changed colour: supports; Severe pain: supports; Pain in just one joint: supports; Takes a statin, or water tablets: supports |
| A torn ligament or cartilage in the knee |  | uncommon | Knee locks, gives way or painfully clicks: strongly supports; Started after an injury, fall or accident: strongly supports; Twisted, rolled or overstretched it: strongly supports; Heard or felt a snap, crack or pop at the time of injury: supports; Badly swollen, or swelled up very quickly: supports |
| Osgood-Schlatter's (a painful bump below the kneecap in growing children) | 72047008 | rare | Pain and a tender lump just below the kneecap: strongly supports; Started after more activity than usual, or doing the same movement many times: strongly supports |
| Osteoarthritis (painful, stiff joints from wear and repair over time) | 396275006 | uncommon | Pain on and off for more than 3 months: strongly supports; Pain worse when moving, easier when resting: strongly supports; Same joints painful on both sides of the body: supports; Grating or crackling when moving the joint: supports; Pain getting worse, or keeps coming back: supports |
| Osteomyelitis (an infection in a bone) | 60168000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Swollen area is red or hot to touch: supports; Skin over the painful area has changed colour: supports; Feels very unwell: supports; Pain worse at night, or not better with rest: supports; Child not using an arm, holding it still: supports; Cannot walk or put weight on the leg: supports |
| Pain at the front of the knee around the kneecap (patellofemoral pain) | 430725003 | common | Pain at the front of the knee, worse on stairs or squatting: strongly supports; Started after more activity than usual, or doing the same movement many times: supports; Same joints painful on both sides of the body: supports |
| Perthes (a problem with the blood supply to the top of the thigh bone in children) | 111255008 | rare | Limping: strongly supports; Pain in the groin, thigh or knee: strongly supports; Pain for 2 weeks or more, not getting better: supports; Cannot move the painful joint or limb, or hold things: supports |
| Reactive arthritis (painful, swollen joints after an infection) | 201736002 | rare | Diarrhoea, or an infection caught through sex, in the weeks before: strongly supports; Red or bloodshot eye: supports; Swelling of the painful area: supports; Pain in several joints: supports; Pain in the heel: supports |
| Septic arthritis (an infection in a joint) | 372939007 | rare | Swollen area is red or hot to touch: strongly supports; Swelling of the painful area: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Cannot move the painful joint or limb, or hold things: supports; Cannot walk or put weight on the leg: supports; Severe pain: supports; Skin over the painful area has changed colour: supports; Pain in just one joint: supports |
| A slipped growth plate at the top of the thigh bone (slipped upper femoral epiphysis) | 26460006 | rare | Pain in the groin, thigh or knee: strongly supports; Limping: strongly supports; Leg looks shorter, or foot turned outwards: supports; Pain for 2 weeks or more, not getting better: supports; Cannot walk or put weight on the leg: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |
| Tendonitis (a swollen, painful tendon), such as Achilles tendonitis | 34840004 | uncommon | Started after more activity than usual, or doing the same movement many times: strongly supports; Pain worse when moving, easier when resting: supports; Swelling of the painful area: supports; Grating or crackling when moving the joint: supports |
| Blood clot in a vein, usually in the leg (deep vein thrombosis, DVT) | 128053003 | uncommon | Pain or swelling in one leg: strongly supports; Swelling is severe, painful or came on suddenly: supports; Swollen area is red or hot to touch: supports; One leg swollen, warm and painful, often in the calf: strongly supports; Swelling of the painful area: supports; Skin over the painful area has changed colour: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
