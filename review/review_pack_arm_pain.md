# Review pack: Elbow and arm pain

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
| [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | 2026-11-19 |  | Page last reviewed: 26 January 2024 |
| [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | 2026-11-19 |  | Page last reviewed: 02 October 2026 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | 2026-11-19 |  | Page last reviewed: 04 September 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | 2026-11-19 |  | Page last reviewed: 22 May 2023 |
| [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | 2026-11-19 |  | Page last reviewed: 5 November 2025 |
| [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | 2026-11-19 |  | Page last reviewed: 27 April 2023 |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |
| [Dislocated shoulder](https://www.nhs.uk/conditions/dislocated-shoulder/) | 2026-11-19 |  | Page last reviewed: 16 September 2026 |
| [Broken ankle](https://www.nhs.uk/conditions/broken-ankle/) | 2026-11-19 |  | Page last reviewed: 05 November 2025 |
| [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | 2026-11-19 |  | Page last reviewed: 11 June 2025 |
| [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/) | 2026-11-19 |  | Page last reviewed: 16 August 2023 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |

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

## Elbow and arm pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_arm_heart`<br>Arm pain with pressure, heaviness, tightness or squeezing in the chest, or chest pain<br>**Note:** This could be a heart attack. A yes to chest pain also brings in the chest pain entry symptom. | "Chest pain" OR "Chest feels tight or squeezed" OR "Chest feels heavy" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_injury_misshapen`<br>Arm injury where the arm has changed shape or is at an odd angle, or a bone is sticking out<br>**Note:** The Elbow and arm pain page says go to an urgent treatment centre or A&E. The Broken arm or wrist page says A&E or 999. The more urgent is used. | "Bone sticking out, or a deep cut over the injury" OR ("Started after an injury, fall or accident" AND "Changed shape, or pointing at an odd angle") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| `rf_arm_numb_after_injury`<br>Arm injury and the arm or hand is numb, tingling or has pins and needles | "Numb, tingling or no feeling below the injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| `rf_arm_cold`<br>Arm or hand cold, pale, white, blue or grey<br>**Note:** Can mean the blood supply to the arm is blocked. Applying the Sprains and strains rule without an injury is AI judgement. | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_arm_compartment`<br>Very bad arm pain that keeps getting worse, even with painkillers<br>**Note:** Could be pressure building up inside the muscles (compartment syndrome), which needs an operation quickly. | "Very bad pain that keeps getting worse, even with painkillers" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | |

## Elbow and arm pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_arm_severe_cannot_move`<br>Severe arm pain and the arm is difficult to move | "Severe pain" AND "Cannot move the painful joint or limb, or hold things" | Urgent (help today)<br>Urgent care<br>Today<br>*Go to an urgent treatment centre or A&E* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_snap_or_misshapen`<br>Arm injury with a snapping noise, or an arm that has changed shape<br>**Note:** The Sprains and strains page says A&E if you heard a crack. The Elbow and arm pain page says an urgent treatment centre or A&E. The arm page is used because it is more specific; needs clinical review. | "Heard or felt a snap, crack or pop at the time of injury" OR "Changed shape, or pointing at an odd angle" | Urgent (help today)<br>Urgent care<br>Today<br>*Go to an urgent treatment centre or A&E* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_tingling`<br>Arm that tingles or feels numb<br>**Note:** Source difference: the Carpal tunnel syndrome and Neck pain pages say see a GP for tingling in the hand or arm. Marked soft so a likely trapped nerve can lower it. | "Pins and needles, tingling or numbness in the arm, hand or fingers" | Urgent (help today)<br>Urgent care<br>Today<br>*Go to an urgent treatment centre or A&E* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_exercise_pain`<br>Arm pain that comes on with exercise and goes away with rest<br>**Note:** Can be a sign of angina (chest pain caused by narrowed blood vessels to the heart) felt in the arm. | "Pain comes on with exercise or walking, and goes with rest" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_hot_or_fever`<br>Arm swollen with a high temperature, or feeling hot, cold or shivery, or a joint that is hot and swollen<br>**Note:** Could be a joint or skin infection. A hot, swollen joint is from the Joint pain page. | "Swollen area is red or hot to touch" OR ("Swelling of the painful area" AND "Very high temperature, or feels hot, cold or shivery") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| `rf_arm_injury_111`<br>Arm injury that is very painful, badly swollen, hard to move, or may be broken | "Started after an injury, fall or accident" AND ("Severe pain" OR "Badly swollen, or swelled up very quickly" OR "Cannot move the painful joint or limb, or hold things" OR "Thinks a bone may be broken") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111, or go to an urgent treatment centre* | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| `rf_arm_cast`<br>A plaster cast that feels too tight, or fingers numb, swollen, blue or white | "Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| `rf_arm_child_not_using`<br>A child who is not using their arm, or whose arm was pulled and now will not use it<br>**Note:** A young child who will not use an arm may have a pulled elbow, a broken bone or an infection. The Osteomyelitis page says take a child to a GP if they do not want to use an arm or leg. Urgent is AI judgement, needs clinical review. | "Under 16 years old" AND ("Child not using an arm, holding it still" OR "Child's arm was pulled or yanked, and now not used") | Urgent (help today)<br>Urgent care<br>Today<br>*Go to an urgent treatment centre today* | **AI judgement, needs clinical review** | |

## Elbow and arm pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_arm_gp`<br>Elbow or arm pain that has not gone away after a few weeks | "Pain for 2 weeks or more, not getting better" OR "Pain getting worse, or keeps coming back" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |

## Default outcome

Used when no rule fires.

- **Elbow or arm pain with nothing that needs more help: ease it yourself for a couple of days**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most elbow and arm pain is not serious and can be eased at home*
- Source: [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Elbow or arm pain | Do you have pain in your arm or elbow? | 102556003 | [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Chest feels tight or squeezed | Does your chest feel tight, or like it is being squeezed? | 23924001 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Chest feels heavy | Does your chest feel heavy? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Bone sticking out, or a deep cut over the injury | Is a bone sticking out through the skin, or is there a deep cut over the injury? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Numb, tingling or no feeling below the injury | Since the injury, has the injured area, or the part below it, gone numb or tingly, or lost feeling? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Very bad pain that keeps getting worse, even with painkillers | Is the pain very bad and getting worse, even with painkillers? For example, a muscle that feels very tight and hurts more when it is moved. |  | [Compartment syndrome](https://www.nhs.uk/conditions/compartment-syndrome/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Cannot move the painful joint or limb, or hold things | Are you unable to move the painful joint, arm or leg, or unable to hold things? |  | [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | |
| Heard or felt a snap, crack or pop at the time of injury | Did you hear or feel a snap, crack, pop or grinding at the time of the injury? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Pins and needles, tingling or numbness in the arm, hand or fingers | Do you have pins and needles, tingling or numbness in your arm, hand or fingers? |  | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Pain comes on with exercise or walking, and goes with rest | Does the pain come on when you exercise or walk, and go away after a few minutes of rest? |  | [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Swelling of the painful area | Is the painful area swollen? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Badly swollen, or swelled up very quickly | Is it badly swollen, or did it swell up very quickly? |  | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| Thinks a bone may be broken | Do you think you might have broken a bone? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured | Do you have a plaster cast or splint that feels too tight? Or have your fingers or toes gone numb, swollen, blue or white? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child not using an arm, holding it still | Is your child not using their arm, and holding it still by their side? |  | **AI judgement, needs clinical review** | |
| Child's arm was pulled or yanked, and now not used | Was your child's arm pulled or yanked, for example when lifted by the hand, and now they will not use it? |  | **AI judgement, needs clinical review** | |
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

### `advice_chest_pain_999`

**What to do:** Call 999 now. You could be having a heart attack and need treatment in hospital straight away.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- If you think you or someone else is having a heart attack, do these things while you wait for help.
- Sit and rest on the floor with your knees bent and your back supported. If you cannot do this, sit on a chair.
- Take aspirin (300mg) if you have any. Do not give aspirin to someone who has an aspirin allergy.
- If you have angina (chest pain caused by narrowed blood vessels to the heart), use your spray if you have it with you. It goes under your tongue. It may be called glyceryl trinitrate or GTN.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Angina](https://www.nhs.uk/conditions/angina/)

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

### `advice_arm_pain_urgent`

**What to do:** Go to an urgent treatment centre or A&E today. You may have a broken bone, an injury to the nerves, or another problem that needs checking.

**Look out for:**
- Your arm or hand going numb, cold, pale or blue
- Your arm changing shape
- Pain that keeps getting worse

**Get more help when:**
- Call 999 if arm pain comes on suddenly with pressure, heaviness or squeezing in your chest
- Go to A&E straight away if a bone is sticking out, or your arm goes cold, pale or blue

**Where to go:** Go to an urgent treatment centre (also called a walk-in centre or minor injuries unit) or A&E. You can also call 111.

**What you can do yourself:**
- Keep the arm still, and support it with a sling or cushion
- Take off any rings or watches
- Put an ice pack wrapped in a towel on it

Source: [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/), [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/)

### `advice_arm_pain_111`

**What to do:** Get help from NHS 111 today. Arm pain that comes on with exercise and goes with rest can be a sign of a heart problem such as angina (chest pain caused by narrowed blood vessels to the heart).

**Look out for:**
- Pain or pressure in your chest
- Being short of breath, sweaty or feeling sick

**Get more help when:**
- Call 999 if arm pain comes on suddenly with pressure, heaviness or squeezing in your chest

**Where to go:** Call 111 or use 111 online.

**What you can do yourself:**
- Avoid the activity that brings on the pain until you have been checked

Source: [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/)

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

### `advice_arm_pain_self_care`

**What to do:** Elbow and arm pain is not usually a sign of anything serious. Try easing it yourself for a couple of days.

**Look out for:**
- Pressure, heaviness or squeezing in your chest
- Tingling or numbness in your arm
- A swollen arm with a high temperature

**Get more help when:**
- Call 999 if arm pain comes on suddenly with pressure, heaviness or squeezing in your chest
- See a GP if the pain does not go away after a few weeks

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers.

**What you can do yourself:**
- Put a heat pack, or frozen peas wrapped in a tea towel, on your arm for 10 to 15 minutes every few hours
- Take painkillers such as paracetamol or ibuprofen
- Raise your arm if it is swollen

Source: [Arm pain](https://www.nhs.uk/symptoms/elbow-and-arm-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_arm_heart`: This could be a heart attack. A yes to chest pain also brings in the chest pain entry symptom.
- `rf_arm_injury_misshapen`: The Elbow and arm pain page says go to an urgent treatment centre or A&E. The Broken arm or wrist page says A&E or 999. The more urgent is used.
- `rf_arm_cold`: Can mean the blood supply to the arm is blocked. Applying the Sprains and strains rule without an injury is AI judgement.
- `rf_arm_compartment`: Could be pressure building up inside the muscles (compartment syndrome), which needs an operation quickly.
- `rf_arm_snap_or_misshapen`: The Sprains and strains page says A&E if you heard a crack. The Elbow and arm pain page says an urgent treatment centre or A&E. The arm page is used because it is more specific; needs clinical review.
- `rf_arm_tingling`: Source difference: the Carpal tunnel syndrome and Neck pain pages say see a GP for tingling in the hand or arm. Marked soft so a likely trapped nerve can lower it.
- `rf_arm_exercise_pain`: Can be a sign of angina (chest pain caused by narrowed blood vessels to the heart) felt in the arm.
- `rf_arm_hot_or_fever`: Could be a joint or skin infection. A hot, swollen joint is from the Joint pain page.
- `rf_arm_child_not_using`: A young child who will not use an arm may have a pulled elbow, a broken bone or an infection. The Osteomyelitis page says take a child to a GP if they do not want to use an arm or leg. Urgent is AI judgement, needs clinical review.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A sudden loss of blood supply to an arm or leg |  | rare | Arm, hand, leg or foot cold, pale, blue or grey: strongly supports; Pain started suddenly: supports; Severe pain: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Weakness in one or both legs, or a foot that drags: supports; An arm or leg suddenly cold, pale or blue and painful: strongly supports; Only the fingers, toes, hands or feet are blue or grey: supports; Pain or swelling in one leg: supports |
| A broken bone (fracture), such as a broken wrist, ankle, finger, toe or collarbone | 125605004 | uncommon | Started after an injury, fall or accident: strongly supports; Very painful to press on the bone: strongly supports; Heard or felt a snap, crack or pop at the time of injury: supports; Swelling of the painful area: supports; Bruising: supports; Cannot walk or put weight on the leg: supports; Cannot move the painful joint or limb, or hold things: supports; Thinks a bone may be broken: supports; Feels faint, dizzy or sick from the pain: supports |
| Bursitis (a swollen, painful fluid-filled pad near a joint) | 84017003 | uncommon | Painful to kneel, lean on or lie on the area: strongly supports; Swelling of the painful area: supports; Started after more activity than usual, or doing the same movement many times: supports; Skin over the painful area has changed colour: supports |
| Carpal tunnel syndrome (a squashed nerve in the wrist) | 57406009 | uncommon | Pins and needles, tingling or numbness in the arm, hand or fingers: strongly supports; Hand pain or tingling worse at night: strongly supports; Weak arm or hand, or a weak grip: supports; Pain in the wrist: supports; Pain in the palm of the hand: supports; Started after more activity than usual, or doing the same movement many times: supports |
| Compartment syndrome (pressure building up inside the muscles) | 111245009 | rare | Very bad pain that keeps getting worse, even with painkillers: strongly supports; Started after an injury, fall or accident: supports; Plaster cast feels too tight, or fingers or toes numb, swollen or discoloured: supports; Numb, tingling or no feeling below the injury: supports; Swelling of the painful area: supports; Severe pain: supports |
| A dislocated joint (a bone pushed out of its usual place), such as a shoulder, kneecap or finger | 108367008 | rare | A joint has moved out of place: strongly supports; Changed shape, or pointing at an odd angle: strongly supports; Cannot move the painful joint or limb, or hold things: strongly supports; Started after an injury, fall or accident: strongly supports; Severe pain: supports |
| Osteomyelitis (an infection in a bone) | 60168000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Swollen area is red or hot to touch: supports; Skin over the painful area has changed colour: supports; Feels very unwell: supports; Pain worse at night, or not better with rest: supports; Child not using an arm, holding it still: supports; Cannot walk or put weight on the leg: supports |
| Pulled elbow (a slipped bone in the elbow of a young child) | 417109008 | rare | Child's arm was pulled or yanked, and now not used: strongly supports; Child not using an arm, holding it still: strongly supports; Pain in or around the elbow: supports |
| Septic arthritis (an infection in a joint) | 372939007 | rare | Swollen area is red or hot to touch: strongly supports; Swelling of the painful area: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Cannot move the painful joint or limb, or hold things: supports; Cannot walk or put weight on the leg: supports; Severe pain: supports; Skin over the painful area has changed colour: supports; Pain in just one joint: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |
| Tendonitis (a swollen, painful tendon), such as Achilles tendonitis | 34840004 | uncommon | Started after more activity than usual, or doing the same movement many times: strongly supports; Pain worse when moving, easier when resting: supports; Swelling of the painful area: supports; Grating or crackling when moving the joint: supports |
| Tennis or golfer's elbow (painful tendons on the outside or inside of the elbow) | 202855006 | common | Pain on the outside of the elbow, worse when gripping: strongly supports; Started after more activity than usual, or doing the same movement many times: strongly supports; Pain in or around the elbow: supports |
| A trapped nerve in the neck, causing pain or tingling down the arm | 54404000 | uncommon | Pain spreads from the neck or shoulder down the arm: strongly supports; Pins and needles, tingling or numbness in the arm, hand or fingers: strongly supports; Weak arm or hand, or a weak grip: supports; Pins and needles all the time: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
