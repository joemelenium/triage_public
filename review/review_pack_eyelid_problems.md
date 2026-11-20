# Review pack: Eyelid problems

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
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | 2026-11-19 |  | Page last reviewed: 18 August 2023 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Ectropion](https://www.nhs.uk/conditions/ectropion/) | 2026-11-19 |  | Page last reviewed: 17 July 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | 2026-11-19 |  | Page last reviewed: 10 September 2026 |
| [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | 2026-11-19 |  | Page last reviewed: 12 November 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Stye](https://www.nhs.uk/conditions/stye/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Shingles](https://www.nhs.uk/conditions/shingles/) | 2026-11-18 |  | Page last reviewed: 23 November 2023 |
| [Blepharitis](https://www.nhs.uk/conditions/blepharitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2025 |

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

## Eyelid problems red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_el_allergic_swelling`<br>Swollen eyelids with the lips, mouth, tongue or throat suddenly swollen: possible severe allergic reaction | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_el_infection_behind_eye`<br>Swollen eyelid with the eye hard or painful to move, a bulging eye, or changes to the sight: possible infection behind the eye<br>**Note:** The Cellulitis page says cellulitis in the eye is very serious. The signs used for infection spreading behind the eye are AI judgement. | "Swollen eyelid" AND ("Hard or painful to move the eye" OR "Eye hurts more when moving it" OR "Bulging eyes" OR "Change in sight or loss of vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_el_infection_very_unwell`<br>Red, hot, swollen eyelid with a very high temperature, feeling very unwell, or feeling faint or confused<br>**Note:** The Cellulitis page says call 999 or go to A&E for cellulitis with feeling dizzy or faint, or other signs of serious illness. A high temperature alone is urgent (Eyelid problems page). | "Swollen eyelid that is red, hot, painful, tender or blistered" AND ("Feels very unwell" OR "Feels light-headed") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_el_droop_and_pupil`<br>An eyelid drooping for the first time with 1 pupil bigger or smaller than the other<br>**Note:** The Cluster headaches page says call 999 or go to A&E for either sign for the first time. Clinical knowledge: together they can mean a nerve to the eye is being pressed on. | "Eyelid started drooping suddenly" AND "1 pupil bigger than the other" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |
| `rf_el_droop_and_headache`<br>An eyelid that has suddenly started drooping, with a severe headache<br>**Note:** The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time, and the Double vision page for a severe headache with double vision. Clinical knowledge: a painful new droop can be a brain aneurysm pressing on a nerve to the eye. Firm: myasthenia gravis, the milder cause of a droop, does not cause a severe headache. | "Eyelid started drooping suddenly" AND "Very painful headache" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |
| `rf_el_droop_and_double`<br>An eyelid that has suddenly started drooping, with double vision<br>**Note:** The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time. The Eyelid problems page says urgent for an eyelid that droops suddenly, which stays as the floor. Clinical knowledge: with double vision it can be a brain aneurysm. Soft, because myasthenia gravis can also cause this. The severe headache part is a separate firm rule. | "Eyelid started drooping suddenly" AND "Double vision" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |

## Eyelid problems red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_el_hot_swollen`<br>Swollen eyelid that is red, hot, painful, tender or blistered | "Swollen eyelid that is red, hot, painful, tender or blistered" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_droops_suddenly`<br>Eyelid droops suddenly | "Eyelid started drooping suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_cannot_open`<br>Cannot open the eye or keep it open | "Cannot open the eye or keep it open" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_eye_symptoms`<br>A very red eye, sensitivity to light, or changes to the sight | "White of the eye very red" OR "Bright lights hurt the eyes or are bothering you" OR "Change in sight or loss of vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_eye_pain`<br>Pain in the eye itself, not only the eyelid<br>**Note:** The page says urgent if the pain is in your eye, not your eyelid. The eye pain question also covers pain around the eye, such as a painful stye, so the rule is soft: a likely stye can lower it. The Stye page says urgent only if a stye is very painful or swollen. | "Eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_headache_or_sick`<br>Eye symptoms with a headache, or feeling or being sick | "Headache" OR "Feels sick or has been sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_newborn_sticky`<br>A baby less than 1 month old with a sticky, red eye | "Baby under 1 month old" AND ("Sticky discharge (pus) from the eye" OR "Red or bloodshot eye") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_temperature_unwell`<br>A very high temperature, feeling hot, cold or shivery, or feeling generally unwell | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_allergy`<br>Swollen eyelids that may be an allergic reaction<br>**Note:** The page says urgent if you think it is an allergic reaction. Using a reaction to a food, medicine or sting to mark this is AI judgement. | "Swollen eyelid" AND "Started soon after a food, medicine or insect sting" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_el_shingles_or_blisters`<br>Blisters or a rash on the eyelid or around the eye<br>**Note:** The page says urgent for a swollen eyelid that is blistered. The Shingles page says urgent for a rash near the eye. | "Blisters or a rash on the eyelid or skin around the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |

## Eyelid problems red flags: Soon (help within a few days)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_el_lump_growing`<br>An eyelid lump that is growing, bleeding or crusting: possible skin cancer<br>**Note:** Clinical knowledge: a lump on the eyelid that grows, bleeds or does not heal can be a skin cancer and should be checked soon. The Eyelid problems page says see a GP for symptoms that last a long time. | "Eyelid lump growing, bleeding or crusting, or eyelashes falling out" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within a few days* | **AI judgement, needs clinical review** | |

## Eyelid problems: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_el_lasting`<br>Eyelid symptoms not improving or lasting a long time<br>**Note:** The Stye page says see a GP if a stye does not get better within a few weeks. | "Eyelid lump lasting weeks, or not better with pharmacy treatment" OR "Red eye, or an eyelid or eyelash problem, for more than a few days" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `or_el_yellow`<br>Yellow lumps or patches around the eyes | "Yellow lumps or patches around the eyes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `or_el_turning_or_drooping`<br>Eyelid turning inwards or outwards, eyelashes rubbing the eye, or a drooping eyelid<br>**Note:** The Ectropion page says see a GP if you think you have it. Including a slowly drooping eyelid is AI judgement: the Eyelid problems page says this is common with age, but a GP can check it. | "Eyelid has changed shape, turns inwards or droops away from the eye" OR "Eyelashes grow inwards and rub the eye" OR "Upper eyelid droops" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Ectropion](https://www.nhs.uk/conditions/ectropion/) | |
| `or_el_worried`<br>Worried about an eyelid problem | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |

## Default outcome

Used when no rule fires.

- **An eyelid problem with nothing that needs more help: most are harmless**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most eyelid problems are harmless. A pharmacist can help.*
- Source: [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Eyelid problem | Do you have a problem with your eyelid? For example, a lump, swelling, drooping, or an itchy, sticky or sore eyelid. |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Swollen eyelid | Is your eyelid swollen? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Hard or painful to move the eye | Is it hard to move your eye, or does it not move as far as the other eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Eye hurts more when moving it | Does it hurt more when you move your eye? |  | **AI judgement, needs clinical review** | |
| Bulging eyes | Do your eyes look like they are bulging or sticking out more than usual? You may see more of the whites of your eyes. | 301919003 | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Swollen eyelid that is red, hot, painful, tender or blistered | Is the swollen eyelid hot, painful, tender, blistered or red? Redness may be harder to see on brown or black skin. |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Eyelid started drooping suddenly | Did the eyelid start drooping suddenly, in the last few days? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| 1 pupil bigger than the other | Is 1 pupil (the black circle in the middle of the eye) bigger than the other? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Cannot open the eye or keep it open | Is your eye so swollen or sore that you cannot open it or keep it open? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| White of the eye very red | Is the white of your eye very red, in part or all over? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Headache | Do you have a headache? | 25064002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Baby under 1 month old | Is the person who is unwell a baby under 1 month old? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Sticky discharge (pus) from the eye | Is sticky stuff (pus) coming from your eye, or are your eyelashes stuck together, for example when you wake up? |  | [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Started soon after a food, medicine or insect sting | Did this start soon after eating a food, taking a medicine or being stung by an insect? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Blisters or a rash on the eyelid or skin around the eye | Do you have blisters or a rash on your eyelid, or on the skin around your eye? |  | [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | |
| Eyelid lump growing, bleeding or crusting, or eyelashes falling out | Is the lump growing, bleeding or crusting, or are the eyelashes falling out around it? |  | **AI judgement, needs clinical review** | |
| Eyelid lump lasting weeks, or not better with pharmacy treatment | Has the lump lasted more than a few weeks, or not got better with treatment from a pharmacist? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Red eye, or an eyelid or eyelash problem, for more than a few days | Has your eye been red, or had a problem with the eyelid or eyelashes, for more than a few days? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Yellow lumps or patches around the eyes | Are there flat yellow lumps or patches on your eyelids or around your eyes? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Eyelid has changed shape, turns inwards or droops away from the eye | Has the shape of your eyelid changed, or is it turning inwards or drooping away from the eye? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Eyelashes grow inwards and rub the eye | Do your eyelashes grow inwards and rub against your eye? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Upper eyelid droops | Does your upper eyelid droop? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
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

### `advice_anaphylaxis_999`

**What to do:** Call 999 now and say you think it is anaphylaxis, a severe allergic reaction. Use an adrenaline auto-injector (such as an EpiPen) straight away if you have one.

**Look out for:**
- Swelling of the lips, mouth, tongue or throat
- Struggling to breathe, or very wheezy
- Skin, tongue or lips turning blue, grey or pale
- Feeling faint, very confused or drowsy

**Get more help when:**
- If you are no better after 5 minutes, use a second auto-injector if you have one
- Call 999 again if the person gets worse or stops responding

**Where to go:** Call 999 for an ambulance. Do not drive to A&E. Stay with the person until help arrives.

**What you can do yourself:**
- Lie down. You can raise your legs. If you are struggling to breathe, sit up slowly.
- If you are pregnant, lie on your left side
- If you were stung by an insect, try to remove the sting if it is still in the skin
- Do not stand or walk at any time, even if you feel better

Source: [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/)

### `advice_eye_infection_spreading`

**What to do:** Go to A&E now, or call 999. Your answers suggest an infection that may be spreading behind the eye. This is very serious and needs treatment in hospital.

**Look out for:**
- Your eye bulging or becoming harder to move
- Changes to your sight
- Feeling very unwell, confused, dizzy or faint
- Cold, clammy or pale skin

**Get more help when:**
- Call 999 if you get worse quickly or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/), [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/), [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

### `advice_eye_emergency`

**What to do:** Go to A&E or call 999 now. Your eye symptoms need to be checked in hospital straight away to protect your sight.

**Look out for:**
- Your sight getting worse
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech
- Pain getting worse, or feeling or being sick

**Get more help when:**
- Call 999 if you get any signs of a stroke, or you cannot get to A&E safely

**Where to go:** Go to A&E. If there is an eye casualty (an emergency eye department) near you, the 111 service or A&E may send you there. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

**What you can do yourself:**
- Do not rub your eye
- If you wear contact lenses, take them out and bring them with you

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/), [Vision loss](https://www.nhs.uk/conditions/vision-loss/), [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

### `advice_eyelid_urgent`

**What to do:** Get this checked today. Ask your GP surgery or an optician for an urgent appointment, or call 111.

**Look out for:**
- Your eye becoming harder or more painful to move
- Your eye starting to bulge
- Changes to your sight
- Feeling very unwell, dizzy or faint

**Get more help when:**
- Go to A&E or call 999 if the swelling spreads quickly, your sight changes, or it hurts to move your eye

**Where to go:** Ask your GP surgery or an optician for an urgent appointment, or call 111 or use 111 online. In an emergency, go to A&E or call 999.

**What you can do yourself:**
- Do not try to burst a lump on your eyelid
- Do not wear contact lenses or eye make-up until it has got better

Source: [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/), [Cellulitis](https://www.nhs.uk/conditions/cellulitis/), [Stye](https://www.nhs.uk/conditions/stye/)

### `advice_baby_eye_urgent`

**What to do:** Get your baby's eye checked today. Ask your GP surgery for an urgent appointment or call 111. Sticky, red eyes in a baby under 1 month old need to be seen quickly.

**Look out for:**
- Your baby having a high temperature, or being floppy or hard to wake
- The eyelids getting very swollen
- Your baby not feeding well

**Get more help when:**
- Call 999 or go to A&E if your baby seems very unwell, or is floppy or hard to wake

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Gently wipe away any sticky stuff with cotton wool soaked in boiled water that has cooled. Use a new piece for each eye.
- Wash your hands before and after touching your baby's eyes

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/)

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

### `advice_eyelid_soon`

**What to do:** See a GP in the next few days. A lump on the eyelid that grows, bleeds or does not heal should be checked to rule out skin cancer.

**Look out for:**
- The lump growing quickly
- The lump bleeding or turning into a sore

**Get more help when:**
- Ask for an urgent appointment or call 111 if the area becomes hot, red and swollen

**Where to go:** Make an appointment with a GP for the next few days.

Source: **AI judgement, needs clinical review**, [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

### `advice_eyelid_gp`

**What to do:** See a GP. They can check your eyelid and suggest treatment.

**Look out for:**
- The eyelid becoming red, hot, painful or swollen
- The eyelid drooping suddenly
- Changes to your sight

**Get more help when:**
- Ask for an urgent appointment or call 111 if the eyelid gets red, hot and sore. Also if it droops suddenly.

**Where to go:** Make an appointment with a GP. A pharmacist or optician can also give advice.

Source: [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

### `advice_eyelid_self_care`

**What to do:** Most eyelid problems are harmless and get better on their own. A pharmacist can help.

**Look out for:**
- The eyelid becoming red, hot, painful or swollen
- Pain in your eye, or changes to your sight
- A lump that does not go away after a few weeks

**Get more help when:**
- See a GP if it is not getting better or lasts a long time
- Ask for an urgent appointment or call 111 if the eyelid becomes red, hot and painful, or you feel unwell

**Where to go:** You do not need an appointment now. A pharmacist can tell you what you can do, or if you need to see a GP or optician.

**What you can do yourself:**
- Hold a clean, warm flannel on the eyelid for 5 to 10 minutes, 2 to 4 times a day
- Clean the edges of your eyelids gently with cotton wool and warm water
- Do not try to burst a lump on your eyelid
- Do not wear contact lenses or eye make-up until it has got better

Source: [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/), [Stye](https://www.nhs.uk/conditions/stye/), [Blepharitis](https://www.nhs.uk/conditions/blepharitis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_el_infection_behind_eye`: The Cellulitis page says cellulitis in the eye is very serious. The signs used for infection spreading behind the eye are AI judgement.
- `rf_el_infection_very_unwell`: The Cellulitis page says call 999 or go to A&E for cellulitis with feeling dizzy or faint, or other signs of serious illness. A high temperature alone is urgent (Eyelid problems page).
- `rf_el_droop_and_pupil`: The Cluster headaches page says call 999 or go to A&E for either sign for the first time. Clinical knowledge: together they can mean a nerve to the eye is being pressed on.
- `rf_el_droop_and_headache`: The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time, and the Double vision page for a severe headache with double vision. Clinical knowledge: a painful new droop can be a brain aneurysm pressing on a nerve to the eye. Firm: myasthenia gravis, the milder cause of a droop, does not cause a severe headache.
- `rf_el_droop_and_double`: The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time. The Eyelid problems page says urgent for an eyelid that droops suddenly, which stays as the floor. Clinical knowledge: with double vision it can be a brain aneurysm. Soft, because myasthenia gravis can also cause this. The severe headache part is a separate firm rule.
- `rf_el_eye_pain`: The page says urgent if the pain is in your eye, not your eyelid. The eye pain question also covers pain around the eye, such as a painful stye, so the rule is soft: a likely stye can lower it. The Stye page says urgent only if a stye is very painful or swollen.
- `rf_el_allergy`: The page says urgent if you think it is an allergic reaction. Using a reaction to a food, medicine or sting to mark this is AI judgement.
- `rf_el_shingles_or_blisters`: The page says urgent for a swollen eyelid that is blistered. The Shingles page says urgent for a rash near the eye.
- `rf_el_lump_growing`: Clinical knowledge: a lump on the eyelid that grows, bleeds or does not heal can be a skin cancer and should be checked soon. The Eyelid problems page says see a GP for symptoms that last a long time.
- `or_el_lasting`: The Stye page says see a GP if a stye does not get better within a few weeks.
- `or_el_turning_or_drooping`: The Ectropion page says see a GP if you think you have it. Including a slowly drooping eyelid is AI judgement: the Eyelid problems page says this is common with age, but a GP can check it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Harmless twitching, often from stress, tiredness or caffeine |  | very common | Twitch in the eyelid: strongly supports; Having a lot of caffeine or alcohol: supports; Going through a stressful time or big life change: supports; Feels very tired: supports; Getting less sleep than needed: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Dry eyes: supports |
| Eye allergy, for example from hay fever (allergic conjunctivitis) | 473460002 | uncommon | Itchy eyes: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Both eyes affected: supports; Has eczema, hay fever or a food allergy: supports; Watering eyes: supports; Swollen eyelid: supports; Red or bloodshot eye: supports |
| Blepharitis (swollen, itchy, crusty eyelid edges) | 41446000 | uncommon | Itchy, sore or crusty eyelid edges: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Sticky discharge (pus) from the eye: supports; Dry eyes: supports |
| A swelling in a blood vessel in the brain (brain aneurysm) pressing on a nerve to the eye | 783421002 | very rare | 1 pupil bigger than the other: strongly supports; Eyelid started drooping suddenly: strongly supports; Double vision started suddenly: strongly supports; Eye pain: supports; Headache: supports; Very painful headache: supports |
| Chalazion (a firm, painless lump in the eyelid from a blocked gland) | 1482004 | common | Firm lump on the eyelid that is not very painful: strongly supports; Lump on or in the eyelid: strongly supports; Eyelid lump lasting weeks, or not better with pharmacy treatment: supports; Itchy, sore or crusty eyelid edges: supports |
| Conjunctivitis (a red, sticky eye infection) | 299699004 | uncommon | Sticky discharge (pus) from the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Red or bloodshot eye: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Watering eyes: supports; Cough or runny nose: supports |
| Drooping eyelid that comes on slowly with age (ptosis) | 271429007 | uncommon | Upper eyelid droops: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Eye surgery or eye treatment in the last 4 weeks: supports |
| A weak nerve to the eye muscles, often linked to diabetes or high blood pressure |  | rare | Double vision started suddenly: strongly supports; Double vision goes when either eye is covered: strongly supports; Eye pain: supports; Upper eyelid droops: supports; Has diabetes: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports |
| Skin infection of the eyelid and the skin around the eye | 314516007 | rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Swollen eyelid: strongly supports; Red, painful lump near the edge of the eyelid: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Skin cancer on the eyelid | 231829006 | very rare | Eyelid lump growing, bleeding or crusting, or eyelashes falling out: strongly supports; Eyelid lump lasting weeks, or not better with pharmacy treatment: strongly supports; Lump on or in the eyelid: strongly supports; Firm lump on the eyelid that is not very painful: supports |
| Eyelid turning outwards or inwards, or eyelashes rubbing the eye |  | rare | Eyelid has changed shape, turns inwards or droops away from the eye: strongly supports; Eyelashes grow inwards and rub the eye: strongly supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Eye waters all the time, with tears running down the cheek: supports; Red or bloodshot eye: supports |
| Herpes simplex eye infection (an eye infection caused by the cold sore virus) | 9389005 | rare | Has had cold sores or a herpes eye infection: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Weakened immune system: supports; Swollen eyelid: supports |
| Myasthenia gravis (muscles that get weak and tired, often in the eyelids and eyes first) | 91637004 | rare | Drooping eyelid or double vision worse when tired: strongly supports; Upper eyelid droops: strongly supports; Difficulty speaking: supports; Double vision: supports; Double vision goes when either eye is covered: supports |
| Infection behind the eye (orbital cellulitis) | 194005002 | very rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Hard or painful to move the eye: strongly supports; Swollen eyelid: strongly supports; Bulging eyes: supports; Eye hurts more when moving it: supports; Very high temperature, or feels hot, cold or shivery: supports; Change in sight or loss of vision: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |
| Shingles near the eye (a painful rash of blisters on one side of the forehead, eyelid or nose) | 87513003 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Shingles rash on or near the eye or nose, or changes to vision: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Swollen eyelid: supports |
| Stye (a small, painful lump on the eyelid) | 397513003 | rare | Red, painful lump near the edge of the eyelid: strongly supports; Lump on or in the eyelid: strongly supports; Swollen eyelid: supports; Watering eyes: supports |
| Thyroid eye problems (swelling behind the eyes linked to a thyroid condition) | 276177000 | rare | Has a thyroid problem, such as an overactive thyroid: strongly supports; Bulging eyes: strongly supports; Both eyes affected: supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Double vision: supports; Swollen eyelid: supports; Smokes, or has smoked in the past: supports |
| Yellow patches on the eyelids (xanthelasma) | 238951005 | uncommon | Yellow lumps or patches around the eyes: strongly supports; Lump on or in the eyelid: supports; Both eyes affected: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
