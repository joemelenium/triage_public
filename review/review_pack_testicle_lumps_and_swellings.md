# Review pack: Testicle lumps and swellings

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
| [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/) | 2026-11-19 |  | Page last reviewed: 18 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/) | 2026-11-19 |  | Page last reviewed: 26 June 2025 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Hernia](https://www.nhs.uk/conditions/hernia/) | 2026-11-19 |  | Page last reviewed: 19 May 2026 |
| [Epididymitis](https://www.nhs.uk/conditions/epididymitis/) | 2026-11-19 |  | Page last reviewed: 06 August 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Testicular cancer: symptoms](https://www.nhs.uk/conditions/testicular-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 2 April 2024 |

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

## Testicle lumps and swellings red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tl_sudden_severe_pain`<br>Sudden, severe pain in a testicle: possible twisted testicle | "Sudden, severe pain in a testicle" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E immediately or call 999* | [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/) | |
| `rf_tl_pain_with_sickness`<br>Testicle pain with feeling sick, being sick, or pain in the tummy | "Pain in the testicles" AND ("Feels sick or has been sick" OR "Stomach ache") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E immediately or call 999* | [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/) | |
| `rf_tl_pain_over_an_hour`<br>Testicle pain that has lasted more than an hour, or carries on when resting<br>**Note:** Marked soft for the same reason as in the testicle pain entry symptom. | "Testicle pain lasting more than an hour, or carrying on at rest" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E immediately or call 999* | [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/) | |
| `rf_tl_hernia_stuck`<br>A groin bulge that is painful and firm, and cannot be pushed back: possible trapped hernia<br>**Note:** Source difference: the Hernia page says get help from 111 for pain in a hernia. The more urgent is used. Needs clinical review. | "The lump is painful or firm, or cannot be pushed back in" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_tl_skin_dark_spreading`<br>Skin around the genitals turning dark, or pain and swelling spreading fast: possible Fournier's gangrene | "Skin of the genitals turning dark, or pain and swelling spreading fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Testicle lumps and swellings red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tl_infection_signs`<br>A swollen testicle with a red, warm scrotum, or a high temperature: possible infection<br>**Note:** Clinical knowledge: signs of epididymitis, which needs antibiotics. The Epididymitis page says see a GP. | "Scrotum red, warm and swollen" OR "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_tl_injury`<br>A swollen testicle after an injury | "Injury to the testicles" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Testicle lumps and swellings: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **A lump or swelling in the testicles: always get it checked by a GP**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Lump or swelling in the testicles | Have you noticed a lump or swelling in or around your testicles (balls)? | 53929009 | [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Sudden, severe pain in a testicle | Did the pain in your testicle come on suddenly, and is it severe? |  | [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/) | |
| Pain in the testicles | Do you have pain or an ache in one or both testicles (balls)? |  | [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Testicle pain lasting more than an hour, or carrying on at rest | Has the pain in your testicle lasted more than an hour, or does it carry on when you are resting? |  | [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/) | |
| The lump is painful or firm, or cannot be pushed back in | Is the lump painful or firm, or can it no longer be pushed back in? |  | [Hernia](https://www.nhs.uk/conditions/hernia/) | |
| Skin of the genitals turning dark, or pain and swelling spreading fast | Is the skin around your genitals or bottom turning dark, purple or black? Or is the pain or swelling spreading fast? |  | **AI judgement, needs clinical review** | |
| Scrotum red, warm and swollen | Is the skin around your testicles (the scrotum) red, warm, swollen or tender? |  | [Epididymitis](https://www.nhs.uk/conditions/epididymitis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Injury to the testicles | Did this start after an injury to your testicles, such as a kick or a blow? |  | [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/) | |

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

### `advice_testicle_ae`

**What to do:** Go to A&E immediately or call 999. This could be a twisted testicle (testicular torsion). It needs an operation within hours to save the testicle.

**Look out for:**
- The pain getting worse
- Being sick
- The testicle becoming more swollen, or higher than the other one

**Get more help when:**
- Call 999 if you cannot get to A&E quickly. Do not wait to see if the pain goes away.

**Where to go:** Go to A&E now. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Do not eat or drink in case you need an operation. Bring any medicines you take.

Source: [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/), [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/), [Epididymitis](https://www.nhs.uk/conditions/epididymitis/)

### `advice_hernia_ae`

**What to do:** Go to A&E now. A hernia (a lump where part of the gut pushes through a weak spot in the tummy wall) that is painful and cannot be pushed back in may be trapped and losing its blood supply. It may need an operation today.

**Look out for:**
- Being sick, or a swollen tummy
- Not being able to poo or fart
- The bulge turning red or dark

**Get more help when:**
- Call 999 if you feel very unwell or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Do not eat or drink in case you need an operation.

Source: **AI judgement, needs clinical review**, [Hernia](https://www.nhs.uk/conditions/hernia/)

### `advice_genital_infection_ae`

**What to do:** Call 999 or go to A&E now. Skin around the genitals turning dark, or pain and swelling that spread fast, can be a rare but very serious infection that needs treatment in hospital straight away.

**Look out for:**
- Feeling very unwell, confused or drowsy
- A high temperature, or feeling cold and shivery
- Blotchy or mottled skin

**Get more help when:**
- Call 999 if you feel very unwell or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_testicle_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Testicle pain or swelling should be checked today.

**Look out for:**
- Sudden, severe pain
- Feeling sick, being sick, or tummy pain
- Pain that lasts more than an hour or carries on when you rest

**Get more help when:**
- Go to A&E immediately or call 999 if you get any of the signs above. This could be a twisted testicle.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. A sexual health clinic can also treat infections.

**What you can do yourself:**
- Take paracetamol for the pain
- Wear supportive underwear
- Hold a cold pack wrapped in a towel on the area

Source: [Pain in testicles](https://www.nhs.uk/symptoms/testicle-pain/), [Epididymitis](https://www.nhs.uk/conditions/epididymitis/)

### `advice_testicle_lump_gp`

**What to do:** See a GP. Most lumps and swellings in the testicles are not serious, but always get them checked. Testicular cancer is easier to treat if it is found early.

**Look out for:**
- Sudden, severe pain in a testicle
- Pain with feeling or being sick, or tummy pain
- The lump getting bigger

**Get more help when:**
- Go to A&E immediately or call 999 if you get sudden, severe pain, or pain with being sick

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

Source: [Testicle lumps and swellings](https://www.nhs.uk/symptoms/testicle-lumps-and-swellings/), [Testicular cancer: symptoms](https://www.nhs.uk/conditions/testicular-cancer/symptoms/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_tl_pain_over_an_hour`: Marked soft for the same reason as in the testicle pain entry symptom.
- `rf_tl_hernia_stuck`: Source difference: the Hernia page says get help from 111 for pain in a hernia. The more urgent is used. Needs clinical review.
- `rf_tl_infection_signs`: Clinical knowledge: signs of epididymitis, which needs antibiotics. The Epididymitis page says see a GP.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Hernia (a lump where part of the gut pushes through a weak spot in the tummy wall) |  | uncommon | A lump or swelling in the tummy or groin: strongly supports; Tummy pain worse when moving, coughing or going over bumps: supports; Pain low down in the tummy, below the belly button: supports; A bulge in the groin that may go down into the scrotum: strongly supports; Dull, dragging ache, worse when standing: supports |
| A trapped hernia (part of the gut stuck in a weak spot in the tummy wall, losing its blood supply) | 236024003 | rare | A lump or swelling in the tummy or groin: strongly supports; The lump is painful or firm, or cannot be pushed back in: strongly supports; Being sick: strongly supports; Cannot poo or fart at all: supports; Severe stomach ache: supports; Tummy looks swollen or much bigger than usual: supports; A bulge in the groin that may go down into the scrotum: strongly supports; Feels sick or has been sick: supports; Stomach ache: supports; Constipation: supports |
| Harmless fluid-filled lump above the testicle (epididymal cyst) | 43077002 | common | Small smooth lump above or behind the testicle: strongly supports; Swelling or lump has grown slowly over months: supports |
| Infection of the tube behind the testicle (epididymitis) | 197983000 | common | Testicle pain came on slowly over a day or more: strongly supports; Scrotum red, warm and swollen: strongly supports; Pain, burning or stinging when peeing: supports; Discharge from the penis: supports; Very high temperature, or feels hot, cold or shivery: supports; Sex without a condom with a new partner in the last 3 months: supports |
| A bad skin infection of the genitals that spreads fast (Fournier's gangrene) | 398318005 | very rare | Skin of the genitals turning dark, or pain and swelling spreading fast: strongly supports; Scrotum red, warm and swollen: strongly supports; Feels very unwell: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Has diabetes: supports |
| Build-up of fluid around a testicle (hydrocele) |  | common | Whole side swollen, soft and smooth, like a water balloon: strongly supports; Swelling or lump has grown slowly over months: supports |
| Injury to a testicle | 262921003 | uncommon | Injury to the testicles: strongly supports; Sudden, severe pain in a testicle: supports; Scrotum red, warm and swollen: supports; Feels sick or has been sick: supports |
| Testicular cancer | 363449006 | uncommon | Hard lump in the testicle, or a testicle that feels heavy or hard: strongly supports; A testicle has got bigger or changed shape: strongly supports; Losing weight without trying: supports; Back pain: supports |
| Twisted testicle (testicular torsion) | 81996005 | uncommon | Sudden, severe pain in a testicle: strongly supports; Testicle pain lasting more than an hour, or carrying on at rest: strongly supports; Feels sick or has been sick: supports; Stomach ache: supports; One testicle sitting higher than usual, or at an odd angle: supports; Pain in the testicles: strongly supports; Pain low down in the tummy, below the belly button: supports; Being sick: supports; Feeling sick (nausea): supports; Stomach ache that started suddenly and is severe: supports |
| Swollen veins in the scrotum (varicocele) | 51070004 | common | Swelling feels like a bag of worms: strongly supports; Dull, dragging ache, worse when standing: strongly supports; Swelling or lump has grown slowly over months: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
