# Review pack: Nail problems

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
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | 2026-11-19 |  | Page last reviewed: 12 March 2024 |
| [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 15 July 2026 |
| [Fungal nail infection](https://www.nhs.uk/conditions/fungal-nail-infection/) | 2026-11-19 |  | Page last reviewed: 27 March 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | 2026-11-19 |  | Page last reviewed: 13 October 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Idiopathic pulmonary fibrosis](https://www.nhs.uk/conditions/idiopathic-pulmonary-fibrosis/) | 2026-11-18 |  | Page last reviewed: 27 August 2026 |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Ingrown toenail](https://www.nhs.uk/conditions/ingrown-toenail/) | 2026-11-19 |  | Page last reviewed: 30 June 2025 |
| [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/) | 2026-11-19 |  | Page last reviewed: 29 April 2024 |
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

## Nail problems red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_na_spreading_infection`<br>Skin around a nail that is painful, hot and swollen, with redness spreading or a high temperature<br>**Note:** The Nail problems and Ingrown toenail pages say see a GP for an infected nail, and a high temperature or feeling shivery. Spreading redness or a high temperature can mean cellulitis, which the Cellulitis page says needs urgent help. | "Swollen area is red or hot to touch" AND ("Redness or swelling spreading" OR "Very high temperature, or feels hot, cold or shivery") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Nail problems: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_na_gp`<br>A nail that changed or fell off for no known reason, or sore, red, swollen skin around a nail | "Nail changed shape or colour, or fell off, for no known reason" OR "Skin around the nail sore, red, swollen and warm" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |
| `or_na_dark_streak`<br>A dark area under a nail not caused by an injury | "Dark area or streak under a nail, not caused by an injury" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |
| `or_na_clubbing`<br>Fingertips wider or rounder, with nails curving over them (clubbing) | "Fingertips wider or rounder, with nails curving over (clubbing)" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |
| `or_na_not_better_or_diabetes`<br>A nail problem not better with pharmacy treatment, or in someone with diabetes or a weakened immune system<br>**Note:** The Fungal nail infection, Ingrown toenail and Athlete's foot pages say see a GP if treatment has not worked, or if you have diabetes or a weakened immune system. | "Not better after treating it yourself, or keeps coming back" OR ("Weakened immune system" AND ("Nail thick, white or yellow, and brittle or crumbly" OR "Nail growing into the skin of the toe" OR "Itchy, white or flaky skin between the toes")) | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Fungal nail infection](https://www.nhs.uk/conditions/fungal-nail-infection/) | |

## Default outcome

Used when no rule fires.

- **A nail problem with nothing that needs a GP: look after it yourself, or ask a pharmacist**
- Outcome: Self-manageable, Self-care, No appointment needed. *Nail problems are not usually serious. A pharmacist can advise on fungal nail treatment.*
- Source: [Nail problems](https://www.nhs.uk/symptoms/nail-problems/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Problem with a fingernail or toenail | Do you have a problem with a fingernail or toenail? For example, it has changed colour or shape, is thick or brittle, or is coming off. | 247491004 | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Redness or swelling spreading | Is the redness or swelling spreading? |  | [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Nail changed shape or colour, or fell off, for no known reason | Has a nail changed shape or colour, or fallen off, and you do not know why? |  | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |
| Skin around the nail sore, red, swollen and warm | Is the skin around the nail sore, red, swollen and warm? | 71906005 | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |
| Dark area or streak under a nail, not caused by an injury | Is there a dark area or dark line under a nail that was not caused by an injury? |  | [Melanoma skin cancer: symptoms](https://www.nhs.uk/conditions/melanoma-skin-cancer/symptoms/) | |
| Fingertips wider or rounder, with nails curving over (clubbing) | Have your fingertips become wider or rounder, with the nails curving over them? |  | [Idiopathic pulmonary fibrosis](https://www.nhs.uk/conditions/idiopathic-pulmonary-fibrosis/) | |
| Not better after treating it yourself, or keeps coming back | Has it not got better after treating it yourself, or does it keep coming back? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Nail thick, white or yellow, and brittle or crumbly | Is the nail thicker than usual, white or yellow, and brittle or crumbly? | 414941008 | [Fungal nail infection](https://www.nhs.uk/conditions/fungal-nail-infection/) | |
| Nail growing into the skin of the toe | Is the nail curving or growing into the skin at its edge, usually on the big toe? | 400097005 | [Ingrown toenail](https://www.nhs.uk/conditions/ingrown-toenail/) | |
| Itchy, white or flaky skin between the toes | Do you have itchy, white, flaky or cracked skin between your toes? | 6020002 | [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/) | |

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

### `advice_skin_infection_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Painful, hot, swollen skin can be a skin infection called cellulitis. Early treatment with antibiotics can stop it becoming more serious.

**Look out for:**
- The redness or swelling spreading
- A very high temperature, or feeling hot, cold or shivery
- A fast heartbeat, fast breathing, or feeling dizzy or faint
- Purple patches on the skin, or cold, clammy, pale skin

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs, or become confused
- Contact your GP if you do not start to feel better 2 to 3 days after starting antibiotics

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Raise the affected area on a pillow or chair to reduce swelling
- Take paracetamol or ibuprofen for the pain
- Drink plenty of fluids

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

### `advice_nail_gp`

**What to do:** See a GP about the nail. The source gives no fixed time. You may also be able to refer yourself to a foot specialist (podiatrist).

**Look out for:**
- The skin around the nail becoming painful, hot and swollen, with the redness spreading
- Pus coming out, or feeling hot, cold or shivery

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if redness spreads or you get a high temperature

**Where to go:** Book an appointment with your GP surgery, or a podiatrist for toenails.

**What you can do yourself:**
- Trim nails straight across, not down the edges
- Keep your feet clean and dry, and treat athlete's foot

Source: [Nail problems](https://www.nhs.uk/symptoms/nail-problems/), [Fungal nail infection](https://www.nhs.uk/conditions/fungal-nail-infection/), [Ingrown toenail](https://www.nhs.uk/conditions/ingrown-toenail/)

### `advice_nail_self_care`

**What to do:** Nail problems are not usually serious. You can look after your nails yourself, and a pharmacist can suggest treatment for a fungal nail infection.

**Look out for:**
- A nail that changes shape or colour, or falls off, and you do not know why
- Sore, red, swollen, warm skin around the nail
- A dark area under a nail that was not caused by an injury

**Get more help when:**
- See a GP if any of these happen, or treatment does not help

**Where to go:** Treat it yourself at home. A pharmacy or podiatrist can help.

**What you can do yourself:**
- Wear rubber gloves if your hands are often in water
- Trim nails straight across, and do not bite or pick them
- A nail that falls off after an injury should grow back: fingernails in about 6 months, toenails in up to 18 months

Source: [Nail problems](https://www.nhs.uk/symptoms/nail-problems/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_na_spreading_infection`: The Nail problems and Ingrown toenail pages say see a GP for an infected nail, and a high temperature or feeling shivery. Spreading redness or a high temperature can mean cellulitis, which the Cellulitis page says needs urgent help.
- `or_na_not_better_or_diabetes`: The Fungal nail infection, Ingrown toenail and Athlete's foot pages say see a GP if treatment has not worked, or if you have diabetes or a weakened immune system.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Fungal nail infection |  | very common | Nail thick, white or yellow, and brittle or crumbly: strongly supports; Itchy, white or flaky skin between the toes: supports |
| Fungal skin infection (such as ringworm or athlete's foot) | 47382004 | common | Itchy, dry, ring-shaped patch: strongly supports; Itchy, white or flaky skin between the toes: strongly supports; Itchy, flaky or scaly scalp: supports; Round or oval bald patches: supports; Rash is itchy: supports |
| Ingrown toenail |  | common | Nail growing into the skin of the toe: strongly supports; Skin around the nail sore, red, swollen and warm: supports; Pus or fluid leaking: supports |
| Melanoma (a type of skin cancer that often starts as a new or changing mole) | 93655004 | rare | New mole, or a mole that has changed size, shape or colour: strongly supports; Mole with an uneven shape or edges, a mix of colours, or wider than 6mm: supports; Mole or growth that bleeds, itches, crusts or is sore: supports; Lump getting bigger: supports; Dark area or streak under a nail, not caused by an injury: supports |
| Injured nail, with blood under it or coming loose |  | common | Nail injured, for example trapped or stubbed: strongly supports; Nail changed shape or colour, or fell off, for no known reason: supports |
| Infected skin around a nail (paronychia) |  | common | Skin around the nail sore, red, swollen and warm: strongly supports; Pus or fluid leaking: supports; Swollen area is red or hot to touch: supports |
| Psoriasis (flaky patches of skin with silvery scales) | 9014002 | uncommon | Raised patches with silvery-white scales: strongly supports; Patches on the outside of the elbows or knees, or on the scalp: strongly supports; Small dents or pits in the nails: supports; Rash is itchy: supports; Painful or swollen joints: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
