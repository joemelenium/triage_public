# Review pack: Blood in urine

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
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | 2026-11-19 |  | Page last reviewed: 19 February 2024 |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Kidney stones](https://www.nhs.uk/conditions/kidney-stones/) | 2026-11-19 |  | Page last reviewed: 17 September 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [When to go to A&E](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-go-to-ae/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Bladder cancer: symptoms](https://www.nhs.uk/conditions/bladder-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 15 April 2025 |

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

## Blood in urine red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_biu_drowsy`<br>Blood in pee and very drowsy, hard to wake or finding it hard to speak<br>**Note:** The UTI and Kidney infection pages say call 999 or go to A&E for being confused, drowsy or having difficulty speaking. Sudden confusion is in the universal red flags. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_biu_sepsis_skin`<br>Blood in pee with blotchy skin, or a rash that does not fade when pressed: possible sepsis<br>**Note:** The Prostatitis page lists these as 999 signs of a serious infection or sepsis. The Sepsis page gives the same advice. | "Blotchy or mottled skin" OR "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |
| `rf_biu_injury`<br>Blood in pee after an injury or hard blow to the back, side, tummy or groin<br>**Note:** Clinical knowledge: blood in the pee after an injury can mean the kidney or bladder is damaged, which needs checking in hospital. No NHS page in the source log covers this. | "Started after an injury to the back, side, tummy or groin" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_biu_cannot_pee`<br>Blood in pee, and a painful or swollen lower tummy with a strong need to pee but unable to<br>**Note:** Clinical knowledge: blood clots can block the bladder. A full, painful bladder needs a tube (catheter) put in at hospital. The unable to pee entry symptom also applies. | "Lower tummy painful or swollen, and badly needs to pee but cannot" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_biu_clots_on_blood_thinners`<br>Blood clots or a lot of blood in the pee in someone taking medicine to thin the blood<br>**Note:** Clinical knowledge: heavy bleeding while on blood thinners may need the blood checked and treated the same day in hospital. Needs clinical review. | "Blood clots in pee, or very red pee" AND "Takes medicine that thins the blood, or bleeds easily" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_biu_stone_with_temperature`<br>Severe pain in the side that comes in waves, with a high temperature or shivering: possible blocked, infected kidney<br>**Note:** Source difference: the Kidney stones page says an urgent GP appointment or 111 for severe pain or a high temperature. Clinical knowledge: a stone blocking an infected kidney needs hospital treatment the same day. The more urgent is used, marked soft. | "Severe pain in the side or back that comes in waves" AND "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Blood in urine: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Blood in pee, or thinks there may be: get it checked today**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/)
- **Note:** The Bladder cancer page gives the same advice: an urgent GP appointment even if it is the first time, a small amount, or you are not sure.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Started after an injury to the back, side, tummy or groin | Did this start after an injury or a hard blow to your back, side, tummy or groin? |  | **AI judgement, needs clinical review** | |
| Lower tummy painful or swollen, and badly needs to pee but cannot | Is your lower tummy painful or swollen, and do you badly need to pee but cannot? |  | **AI judgement, needs clinical review** | |
| Blood clots in pee, or very red pee | Are there blood clots in your pee, or is your pee very red, like it is full of blood? |  | **AI judgement, needs clinical review** | |
| Takes medicine that thins the blood, or bleeds easily | Do you take medicine that thins your blood, such as warfarin, apixaban or rivaroxaban? Or do you have a condition that makes you bleed more easily? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Severe pain in the side or back that comes in waves | Is the pain in your side or back severe, and does it come in waves so that you cannot keep still? | 7093002 | [Kidney stones](https://www.nhs.uk/conditions/kidney-stones/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

### `advice_blood_in_urine_ae`

**What to do:** Go to A&E now, or call 999. Blood in your pee after an injury, or a lot of blood while you take blood thinners, needs checking in hospital.

**Look out for:**
- Feeling faint, dizzy or very pale
- Not being able to pee
- Pain in your back, side or tummy getting worse

**Get more help when:**
- Call 999 if you faint, feel very unwell, or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/), [When to go to A&E](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-go-to-ae/)

### `advice_cannot_pee_ae`

**What to do:** Go to A&E now. A full bladder that you cannot empty is very painful and needs a thin tube (catheter) put in to drain it.

**Look out for:**
- Pain or swelling in your lower tummy getting worse
- A high temperature, or feeling hot, cold or shivery
- Feeling confused or very drowsy

**Get more help when:**
- Call 999 if you feel very unwell, confused or drowsy, or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/), [Prostatitis](https://www.nhs.uk/conditions/prostatitis/)

### `advice_kidney_pain_ae`

**What to do:** Go to A&E now, or call 999. Severe pain in your side with a high temperature can mean a kidney stone is blocking an infected kidney. This needs treatment in hospital today.

**Look out for:**
- Feeling confused or very drowsy
- Shivering, or feeling very cold
- Being sick and not able to keep fluids down

**Get more help when:**
- Call 999 if you feel very unwell, confused or drowsy, or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Kidney stones](https://www.nhs.uk/conditions/kidney-stones/), [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/)

### `advice_blood_in_urine_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Blood in your pee is not usually serious, but it must be checked, even if there is only a little or you are not sure it is blood.

**Look out for:**
- Not being able to pee
- Severe pain in your side, back or tummy
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Go to A&E if you cannot pee and your tummy is painful or swollen
- Call 999 or go to A&E if you feel confused, very drowsy or find it hard to speak

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Take a sample of your pee if you can.

**What you can do yourself:**
- Drink plenty of water
- Beetroot or some medicines can turn pee pink or red. Still get it checked if you are not sure.

Source: [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/), [Bladder cancer: symptoms](https://www.nhs.uk/conditions/bladder-cancer/symptoms/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_biu_drowsy`: The UTI and Kidney infection pages say call 999 or go to A&E for being confused, drowsy or having difficulty speaking. Sudden confusion is in the universal red flags.
- `rf_biu_sepsis_skin`: The Prostatitis page lists these as 999 signs of a serious infection or sepsis. The Sepsis page gives the same advice.
- `rf_biu_injury`: Clinical knowledge: blood in the pee after an injury can mean the kidney or bladder is damaged, which needs checking in hospital. No NHS page in the source log covers this.
- `rf_biu_cannot_pee`: Clinical knowledge: blood clots can block the bladder. A full, painful bladder needs a tube (catheter) put in at hospital. The unable to pee entry symptom also applies.
- `rf_biu_clots_on_blood_thinners`: Clinical knowledge: heavy bleeding while on blood thinners may need the blood checked and treated the same day in hospital. Needs clinical review.
- `rf_biu_stone_with_temperature`: Source difference: the Kidney stones page says an urgent GP appointment or 111 for severe pain or a high temperature. Clinical knowledge: a stone blocking an infected kidney needs hospital treatment the same day. The more urgent is used, marked soft.
- `blood_in_urine default outcome`: The Bladder cancer page gives the same advice: an urgent GP appointment even if it is the first time, a small amount, or you are not sure.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sudden inability to empty the bladder (urinary retention) | 236648008 | common | Lower tummy painful or swollen, and badly needs to pee but cannot: strongly supports; Not able to pee at all for several hours: strongly supports; Hard to start peeing, or a weak or stop-start flow: supports; Pain low down in the tummy, below the belly button: supports; Started a new medicine or changed a dose in the last few weeks: supports; Constipation: supports |
| Bladder cancer | 399326009 | rare | Blood in pee with no pain: strongly supports; Smokes, or has smoked in the past: supports; Blood clots in pee, or very red pee: supports; Losing weight without trying: supports; Feels very tired: supports; Keeps getting urine infections: supports |
| Enlarged prostate | 266569009 | uncommon | Hard to start peeing, or a weak or stop-start flow: strongly supports; Bladder does not feel empty after peeing, or dribbling afterwards: strongly supports; Getting up in the night to pee: strongly supports; Peeing problems for months or longer: supports; Peeing more often than usual: supports |
| Swelling inside the kidneys (glomerulonephritis) | 36171008 | rare | Very frothy or foamy pee: strongly supports; Puffy face or eyes: strongly supports; Swollen feet, ankles or legs: supports; Sore throat or skin infection in the last few weeks: supports; Making much less pee than usual: supports |
| Kidney cancer | 363518003 | rare | Lump or swelling in the back or side: strongly supports; Pain in the back or side, just under the ribs: supports; Losing weight without trying: supports; Night sweats: supports; Feels very tired: supports; Blood in pee with no pain: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |
| Pee changed for a harmless reason, such as food, a medicine or a period |  | common | Recently had food, drink or medicine that can change pee: strongly supports; Started a new medicine or changed a dose in the last few weeks: supports; On a period, or bleeding from the vagina: supports |
| Prostate cancer | 399068003 | very rare | Hard to start peeing, or a weak or stop-start flow: supports; Getting up in the night to pee: supports; Losing weight without trying: strongly supports; Back pain: supports; Blood in semen: supports; Blood in pee: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
