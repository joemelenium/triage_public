# Review pack: Unable to pee

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
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | 2026-11-19 |  | Page last reviewed: 19 February 2024 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | 2026-11-19 |  | Page last reviewed: 15 August 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |

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

## Unable to pee red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cp_full_painful_bladder`<br>A painful or swollen lower tummy and a strong need to pee, but unable to<br>**Note:** Source difference: the Prostate enlargement and Prostatitis pages say an urgent GP appointment or 111 if you cannot pee. Clinical knowledge: a full, painful bladder (acute urinary retention) needs a tube (catheter) put in within hours, which is usually done at A&E. The more urgent is used. Needs clinical review. | "Lower tummy painful or swollen, and badly needs to pee but cannot" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_cp_nerve_signs`<br>Unable to pee, with numbness around the genitals or bottom, or new weakness or numbness in both legs: possible cauda equina syndrome<br>**Note:** The Back pain page gives these with back pain. Applying them without back pain is AI judgement, since the nerve signs matter most. | "Numb or no feeling around the genitals or bottom" OR "Numbness or weakness in both legs" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_cp_back_pain_bowels`<br>Back pain with being unable to pee and pooing without meaning to | "Back pain" AND "Cannot control when you poo" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_cp_back_pain`<br>Back pain with difficulty peeing<br>**Note:** The Back pain page says call 999 or go to A&E for back pain with difficulty peeing. Marked soft: back ache is common in older men who cannot pee because of an enlarged prostate. Cauda equina syndrome keeps the outcome high while it is possible. | "Back pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_cp_drowsy`<br>Unable to pee and very drowsy, hard to wake or finding it hard to speak | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_cp_sepsis_skin`<br>Unable to pee with blotchy skin: possible sepsis | "Blotchy or mottled skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |

## Unable to pee: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Unable to pee, or only a few drops: get help today**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111 now*
- Source: [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/)
- **Note:** The Prostatitis page gives the same advice for being unable to pee.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Unable to pee | Are you unable to pee, or can you only pass a few drops, even though you need to go? | 102835006 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lower tummy painful or swollen, and badly needs to pee but cannot | Is your lower tummy painful or swollen, and do you badly need to pee but cannot? |  | **AI judgement, needs clinical review** | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Back pain | Do you have back pain? | 161891005 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Cannot control when you poo | Are you unable to control when you poo? For example, poo leaks out, or you cannot get to the toilet in time. | 72042002 | [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

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

### `advice_back_nerves_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs that the nerves at the bottom of the spine are being squashed (cauda equina syndrome). This needs treatment in hospital straight away to prevent lasting damage.

**Look out for:**
- Numbness around your genitals or bottom getting worse
- Not being able to pee, or leaking pee or poo
- Weakness in your legs getting worse

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

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

### `advice_cannot_pee_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 now. Not being able to pee needs checking today.

**Look out for:**
- Pain or swelling in your lower tummy
- A high temperature, or feeling hot, cold or shivery
- Numbness around your genitals or bottom, or weakness in your legs

**Get more help when:**
- Go to A&E if your lower tummy becomes painful or swollen and you still cannot pee
- Call 999 or go to A&E if you get numbness around your genitals or bottom, or weakness in both legs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Try sitting in a warm bath and relaxing to see if you can pee

Source: [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/), [Prostatitis](https://www.nhs.uk/conditions/prostatitis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cp_full_painful_bladder`: Source difference: the Prostate enlargement and Prostatitis pages say an urgent GP appointment or 111 if you cannot pee. Clinical knowledge: a full, painful bladder (acute urinary retention) needs a tube (catheter) put in within hours, which is usually done at A&E. The more urgent is used. Needs clinical review.
- `rf_cp_nerve_signs`: The Back pain page gives these with back pain. Applying them without back pain is AI judgement, since the nerve signs matter most.
- `rf_cp_back_pain`: The Back pain page says call 999 or go to A&E for back pain with difficulty peeing. Marked soft: back ache is common in older men who cannot pee because of an enlarged prostate. Cauda equina syndrome keeps the outcome high while it is possible.
- `cannot_pee default outcome`: The Prostatitis page gives the same advice for being unable to pee.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Mild dehydration (not having enough water in the body) |  | very common | Diarrhoea, or being sick: strongly supports; Feeling very thirsty all the time: strongly supports; Unwell after being in the heat or exercising hard: supports; Feels light-headed: supports; Signs of dehydration: strongly supports; Making much less pee than usual: supports; Feels sick or has been sick: supports; Feels very tired: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Kidneys suddenly not working well (kidney injury) | 14669001 | uncommon | Making much less pee than usual: strongly supports; Feels sick or has been sick: supports; Swollen feet, ankles or legs: supports; Feels very unwell: supports; Signs of dehydration: supports |
| Sudden inability to empty the bladder (urinary retention) | 236648008 | common | Lower tummy painful or swollen, and badly needs to pee but cannot: strongly supports; Not able to pee at all for several hours: strongly supports; Hard to start peeing, or a weak or stop-start flow: supports; Pain low down in the tummy, below the belly button: supports; Started a new medicine or changed a dose in the last few weeks: supports; Constipation: supports |
| Enlarged prostate | 266569009 | uncommon | Hard to start peeing, or a weak or stop-start flow: strongly supports; Bladder does not feel empty after peeing, or dribbling afterwards: strongly supports; Getting up in the night to pee: strongly supports; Peeing problems for months or longer: supports; Peeing more often than usual: supports |
| Prostate cancer | 399068003 | very rare | Hard to start peeing, or a weak or stop-start flow: supports; Getting up in the night to pee: supports; Losing weight without trying: strongly supports; Back pain: supports; Blood in semen: supports; Blood in pee: supports |
| Prostatitis (a swollen, painful prostate, usually from an infection) | 9713002 | rare | Pain between the testicles and bottom: strongly supports; Pain when ejaculating (coming): supports; Pain, burning or stinging when peeing: supports; Hard to start peeing, or a weak or stop-start flow: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels cold to the touch, or shivery: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
