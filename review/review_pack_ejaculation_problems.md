# Review pack: Ejaculation problems

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
| [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | 2026-11-19 |  | Page last reviewed: 19 February 2024 |
| [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | 2026-11-19 |  | Page last reviewed: 09 February 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
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

## Ejaculation problems red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ej_nerve_signs`<br>Problems coming, with numbness around the genitals or bottom, or new weakness or numbness in both legs: possible cauda equina syndrome<br>**Note:** The Back pain page lists not being able to orgasm with back pain and these signs as a reason to call 999 or go to A&E. | "Numb or no feeling around the genitals or bottom" OR "Numbness or weakness in both legs" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Ejaculation problems red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ej_painful_with_temperature`<br>Pain when coming, or pain when peeing, with a high temperature: possible prostatitis<br>**Note:** The Prostatitis page says it can be serious and needs urgent medical help. Using a high temperature to mark it is AI judgement. | "Very high temperature, or feels hot, cold or shivery" AND ("Pain when ejaculating (coming)" OR "Pain, burning or stinging when peeing") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |

## Ejaculation problems: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ej_keeps_happening`<br>A problem with coming that keeps happening and is bothering the person | "Ejaculation problem keeps happening" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |
| `or_ej_pain`<br>Pain when coming | "Pain when ejaculating (coming)" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |
| `or_ej_little_semen`<br>Little or no semen when coming: possible retrograde ejaculation | "Little or no semen, with cloudy pee afterwards" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |
| `or_ej_medicine`<br>Problems coming after starting or changing a medicine | "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Do not stop a prescribed medicine without talking to them.* | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |

## Default outcome

Used when no rule fires.

- **Problems coming now and then, with nothing else that needs help**
- Outcome: Self-manageable, Self-care, No appointment needed. *Problems now and then are common. See a GP if it keeps happening.*
- Source: [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Problems with ejaculating (coming) | Do you have problems with ejaculating (coming)? For example, coming too soon, taking a long time, or not at all. |  | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pain when ejaculating (coming) | Does it hurt when you ejaculate (come)? | 50818007 | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Ejaculation problem keeps happening | Does the problem with coming keep happening? Is it bothering you? |  | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |
| Little or no semen, with cloudy pee afterwards | When you come, is there little or no semen? Is your pee cloudy the first time you go afterwards? |  | [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |

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

### `advice_prostatitis_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You may have prostatitis, an infection of the prostate gland below the bladder. It can be serious and needs treatment soon.

**Look out for:**
- Not being able to pee
- Feeling very unwell, confused or drowsy
- Blotchy, blue or grey skin

**Get more help when:**
- Call 999 or go to A&E if you feel confused, your skin turns blotchy or grey, or you find it very hard to breathe. These can be signs of sepsis, a life-threatening reaction to an infection.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink plenty of fluids
- Take paracetamol or ibuprofen for pain

Source: [Prostatitis](https://www.nhs.uk/conditions/prostatitis/)

### `advice_ejaculation_gp`

**What to do:** See a GP. Problems with coming that keep happening can usually be helped.

**Look out for:**
- Pain when coming with a high temperature
- Blood in your semen or pee

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you have pain with a high temperature

**Where to go:** Make an appointment with a GP.

**What you can do yourself:**
- Do not stop a prescribed medicine without talking to a doctor
- Talk to your partner about it, if you have one

Source: [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/)

### `advice_ejaculation_self_care`

**What to do:** You can look after this yourself. Problems with coming now and then are common and are not a cause for concern.

**Look out for:**
- The problem keeps happening and bothers you
- Pain when coming

**Get more help when:**
- See a GP if it keeps happening or there is pain

**Where to go:** You do not need an appointment now. See a GP if it keeps happening.

**What you can do yourself:**
- Talk to your partner about it, if you have one
- Try to reduce stress, and cut down on alcohol

Source: [Ejaculation problems](https://www.nhs.uk/conditions/ejaculation-problems/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ej_nerve_signs`: The Back pain page lists not being able to orgasm with back pain and these signs as a reason to call 999 or go to A&E.
- `rf_ej_painful_with_temperature`: The Prostatitis page says it can be serious and needs urgent medical help. Using a high temperature to mark it is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Taking a long time to come, or not coming at all (delayed ejaculation) |  | common | Takes a long time to come, or cannot come: strongly supports; Takes antidepressants or blood pressure medicine: supports; Has diabetes: supports; Drinks a lot of alcohol: supports |
| Coming too soon (premature ejaculation) | 44001008 | very common | Comes sooner than wanted: strongly supports; Going through a stressful time or big life change: supports |
| Prostatitis (a swollen, painful prostate, usually from an infection) | 9713002 | rare | Pain between the testicles and bottom: strongly supports; Pain when ejaculating (coming): supports; Pain, burning or stinging when peeing: supports; Hard to start peeing, or a weak or stop-start flow: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels cold to the touch, or shivery: supports |
| Semen going back into the bladder (retrograde ejaculation) | 50112006 | uncommon | Little or no semen, with cloudy pee afterwards: strongly supports; Has ever had an operation on the prostate or bladder: strongly supports; Has diabetes: supports |
| Stress, tiredness, alcohol or relationship problems |  | common | Going through a stressful time or big life change: strongly supports; Problems in a relationship: supports; Still gets erections at other times, such as on waking: supports; Drinks a lot of alcohol: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
