# Review pack: Lump or growth on or under the skin

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
| [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | 2026-11-19 |  | Page last reviewed: 02 February 2026 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | 2026-11-19 |  | Page last reviewed: 13 October 2026 |
| [Lumps](https://www.nhs.uk/symptoms/lumps/) | 2026-11-19 |  | Page last reviewed: 05 February 2024 |
| [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 15 July 2026 |
| [Lipoma](https://www.nhs.uk/conditions/lipoma/) | 2026-11-19 |  | Page last reviewed: 25 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Hernia](https://www.nhs.uk/conditions/hernia/) | 2026-11-19 |  | Page last reviewed: 19 May 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Non-melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/non-melanoma-skin-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 16 September 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Skin cyst](https://www.nhs.uk/conditions/skin-cyst/) | 2026-11-19 |  | Page last reviewed: 09 May 2023 |

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

## Lump or growth on or under the skin red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_lu_stuck_hernia`<br>A painful, hard lump in the groin or tummy that cannot be pushed back in (possible trapped hernia)<br>**Note:** Clinical knowledge: a hernia that becomes painful, hard and cannot be pushed back can lose its blood supply and needs surgery the same day. The Lumps page lists a lump in the groin as a possible hernia. The stomach and bowel build will hold the hernia cards. | "The lump is painful or firm, or cannot be pushed back in" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_lu_deep_infection`<br>A red, swollen lump with pain much worse than expected, or black, purple or grey patches | "Pain much worse than you would expect" OR "Black, purple or grey patches or blisters near a wound or red area" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| `rf_lu_seriously_unwell`<br>A lump with feeling very unwell and getting worse | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_lu_infected_unwell`<br>A painful, hot, swollen lump with a high temperature and a fast heartbeat or feeling dizzy | "Swollen area is red or hot to touch" AND "Very high temperature, or feels hot, cold or shivery" AND ("Heart beating very fast" OR "Feels light-headed") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Lump or growth on or under the skin red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_lu_painful_red_hot`<br>A lump that is painful, red or hot (possible abscess or infected cyst)<br>**Note:** Source difference: the Lumps and Lipoma pages say see a GP for a painful, red or hot lump. The Skin abscess and Skin cyst pages say an urgent GP appointment or 111. The more urgent is used. | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | |
| `rf_lu_spreading_or_shivery`<br>A lump with redness spreading away from it, or with a high temperature or feeling shivery | "Redness or swelling spreading" OR "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | |

## Lump or growth on or under the skin: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_lu_gp_signs`<br>A lump that is getting bigger, hard and fixed, there for more than 2 weeks, or grew back after removal | "Lump getting bigger" OR "Lump hard and does not move" OR "Lump there for more than 2 weeks" OR "Lump grew back after it was removed" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| `or_lu_breast_testicle_glands`<br>A lump in a breast or testicle, or a swelling in the neck, armpit or groin that has not gone down in 2 weeks | "Lump in the breast or testicle" OR "Swelling on the side of the neck, armpit or groin that has not gone down in 2 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| `or_lu_mole`<br>A new or changing mole, or a mole or growth that bleeds, itches, crusts or will not heal<br>**Note:** The Melanoma page labels this non-urgent, but a GP may make an urgent referral. A likely melanoma raises the outcome to within a few days. | "New mole, or a mole that has changed size, shape or colour" OR "Mole or growth that bleeds, itches, crusts or is sore" OR "Growth or patch of skin that has not healed for more than 4 weeks" OR "Dark area or streak under a nail, not caused by an injury" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |

## Default outcome

Used when no rule fires.

- **A lump that has not been checked: see a GP**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Lipoma](https://www.nhs.uk/conditions/lipoma/)
- **Note:** The Lipoma page says see a GP if you get a lump anywhere on your body, and the Lumps page says see a GP if you are worried. Not a floor: a skin tag or wart that is clearly recognised can be lowered to self-care. A lump already checked by a doctor is handled by the exception below.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Lump or growth on or under the skin | Do you have a lump, bump or growth on or under your skin? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| The lump is painful or firm, or cannot be pushed back in | Is the lump painful or firm, or can it no longer be pushed back in? |  | [Hernia](https://www.nhs.uk/conditions/hernia/) | |
| Pain much worse than you would expect | Is the pain much worse than you would expect, for example from a small cut or a red patch of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Black, purple or grey patches or blisters near a wound or red area | Are there black, purple or grey patches, or blisters, near a wound or a red or swollen area of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Redness or swelling spreading | Is the redness or swelling spreading? |  | [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | |
| Lump getting bigger | Is the lump getting bigger? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Lump hard and does not move | Is the lump hard, and does it stay still when you press it? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Lump there for more than 2 weeks | Has the lump been there for more than 2 weeks? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Lump grew back after it was removed | Has the lump grown back after it was removed? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Lump in the breast or testicle | Is the lump in a breast or a testicle? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Swelling on the side of the neck, armpit or groin that has not gone down in 2 weeks | Is there a swelling on the side of your neck, in your armpit or in your groin that has not gone down within 2 weeks? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| New mole, or a mole that has changed size, shape or colour | Is it a new mole, or a mole that has changed size, shape or colour? |  | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |
| Mole or growth that bleeds, itches, crusts or is sore | Does the mole or growth bleed, itch, crust or scab, or is it sore or swollen? |  | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |
| Growth or patch of skin that has not healed for more than 4 weeks | Is there a growth, sore or patch of skin that has not healed for more than 4 weeks? |  | [Non-melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/non-melanoma-skin-cancer/symptoms/) | |
| Dark area or streak under a nail, not caused by an injury | Is there a dark area or dark line under a nail that was not caused by an injury? |  | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |

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

### `advice_lump_emergency`

**What to do:** Go to A&E now, or call 999. A painful, hard lump in the groin or tummy that will not go back in can be a trapped hernia, which needs treatment the same day.

**Look out for:**
- Being sick
- Not being able to poo or fart
- The pain getting worse

**Get more help when:**
- Call 999 if the pain is severe or you feel very unwell

**Where to go:** Go to A&E or call 999. Do not drive yourself. Do not eat or drink until you have been checked.

Source: **AI judgement, needs clinical review**

### `advice_skin_infection_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of a serious skin infection that is spreading, which can be life-threatening.

**Look out for:**
- Pain much worse than you would expect
- Black, purple or grey patches or blisters on the skin
- Feeling dizzy or faint, confused, or a fast heartbeat

**Get more help when:**
- Call 999 if the person gets worse, becomes confused or stops responding

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/), [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

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

### `advice_lump_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A painful, red or hot lump may be an abscess (a pocket of pus) or an infected cyst, which may need draining or antibiotics.

**Look out for:**
- Redness or swelling spreading away from the lump
- Feeling hot, cold or shivery
- Feeling dizzy or faint, or a fast heartbeat

**Get more help when:**
- Call 999 or go to A&E if you feel very unwell, dizzy or confused, or the skin turns black, purple or grey

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Do not squeeze or try to burst the lump
- Take paracetamol or ibuprofen for the pain

Source: [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/), [Skin cyst](https://www.nhs.uk/conditions/skin-cyst/)

### `advice_lump_gp`

**What to do:** See a GP about the lump. The source gives no fixed time. Most lumps are harmless, but it is important to get a new lump checked. If the GP is not sure, they may send you for a scan or test.

**Look out for:**
- The lump getting bigger, or becoming hard and fixed
- The lump becoming painful, red or hot
- A mole that changes size, shape or colour, bleeds or crusts

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if the lump gets painful, red or hot. Do the same if you feel hot, cold or shivery.

**Where to go:** Book an appointment with your GP surgery.

Source: [Lumps](https://www.nhs.uk/symptoms/lumps/), [Lipoma](https://www.nhs.uk/conditions/lipoma/), [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_lu_stuck_hernia`: Clinical knowledge: a hernia that becomes painful, hard and cannot be pushed back can lose its blood supply and needs surgery the same day. The Lumps page lists a lump in the groin as a possible hernia. The stomach and bowel build will hold the hernia cards.
- `rf_lu_painful_red_hot`: Source difference: the Lumps and Lipoma pages say see a GP for a painful, red or hot lump. The Skin abscess and Skin cyst pages say an urgent GP appointment or 111. The more urgent is used.
- `or_lu_mole`: The Melanoma page labels this non-urgent, but a GP may make an urgent referral. A likely melanoma raises the outcome to within a few days.
- `skin_lump default outcome`: The Lipoma page says see a GP if you get a lump anywhere on your body, and the Lumps page says see a GP if you are worried. Not a floor: a skin tag or wart that is clearly recognised can be lowered to self-care. A lump already checked by a doctor is handled by the exception below.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Lipoma (a soft, fatty lump under the skin) | 93163002 | common | Soft, squashy lump that moves under the skin: strongly supports; Lump there for more than 2 weeks: supports |
| Melanoma (a type of skin cancer that often starts as a new or changing mole) | 93655004 | rare | New mole, or a mole that has changed size, shape or colour: strongly supports; Mole with an uneven shape or edges, a mix of colours, or wider than 6mm: supports; Mole or growth that bleeds, itches, crusts or is sore: supports; Lump getting bigger: supports; Dark area or streak under a nail, not caused by an injury: supports |
| Non-melanoma skin cancer (a growth or patch of skin that does not heal, often on sun-exposed skin) | 254701007 | rare | Growth or patch of skin that has not healed for more than 4 weeks: strongly supports; Mole or growth that bleeds, itches, crusts or is sore: supports; Lump getting bigger: supports |
| Skin abscess (a painful pocket of pus in the skin) | 31928004 | uncommon | Swollen area is red or hot to touch: strongly supports; Pus or fluid leaking: supports; Very high temperature, or feels hot, cold or shivery: supports; Lump getting bigger: supports |
| Skin cyst (a round lump under the skin, often filled with fluid) | 419603000 | common | Smooth, round lump just under the skin, sometimes with a dark dot in the middle: strongly supports; Pus or fluid leaking: supports; Swollen area is red or hot to touch: supports; Lump there for more than 2 weeks: supports |
| Skin tag (a small, soft growth that hangs off the skin) |  | common | Small, soft, fleshy growth that hangs off the skin: strongly supports; Lump there for more than 2 weeks: supports |
| Soft tissue sarcoma (a rare cancer that starts as a lump in muscle or fat) | 424952003 | very rare | Lump getting bigger: strongly supports; Lump bigger than a golf ball (about 5cm): supports; Lump hard and does not move: supports |
| Wart or verruca |  | common | Small, rough, hard growth, often on the hands or feet: strongly supports; Lump there for more than 2 weeks: supports |
| Hernia (a lump where part of the gut pushes through a weak spot in the tummy wall) |  | uncommon | A lump or swelling in the tummy or groin: strongly supports; Tummy pain worse when moving, coughing or going over bumps: supports; Pain low down in the tummy, below the belly button: supports; A bulge in the groin that may go down into the scrotum: strongly supports; Dull, dragging ache, worse when standing: supports |
| A trapped hernia (part of the gut stuck in a weak spot in the tummy wall, losing its blood supply) | 236024003 | rare | A lump or swelling in the tummy or groin: strongly supports; The lump is painful or firm, or cannot be pushed back in: strongly supports; Being sick: strongly supports; Cannot poo or fart at all: supports; Severe stomach ache: supports; Tummy looks swollen or much bigger than usual: supports; A bulge in the groin that may go down into the scrotum: strongly supports; Feels sick or has been sick: supports; Stomach ache: supports; Constipation: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
