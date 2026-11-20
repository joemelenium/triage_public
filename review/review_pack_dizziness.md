# Review pack: Dizziness

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
| [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/) | 2026-11-19 |  | Page last reviewed: 11 September 2026 |
| [Vertigo](https://www.nhs.uk/conditions/vertigo/) | 2026-11-19 |  | Page last reviewed: 02 May 2023 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Labyrinthitis and vestibular neuritis](https://www.nhs.uk/conditions/labyrinthitis/) | 2026-11-19 |  | Page last reviewed: 06 August 2026 |
| [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | 2026-11-19 |  | Page last reviewed: 16 December 2025 |
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | 2026-11-19 |  | Page last reviewed: 21 April 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | 2026-11-19 |  | Page last reviewed: 04 January 2024 |
| [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | 2026-11-19 |  | Page last reviewed: 30 May 2025 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |

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

## Dizziness red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dz_stroke_signs`<br>Dizziness with numbness or weakness in the face, arms or legs, or difficulty speaking<br>**Note:** Source difference: the Dizziness page says see a GP if your face, arms or legs feel numb or weak, or you find it harder to speak. The Vertigo page says call 999 or go to A&E. The Ménière's disease and Stroke pages say call 999, because these can be signs of a stroke. The most urgent is used. | "Numbness or weakness in the face, arms or legs" OR "Difficulty speaking" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/) | |
| `rf_dz_vision_loss`<br>Dizziness with loss of vision<br>**Note:** The Ménière's disease page says call 999 for spinning with sudden problems with the vision in one eye. The Vertigo page says 999 or A&E for loss of vision. | "Cannot see out of 1 or both eyes, or a large part of the sight is missing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/) | |
| `rf_dz_spinning_double_vision`<br>Spinning (vertigo) with double vision or other changes to vision<br>**Note:** The Vertigo page names double vision. It is a separate observation from other changes in sight, so it is named here too. | "Feels like you or the room is spinning (vertigo)" AND ("Change in sight or loss of vision" OR "Double vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_spinning_tingling`<br>Spinning (vertigo) with tingling or pins and needles<br>**Note:** The Vertigo page says call 999 or go to A&E for vertigo with leg or arm weakness, numbness or tingling. Numbness and weakness are covered by the firm stroke rule above. Tingling alone is soft, because long-standing tingling (for example from a trapped nerve) and the tingling of a migraine aura are common. | "Feels like you or the room is spinning (vertigo)" AND "Pins and needles, tingling or numbness" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_spinning_off_balance`<br>Spinning (vertigo) and feeling very off-balance, finding it hard to walk<br>**Note:** The Ménière's disease page says call 999 for spinning with feeling very off-balance, as a sign of a stroke. The Labyrinthitis page lists finding it difficult to stay upright or walk in a straight line as a usual symptom. Soft, with the urgent rule below as its floor. Needs clinical review: telling a stroke from labyrinthitis needs an examination. | "Feels like you or the room is spinning (vertigo)" AND "Finding it hard to balance or walk" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/) | |
| `rf_dz_spinning_hearing`<br>Spinning (vertigo) with hearing loss<br>**Note:** Source difference: the Vertigo page says call 999 or go to A&E for vertigo with hearing loss. The Labyrinthitis page lists hearing loss and ringing as usual symptoms and says an urgent GP appointment or 111 for sudden hearing loss in one ear. The Ménière's disease page says see a GP. The most urgent is used, marked soft, with the urgent rule below as its floor. Ringing in the ears (tinnitus) is not on the Vertigo page's list. A yes to it brings in the tinnitus entry symptom, whose own soft A&E rule for tinnitus with vertigo (Tinnitus page) then applies, so it is not repeated here. | "Feels like you or the room is spinning (vertigo)" AND "Hearing loss or a change in hearing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_headache_sudden`<br>Dizziness with a headache that came on suddenly and is extremely painful | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |

## Dizziness red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dz_off_balance`<br>Dizziness and finding it hard to balance or walk<br>**Note:** AI judgement: a floor under the soft 999 rule above, so that someone who cannot walk straight is checked the same day. | "Finding it hard to balance or walk" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_dz_spinning_hearing_urgent`<br>Spinning (vertigo) with hearing loss: the floor under the soft rule above<br>**Note:** The Labyrinthitis page says an urgent GP appointment or 111 for sudden hearing loss in one ear. Hearing loss that comes on quickly can need treatment within days to save the hearing. | "Feels like you or the room is spinning (vertigo)" AND "Hearing loss or a change in hearing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Labyrinthitis and vestibular neuritis](https://www.nhs.uk/conditions/labyrinthitis/) | |
| `rf_dz_spinning_severe_headache`<br>Spinning (vertigo) with a severe headache<br>**Note:** The Vertigo page says this for a severe headache. Firm. The soft rule below covers any headache. | "Feels like you or the room is spinning (vertigo)" AND "Very painful headache" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_spinning_being_sick`<br>Spinning (vertigo) and being sick | "Feels like you or the room is spinning (vertigo)" AND "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_spinning_temperature`<br>Spinning (vertigo) with a very high temperature, or feeling hot, cold or shivery | "Feels like you or the room is spinning (vertigo)" AND "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_spinning_headache`<br>Spinning (vertigo) with a headache<br>**Note:** The Vertigo page says a severe headache. The question asks about any headache, so the rule is soft: migraine often causes both. | "Feels like you or the room is spinning (vertigo)" AND "Headache" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| `rf_dz_others_unwell`<br>Dizziness, and other people at home or pets unwell too: possible carbon monoxide poisoning | "Others at home, or pets, unwell with similar symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Go outside into fresh air, then call NHS 111 now* | [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | |
| `rf_dz_low_sugar`<br>Diabetes and signs of low blood sugar (a hypo)<br>**Note:** The Low blood sugar page says to treat a hypo yourself straight away, and to call 999 if someone is not responding normally. Same-day help if it does not settle is AI judgement. | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Treat the low blood sugar now. If it does not improve, get help from NHS 111, or call 999 if the person becomes drowsy or confused.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Dizziness: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_dz_keeps_coming_back`<br>Dizziness that will not go away or keeps coming back | "Dizziness keeps coming back, or will not go away" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| `or_dz_hearing`<br>Dizziness with hearing loss, or ringing or other sounds in the ears | "Hearing loss or a change in hearing" OR "Tinnitus (ringing or buzzing in the ears)" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| `or_dz_vision`<br>Dizziness with double vision, blurred vision or other changes in eyesight<br>**Note:** With spinning, the emergency rule above applies instead. | "Change in sight or loss of vision" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| `or_dz_other_symptoms`<br>Dizziness with other symptoms: headaches, feeling or being sick, fainting, or a change to the pulse | "Headache" OR "Feels sick or has been sick" OR "Passed out (fainted)" OR "Heart racing, slow, skipping or fluttering" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| `or_dz_new_medicine`<br>Dizziness that started after a new medicine | "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or speak to a pharmacist. Do not stop a prescribed medicine without advice.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| `or_dz_worried`<br>Worried about dizziness or vertigo | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |

## Default outcome

Used when no rule fires.

- **Dizziness with nothing that needs more help: it usually goes away on its own**
- Outcome: Self-manageable, Self-care, No appointment needed. *Dizziness usually goes away on its own*
- Source: [Dizziness](https://www.nhs.uk/symptoms/dizziness/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Dizzy or off-balance | Do you feel dizzy or off-balance, or like you or the room is spinning? | 404640003 | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numbness or weakness in the face, arms or legs | Do you have numbness or weakness in your face, arms or legs? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Feels like you or the room is spinning (vertigo) | Does it feel like you, or everything around you, is spinning? | 399153001 | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Pins and needles, tingling or numbness | Do you have pins and needles, tingling or numbness in part of your body, such as your hands, arms, legs or feet? | 62507009 | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| Finding it hard to balance or walk | Are you finding it hard to balance or walk, or are you falling over? | 22631008 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Hearing loss or a change in hearing | Have you lost some or all of your hearing, or has your hearing changed? |  | [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Headache | Do you have a headache? | 25064002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Others at home, or pets, unwell with similar symptoms | Are other people you live with, or your pets, unwell with similar symptoms? |  | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |
| Dizziness keeps coming back, or will not go away | Does the dizziness keep coming back, or will it not go away? |  | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| Tinnitus (ringing or buzzing in the ears) | Can you hear noises like ringing, buzzing or humming that do not come from around you? This is called tinnitus. | 60862001 | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Heart racing, slow, skipping or fluttering | Does your heart feel like it is racing, going too slowly, skipping a beat or fluttering? | 80313002 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
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

### `advice_dizziness_ae`

**What to do:** Call 999 or go to A&E now. Dizziness or spinning with these symptoms needs to be checked in hospital, because it can be a sign of a stroke.

**Look out for:**
- One side of the face drooping, weakness in an arm, or slurred speech
- Getting worse, or not being able to stand

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Vertigo](https://www.nhs.uk/conditions/vertigo/), [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/)

### `advice_headache_999`

**What to do:** Call 999 now. A sudden, extremely painful headache can be a sign of bleeding on the brain. This needs treatment in hospital straight away.

**Look out for:**
- The person becoming drowsy, confused or hard to wake
- A seizure (fit)
- One side of the face drooping, weakness in an arm, or slurred speech

**Get more help when:**
- Call 999 again if the person gets worse before help arrives
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Migraine](https://www.nhs.uk/conditions/migraine/)

### `advice_dizziness_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your dizziness should be checked today.

**Look out for:**
- Numbness or weakness in your face, arms or legs
- Double vision, loss of sight, or trouble speaking
- A sudden, extremely painful headache

**Get more help when:**
- Call 999 if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Lie down until the dizziness passes, then get up slowly
- Drink plenty of water, especially if you are being sick
- Do not drive, climb ladders or use machinery while you feel dizzy

Source: [Vertigo](https://www.nhs.uk/conditions/vertigo/), [Dizziness](https://www.nhs.uk/symptoms/dizziness/)

### `advice_carbon_monoxide`

**What to do:** Go outside into fresh air now, then call NHS 111. Other people being unwell too can be a sign of carbon monoxide, a poisonous gas from faulty boilers, cookers, fires or engines.

**Look out for:**
- Finding it hard to breathe
- Sudden confusion, feeling weak, or chest or muscle pain
- Anyone passing out

**Get more help when:**
- Call 999 or go to A&E if anyone has any of the signs above
- If you think an appliance is leaking gas, call the free National Gas Helpline on 0800 111 999

**Where to go:** Call 111 or use 111 online. In an emergency call 999. Do not go back inside until you have got advice.

**What you can do yourself:**
- Stop using any boiler, cooker or heater you think may be the cause, if you can do it safely
- Get a carbon monoxide alarm for each room with a gas, oil, coal or wood appliance

Source: [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/)

### `advice_low_blood_sugar`

**What to do:** Treat the low blood sugar now. Have something sugary straight away, such as a small glass of fruit juice or a sugary fizzy drink, or glucose tablets. Check your blood sugar again after 10 to 15 minutes.

**Look out for:**
- Blood sugar still below 4 after treating it twice
- Getting confused, very drowsy or hard to wake
- A seizure (fit)

**Get more help when:**
- Once you feel better, eat something like biscuits or a sandwich to keep your sugar up
- Get help from NHS 111 or your diabetes team if it does not get better, or you keep having hypos
- Call 999 if the person stops responding as usual or has a seizure. Do not give them food or drink if they are not fully awake.

**Where to go:** Treat it yourself first. For help call 111 or use 111 online, or contact your diabetes team. In an emergency call 999.

**What you can do yourself:**
- Always carry something sugary with you
- Do not drive for at least 45 minutes after your blood sugar is back to normal

Source: [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/)

### `advice_dizziness_gp`

**What to do:** See a GP about your dizziness. It is not usually serious, but they can help find the cause.

**Look out for:**
- Numbness or weakness in your face, arms or legs
- Double vision, loss of sight, or trouble speaking
- Fainting, or chest pain

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you are being sick or have a very high temperature
- Call 999 if you get any of the serious signs above

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Lie down until the dizziness passes, then get up slowly
- Move slowly and carefully, and get plenty of rest
- Drink plenty of water. Avoid coffee, cigarettes and alcohol.
- Do not stop a medicine your doctor gave you without asking a doctor or pharmacist first
- Do not drive while you feel dizzy. You may need to tell the DVLA if it keeps happening.

Source: [Dizziness](https://www.nhs.uk/symptoms/dizziness/), [Vertigo](https://www.nhs.uk/conditions/vertigo/), [Labyrinthitis and vestibular neuritis](https://www.nhs.uk/conditions/labyrinthitis/)

### `advice_dizziness_self_care`

**What to do:** Dizziness usually goes away on its own. You can look after yourself at home.

**Look out for:**
- Dizziness that will not go away or keeps coming back
- Changes to your hearing or eyesight
- Numbness or weakness, trouble speaking, or fainting

**Get more help when:**
- See a GP if it will not go away, keeps coming back, or you are worried
- Call 999 if you get numbness or weakness, trouble speaking, or loss of sight

**Where to go:** You do not need an appointment now. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Lie down until the dizziness passes, then get up slowly
- Do not bend down or get up suddenly
- Drink plenty of fluids, especially water
- Do not drive, climb ladders or use machinery while you feel dizzy

Source: [Dizziness](https://www.nhs.uk/symptoms/dizziness/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_dz_stroke_signs`: Source difference: the Dizziness page says see a GP if your face, arms or legs feel numb or weak, or you find it harder to speak. The Vertigo page says call 999 or go to A&E. The Ménière's disease and Stroke pages say call 999, because these can be signs of a stroke. The most urgent is used.
- `rf_dz_vision_loss`: The Ménière's disease page says call 999 for spinning with sudden problems with the vision in one eye. The Vertigo page says 999 or A&E for loss of vision.
- `rf_dz_spinning_double_vision`: The Vertigo page names double vision. It is a separate observation from other changes in sight, so it is named here too.
- `rf_dz_spinning_tingling`: The Vertigo page says call 999 or go to A&E for vertigo with leg or arm weakness, numbness or tingling. Numbness and weakness are covered by the firm stroke rule above. Tingling alone is soft, because long-standing tingling (for example from a trapped nerve) and the tingling of a migraine aura are common.
- `rf_dz_spinning_off_balance`: The Ménière's disease page says call 999 for spinning with feeling very off-balance, as a sign of a stroke. The Labyrinthitis page lists finding it difficult to stay upright or walk in a straight line as a usual symptom. Soft, with the urgent rule below as its floor. Needs clinical review: telling a stroke from labyrinthitis needs an examination.
- `rf_dz_spinning_hearing`: Source difference: the Vertigo page says call 999 or go to A&E for vertigo with hearing loss. The Labyrinthitis page lists hearing loss and ringing as usual symptoms and says an urgent GP appointment or 111 for sudden hearing loss in one ear. The Ménière's disease page says see a GP. The most urgent is used, marked soft, with the urgent rule below as its floor. Ringing in the ears (tinnitus) is not on the Vertigo page's list. A yes to it brings in the tinnitus entry symptom, whose own soft A&E rule for tinnitus with vertigo (Tinnitus page) then applies, so it is not repeated here.
- `rf_dz_off_balance`: AI judgement: a floor under the soft 999 rule above, so that someone who cannot walk straight is checked the same day.
- `rf_dz_spinning_hearing_urgent`: The Labyrinthitis page says an urgent GP appointment or 111 for sudden hearing loss in one ear. Hearing loss that comes on quickly can need treatment within days to save the hearing.
- `rf_dz_spinning_severe_headache`: The Vertigo page says this for a severe headache. Firm. The soft rule below covers any headache.
- `rf_dz_spinning_headache`: The Vertigo page says a severe headache. The question asks about any headache, so the rule is soft: migraine often causes both.
- `rf_dz_low_sugar`: The Low blood sugar page says to treat a hypo yourself straight away, and to call 999 if someone is not responding normally. Same-day help if it does not settle is AI judgement.
- `or_dz_vision`: With spinning, the emergency rule above applies instead.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Short spells of spinning when you move your head (BPPV) | 111541001 | common | Brief spinning brought on by moving the head: strongly supports; Feels like you or the room is spinning (vertigo): strongly supports; Dizziness keeps coming back, or will not go away: supports; Feels sick or has been sick: supports |
| Poisoning by carbon monoxide, a gas from a faulty boiler, fire or car | 17383000 | rare | Others at home, or pets, unwell with similar symptoms: strongly supports; Better when away from home, worse on returning: strongly supports; Headache: strongly supports; Dizzy or off-balance: supports; Feels sick or has been sick: supports |
| Low blood pressure when standing up (postural hypotension) | 28651003 | common | Dizzy when standing or sitting up quickly: strongly supports; Fainted just after standing up: supports; Feels light-headed: supports; Started a new medicine or changed a dose in the last few weeks: supports; Signs of dehydration: supports |
| Low blood sugar (hypoglycaemia, a hypo) | 302866003 | rare | Has diabetes: strongly supports; Signs of low blood sugar in someone with diabetes: strongly supports; Feels sweaty: supports; Shaking or trembling (tremor): supports; Feels light-headed: supports; Suddenly confused: supports; Tingling or pins and needles in the fingers or around the mouth: supports; Heart racing, slow, skipping or fluttering: supports |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Mini-stroke (transient ischaemic attack, TIA) | 266257000 | rare | Signs of a stroke: strongly supports; Weakness that comes and goes: strongly supports; Weakness that came on suddenly: supports; Weakness on one side of the face or body: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Difficulty speaking: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Anxiety or panic attack | 48694002 | common | Sudden rush of intense fear or panic: strongly supports; Pain triggered by worry or stress: strongly supports; Tingling or pins and needles in the fingers or around the mouth: supports; Breathing very fast: supports; Heart beating very fast: supports; Heart racing, slow, skipping or fluttering: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Short of breath: supports |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Labyrinthitis (an ear infection that affects balance) | 23919004 | uncommon | Feels like you or the room is spinning (vertigo): strongly supports; Feels sick or has been sick: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Hearing loss that came on suddenly: supports; Tinnitus (ringing or buzzing in the ears): supports; Hearing loss or a change in hearing: supports; Dizziness there all the time since it started: strongly supports; Being sick: supports; Finding it hard to balance or walk: supports |
| Meniere's (a condition deep in the ear that causes bouts of spinning, hearing loss and ringing) | 13445001 | rare | Symptoms come in attacks lasting minutes to hours: strongly supports; Feels like you or the room is spinning (vertigo): strongly supports; Ear feels blocked or full: supports; Hearing loss or a change in hearing: strongly supports; Tinnitus (ringing or buzzing in the ears): strongly supports; Feels sick or has been sick: supports; Dizziness keeps coming back, or will not go away: strongly supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
