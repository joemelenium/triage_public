# Review pack: Dehydration

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
| [Dehydration](https://www.nhs.uk/conditions/dehydration/) | 2026-11-19 |  | Page last reviewed: 01 May 2026 |
| [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | 2026-11-19 |  | Page last reviewed: 28 May 2026 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | 2026-11-19 |  | Page last reviewed: 03 January 2024 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
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

## Dehydration red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dh_shock_skin`<br>Signs of dehydration with blotchy skin, or skin that feels cold: possible shock | "Blotchy or mottled skin" OR "Hands and feet, or skin, unusually cold to touch" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_fast_breathing`<br>Signs of dehydration with difficulty breathing or lots of quick breaths | "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_drowsy`<br>Signs of dehydration and so drowsy they are hard to wake or cannot stay awake | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_heatstroke`<br>Hot skin that is not sweating, or still unwell after 30 minutes of cooling down: possible heatstroke | "Hot skin that is not sweating" OR "Still unwell after 30 minutes of cooling down" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |
| `rf_dh_young_child_not_peed`<br>A child under 5 who has not had a pee for 12 hours<br>**Note:** Source difference: the Dehydration page says urgent for fewer wet nappies. The Sepsis page says 999 or A&E for no pee in 12 hours in a child under 5. The more urgent is used. | "Under 5 years old" AND "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Dehydration red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dh_dizzy_standing`<br>Dizzy when standing up, and it does not go away | "Dizzy when standing up, and it does not go away" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_fast_heart`<br>Signs of dehydration with a fast heartbeat | "Heart beating very fast" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_not_peed`<br>No pee for 12 hours or more | "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_child_signs`<br>A child with dry nappies, sunken eyes or no tears, or a baby with a sunken soft spot | "Child with dry nappies, sunken eyes or no tears" OR "Baby's soft spot on top of the head sinks inwards" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 or ask for an urgent GP appointment* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dh_cannot_keep_fluids_down`<br>Signs of dehydration and cannot keep fluids down<br>**Note:** Clinical knowledge: someone who cannot keep any fluids down cannot rehydrate at home. The Dehydration page says to start with small sips. | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_dh_baby`<br>A baby under 1 with signs of dehydration<br>**Note:** The page says babies are more at risk of dehydration and to call 111 for advice for a child under 5. Making every baby under 1 urgent is AI judgement. | "Under 1 year old" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |

## Dehydration: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_dh_unusually_tired`<br>Signs of dehydration and feeling unusually tired<br>**Note:** The page lists feeling unusually tired as a sign of serious dehydration, and also lists feeling tired as an ordinary symptom of dehydration. Soft for that reason. | "Feels very tired" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `or_dh_after_sickness_or_diarrhoea`<br>Signs of dehydration after diarrhoea or being sick: a pharmacist can recommend rehydration drinks | "Diarrhoea, or being sick" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*See a pharmacist. The source gives no fixed time.* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |

## Default outcome

Used when no rule fires.

- **Signs of dehydration: peeing less or dark pee is listed by the source as a reason for urgent help**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Dehydration](https://www.nhs.uk/conditions/dehydration/)
- **Note:** Soft: likely mild dehydration with a clear cause (heat, exercise, a tummy bug) lowers it to drinking more fluids at home. That reading of the page is AI judgement.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Hands and feet, or skin, unusually cold to touch | Are your hands and feet, or your skin, unusually cold to touch, or cold and damp (clammy)? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Hot skin that is not sweating | Is the skin very hot but not sweating, and maybe red? |  | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |
| Still unwell after 30 minutes of cooling down | Is the person still unwell after 30 minutes of resting in a cool place, being cooled and drinking fluids? |  | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Dizzy when standing up, and it does not go away | Do you feel dizzy when you stand up, and it does not go away? |  | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Child with dry nappies, sunken eyes or no tears | Does the child have signs of not having enough water in their body? For example, dry nappies, sunken eyes, or no tears when crying. |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Baby's soft spot on top of the head sinks inwards | Has the soft spot on top of your baby's head (fontanelle) sunk inwards? | 8381001 | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Diarrhoea, or being sick | Do you have diarrhoea, or have you been sick? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |

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

### `advice_dehydration_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of shock, a serious problem caused by not having enough water in the body.

**Look out for:**
- Becoming confused, very sleepy or hard to wake
- Skin, lips or tongue turning blue, grey or pale
- Lots of quick breaths

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Dehydration](https://www.nhs.uk/conditions/dehydration/)

### `advice_heatstroke_999`

**What to do:** Call 999 now. These are signs of heatstroke, which is an emergency.

**Look out for:**
- Confusion, or not being able to stand or walk properly
- A fit (seizure)
- Passing out

**Get more help when:**
- Call 999 again if the person gets worse before help arrives

**Where to go:** Call 999. Stay with the person until help arrives.

**What you can do yourself:**
- Move the person somewhere cool
- Cool their skin with cool water, or wet cloths, and fan them
- Give them sips of water if they are awake and can swallow
- If they stop responding, put them on their side

Source: [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/)

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

### `advice_dehydration_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. These can be signs of serious dehydration (not having enough water in the body) that needs treatment.

**Look out for:**
- Skin, lips or tongue turning blue, grey, pale or blotchy
- Skin that feels cold, or lots of quick breaths
- Becoming confused, or sleepier than usual or hard to wake
- Feeling dizzy when you stand up, and it does not go away
- Breathing quickly, or a fast heartbeat

**Get more help when:**
- Call 999 or go to A&E if your skin, lips or tongue turn blue, grey or blotchy. Do the same if you feel cold, confused or hard to wake.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 if you need advice for a child under 5. In an emergency call 999.

**What you can do yourself:**
- Keep drinking. If you feel sick, start with small sips and slowly drink more.
- A pharmacist can suggest rehydration drinks. These put back the sugar and salts you have lost.
- Keep breastfeeding or giving formula to a baby, in small amounts more often. Do not make formula weaker.

Source: [Dehydration](https://www.nhs.uk/conditions/dehydration/)

### `advice_dehydration_pharmacy`

**What to do:** See a pharmacist. They can recommend rehydration drinks to replace what you have lost through diarrhoea or being sick. Keep drinking fluids.

**Look out for:**
- Feeling unusually tired, or a child seeming drowsy
- Feeling dizzy when you stand up, and it does not go away
- Peeing less than usual, or a baby having fewer wet nappies
- Breathing quickly or a fast heartbeat

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if your skin turns blotchy or cold, or you become confused or very sleepy

**Where to go:** Go to a pharmacy. You do not need an appointment. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Start with small sips if you feel sick, then slowly drink more
- Avoid alcohol and drinks with caffeine
- Do not give young children fruit juice or fizzy drinks

Source: [Dehydration](https://www.nhs.uk/conditions/dehydration/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_dh_young_child_not_peed`: Source difference: the Dehydration page says urgent for fewer wet nappies. The Sepsis page says 999 or A&E for no pee in 12 hours in a child under 5. The more urgent is used.
- `rf_dh_cannot_keep_fluids_down`: Clinical knowledge: someone who cannot keep any fluids down cannot rehydrate at home. The Dehydration page says to start with small sips.
- `rf_dh_baby`: The page says babies are more at risk of dehydration and to call 111 for advice for a child under 5. Making every baby under 1 urgent is AI judgement.
- `or_dh_unusually_tired`: The page lists feeling unusually tired as a sign of serious dehydration, and also lists feeling tired as an ordinary symptom of dehydration. Soft for that reason.
- `dehydration default outcome`: Soft: likely mild dehydration with a clear cause (heat, exercise, a tummy bug) lowers it to drinking more fluids at home. That reading of the page is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Diabetic ketoacidosis (DKA). This is when a lack of insulin makes you very ill. | 420422005 | rare | Breath smells fruity: strongly supports; Breathing faster and more deeply than usual: strongly supports; Blood sugar high and not coming down, or ketones raised: strongly supports; Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Keeps being sick and cannot keep fluids down: supports; Stomach ache: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Being sick: strongly supports; High ketones, or high blood sugar that insulin is not bringing down: strongly supports; Breathing very fast: supports; Losing weight without trying: supports; Feels very tired: supports |
| Heat exhaustion | 95868006 | uncommon | Unwell after being in the heat or exercising hard: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Feels sick or has been sick: supports; Feeling very thirsty all the time: supports; Feels very tired: supports; Signs of dehydration: supports |
| Heatstroke (the body overheating dangerously) | 52072009 | rare | Unwell after being in the heat or exercising hard: strongly supports; Hot skin that is not sweating: strongly supports; Still unwell after 30 minutes of cooling down: strongly supports; Suddenly confused: supports; Has had a seizure (fit): supports; Breathing very fast: supports; Heart beating very fast: supports |
| Mild dehydration (not having enough water in the body) |  | very common | Diarrhoea, or being sick: strongly supports; Feeling very thirsty all the time: strongly supports; Unwell after being in the heat or exercising hard: supports; Feels light-headed: supports; Signs of dehydration: strongly supports; Making much less pee than usual: supports; Feels sick or has been sick: supports; Feels very tired: supports |
| Serious dehydration (not having enough water in the body) |  | uncommon | Keeps being sick and cannot keep fluids down: strongly supports; Dizzy when standing up, and it does not go away: strongly supports; No pee for 12 hours or more: strongly supports; Heart beating very fast: supports; Child with dry nappies, sunken eyes or no tears: supports; Baby's soft spot on top of the head sinks inwards: supports; Diarrhoea, or being sick: supports; Feels very tired: supports; Child limp, floppy, hard to wake or not responding as usual: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
