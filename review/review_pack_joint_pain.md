# Review pack: Joint pain

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
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Reactive arthritis](https://www.nhs.uk/conditions/reactive-arthritis/) | 2026-11-19 |  | Page last reviewed: 16 December 2024 |
| [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | 2026-11-19 |  | Page last reviewed: 23 April 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | 2026-11-19 |  | Page last reviewed: 02 October 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | 2026-11-19 |  | Page last reviewed: 22 May 2023 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | 2026-11-19 |  | Page last reviewed: 27 April 2023 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | 2026-11-19 |  | Page last reviewed: 12 June 2023 |
| [Rheumatoid arthritis](https://www.nhs.uk/conditions/rheumatoid-arthritis/) | 2026-11-19 |  | Page last reviewed: 08 March 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dislocated shoulder](https://www.nhs.uk/conditions/dislocated-shoulder/) | 2026-11-19 |  | Page last reviewed: 16 September 2026 |
| [Broken ankle](https://www.nhs.uk/conditions/broken-ankle/) | 2026-11-19 |  | Page last reviewed: 05 November 2025 |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
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

## Joint pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_joint_severe_after_injury`<br>Very bad joint pain after a fall or injury | "Started after an injury, fall or accident" AND "Severe pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_cannot_bear_weight`<br>Unable to walk or put weight on a joint | "Cannot walk or put weight on the leg" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_out_of_place`<br>A joint has moved out of place<br>**Note:** The Dislocated kneecap page says 111 if the kneecap moved out and then went back by itself. The more urgent Joint pain page is used. | "A joint has moved out of place" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_numb_after_injury`<br>Tingling or no feeling in the area around the joint after an injury | "Numb, tingling or no feeling below the injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_misshapen_after_injury`<br>A joint injury where it has changed shape or a bone is sticking out | "Bone sticking out, or a deep cut over the injury" OR ("Started after an injury, fall or accident" AND "Changed shape, or pointing at an odd angle") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| `rf_joint_cold_limb`<br>Arm, hand, leg or foot cold, pale, white, blue or grey | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |

## Joint pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_joint_hot_swollen`<br>Joint pain and the skin around the joint is swollen and feels hot | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_unwell`<br>Joint pain and feeling generally unwell, a high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `rf_joint_sudden_severe`<br>Severe joint pain that started suddenly<br>**Note:** The Septic arthritis and Reactive arthritis pages say this, usually in just one joint. Gout also starts like this. | "Severe pain" AND "Pain started suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | |
| `rf_joint_colour_change`<br>The skin around a joint has changed colour | "Skin over the painful area has changed colour" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | |
| `rf_joint_swelling_or_hard_to_move`<br>Swelling around a joint, or a joint that is difficult to move<br>**Note:** Source difference: the Septic arthritis page lists these as urgent signs. The Joint pain, Rheumatoid arthritis and Psoriatic arthritis pages say see a GP for joint swelling that keeps coming back. Marked soft so a likely long-term arthritis can lower it. | "Swelling of the painful area" OR "Cannot move the painful joint or limb, or hold things" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | |
| `rf_joint_reactive_signs`<br>Sore joints with sore or red eyes or sight problems, or after diarrhoea or an infection caught through sex<br>**Note:** Signs of reactive arthritis. The page lists sore eyes with sight problems, and pain when peeing or genital symptoms. Applying it to a recent infection is AI judgement. | "Red or bloodshot eye" OR "Diarrhoea, or an infection caught through sex, in the weeks before" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Reactive arthritis](https://www.nhs.uk/conditions/reactive-arthritis/) | |
| `rf_joint_painkillers_not_helping`<br>Joint pain not controlled with simple painkillers<br>**Note:** From the Reactive arthritis page. Applying it to all joint pain is AI judgement; marked soft. | "Painkillers have not helped" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Reactive arthritis](https://www.nhs.uk/conditions/reactive-arthritis/) | |
| `rf_joint_giant_cell_arteritis`<br>Joint or muscle pain with a new headache, a tender scalp, jaw pain when eating or problems with sight | "Jaw pain when eating, or a sore or tender scalp or temple" OR "Change in sight or loss of vision" OR "Headache feels different from usual headaches" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact a GP now, or get help from NHS 111* | [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | |

## Joint pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_joint_gp`<br>Joint pain stopping usual activities or sleep, getting worse or coming back, not better after 2 weeks, or stiff for more than 30 minutes after waking<br>**Note:** Small joints of the hands or feet are from the Rheumatoid arthritis page. Both shoulders or hips are from the Polymyalgia rheumatica page. | "Pain stopping usual activities or affecting sleep" OR "Pain getting worse, or keeps coming back" OR "Pain for 2 weeks or more, not getting better" OR "Stiff for more than 30 minutes after waking" OR "Small joints of the hands or feet painful, swollen or stiff" OR "Pain and stiffness in both shoulders or both hips, worst in the morning" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| `or_joint_child`<br>A child with joint problems | "Under 16 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP* | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |

## Default outcome

Used when no rule fires.

- **Joint pain with nothing that needs more help: ease it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *See a GP if it has not improved after 2 weeks*
- Source: [Joint pain](https://www.nhs.uk/symptoms/joint-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Joint pain | Do you have pain in one or more of your joints? | 57676002 | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
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
| A joint has moved out of place | Do you think a joint has moved out of place (dislocated), even if it then went back by itself? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Numb, tingling or no feeling below the injury | Since the injury, has the injured area, or the part below it, gone numb or tingly, or lost feeling? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Bone sticking out, or a deep cut over the injury | Is a bone sticking out through the skin, or is there a deep cut over the injury? |  | [Broken arm or wrist](https://www.nhs.uk/conditions/broken-arm-or-wrist/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Skin over the painful area has changed colour | Has the skin over the painful area changed colour, for example gone red or purple? This may be harder to see on brown or black skin. |  | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Swelling of the painful area | Is the painful area swollen? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Cannot move the painful joint or limb, or hold things | Are you unable to move the painful joint, arm or leg, or unable to hold things? |  | [Shoulder pain](https://www.nhs.uk/symptoms/shoulder-pain/) | |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Diarrhoea, or an infection caught through sex, in the weeks before | In the 4 weeks before the joint pain started, did you have diarrhoea, or an infection you caught through sex? |  | [Reactive arthritis](https://www.nhs.uk/conditions/reactive-arthritis/) | |
| Painkillers have not helped | Have painkillers like paracetamol or ibuprofen not helped? |  | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Headache feels different from usual headaches | Does this headache feel different from the headaches you usually get? |  | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain getting worse, or keeps coming back | Is the pain slowly getting worse, or does it keep coming back? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Stiff for more than 30 minutes after waking | Are you stiff for more than 30 minutes after you wake up in the morning? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Small joints of the hands or feet painful, swollen or stiff | Are the small joints of your fingers, hands or feet painful, swollen or stiff? |  | [Rheumatoid arthritis](https://www.nhs.uk/conditions/rheumatoid-arthritis/) | |
| Pain and stiffness in both shoulders or both hips, worst in the morning | Do you have pain and stiffness in both shoulders, or both hips, that is worst in the morning? |  | [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |

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

### `advice_joint_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today.

**Look out for:**
- A joint becoming hot, red and swollen
- A high temperature, or feeling hot, cold or shivery
- Sore eyes or problems with your sight

**Get more help when:**
- Call 999 or go to A&E if you feel very unwell, or cannot walk or put weight on a joint

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Rest the painful joints
- Ask a pharmacist which painkiller is right for you

Source: [Reactive arthritis](https://www.nhs.uk/conditions/reactive-arthritis/)

### `advice_giant_cell_arteritis_urgent`

**What to do:** Contact a GP straight away, or get help from NHS 111 today. A new headache, a tender scalp, jaw pain when eating, or sight problems can be inflamed blood vessels in the head (giant cell arteritis). Without quick treatment it can cause blindness or a stroke.

**Look out for:**
- Any loss of sight, or double vision
- Signs of a stroke: face drooping, not being able to lift both arms, or slurred speech

**Get more help when:**
- Call 999 or go to A&E if you lose any sight, or have signs of a stroke

**Where to go:** Contact your GP surgery now, or call 111 or use 111 online.

Source: [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/)

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

### `advice_joint_pain_self_care`

**What to do:** You can ease joint pain yourself. See a GP if it has not improved after 2 weeks.

**Look out for:**
- A joint becoming hot, swollen or red
- Feeling unwell, with a high temperature
- Stiffness for more than 30 minutes after waking up

**Get more help when:**
- Get help from 111 or an urgent GP appointment if a joint gets hot and swollen. Do the same if you feel unwell with a high temperature.
- See a GP if the pain stops you doing normal things, keeps coming back, or your child has joint problems

**Where to go:** You do not need to see anyone now. A pharmacist can help you choose a painkiller.

**What you can do yourself:**
- Rest the painful joint, but do not stop moving it completely
- Put an ice pack wrapped in a towel on it for up to 20 minutes every 2 to 3 hours
- Try to lose weight if you are overweight, and do not smoke

Source: [Joint pain](https://www.nhs.uk/symptoms/joint-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_joint_out_of_place`: The Dislocated kneecap page says 111 if the kneecap moved out and then went back by itself. The more urgent Joint pain page is used.
- `rf_joint_sudden_severe`: The Septic arthritis and Reactive arthritis pages say this, usually in just one joint. Gout also starts like this.
- `rf_joint_swelling_or_hard_to_move`: Source difference: the Septic arthritis page lists these as urgent signs. The Joint pain, Rheumatoid arthritis and Psoriatic arthritis pages say see a GP for joint swelling that keeps coming back. Marked soft so a likely long-term arthritis can lower it.
- `rf_joint_reactive_signs`: Signs of reactive arthritis. The page lists sore eyes with sight problems, and pain when peeing or genital symptoms. Applying it to a recent infection is AI judgement.
- `rf_joint_painkillers_not_helping`: From the Reactive arthritis page. Applying it to all joint pain is AI judgement; marked soft.
- `or_joint_gp`: Small joints of the hands or feet are from the Rheumatoid arthritis page. Both shoulders or hips are from the Polymyalgia rheumatica page.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bleeding into a joint | 81808003 | rare | Badly swollen, or swelled up very quickly: strongly supports; Bruising: supports; Swollen area is red or hot to touch: supports; Started after an injury, fall or accident: supports |
| Bursitis (a swollen, painful fluid-filled pad near a joint) | 84017003 | uncommon | Painful to kneel, lean on or lie on the area: strongly supports; Swelling of the painful area: supports; Started after more activity than usual, or doing the same movement many times: supports; Skin over the painful area has changed colour: supports |
| A dislocated joint (a bone pushed out of its usual place), such as a shoulder, kneecap or finger | 108367008 | rare | A joint has moved out of place: strongly supports; Changed shape, or pointing at an odd angle: strongly supports; Cannot move the painful joint or limb, or hold things: strongly supports; Started after an injury, fall or accident: strongly supports; Severe pain: supports |
| Fibromyalgia (long-term pain all over the body) | 203082005 | uncommon | Pain all over the body, with tiredness and poor sleep: strongly supports; Feels very tired: supports; Pain on and off for more than 3 months: supports; Pain in several joints: supports |
| Gout (sudden, very painful swelling in a joint, often the big toe) | 90560007 | uncommon | Swollen area is red or hot to touch: strongly supports; Pain started suddenly: strongly supports; Pain in a toe, or the joint at the base of the big toe: strongly supports; Skin over the painful area has changed colour: supports; Severe pain: supports; Pain in just one joint: supports; Takes a statin, or water tablets: supports |
| Joint hypermobility (very bendy joints that can hurt) | 85551004 | rare | Very bendy joints that often click, sprain or dislocate: strongly supports; Pain in several joints: supports; Pain getting worse, or keeps coming back: supports |
| Juvenile arthritis (long-term joint swelling in children) | 410502007 | rare | Swelling of the painful area: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Pain for 2 weeks or more, not getting better: supports; Pain in several joints: supports |
| Aching joints during the menopause or the time leading up to it |  | rare | Going through the menopause or the time leading up to it: strongly supports; Pain in several joints: supports; Feels very tired: supports |
| Osteoarthritis (painful, stiff joints from wear and repair over time) | 396275006 | uncommon | Pain on and off for more than 3 months: strongly supports; Pain worse when moving, easier when resting: strongly supports; Same joints painful on both sides of the body: supports; Grating or crackling when moving the joint: supports; Pain getting worse, or keeps coming back: supports |
| Polymyalgia rheumatica (stiff, sore shoulders and hips) | 65323003 | rare | Pain and stiffness in both shoulders or both hips, worst in the morning: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Feels very tired: supports; Losing weight without trying: supports; Jaw pain when eating, or a sore or tender scalp or temple: supports |
| Psoriatic arthritis (joint pain linked to psoriasis) | 156370009 | rare | Swelling of the painful area: supports; Small joints of the hands or feet painful, swollen or stiff: supports; Stiff for more than 30 minutes after waking: supports; Pain getting worse, or keeps coming back: supports |
| Reactive arthritis (painful, swollen joints after an infection) | 201736002 | rare | Diarrhoea, or an infection caught through sex, in the weeks before: strongly supports; Red or bloodshot eye: supports; Swelling of the painful area: supports; Pain in several joints: supports; Pain in the heel: supports |
| Rheumatoid arthritis (the body's defences attack the joints) | 69896004 | uncommon | Small joints of the hands or feet painful, swollen or stiff: strongly supports; Same joints painful on both sides of the body: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Swelling of the painful area: supports; Feels very tired: supports; Pain in several joints: supports |
| Septic arthritis (an infection in a joint) | 372939007 | rare | Swollen area is red or hot to touch: strongly supports; Swelling of the painful area: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Cannot move the painful joint or limb, or hold things: supports; Cannot walk or put weight on the leg: supports; Severe pain: supports; Skin over the painful area has changed colour: supports; Pain in just one joint: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |
| Tendonitis (a swollen, painful tendon), such as Achilles tendonitis | 34840004 | uncommon | Started after more activity than usual, or doing the same movement many times: strongly supports; Pain worse when moving, easier when resting: supports; Swelling of the painful area: supports; Grating or crackling when moving the joint: supports |
| Aching joints from a viral infection |  | common | Cold, flu, COVID-19 or a similar illness in the last few weeks: strongly supports; Aching body: supports; Pain in several joints: supports; Very high temperature, or feels hot, cold or shivery: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
