# Review pack: Penis lumps and spots

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
| [Tight foreskin (phimosis)](https://www.nhs.uk/conditions/phimosis/) | 2026-11-19 |  | Page last reviewed: 06 March 2026 |
| [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/) | 2026-11-19 |  | Page last reviewed: 16 December 2024 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Genital herpes](https://www.nhs.uk/conditions/genital-herpes/) | 2026-11-19 |  | Page last reviewed: 27 June 2023 |
| [Penis lumps and spots](https://www.nhs.uk/symptoms/penis-lumps-and-spots/) | 2026-11-19 |  | Page last reviewed: 25 June 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | 2026-11-19 |  | Page last reviewed: 19 February 2024 |
| [Balanitis](https://www.nhs.uk/conditions/balanitis/) | 2026-11-19 |  | Page last reviewed: 30 May 2023 |
| [Genital warts](https://www.nhs.uk/conditions/genital-warts/) | 2026-11-19 |  | Page last reviewed: 10 July 2023 |

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

## Penis lumps and spots red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pl_foreskin_stuck`<br>Foreskin pulled back and will not go back over the end of the penis | "Foreskin pulled back and cannot go back over the tip" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Tight foreskin (phimosis)](https://www.nhs.uk/conditions/phimosis/) | |
| `rf_pl_injury`<br>Penis bent or hurt, often during sex, with a snap or pop, then swelling or bruising: possible broken penis<br>**Note:** Clinical knowledge: a tear in the erect penis (penile fracture) needs surgery soon. No NHS page in the source log covers it. | "Penis bent or injured, often during sex, with a snap or pop" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_pl_skin_dark_spreading`<br>Skin around the genitals turning dark, or pain and swelling spreading fast: possible Fournier's gangrene | "Skin of the genitals turning dark, or pain and swelling spreading fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Penis lumps and spots red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pl_temperature`<br>A lump, sore or rash on the penis with a high temperature<br>**Note:** The Gonorrhoea page asks for an urgent GP appointment or 111 for a high temperature with gonorrhoea, as a sign of a more serious infection. Applying it to all genital symptoms with a high temperature is AI judgement; a first outbreak of genital herpes often comes with one, so it is soft. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/) | |
| `rf_pl_cannot_pee`<br>A problem with the penis and unable to pee<br>**Note:** The unable to pee entry symptom also applies once this is reported. | "Unable to pee" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |

## Penis lumps and spots: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_pl_painful_blisters`<br>Small painful blisters or sores: possible genital herpes<br>**Note:** The page says go to a sexual health clinic as soon as possible. 'Soon' (within a few days) is the nearest level. | "Small painful blisters or sores around the genitals" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*Go to a sexual health clinic as soon as possible* | [Genital herpes](https://www.nhs.uk/conditions/genital-herpes/) | |

## Default outcome

Used when no rule fires.

- **A lump, spot, sore, rash or swelling on the penis: always get it checked**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP or go to a sexual health clinic. The source gives no fixed time.*
- Source: [Penis lumps and spots](https://www.nhs.uk/symptoms/penis-lumps-and-spots/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Lump, spot, sore or rash on the penis | Do you have a lump, spot, sore, rash or swelling on your penis? |  | [Penis lumps and spots](https://www.nhs.uk/symptoms/penis-lumps-and-spots/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Foreskin pulled back and cannot go back over the tip | Has the foreskin been pulled back and now will not go back over the end of the penis? |  | [Tight foreskin (phimosis)](https://www.nhs.uk/conditions/phimosis/) | |
| Penis bent or injured, often during sex, with a snap or pop | Did your penis get bent or hurt during sex or an injury, maybe with a snap or popping sound? Is it now swollen or bruised? |  | **AI judgement, needs clinical review** | |
| Skin of the genitals turning dark, or pain and swelling spreading fast | Is the skin around your genitals or bottom turning dark, purple or black? Or is the pain or swelling spreading fast? |  | **AI judgement, needs clinical review** | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Unable to pee | Are you unable to pee, or can you only pass a few drops, even though you need to go? | 102835006 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Small painful blisters or sores around the genitals | Do you have small blisters that burst and leave red, open, painful sores? You may have tingling or burning first. |  | [Genital herpes](https://www.nhs.uk/conditions/genital-herpes/) | |

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

### `advice_penis_ae`

**What to do:** Go to A&E now, or call 999. A foreskin stuck behind the head of the penis, or a penis injury with swelling or bruising, needs treatment in hospital quickly.

**Look out for:**
- Swelling or pain getting worse
- The head of the penis changing colour
- Not being able to pee

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Do not try to force the foreskin back over the head of the penis
- Hold a cold pack wrapped in a towel on the area on the way, to help with swelling

Source: [Tight foreskin (phimosis)](https://www.nhs.uk/conditions/phimosis/)

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

### `advice_penis_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A high temperature with a problem on your penis can mean an infection that needs treatment soon.

**Look out for:**
- Redness or swelling spreading
- Skin turning dark
- Not being able to pee

**Get more help when:**
- Call 999 or go to A&E if the skin turns dark or the swelling spreads fast

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. A sexual health clinic may be able to see you today.

Source: [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/), [Penis lumps and spots](https://www.nhs.uk/symptoms/penis-lumps-and-spots/)

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

### `advice_sexual_health_clinic_soon`

**What to do:** Go to a sexual health clinic as soon as possible, within the next few days. Small painful blisters or sores may be genital herpes. Treatment works best if it starts early.

**Look out for:**
- Not being able to pee because of the pain
- A high temperature or feeling very unwell

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you cannot pee or you feel very unwell

**Where to go:** Go to a sexual health clinic. Many offer walk-in sessions. Or make an appointment with a GP.

**What you can do yourself:**
- Take paracetamol for the pain
- Keep the area clean and dry, and wash your hands after touching it
- Do not have sex until the sores have healed
- It may help to pee in a warm bath

Source: [Genital herpes](https://www.nhs.uk/conditions/genital-herpes/)

### `advice_penis_gp`

**What to do:** See a GP or go to a sexual health clinic. Lumps or spots on the penis are not usually serious, but always get them checked. Try not to be embarrassed.

**Look out for:**
- A sore or lump that has not healed in 4 weeks, or is getting bigger
- Discharge or bleeding from your penis
- Foreskin stuck behind the head of the penis

**Get more help when:**
- Call 999 or go to A&E if your foreskin is pulled back and will not go back over the head of the penis

**Where to go:** Make an appointment with a GP, or go to a sexual health clinic. Many offer walk-in sessions.

**What you can do yourself:**
- Do not have sex until it has been checked, in case it is an infection
- Wash your penis every day with water, and dry it gently

Source: [Penis lumps and spots](https://www.nhs.uk/symptoms/penis-lumps-and-spots/), [Balanitis](https://www.nhs.uk/conditions/balanitis/), [Genital warts](https://www.nhs.uk/conditions/genital-warts/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_pl_injury`: Clinical knowledge: a tear in the erect penis (penile fracture) needs surgery soon. No NHS page in the source log covers it.
- `rf_pl_temperature`: The Gonorrhoea page asks for an urgent GP appointment or 111 for a high temperature with gonorrhoea, as a sign of a more serious infection. Applying it to all genital symptoms with a high temperature is AI judgement; a first outbreak of genital herpes often comes with one, so it is soft.
- `rf_pl_cannot_pee`: The unable to pee entry symptom also applies once this is reported.
- `or_pl_painful_blisters`: The page says go to a sexual health clinic as soon as possible. 'Soon' (within a few days) is the nearest level.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Swollen, sore head of the penis (balanitis) | 44882003 | common | Tip of the penis red, swollen, itchy or sore: strongly supports; Discharge from the penis: supports; Pain, burning or stinging when peeing: supports |
| A bad skin infection of the genitals that spreads fast (Fournier's gangrene) | 398318005 | very rare | Skin of the genitals turning dark, or pain and swelling spreading fast: strongly supports; Scrotum red, warm and swollen: strongly supports; Feels very unwell: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Has diabetes: supports |
| Genital herpes | 33839006 | common | Small painful blisters or sores around the genitals: strongly supports; Pain, burning or stinging when peeing: supports; Sex without a condom with a new partner in the last 3 months: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Genital warts | 266113007 | common | Small, rough, painless lumps (warts): strongly supports; Sex without a condom with a new partner in the last 3 months: supports; A sexual partner has a sexually transmitted infection: supports |
| Harmless spots on the penis, such as pearly penile papules | 308006 | common | Rows of tiny, smooth, skin-coloured bumps that do not change: strongly supports; Spots have been there for months without changing: strongly supports |
| Foreskin stuck behind the head of the penis (paraphimosis) | 13758004 | rare | Foreskin pulled back and cannot go back over the tip: strongly supports; Tip of the penis red, swollen, itchy or sore: supports |
| Penile cancer | 363516004 | very rare | A growth, lump or sore on the penis that has not healed in 4 weeks: strongly supports; Discharge from the penis: supports; Losing weight without trying: supports |
| Broken penis (penile fracture) | 373596001 | rare | Penis bent or injured, often during sex, with a snap or pop: strongly supports; Unable to pee: supports |
| Sexually transmitted infection (STI), such as chlamydia or gonorrhoea | 8098009 | uncommon | Discharge from the penis: strongly supports; Sex without a condom with a new partner in the last 3 months: strongly supports; Pain, burning or stinging when peeing: supports; Tip of the penis red, swollen, itchy or sore: supports; A sexual partner has a sexually transmitted infection: strongly supports; Discharge is green, yellow or frothy: supports; Bleeding after sex: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports |
| Syphilis | 266127002 | rare | A painless sore or ulcer on the penis: strongly supports; Sex without a condom with a new partner in the last 3 months: strongly supports; Rash on the palms of the hands and soles of the feet: supports; Swollen glands in the neck: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
