# Review pack: Chest pain

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
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | 2026-11-18 |  | Page last reviewed: 14 August 2026 |
| [Pleurisy](https://www.nhs.uk/conditions/pleurisy/) | 2026-11-18 |  | Page last reviewed: 16 September 2026 |
| [Pericarditis](https://www.nhs.uk/conditions/pericarditis/) | 2026-11-18 |  | Page last reviewed: 17 July 2023 |
| [Shingles](https://www.nhs.uk/conditions/shingles/) | 2026-11-18 |  | Page last reviewed: 23 November 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |

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

## Chest pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to you right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cp_sudden_not_going_away`<br>Sudden pain or discomfort in the chest that does not go away | "Sudden chest pain that does not go away" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 straight away* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_cp_tight_or_squeezing`<br>Chest pain that feels tight or like squeezing | "Chest feels tight or squeezed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_cp_heavy`<br>Chest that feels heavy<br>**Note:** The source lists a chest that feels 'tight or heavy' for people who are short of breath. Applying it to chest pain is AI judgement, needs clinical review. Added after a development test case showed the question list could not express it. | "Chest feels heavy" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| `rf_cp_spreads`<br>Chest pain that spreads to the arm, neck, jaw, shoulder, stomach or back<br>**Note:** The Chest pain page gives the same advice without naming the shoulder. | "Pain spreads to arm, neck, jaw, shoulder, stomach or back" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 straight away* | [Angina](https://www.nhs.uk/conditions/angina/) | |
| `rf_cp_with_sweating_sickness_or_breathlessness`<br>Chest pain with feeling sweaty, sick, light-headed or short of breath<br>**Note:** Source difference: the Heart attack page says to call 111 for chest pain with feeling or being sick. The Chest pain page says 999. The more urgent is used. | "Feels sweaty" OR "Feels sick or has been sick" OR "Feels light-headed" OR "Short of breath" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 straight away* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_cp_heart_beating_very_fast`<br>Chest pain with the heart beating very fast<br>**Note:** Source difference: the Heart attack page says to call 111 for chest pain with a racing heart. The Pulmonary embolism page says 999 or A&E for a heart beating very fast. The more urgent is used. | "Heart beating very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_cp_present_now`<br>Chest pain that is there now<br>**Note:** Pragmatic resolution of a source difference, needs clinical review. The Pulmonary embolism page says to call 999 or go to A&E if 'you feel pain in your chest or upper back'. The Chest pain page says to see a GP for pain that comes and goes or has gone away. Both are followed: pain that is there now is an emergency, and pain that has stopped uses the Chest pain page. This will over-triage some people, for example someone with a pulled muscle that still hurts. | "Chest pain is there now" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_cp_fainted`<br>Chest pain and has passed out | "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_cp_angina_not_settling`<br>Diagnosed angina, and chest pain that does not stop after resting or taking angina medicine | "Diagnosed with angina" AND "Pain not stopped by rest or angina medicine" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Angina](https://www.nhs.uk/conditions/angina/) | |
| `rf_cp_tearing_to_back`<br>Sudden, severe chest or back pain that feels like something tearing inside<br>**Note:** Added in the chest and breathing pilot. The Costochondritis page says call 999 for sudden chest or back pain that feels like something being torn inside. Clinically this is a sign of a tear in the body's main blood vessel (aortic dissection), which can be fatal within hours. | "Sudden severe chest or back pain, like something tearing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | |
| `rf_cp_lasted_15_minutes`<br>Sudden chest pain that lasted 15 minutes or more, even if it has stopped<br>**Note:** The Pleurisy page says call 999 or go to A&E for sudden chest pain that lasts for 15 minutes or more, which could be a heart attack or a blood clot in the lung. Asking about it even if the pain has stopped is AI judgement. Kept firm, not soft: angina that lasts this long may be a heart attack, so likely angina must not lower it. This will over-triage some chest wall pain that came on suddenly. Added in the breathing batch after test-case authors found no question for it. Needs clinical review. | "Sudden chest pain that lasted 15 minutes or more, even if it has stopped" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pleurisy](https://www.nhs.uk/conditions/pleurisy/) | |

## Chest pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to you? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cp_angina_worse`<br>Diagnosed angina that is worse than before, more frequent, longer lasting or happening at rest | "Diagnosed with angina" AND "Angina worse than before" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Angina](https://www.nhs.uk/conditions/angina/) | |
| `rf_cp_comes_and_goes`<br>Chest pain that comes and goes and looks like angina (brought on by activity, tight or squeezing, or with heart risk factors), in someone not diagnosed with angina<br>**Note:** Source difference: the Chest pain page says to see a GP (non-urgent) for chest pain that comes and goes. The Angina page says to get help from 111. The more urgent is used when the pain looks like angina (AI judgement: brought on by activity, tight or squeezing, or with heart risk factors); other chest pain that comes and goes falls to the default, see a GP, as the Chest pain page says. Narrowed after development cases showed over-triage. For people already diagnosed with angina, the Angina page gives separate advice, so this rule does not apply to them. | "Chest pain comes and goes" AND NOT "Diagnosed with angina" AND ("Pain comes on with activity, stress or cold, and eases with rest" OR "Chest feels tight or squeezed" OR "Smokes, or has high blood pressure, diabetes or high cholesterol") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Angina](https://www.nhs.uk/conditions/angina/) | |
| `rf_cp_palpitations`<br>Chest pain with the heart racing, going too slowly, skipping a beat or fluttering | "Heart racing, slow, skipping or fluttering" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_cp_coughing_up_blood`<br>Chest pain and coughing up blood | "Coughing up blood" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_cp_worse_breathing_in`<br>Chest pain that is worse when breathing in<br>**Note:** AI interpretation, needs clinical review. The Pulmonary embolism page lists this as a symptom and says its symptoms need urgent medical help. That page's own action list says to call 999 or go to A&E for pain in the chest, so 'urgent' may be too low. The Chest pain page links this symptom to a chest strain or chest infection and gives no urgency, so 'urgent' may also be too high. | "Chest pain worse when breathing in" | Urgent (help today)<br>Urgent care<br>Today<br>*Urgent medical help* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_cp_leg_pain_or_swelling`<br>Chest pain with pain or swelling in one leg<br>**Note:** The Shortness of breath page says to contact 111 for pain or swelling in one leg. The Pulmonary embolism page lists it as a sign of a blood clot. Applying it to chest pain without breathlessness is AI interpretation, needs clinical review. | "Pain or swelling in one leg" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact NHS 111* | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| `rf_cp_sharp_or_stabbing`<br>Chest pain that is sharp or stabbing<br>**Note:** Added in the chest and breathing pilot. The Costochondritis page also says to get help from 111 for sharp chest pain, to rule out more serious causes. | "Chest pain is sharp or stabbing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pericarditis](https://www.nhs.uk/conditions/pericarditis/) | |
| `rf_cp_better_leaning_forward`<br>Chest pain that eases when leaning forward and is worse lying down<br>**Note:** Added in the chest and breathing pilot. A sign of swelling of the lining around the heart (pericarditis). | "Chest pain eases when leaning forward, and is worse lying down" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pericarditis](https://www.nhs.uk/conditions/pericarditis/) | |
| `rf_cp_shingles_eye_or_vision`<br>A rash or painful patch on one side, on or near the eye or nose, or with changes to vision (possible shingles)<br>**Note:** The Shingles page says an urgent GP appointment or 111 if the rash is on your eye or nose, or you have changes to your vision. Added in the breathing batch after test-case authors found no question for it. | "Tingling, pain or a rash of blisters on one side of the body" AND "Shingles rash on or near the eye or nose, or changes to vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Shingles](https://www.nhs.uk/conditions/shingles/) | |

## Chest pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Chest pain where no rule for a more urgent outcome applies: get medical advice to make sure it is nothing serious**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Chest pain](https://www.nhs.uk/symptoms/chest-pain/)
- **Note:** Only reached when the pain is not there now and no red flag applies. The NHS website labels 'See a GP' as non-urgent, so mapping it to 'routine' and not 'soon' is AI judgement. The Angina page says to see a GP 'as soon as possible'.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Sudden chest pain that does not go away | Did the pain or discomfort in your chest come on suddenly, and has it not gone away? It can feel like squeezing, pressure, burning or indigestion. |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Chest feels tight or squeezed | Does your chest feel tight, or like it is being squeezed? | 23924001 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Chest feels heavy | Does your chest feel heavy? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Pain spreads to arm, neck, jaw, shoulder, stomach or back | Does the pain spread to your left or right arm, or to your neck, jaw, shoulder, stomach or back? | 10000006 | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Feels sweaty | Do you feel sweaty? | 415690000 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Chest pain is there now | Is the pain or discomfort in your chest there right now? |  | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Diagnosed with angina | Has a doctor told you that you have angina? Angina is chest pain caused by narrowed blood vessels to the heart. | 194828000 | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Pain not stopped by rest or angina medicine | Is the chest pain still there after a few minutes of rest? Or after you take your angina medicine? |  | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Sudden severe chest or back pain, like something tearing | Did severe pain in your chest or back start suddenly, and feel like something is tearing inside? |  | [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | |
| Sudden chest pain that lasted 15 minutes or more, even if it has stopped | Did the chest pain come on suddenly and last for 15 minutes or more? Answer yes even if it has stopped now. |  | [Pleurisy](https://www.nhs.uk/conditions/pleurisy/) | |
| Angina worse than before | Is your angina worse than before? For example, it happens more often, lasts longer or happens when you are resting. |  | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Chest pain comes and goes | Does the chest pain come and go? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Pain comes on with activity, stress or cold, and eases with rest | Does the pain come on when you are active, stressed or cold, and ease when you rest? |  | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Smokes, or has high blood pressure, diabetes or high cholesterol | Do you smoke, or have high blood pressure, diabetes or high cholesterol? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heart racing, slow, skipping or fluttering | Does your heart feel like it is racing, going too slowly, skipping a beat or fluttering? | 80313002 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Coughing up blood | Are you coughing up blood? | 66857006 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Chest pain worse when breathing in | Is the chest pain worse when you breathe in? | 2237002 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Pain or swelling in one leg | Do you have pain or swelling in one of your legs? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Chest pain is sharp or stabbing | Is the chest pain sharp or stabbing? |  | [Pericarditis](https://www.nhs.uk/conditions/pericarditis/) | |
| Chest pain eases when leaning forward, and is worse lying down | Does the chest pain get better when you sit up and lean forward? Is it worse when you lie down? |  | [Pericarditis](https://www.nhs.uk/conditions/pericarditis/) | |
| Tingling, pain or a rash of blisters on one side of the body | Do you have a tingling or painful patch of skin, or a rash of blisters, on one side of your body only? |  | [Shingles](https://www.nhs.uk/conditions/shingles/) | |
| Shingles rash on or near the eye or nose, or changes to vision | Is the rash or painful patch on or near your eye or nose? Or have you noticed any changes to your vision? |  | [Shingles](https://www.nhs.uk/conditions/shingles/) | |

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

### `advice_chest_pain_ae`

**What to do:** Call 999 or go to A&E now. This could be a sign of a serious condition.

**Look out for:**
- Pain that spreads to your arm, neck, jaw, stomach or back
- Your chest feeling tight or squeezed
- Feeling sweaty, sick, light-headed or short of breath
- Difficulty breathing that comes on suddenly, or passing out

**Get more help when:**
- Call 999 straight away if you get any of the signs above. You could be having a heart attack.
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/)

### `advice_chest_pain_angina_urgent`

**What to do:** Get help from NHS 111 today, because your angina (chest pain caused by narrowed blood vessels to the heart) is worse than usual. You can call 111 or use 111 online.

**Look out for:**
- Chest pain that does not stop after a few minutes of rest. Or that does not stop after you take your angina medicine.
- Sudden pain or discomfort in your chest that does not go away
- Pain that spreads to your arm, neck, jaw, shoulder, stomach or back
- Chest pain with feeling sweaty, sick, light-headed or short of breath

**Get more help when:**
- Call 999 now if you get any of the signs above. You could be having a heart attack.

**Where to go:** Call 111 or use 111 online today. Call 999 if you get any of the signs above. Do not drive yourself to A&E.

**What you can do yourself:**
- If you get chest pain, stop what you are doing and rest
- Use the angina medicine you have been prescribed. This is usually a spray you use under your tongue. Take another dose after 5 minutes if the first dose does not help.
- If you still have symptoms 5 minutes after the second dose, call 999 for an ambulance

Source: [Angina](https://www.nhs.uk/conditions/angina/)

### `advice_chest_pain_urgent`

**What to do:** Get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Sudden pain or discomfort in your chest that does not go away
- Chest pain that feels tight or like squeezing
- Pain that spreads to your arm, neck, jaw, stomach or back
- Chest pain with feeling sweaty, sick, light-headed or short of breath

**Get more help when:**
- Call 999 straight away if you get any of the signs above. You could be having a heart attack.
- Call 999 or go to A&E if the chest pain comes back and does not go away. Do the same if your heart beats very fast, you suddenly find it hard to breathe, or you pass out.

**Where to go:** Call 111 or use 111 online today. Call 999 if you get any of the signs above.

Source: [Angina](https://www.nhs.uk/conditions/angina/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/)

### `advice_chest_pain_urgent_gp_or_111`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Difficulty breathing that comes on suddenly
- Your heart beating very fast
- Passing out
- Sudden chest pain that does not go away, feels tight or like squeezing, or spreads to your arm, neck, jaw, stomach or back

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 999 or go to A&E if you get any of the signs above. Do not drive to A&E.

Source: [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/)

### `advice_shingles_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Shingles near the eye or nose, or with changes to your vision, needs checking quickly to protect your sight.

**Look out for:**
- Your eye becoming more red or painful
- Your vision getting worse
- The rash spreading, or you feeling very unwell

**Get more help when:**
- Medicine for shingles works best if you start it within 3 days of the rash appearing
- Call 999 if you get sudden chest pain. Call 999 if pain spreads to your arm, neck, jaw or back.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Take paracetamol to help with the pain
- Keep the rash clean and dry, and wear loose clothing
- Do not share towels. Keep away from babies and people who are pregnant until the blisters dry.

Source: [Shingles](https://www.nhs.uk/conditions/shingles/)

### `advice_chest_pain_gp`

**What to do:** See a GP. Most chest pain is not a sign of anything serious, but get medical advice to make sure.

**Look out for:**
- Sudden pain or discomfort in your chest that does not go away
- Chest pain that feels tight or like squeezing
- Pain that spreads to your arm, neck, jaw, stomach or back
- Chest pain with feeling sweaty, sick, light-headed or short of breath

**Get more help when:**
- Call 999 straight away if you get any of the signs above. You could be having a heart attack.
- Call 999 or go to A&E if the chest pain comes back and does not go away. Do the same if your heart beats very fast, you suddenly find it hard to breathe, or you pass out.
- Get help from NHS 111 if the chest pain keeps coming and going

**Where to go:** Make an appointment with a GP. Call 999 if you get any of the signs above.

Source: [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Angina](https://www.nhs.uk/conditions/angina/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cp_heavy`: The source lists a chest that feels 'tight or heavy' for people who are short of breath. Applying it to chest pain is AI judgement, needs clinical review. Added after a development test case showed the question list could not express it.
- `rf_cp_spreads`: The Chest pain page gives the same advice without naming the shoulder.
- `rf_cp_with_sweating_sickness_or_breathlessness`: Source difference: the Heart attack page says to call 111 for chest pain with feeling or being sick. The Chest pain page says 999. The more urgent is used.
- `rf_cp_heart_beating_very_fast`: Source difference: the Heart attack page says to call 111 for chest pain with a racing heart. The Pulmonary embolism page says 999 or A&E for a heart beating very fast. The more urgent is used.
- `rf_cp_present_now`: Pragmatic resolution of a source difference, needs clinical review. The Pulmonary embolism page says to call 999 or go to A&E if 'you feel pain in your chest or upper back'. The Chest pain page says to see a GP for pain that comes and goes or has gone away. Both are followed: pain that is there now is an emergency, and pain that has stopped uses the Chest pain page. This will over-triage some people, for example someone with a pulled muscle that still hurts.
- `rf_cp_tearing_to_back`: Added in the chest and breathing pilot. The Costochondritis page says call 999 for sudden chest or back pain that feels like something being torn inside. Clinically this is a sign of a tear in the body's main blood vessel (aortic dissection), which can be fatal within hours.
- `rf_cp_lasted_15_minutes`: The Pleurisy page says call 999 or go to A&E for sudden chest pain that lasts for 15 minutes or more, which could be a heart attack or a blood clot in the lung. Asking about it even if the pain has stopped is AI judgement. Kept firm, not soft: angina that lasts this long may be a heart attack, so likely angina must not lower it. This will over-triage some chest wall pain that came on suddenly. Added in the breathing batch after test-case authors found no question for it. Needs clinical review.
- `rf_cp_comes_and_goes`: Source difference: the Chest pain page says to see a GP (non-urgent) for chest pain that comes and goes. The Angina page says to get help from 111. The more urgent is used when the pain looks like angina (AI judgement: brought on by activity, tight or squeezing, or with heart risk factors); other chest pain that comes and goes falls to the default, see a GP, as the Chest pain page says. Narrowed after development cases showed over-triage. For people already diagnosed with angina, the Angina page gives separate advice, so this rule does not apply to them.
- `rf_cp_worse_breathing_in`: AI interpretation, needs clinical review. The Pulmonary embolism page lists this as a symptom and says its symptoms need urgent medical help. That page's own action list says to call 999 or go to A&E for pain in the chest, so 'urgent' may be too low. The Chest pain page links this symptom to a chest strain or chest infection and gives no urgency, so 'urgent' may also be too high.
- `rf_cp_leg_pain_or_swelling`: The Shortness of breath page says to contact 111 for pain or swelling in one leg. The Pulmonary embolism page lists it as a sign of a blood clot. Applying it to chest pain without breathlessness is AI interpretation, needs clinical review.
- `rf_cp_sharp_or_stabbing`: Added in the chest and breathing pilot. The Costochondritis page also says to get help from 111 for sharp chest pain, to rule out more serious causes.
- `rf_cp_better_leaning_forward`: Added in the chest and breathing pilot. A sign of swelling of the lining around the heart (pericarditis).
- `rf_cp_shingles_eye_or_vision`: The Shingles page says an urgent GP appointment or 111 if the rash is on your eye or nose, or you have changes to your vision. Added in the breathing batch after test-case authors found no question for it.
- `chest_pain default outcome`: Only reached when the pain is not there now and no red flag applies. The NHS website labels 'See a GP' as non-urgent, so mapping it to 'routine' and not 'soon' is AI judgement. The Angina page says to see a GP 'as soon as possible'.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Chest infection that may need treatment from a GP | 50417007 | common | Cough: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Coughing up phlegm: strongly supports; Yellow or green phlegm: strongly supports; Symptoms getting worse, or not getting better after about a week: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Very high temperature, or feels hot, cold or shivery: supports; Chest pain worse when breathing in: supports; Short of breath: supports |
| Pleurisy (swelling of the lining around the lungs) | 196075003 | rare | Chest pain worse when breathing in: strongly supports; Chest pain is sharp or stabbing: strongly supports; Chest pain is there now: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Cough: supports; Very high temperature, or feels hot, cold or shivery: supports; Pain in the upper back: supports |
| Collapsed lung (pneumothorax) | 36118008 | rare | Breathlessness came on suddenly, or suddenly got much worse: strongly supports; Chest pain is sharp or stabbing: strongly supports; Chest pain worse when breathing in: strongly supports; Short of breath: strongly supports; Chest pain is there now: supports; Heart beating very fast: supports; Smokes, or has smoked in the past: supports |
| Angina (chest pain caused by narrowed blood vessels to the heart) | 194828000 | uncommon | Pain comes on with activity, stress or cold, and eases with rest: strongly supports; Chest pain comes and goes: strongly supports; Chest feels tight or squeezed: supports; Chest feels heavy: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: supports; Short of breath: supports; Angina worse than before: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Close relative had a heart attack or angina before 60: supports; Chest pain worse when breathing in: argues against; Chest hurts more when pressed: argues against |
| Anxiety or panic attack | 48694002 | common | Sudden rush of intense fear or panic: strongly supports; Pain triggered by worry or stress: strongly supports; Tingling or pins and needles in the fingers or around the mouth: supports; Breathing very fast: supports; Heart beating very fast: supports; Heart racing, slow, skipping or fluttering: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Short of breath: supports |
| A tear in the body's main blood vessel (aortic dissection) | 308546005 | rare | Sudden severe chest or back pain, like something tearing: strongly supports; Pain in the upper back: strongly supports; Sudden chest pain that does not go away: strongly supports; Chest pain is there now: strongly supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Feels sweaty: supports |
| Irregular heartbeat (atrial fibrillation) | 49436004 | rare | Heart racing, slow, skipping or fluttering: strongly supports; Heartbeat feels irregular, with no steady rhythm: strongly supports; Each episode lasts longer than a few minutes: supports; Heart racing, pounding or fluttering right now: supports; Heart beating very fast: supports; Short of breath: supports; Feels very tired: supports |
| Chest sprain or strain, or costochondritis (swelling where the ribs join the breastbone) | 281245003 | common | Pain started after a chest injury or exercise: strongly supports; Chest hurts more when pressed: supports; Chest pain worse when breathing in: supports; Chest pain is sharp or stabbing: supports; Chest pain is there now: supports; Feels sweaty: argues against; Feels sick or has been sick: argues against; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Pain starts after eating: argues against |
| Heart attack | 22298006 | very rare | Chest feels tight or squeezed: strongly supports; Sudden chest pain that does not go away: strongly supports; Chest feels heavy: supports; Chest pain is there now: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feels light-headed: supports; Short of breath: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Close relative had a heart attack or angina before 60: supports; Chest pain worse when breathing in: argues against; Chest hurts more when pressed: argues against |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Swelling of the heart muscle (myocarditis) | 50920009 | rare | Cold, flu, COVID-19 or a similar illness in the last few weeks: strongly supports; Short of breath: supports; Heart racing, slow, skipping or fluttering: supports; Heart beating very fast: supports; Feels very tired: supports; Out of breath doing everyday things: supports; Chest pain is there now: strongly supports |
| Swelling of the lining around the heart (pericarditis) | 3238004 | rare | Chest pain eases when leaning forward, and is worse lying down: strongly supports; Chest pain is sharp or stabbing: strongly supports; Chest pain worse when breathing in: strongly supports; Chest pain is there now: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Very high temperature, or feels hot, cold or shivery: supports; Pain comes on with activity, stress or cold, and eases with rest: argues against |
| Blood clot in the lung (pulmonary embolism) | 59282003 | rare | Short of breath: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: strongly supports; Chest pain worse when breathing in: strongly supports; Breathing very fast: supports; Heart beating very fast: supports; Pain or swelling in one leg: supports; Coughing up blood: supports; Chest pain is there now: strongly supports |
| Shingles (an infection that causes a painful rash on one side of the body) | 4740000 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Chest pain is there now: supports; Chest pain is sharp or stabbing: supports; Pain in the upper back: supports; Blisters or fluid-filled spots: supports; Shingles rash on or near the eye or nose, or changes to vision: supports; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
