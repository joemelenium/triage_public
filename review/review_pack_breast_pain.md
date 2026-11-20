# Review pack: Breast pain

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
| [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | 2026-11-19 |  | Page last reviewed: 23 October 2026 |
| [Breast abscess](https://www.nhs.uk/conditions/breast-abscess/) | 2026-11-19 |  | Page last reviewed: 14 June 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Breast lumps](https://www.nhs.uk/symptoms/breast-lump/) | 2026-11-19 |  | Page last reviewed: 10 November 2026 |
| [Breast cancer in women: symptoms](https://www.nhs.uk/conditions/breast-cancer-in-women/symptoms-of-breast-cancer-in-women/) | 2026-11-19 |  | Page last reviewed: 4 March 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Mastitis](https://www.nhs.uk/conditions/mastitis/) | 2026-11-19 |  | Page last reviewed: 17 March 2023 |

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

## Breast pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bp_high_temperature`<br>Breast pain with a very high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `rf_bp_hot_red_swollen`<br>Any part of the breast hot, swollen or a different colour | "Part of the breast is hot, swollen or a different colour" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `rf_bp_very_unwell`<br>Breast pain with feeling very unwell | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Breast abscess](https://www.nhs.uk/conditions/breast-abscess/) | |

## Breast pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bp_breast_changes`<br>Breast pain with a lump, swelling, nipple changes or dimpled skin | "Lump or swelling in the breast, chest or armpit" OR "Skin on the breast is dimpled, like orange peel" OR "Nipple has turned inwards or has a rash" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `or_bp_not_improving`<br>Breast pain that is not improving, or painkillers are not helping | "Breast pain not improving, or painkillers not helping" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `or_bp_family_history`<br>Breast pain with a family history of breast cancer<br>**Note:** The Breast cancer symptoms page also says see a GP for breast pain when relatives have had breast or ovarian cancer. | "A close relative has had breast or ovarian cancer" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `or_bp_new_or_different`<br>Breast pain that is new or different | "Breast pain is new or different" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| `or_bp_worried`<br>Breast pain and worried about it | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |

## Default outcome

Used when no rule fires.

- **Breast pain: it is best to get it checked, but pain clearly linked to periods can be eased at home**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Breast pain](https://www.nhs.uk/symptoms/breast-pain/)
- **Note:** The page says breast pain is not usually serious, but it is best to get it checked. Not a floor: pain clearly linked to periods, or to a strain, can lower this to self-care.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Breast pain | Do you have pain in one or both breasts? | 53430007 | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Part of the breast is hot, swollen or a different colour | Is any part of your breast hot, swollen or a different colour? On black or brown skin it may look darker than usual. On white skin it may look red. |  | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Lump or swelling in the breast, chest or armpit | Do you have a lump or swelling in your breast, chest or armpit? | 89164003 | [Breast lumps](https://www.nhs.uk/symptoms/breast-lump/) | |
| Skin on the breast is dimpled, like orange peel | Is the skin on your breast dimpled, like orange peel? |  | [Breast cancer in women: symptoms](https://www.nhs.uk/conditions/breast-cancer-in-women/symptoms-of-breast-cancer-in-women/) | |
| Nipple has turned inwards or has a rash | Has your nipple changed? For example, it has turned inwards, or there is a rash on it. |  | [Breast cancer in women: symptoms](https://www.nhs.uk/conditions/breast-cancer-in-women/symptoms-of-breast-cancer-in-women/) | |
| Breast pain not improving, or painkillers not helping | Is the breast pain not getting better, or are painkillers not helping? |  | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| A close relative has had breast or ovarian cancer | Has a close relative had breast cancer or ovarian cancer? For example, a parent, brother or sister. |  | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| Breast pain is new or different | Is the breast pain new for you, or different from breast pain you have had before? |  | [Breast pain](https://www.nhs.uk/symptoms/breast-pain/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_breast_infection_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A hot, swollen or red breast, or a high temperature, can be a breast infection that needs treatment.

**Look out for:**
- Feeling very unwell, or getting worse
- A painful lump that is getting bigger

**Get more help when:**
- Go back to the GP if you are not getting better within 2 days of starting antibiotics
- Call 999 or go to A&E if you feel very unwell, confused or faint

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- If you are breastfeeding, keep feeding your baby, including from the sore breast
- Take paracetamol or ibuprofen for pain. They also help bring a high temperature down.
- Rest and drink plenty of fluids

Source: [Breast pain](https://www.nhs.uk/symptoms/breast-pain/), [Mastitis](https://www.nhs.uk/conditions/mastitis/), [Breast abscess](https://www.nhs.uk/conditions/breast-abscess/)

### `advice_breast_pain_gp`

**What to do:** See a GP about your breast pain. It is not usually anything serious, but it is best to get it checked.

**Look out for:**
- A lump, swelling or change to your nipple
- Dimpled skin on your breast
- Any part of your breast becoming hot, swollen or red
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your breast gets hot, red or swollen. Or if you get a high temperature.

**Where to go:** Ask your GP surgery for an appointment. The source gives no fixed time.

**What you can do yourself:**
- Take paracetamol or ibuprofen. Or rub a painkilling gel on your breast.
- Wear a well-fitting bra in the day and a soft bra at night

Source: [Breast pain](https://www.nhs.uk/symptoms/breast-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `or_bp_family_history`: The Breast cancer symptoms page also says see a GP for breast pain when relatives have had breast or ovarian cancer.
- `breast_pain default outcome`: The page says breast pain is not usually serious, but it is best to get it checked. Not a floor: pain clearly linked to periods, or to a strain, can lower this to self-care.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A harmless breast lump, such as a fibroadenoma (a non-cancerous growth) or a breast cyst (a sac of fluid) |  | rare | The lump is smooth and rubbery, and moves easily: strongly supports; Lump or swelling in the breast, chest or armpit: strongly supports; The lump gets bigger or more tender before a period: supports; Breast pain: supports; Nipple discharge: supports |
| Breast abscess (a pocket of pus in the breast) | 28432003 | rare | Part of the breast is hot, swollen or a different colour: strongly supports; Lump or swelling in the breast, chest or armpit: strongly supports; Breast pain: strongly supports; Had a breast infection (mastitis) in the last few weeks: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Breastfeeding: supports |
| Breast cancer | 254837009 | uncommon | The lump feels hard, or seems stuck in place: strongly supports; Lump or swelling in the breast, chest or armpit: strongly supports; Skin on the breast is dimpled, like orange peel: supports; Nipple has turned inwards or has a rash: supports; Nipple discharge with blood in it: supports |
| Breast pain from a strained muscle, the chest wall or a badly fitting bra | 237454007 | common | Pain in one spot, worse when moving the arm or pressing: strongly supports; Breast pain started after an injury, lifting, exercise or a badly fitting bra: strongly supports |
| Breast pain linked to periods | 237453001 | uncommon | Breast pain starts before a period and goes when it ends: strongly supports; Breast pain: strongly supports; Pain in both breasts: supports; The lump gets bigger or more tender before a period: supports; Takes the combined pill or HRT: supports |
| Pregnancy | 77386006 | rare | Pregnant, or could be pregnant: strongly supports; Missed or late period: strongly supports; Feels sick or has been sick: supports; Breast pain: supports; Feels very tired: supports; Peeing more often than usual: supports |
| Breast swelling in men (gynaecomastia) | 4754008 | uncommon | Rubbery swelling just behind the nipple: strongly supports; Lump or swelling in the breast, chest or armpit: strongly supports; Breast pain: supports; Pain in both breasts: supports |
| Breast infection or inflammation (mastitis) | 82789004 | uncommon | Part of the breast is hot, swollen or a different colour: strongly supports; Breast pain: strongly supports; Breastfeeding: supports; Very high temperature, or feels hot, cold or shivery: supports; Aching body: supports; Nipple discharge: supports; Lump or swelling in the breast, chest or armpit: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
