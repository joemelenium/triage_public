# Review pack: Red eye

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
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Shingles](https://www.nhs.uk/conditions/shingles/) | 2026-11-18 |  | Page last reviewed: 23 November 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | 2026-11-19 |  | Page last reviewed: 10 September 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | 2026-11-19 |  | Page last reviewed: 03 October 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Stye](https://www.nhs.uk/conditions/stye/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |

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

## Red eye red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_re_chemical`<br>A chemical or other harmful liquid in the eye<br>**Note:** The Red eye page says the same. Kept firm: rinsing straight away and getting checked protects the sight. | "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Rinse the eye with clean water for at least 20 minutes, then go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_re_pierced_or_stuck`<br>Something sharp has pierced the eye, something hit it at high speed, or something is stuck in it<br>**Note:** The Eye injuries page gives the same advice for a pierced eye or something hitting it at high speed. 'Stuck' is read as not removed by rinsing (AI reading). | "Something sharp cut or pierced the eye" OR "Something hit the eye at high speed" OR "Something stuck in the eye that rinsing has not removed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_headache_and_sick`<br>Red eye with a severe headache and feeling or being sick<br>**Note:** Can be a sign of sudden glaucoma. The Eye pain and Dry eyes pages say the same. | "Very painful headache" AND "Feels sick or has been sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_pupil`<br>Red eye and 1 pupil bigger than the other<br>**Note:** The Herpes simplex eye infections page says the same. | "1 pupil bigger than the other" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_vision_change`<br>Red eye with any change to the sight, like wavy lines, flashing or loss of vision<br>**Note:** Source difference: the Red eye and Dry eyes pages say call 999 or go to A&E. The Conjunctivitis, Uveitis and Blepharitis pages say an urgent GP appointment or 111 for changes in vision. The more urgent is used, marked soft, with the firm urgent rule below as its floor. | "Change in sight or loss of vision" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_light`<br>Red eye and it hurts to look at light<br>**Note:** Source difference: the Red eye and Herpes simplex pages say call 999 or go to A&E. The Conjunctivitis and Uveitis pages say an urgent GP appointment or 111 for sensitivity to light. The more urgent is used, marked soft, with the firm urgent rule below as its floor. | "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_very_dark_red`<br>Eye or eyes very dark red<br>**Note:** Source difference: the Red eye page says call 999 or go to A&E for an eye that is very dark red. The Eyelid problems and Conjunctivitis pages say an urgent GP appointment for a very red eye. Soft, with the firm urgent rule for a very red eye as its floor. | "Eye very dark red" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_injury`<br>Red eye after an injury to the eye<br>**Note:** Source difference: the Red eye page says call 999 or go to A&E for any injury. The Eye injuries page says minor injuries often get better within a day, and gives an urgent appointment if not better after 24 hours. Soft, with the firm urgent rule below as its floor. | "Injured eye, or something hit the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E, or call 999* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_eyelid_infection_spreading`<br>Swollen eyelid with the eye hard or painful to move, a bulging eye, or changes to the sight: possible infection behind the eye<br>**Note:** The Cellulitis page says cellulitis in the eye is very serious. The signs used for infection spreading behind the eye are AI judgement. | "Swollen eyelid" AND ("Hard or painful to move the eye" OR "Eye hurts more when moving it" OR "Bulging eyes" OR "Change in sight or loss of vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Red eye red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_re_vision_or_light_urgent`<br>Red eye with changes to the sight or sensitivity to light<br>**Note:** The firm floor under the soft emergency rules above. The Uveitis and Blepharitis pages say the same. | "Change in sight or loss of vision" OR "Bright lights hurt the eyes or are bothering you" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | |
| `rf_re_injury_urgent`<br>Red eye after an injury to the eye<br>**Note:** The firm floor under the soft emergency rule for an injury. | "Injured eye, or something hit the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_re_very_red`<br>The white of the eye is very red<br>**Note:** The Conjunctivitis, Uveitis and Ectropion pages say the same. | "White of the eye very red" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_re_very_painful`<br>The eye is very painful and red | "Severe eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_painful`<br>Red eye that is painful<br>**Note:** The Dry eyes page says urgent for an eye that is painful and red, and the Conjunctivitis page for pain in the eyes. The Red eye page says urgent only when it is very painful. Soft, so that the gritty soreness of conjunctivitis can lower it; severe pain is firm (rule above). | "Eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_re_contact_lenses`<br>Red eye in someone who wears contact lenses: could be an eye infection<br>**Note:** The Dry eyes page says the same. | "Wears contact lenses" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111. Take your lenses out.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_newborn`<br>A baby less than 1 month old with a red eye<br>**Note:** The Red eye page says 28 days, the Conjunctivitis page 30 days, the Eyelid problems page 1 month. 1 month is used. | "Baby under 1 month old" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_re_eyelid_hot_swollen`<br>Swollen eyelid that is red, hot, painful, tender or blistered | "Swollen eyelid that is red, hot, painful, tender or blistered" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| `rf_re_shingles_or_blisters`<br>Red eye with blisters or a rash around the eye, such as shingles<br>**Note:** The Herpes simplex eye infections page lists blisters or a rash around the eye, and says to get urgent help if the eye is painful or getting worse. Making blisters with a red eye urgent on their own is AI judgement. | "Blisters or a rash on the eyelid or skin around the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today* | [Shingles](https://www.nhs.uk/conditions/shingles/) | |
| `rf_re_unwell`<br>Red eye with a high temperature, or feeling very unwell<br>**Note:** The Red eye page says a red eye is probably nothing serious if you do not feel sick or unwell. The Eyelid problems page says urgent for eye symptoms with a very high temperature or feeling unwell. Soft, since a cold often comes with conjunctivitis. | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |

## Red eye: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_re_child_under_2`<br>A child under 2 with a red eye<br>**Note:** The Conjunctivitis page says a child under 2 needs a prescription from a GP for treatment. | "Under 2 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `or_re_sticky`<br>Red eyes with a sticky discharge<br>**Note:** Source difference: the Red eye page says see a GP or optician. The Conjunctivitis page says a pharmacist can help, and to see a GP if it has not cleared within 7 days. Soft. | "Sticky discharge (pus) from the eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or optician. The source gives no fixed time.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `or_re_lasting`<br>Red patches, or an eyelid or eyelash problem, for more than a few days<br>**Note:** The Herpes simplex page says the same for a red eye with no pain for more than a few days. | "Red eye, or an eyelid or eyelash problem, for more than a few days" OR "Eyelashes grow inwards and rub the eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or optician. The source gives no fixed time.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `or_re_worried`<br>Worried about the eyes | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or optician. The source gives no fixed time.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |

## Default outcome

Used when no rule fires.

- **A red eye that does not hurt, with sight not affected and not feeling unwell: probably nothing serious**
- Outcome: Self-manageable, Self-care, No appointment needed. *It may get better on its own in a few days. A pharmacist can help.*
- Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/)
- **Note:** The page says that if the eye does not hurt, the sight is not affected and you do not feel sick or unwell, it is probably nothing serious and may get better on its own.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chemical or other harmful liquid in the eye | Has a chemical or other harmful liquid got in your eye? For example, bleach, oven cleaner, cement or plaster. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something sharp cut or pierced the eye | Has something sharp cut or pierced your eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something hit the eye at high speed | Did something hit your eye at high speed? For example, while hammering, drilling, grinding, using power tools or mowing. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something stuck in the eye that rinsing has not removed | Is something stuck in your eye that rinsing with water has not removed, such as a piece of glass, metal or grit? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| 1 pupil bigger than the other | Is 1 pupil (the black circle in the middle of the eye) bigger than the other? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Eye very dark red | Is your eye very dark red, rather than pink or bright red? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Swollen eyelid | Is your eyelid swollen? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Hard or painful to move the eye | Is it hard to move your eye, or does it not move as far as the other eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Eye hurts more when moving it | Does it hurt more when you move your eye? |  | **AI judgement, needs clinical review** | |
| Bulging eyes | Do your eyes look like they are bulging or sticking out more than usual? You may see more of the whites of your eyes. | 301919003 | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| White of the eye very red | Is the white of your eye very red, in part or all over? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Wears contact lenses | Do you wear contact lenses? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Baby under 1 month old | Is the person who is unwell a baby under 1 month old? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Swollen eyelid that is red, hot, painful, tender or blistered | Is the swollen eyelid hot, painful, tender, blistered or red? Redness may be harder to see on brown or black skin. |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Blisters or a rash on the eyelid or skin around the eye | Do you have blisters or a rash on your eyelid, or on the skin around your eye? |  | [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Under 2 years old | Is the person who is unwell under 2 years old? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Sticky discharge (pus) from the eye | Is sticky stuff (pus) coming from your eye, or are your eyelashes stuck together, for example when you wake up? |  | [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | |
| Red eye, or an eyelid or eyelash problem, for more than a few days | Has your eye been red, or had a problem with the eyelid or eyelashes, for more than a few days? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Eyelashes grow inwards and rub the eye | Do your eyelashes grow inwards and rub against your eye? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
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

### `advice_chemical_eye`

**What to do:** Rinse your eye with lots of clean water straight away, for at least 20 minutes. Then go to A&E or call 999.

**Look out for:**
- Pain or redness getting worse
- Changes to your sight

**Get more help when:**
- Keep rinsing your eye with water while you wait for help, or on the way to hospital
- Call 999 if you cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Take the container of the chemical with you, as the label may help with treatment. Do not drive yourself.

**What you can do yourself:**
- Hold your eye open and run clean, cool water over the eyeball. The flow should not be too strong.
- Take out contact lenses if you can do it easily
- Do not rub your eye

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/)

### `advice_eye_injury_ae`

**What to do:** Go to A&E now, or call 999. An injury like this needs to be checked in hospital to protect your sight.

**Look out for:**
- Changes to your sight
- Blood or pus coming from your eye
- Feeling or being sick

**Get more help when:**
- Call 999 if you cannot get to A&E safely, or if there is heavy bleeding

**Where to go:** Go to A&E. Some areas have an eye casualty (an emergency eye department) you may be sent to. Do not drive yourself. Ask someone to drive you or call 999.

**What you can do yourself:**
- Do not try to remove anything that has pierced your eye or is stuck in it
- Do not rub or press on your eye
- If you can, cover the eye loosely with something clean, such as a paper cup taped in place
- Do not wear contact lenses

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/), [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

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

### `advice_eye_urgent`

**What to do:** Get your eye checked today. Ask your GP surgery for an urgent appointment, or see an optician today if they can, or call 111.

**Look out for:**
- Any changes to your sight, like wavy lines, flashing or loss of vision
- It starting to hurt to look at light
- A severe headache and feeling sick
- Pain getting worse

**Get more help when:**
- Go to A&E or call 999 if you suddenly cannot see, or get sudden severe eye pain

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Many opticians can see eye problems on the same day, and some areas have a minor eye conditions service. In an emergency, go to A&E or call 999.

**What you can do yourself:**
- Do not rub your eye
- Do not wear contact lenses until your eye has been checked

Source: [Eye pain](https://www.nhs.uk/symptoms/eye-pain/), [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/)

### `advice_eye_contact_lens_urgent`

**What to do:** Take your contact lenses out and get your eye checked today. A red or painful eye when you wear lenses could be an infection on the clear front of the eye, which can harm your sight.

**Look out for:**
- Changes to your sight, or a white spot on the eye
- It hurting to look at light
- Pain getting worse

**Get more help when:**
- Go to A&E or call 999 if you have eye pain and your sight gets worse

**Where to go:** Ask your GP surgery or an optician for an urgent appointment, or call 111 or use 111 online. Take your lenses and their case with you.

**What you can do yourself:**
- Do not put your lenses back in until your eye has been checked
- Wear glasses instead

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

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

### `advice_red_eye_gp`

**What to do:** See a GP or an optician. They can find out what is causing your red eye and treat it.

**Look out for:**
- Pain in the eye, or it hurting to look at light
- Any changes to your sight
- The eye becoming very red

**Get more help when:**
- Ask for an urgent appointment or call 111 if your eye becomes very painful or very red
- Go to A&E or call 999 if your sight changes or it hurts to look at light

**Where to go:** Make an appointment with a GP, or see an optician. A pharmacist can also give advice.

**What you can do yourself:**
- Try not to touch or rub your eye
- Do not wear contact lenses until it has got better
- Wash your hands often, and do not share towels or pillows

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/)

### `advice_red_eye_self_care`

**What to do:** A red eye that does not hurt, with your sight not affected, is probably nothing serious. It may get better on its own in a few days.

**Look out for:**
- Pain in the eye, or it hurting to look at light
- Any changes to your sight
- Sticky stuff (pus) from the eye
- The redness lasting more than a few days

**Get more help when:**
- See a GP or optician if it lasts more than a few days or you are worried
- Ask for an urgent appointment or call 111 if it becomes painful
- Call 999 or go to A&E if your sight changes or it hurts to look at light

**Where to go:** You do not need an appointment now. A pharmacist can tell you what you can do, or if you need to see a GP or optician.

**What you can do yourself:**
- Try not to touch or rub your eye
- Do not wear contact lenses until it has got better
- Wash your hands often, and do not share towels

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_re_chemical`: The Red eye page says the same. Kept firm: rinsing straight away and getting checked protects the sight.
- `rf_re_pierced_or_stuck`: The Eye injuries page gives the same advice for a pierced eye or something hitting it at high speed. 'Stuck' is read as not removed by rinsing (AI reading).
- `rf_re_headache_and_sick`: Can be a sign of sudden glaucoma. The Eye pain and Dry eyes pages say the same.
- `rf_re_pupil`: The Herpes simplex eye infections page says the same.
- `rf_re_vision_change`: Source difference: the Red eye and Dry eyes pages say call 999 or go to A&E. The Conjunctivitis, Uveitis and Blepharitis pages say an urgent GP appointment or 111 for changes in vision. The more urgent is used, marked soft, with the firm urgent rule below as its floor.
- `rf_re_light`: Source difference: the Red eye and Herpes simplex pages say call 999 or go to A&E. The Conjunctivitis and Uveitis pages say an urgent GP appointment or 111 for sensitivity to light. The more urgent is used, marked soft, with the firm urgent rule below as its floor.
- `rf_re_very_dark_red`: Source difference: the Red eye page says call 999 or go to A&E for an eye that is very dark red. The Eyelid problems and Conjunctivitis pages say an urgent GP appointment for a very red eye. Soft, with the firm urgent rule for a very red eye as its floor.
- `rf_re_injury`: Source difference: the Red eye page says call 999 or go to A&E for any injury. The Eye injuries page says minor injuries often get better within a day, and gives an urgent appointment if not better after 24 hours. Soft, with the firm urgent rule below as its floor.
- `rf_re_eyelid_infection_spreading`: The Cellulitis page says cellulitis in the eye is very serious. The signs used for infection spreading behind the eye are AI judgement.
- `rf_re_vision_or_light_urgent`: The firm floor under the soft emergency rules above. The Uveitis and Blepharitis pages say the same.
- `rf_re_injury_urgent`: The firm floor under the soft emergency rule for an injury.
- `rf_re_very_red`: The Conjunctivitis, Uveitis and Ectropion pages say the same.
- `rf_re_painful`: The Dry eyes page says urgent for an eye that is painful and red, and the Conjunctivitis page for pain in the eyes. The Red eye page says urgent only when it is very painful. Soft, so that the gritty soreness of conjunctivitis can lower it; severe pain is firm (rule above).
- `rf_re_contact_lenses`: The Dry eyes page says the same.
- `rf_re_newborn`: The Red eye page says 28 days, the Conjunctivitis page 30 days, the Eyelid problems page 1 month. 1 month is used.
- `rf_re_shingles_or_blisters`: The Herpes simplex eye infections page lists blisters or a rash around the eye, and says to get urgent help if the eye is painful or getting worse. Making blisters with a red eye urgent on their own is AI judgement.
- `rf_re_unwell`: The Red eye page says a red eye is probably nothing serious if you do not feel sick or unwell. The Eyelid problems page says urgent for eye symptoms with a very high temperature or feeling unwell. Soft, since a cold often comes with conjunctivitis.
- `or_re_child_under_2`: The Conjunctivitis page says a child under 2 needs a prescription from a GP for treatment.
- `or_re_sticky`: Source difference: the Red eye page says see a GP or optician. The Conjunctivitis page says a pharmacist can help, and to see a GP if it has not cleared within 7 days. Soft.
- `or_re_lasting`: The Herpes simplex page says the same for a red eye with no pain for more than a few days.
- `red_eye default outcome`: The page says that if the eye does not hurt, the sight is not affected and you do not feel sick or unwell, it is probably nothing serious and may get better on its own.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Eye allergy, for example from hay fever (allergic conjunctivitis) | 473460002 | uncommon | Itchy eyes: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Both eyes affected: supports; Has eczema, hay fever or a food allergy: supports; Watering eyes: supports; Swollen eyelid: supports; Red or bloodshot eye: supports |
| Sudden glaucoma (a quick build-up of pressure inside the eye) |  | rare | Severe eye pain: strongly supports; Glowing rings (halos) around lights: strongly supports; Headache: strongly supports; Feels sick or has been sick: strongly supports; Very painful headache: supports; Blurred, cloudy or misty sight: supports; White of the eye very red: supports; Front of the eye looks cloudy, or has a white spot: supports; Eye pain or other eye symptoms started suddenly: supports; Red or bloodshot eye: supports |
| Arc eye (a burn to the surface of the eye from welding or sunbed light) | 1714005 | very rare | Welding, or a sunbed, without eye protection in the last day: strongly supports; Both eyes affected: strongly supports; Gritty, scratchy or burning feeling in the eye: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports |
| Blepharitis (swollen, itchy, crusty eyelid edges) | 41446000 | uncommon | Itchy, sore or crusty eyelid edges: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Sticky discharge (pus) from the eye: supports; Dry eyes: supports |
| Serious injury from a blow to the eye (bleeding inside the eye or a broken eye socket) |  | very rare | Hit in the eye by something blunt: strongly supports; Injured eye, or something hit the eye: strongly supports; Double vision: supports; Hard or painful to move the eye: supports; Severe eye pain: supports; Feels sick or has been sick: supports; Change in sight or loss of vision: supports |
| Chemical in the eye |  | very rare | Chemical or other harmful liquid in the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Watering eyes: supports |
| Conjunctivitis (a red, sticky eye infection) | 299699004 | uncommon | Sticky discharge (pus) from the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Red or bloodshot eye: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Watering eyes: supports; Cough or runny nose: supports |
| Scratch on the clear front of the eye (corneal abrasion) | 85848002 | rare | Injured eye, or something hit the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Feels like something is in the eye: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| Episcleritis (a red patch on the white of the eye, with mild soreness) | 815008 | rare | Redness in one patch of the white of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports |
| Skin infection of the eyelid and the skin around the eye | 314516007 | rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Swollen eyelid: strongly supports; Red, painful lump near the edge of the eyelid: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Eyelid turning outwards or inwards, or eyelashes rubbing the eye |  | rare | Eyelid has changed shape, turns inwards or droops away from the eye: strongly supports; Eyelashes grow inwards and rub the eye: strongly supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Eye waters all the time, with tears running down the cheek: supports; Red or bloodshot eye: supports |
| Something on the surface of the eye, such as dust, grit or an eyelash | 450671000124109 | uncommon | Feels like something is in the eye: strongly supports; Watering eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Red or bloodshot eye: supports |
| Herpes simplex eye infection (an eye infection caused by the cold sore virus) | 9389005 | rare | Has had cold sores or a herpes eye infection: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Weakened immune system: supports; Swollen eyelid: supports |
| Infection inside the eye after surgery or an injection in the eye | 1847009 | very rare | Eye surgery or eye treatment in the last 4 weeks: strongly supports; Severe eye pain: strongly supports; Change in sight or loss of vision: strongly supports; Red or bloodshot eye: supports; Sticky discharge (pus) from the eye: supports |
| Keratitis or an eye ulcer (a sore on the clear front of the eye), often from contact lenses | 5888003 | rare | Wears contact lenses: strongly supports; Front of the eye looks cloudy, or has a white spot: strongly supports; Eye pain: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Red or bloodshot eye: supports; Watering eyes: supports; Blurred, cloudy or misty sight: supports; Feels like something is in the eye: supports |
| Infection behind the eye (orbital cellulitis) | 194005002 | very rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Hard or painful to move the eye: strongly supports; Swollen eyelid: strongly supports; Bulging eyes: supports; Eye hurts more when moving it: supports; Very high temperature, or feels hot, cold or shivery: supports; Change in sight or loss of vision: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |
| A cut through the eye, or something inside the eye |  | very rare | Something sharp cut or pierced the eye: strongly supports; Something hit the eye at high speed: strongly supports; Injured eye, or something hit the eye: strongly supports; Change in sight or loss of vision: supports; Eye pain: supports |
| Scleritis (painful swelling of the white outer layer of the eye) | 78370002 | rare | Deep, boring ache in the eye: strongly supports; Eye very dark red: strongly supports; Eye pain keeps them awake at night: supports; Severe eye pain: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Redness in one patch of the white of the eye: supports |
| Shingles near the eye (a painful rash of blisters on one side of the forehead, eyelid or nose) | 87513003 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Shingles rash on or near the eye or nose, or changes to vision: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Swollen eyelid: supports |
| Burst blood vessel in the eye (a bright red patch on the white of the eye) |  | common | Flat, bright red patch on the white of the eye: strongly supports; Takes medicine that thins the blood, or bleeds easily: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Injured eye, or something hit the eye: supports |
| Iritis or uveitis (swelling inside the eye that makes it red, sore and hurt in bright light) | 128473001 | rare | Bright lights hurt the eyes or are bothering you: strongly supports; Redness worst in a ring around the coloured part of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: strongly supports; Deep, boring ache in the eye: supports; Blurred, cloudy or misty sight: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Floaters or flashes in the eyes: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
