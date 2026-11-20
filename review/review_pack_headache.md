# Review pack: Headache

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
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | 2026-11-19 |  | Page last reviewed: 18 August 2023 |
| [Tension headaches](https://www.nhs.uk/conditions/tension-headaches/) | 2026-11-19 |  | Page last reviewed: 01 August 2025 |
| [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | 2026-11-19 |  | Page last reviewed: 16 December 2025 |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |
| [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | 2026-11-19 |  | Page last reviewed: 12 June 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/) | 2026-11-19 |  | Page last reviewed: 14 August 2023 |

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

## Headache red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ha_sudden_severe`<br>A headache that came on suddenly and is extremely painful (a 'thunderclap' headache)<br>**Note:** Source difference: the Headaches page says call 999 or go to A&E. The Subarachnoid haemorrhage and Migraine pages say call 999. The more urgent is used. | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_ha_seizure`<br>Headache and a seizure (fit)<br>**Note:** The seizure entry symptom also applies once a seizure is reported. It sends a first seizure to 999. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_numb_or_weak`<br>Headache with numbness or weakness in the body or face<br>**Note:** Weakness on one side, or a drooping face, is a sign of a stroke and is sent to 999 by the universal red flag and the weakness rules. | "Numbness or weakness in the face, arms or legs" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_speech_balance_memory`<br>Headache with difficulty speaking, balancing, walking or remembering things | "Difficulty speaking" OR "Finding it hard to balance or walk" OR "Problems remembering things that started suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_drowsy`<br>Headache and drowsy or confused<br>**Note:** Sudden confusion is checked for everyone by the universal red flags. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_vision_loss`<br>Headache with loss of vision | "Cannot see out of 1 or both eyes, or a large part of the sight is missing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_rash`<br>Headache with a rash that does not fade when a glass is pressed on it<br>**Note:** The Meningitis page gives the same advice. | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_stiff_neck`<br>Headache with a stiff neck | "Stiff neck" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_temperature_and_light`<br>Headache with a very high temperature and bright lights bothering you<br>**Note:** Both together are signs of meningitis. Kept firm. | "Very high temperature, or feels hot, cold or shivery" AND "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_ha_high_temperature`<br>Headache with a very high temperature<br>**Note:** The Headaches page says call 999 or go to A&E for a headache with 'a very high temperature, a stiff neck, or bright lights bothering you'. Read literally, every headache with flu would go to A&E. Marked soft so that likely flu can lower it. A stiff neck, or a high temperature with bright lights bothering you, stay firm. | "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_light`<br>Headache with bright lights bothering you<br>**Note:** Same reading as the high temperature rule. Being very sensitive to light is one of the main symptoms of migraine on the Migraine page, so this is soft. | "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_head_injury`<br>Headache and a head injury in the last 3 months<br>**Note:** Bleeding on the brain can build up slowly over weeks after a head injury, especially in older people and people who take blood thinners. | "Head injury in the last 3 months" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_eyelid_or_pupil`<br>An eyelid drooping, or one pupil smaller than the other, for the first time<br>**Note:** The Cluster headaches page says this even for people already diagnosed with cluster headaches. | "One eyelid drooping, or one pupil smaller, for the first time" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |
| `rf_ha_temporal_arteritis_vision`<br>Jaw pain when eating or a tender scalp, with changes to vision: possible temporal arteritis affecting the eyes<br>**Note:** The Temporal arteritis page says anyone with vision problems should be seen the same day by an eye specialist in a hospital eye department. Using A&E for that is AI judgement: sight can be lost within hours. Double vision, and sight lost in 1 eye for a short time that came back, are common warning signs, so they count too (the Cluster headaches page names double vision). | "Jaw pain when eating, or a sore or tender scalp or temple" AND ("Change in sight or loss of vision" OR "Double vision" OR "Lost the sight in 1 eye for a short time, then it came back") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or an eye emergency service now* | **AI judgement, needs clinical review** | |
| `rf_ha_child_neuro`<br>A child with a headache and vision problems<br>**Note:** The Tension headaches page says this for a child under 12. Using under 16 is AI judgement, because the age observations available are under 5 and under 16. | "Under 16 years old" AND ("Change in sight or loss of vision" OR "Double vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Tension headaches](https://www.nhs.uk/conditions/tension-headaches/) | |

## Headache red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ha_vision`<br>Headache with vision or eye problems | "Change in sight or loss of vision" OR "Double vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_cough_or_bend`<br>Headache brought on or made worse by coughing, sneezing, bending down or exercise | "Headache brought on or made worse by coughing, sneezing, bending down or exercise" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_being_sick`<br>Headache and being sick<br>**Note:** Taken directly from the Headaches page. Marked soft because the Migraine page lists feeling or being sick as a main symptom of a migraine attack. Needs clinical review. | "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_child_worse_or_night`<br>A child whose headache is getting worse, or wakes them at night<br>**Note:** The Tension headaches page says the same for a child under 12, and adds a headache when they wake up in the morning. | "Under 16 years old" AND ("Headache getting worse over days or weeks" OR "Headache wakes them at night, or is worst on waking") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_jaw_or_scalp`<br>Headache with jaw pain when eating, or a sore or tender scalp: possible temporal arteritis<br>**Note:** The Temporal arteritis page says the same. | "Jaw pain when eating, or a sore or tender scalp or temple" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_ha_others_unwell`<br>Headache, and other people at home or pets unwell too: possible carbon monoxide poisoning<br>**Note:** The Carbon monoxide poisoning page says call 111 if you think you might have it, and 999 or A&E if someone is short of breath, confused, weak, has chest or muscle pain or has passed out. | "Others at home, or pets, unwell with similar symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Go outside into fresh air, then call NHS 111 now* | [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | |
| `rf_ha_pregnant`<br>Headache in someone who is pregnant or has just had a baby<br>**Note:** The Migraine page says an urgent GP appointment or 111 for a migraine attack in someone pregnant or who has just had a baby. Applying it to any headache, because a headache can be a sign of pre-eclampsia (high blood pressure in pregnancy), is AI judgement. The pre-eclampsia condition card belongs to the women's health batch. | "Pregnant, or gave birth in the last 6 weeks" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your midwife or maternity unit, or get help from NHS 111, today* | [Migraine](https://www.nhs.uk/conditions/migraine/) | |
| `rf_ha_aura_long`<br>Migraine warning signs (aura) lasting longer than 1 hour | "Warning signs (aura) lasting longer than 1 hour" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Migraine](https://www.nhs.uk/conditions/migraine/) | |
| `rf_ha_migraine_72_hours`<br>A migraine attack that has lasted longer than 72 hours | "Diagnosed with migraine" AND "Migraine lasting longer than 72 hours" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Migraine](https://www.nhs.uk/conditions/migraine/) | |

## Headache: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ha_worried`<br>Headache and worried about other symptoms<br>**Note:** The Headaches page says 'any other symptoms you're worried about'. Same reasoning as the sore throat rule: likely to over-triage, so soft. | "Worried about symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `or_ha_regular`<br>Gets headaches regularly | "Gets headaches regularly" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `or_ha_not_getting_better`<br>A headache that is not getting better with self-care, or is getting worse | "Headache not getting better with self-care" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `or_ha_worse_over_time`<br>A headache that has been getting worse over days or weeks<br>**Note:** For a child, the urgent rule above applies instead. | "Headache getting worse over days or weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| `or_ha_unlike_usual`<br>A headache that feels different from the usual headaches | "Headache feels different from usual headaches" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| `or_ha_painkillers`<br>Taking painkillers for headaches on more than 2 days a week<br>**Note:** The Migraine page warns that painkillers on more than 2 days a week can cause more headaches. The Tension headaches page says see a GP if painkillers do not help. | "Taking painkillers for headaches on more than 2 days a week" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Migraine](https://www.nhs.uk/conditions/migraine/) | |

## Default outcome

Used when no rule fires.

- **Headache with nothing that needs more help: most headaches go away on their own**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most headaches go away on their own and are not a sign of something more serious*
- Source: [Headaches](https://www.nhs.uk/symptoms/headaches/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Headache | Do you have a headache? | 25064002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Numbness or weakness in the face, arms or legs | Do you have numbness or weakness in your face, arms or legs? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Finding it hard to balance or walk | Are you finding it hard to balance or walk, or are you falling over? | 22631008 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Problems remembering things that started suddenly | Did the problems remembering things start suddenly, in the last few hours or days? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Head injury in the last 3 months | Have you hit your head, or had a head injury, in the last 3 months? For example, from a fall or accident. |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| One eyelid drooping, or one pupil smaller, for the first time | Is one of your eyelids drooping, or is the black centre of one eye smaller than the other, for the first time? |  | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Lost the sight in 1 eye for a short time, then it came back | Did you lose the sight in 1 eye for a few seconds or minutes, like a curtain coming down, and then it came back? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Headache brought on or made worse by coughing, sneezing, bending down or exercise | Is the headache brought on, or made worse, by coughing, sneezing, bending down or exercise? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Headache getting worse over days or weeks | Has the headache been getting worse over days or weeks? |  | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| Headache wakes them at night, or is worst on waking | Does the headache wake you up at night, or is it worst when you wake up? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Others at home, or pets, unwell with similar symptoms | Are other people you live with, or your pets, unwell with similar symptoms? |  | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Warning signs (aura) lasting longer than 1 hour | Have the warning signs, such as zigzag lines, flashing lights or tingling, lasted longer than 1 hour this time? |  | [Migraine](https://www.nhs.uk/conditions/migraine/) | |
| Diagnosed with migraine | Has a doctor told you that you get migraines? |  | [Migraine](https://www.nhs.uk/conditions/migraine/) | |
| Migraine lasting longer than 72 hours | Has this migraine lasted longer than 3 days (72 hours)? |  | [Migraine](https://www.nhs.uk/conditions/migraine/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Gets headaches regularly | Do you get headaches a lot, for example a few times a week? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Headache not getting better with self-care | Have you tried treating the headache yourself, and it is not getting better, or is getting worse? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Headache feels different from usual headaches | Does this headache feel different from the headaches you usually get? |  | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| Taking painkillers for headaches on more than 2 days a week | For a month or more, have you been taking painkillers for headaches on more than 2 days a week? |  | [Migraine](https://www.nhs.uk/conditions/migraine/) | |

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

### `advice_headache_ae`

**What to do:** Call 999 or go to A&E now. A headache with these symptoms needs to be checked in hospital straight away.

**Look out for:**
- Getting drowsy, confused or hard to wake
- A seizure (fit)
- Weakness, numbness or a drooping face, or slurred speech

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Headaches](https://www.nhs.uk/symptoms/headaches/)

### `advice_meningitis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of meningitis (an infection of the layers around the brain) or sepsis (a life-threatening reaction to an infection). They need treatment in hospital straight away.

**Look out for:**
- A rash that does not fade when you press a glass against it. On brown or black skin, check paler areas such as the palms of the hands.
- Being very sleepy, confused or hard to wake
- A seizure (fit)
- In a baby: being floppy, not feeding, or a high-pitched cry
- Skin, lips or tongue turning blue, grey, pale or blotchy

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Do not wait for a rash. Get help if you are worried, even if there is no rash.
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive yourself to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Meningitis](https://www.nhs.uk/conditions/meningitis/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_headache_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your headache should be checked today.

**Look out for:**
- A headache that suddenly becomes extremely painful
- Numbness or weakness. Or it is hard to speak, walk or remember things.
- A stiff neck, a very high temperature, or a rash that does not fade when pressed
- Getting drowsy or confused

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5. In an emergency call 999.

**What you can do yourself:**
- Rest, and drink plenty of water
- Take paracetamol or ibuprofen while you wait

Source: [Headaches](https://www.nhs.uk/symptoms/headaches/)

### `advice_headache_temporal_arteritis`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A headache with jaw pain when eating, or a tender scalp, can be temporal arteritis (swollen blood vessels in the head). It needs treatment quickly to protect your sight.

**Look out for:**
- Any change to your vision, such as double vision or losing sight in one eye
- Pain or tenderness at the sides of your head

**Get more help when:**
- Go to A&E now if you get any change to your vision
- Call 999 if one side of your face droops, you cannot lift both arms, or your speech is slurred

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/), [Headaches](https://www.nhs.uk/symptoms/headaches/)

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

### `advice_headache_pregnancy`

**What to do:** Contact your midwife or maternity unit, or get help from NHS 111, today. A headache in pregnancy or just after having a baby can be a sign of high blood pressure (pre-eclampsia), which needs checking.

**Look out for:**
- Blurred vision or flashing lights
- Pain just below your ribs
- Sudden swelling of your face, hands or feet
- Feeling very unwell, or being sick

**Get more help when:**
- Call 999 or go to A&E if you have a sudden, very bad headache, a seizure (fit), or trouble seeing or speaking

**Where to go:** Call your midwife or maternity unit, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Paracetamol is the first choice of painkiller in pregnancy. Do not take ibuprofen unless a doctor says you can.

Source: [Migraine](https://www.nhs.uk/conditions/migraine/), [Tension headaches](https://www.nhs.uk/conditions/tension-headaches/)

### `advice_headache_gp`

**What to do:** See a GP about your headaches. It is not urgent, but they can help find the cause and the right treatment.

**Look out for:**
- A headache that suddenly becomes extremely painful
- Numbness or weakness. Or it is hard to speak, walk or remember things.
- A headache with being sick, or one that gets worse when you cough or bend down

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your headache gets worse or you get new symptoms
- Call 999 or go to A&E if you get any of the serious signs above

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep a headache diary: when they happen, how long they last, and what might set them off
- Try not to take painkillers on more than 2 days a week. Taking them more often can cause more headaches.
- Drink plenty of water, eat regular meals and try to relax

Source: [Headaches](https://www.nhs.uk/symptoms/headaches/), [Migraine](https://www.nhs.uk/conditions/migraine/), [Tension headaches](https://www.nhs.uk/conditions/tension-headaches/), [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/)

### `advice_headache_self_care`

**What to do:** You can usually treat a headache yourself. Most headaches go away on their own and are not a sign of something more serious.

**Look out for:**
- A headache that is not getting better, or is getting worse
- Headaches that keep coming back
- Being sick, or a headache made worse by coughing or bending down

**Get more help when:**
- See a GP if your headache is not getting better or you get headaches regularly
- Ask for an urgent GP appointment or call 111 if you have problems with your vision or are being sick
- Call 999 or go to A&E for a sudden, extremely painful headache, a stiff neck, or weakness or numbness

**Where to go:** You do not need an appointment now. A pharmacist can help you choose a painkiller. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink plenty of water and get plenty of rest
- Take paracetamol or ibuprofen
- Try to relax: stress can make headaches worse
- Do not skip meals, drink alcohol, or strain your eyes for a long time

Source: [Headaches](https://www.nhs.uk/symptoms/headaches/), [Tension headaches](https://www.nhs.uk/conditions/tension-headaches/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ha_sudden_severe`: Source difference: the Headaches page says call 999 or go to A&E. The Subarachnoid haemorrhage and Migraine pages say call 999. The more urgent is used.
- `rf_ha_seizure`: The seizure entry symptom also applies once a seizure is reported. It sends a first seizure to 999.
- `rf_ha_numb_or_weak`: Weakness on one side, or a drooping face, is a sign of a stroke and is sent to 999 by the universal red flag and the weakness rules.
- `rf_ha_drowsy`: Sudden confusion is checked for everyone by the universal red flags.
- `rf_ha_rash`: The Meningitis page gives the same advice.
- `rf_ha_temperature_and_light`: Both together are signs of meningitis. Kept firm.
- `rf_ha_high_temperature`: The Headaches page says call 999 or go to A&E for a headache with 'a very high temperature, a stiff neck, or bright lights bothering you'. Read literally, every headache with flu would go to A&E. Marked soft so that likely flu can lower it. A stiff neck, or a high temperature with bright lights bothering you, stay firm.
- `rf_ha_light`: Same reading as the high temperature rule. Being very sensitive to light is one of the main symptoms of migraine on the Migraine page, so this is soft.
- `rf_ha_head_injury`: Bleeding on the brain can build up slowly over weeks after a head injury, especially in older people and people who take blood thinners.
- `rf_ha_eyelid_or_pupil`: The Cluster headaches page says this even for people already diagnosed with cluster headaches.
- `rf_ha_temporal_arteritis_vision`: The Temporal arteritis page says anyone with vision problems should be seen the same day by an eye specialist in a hospital eye department. Using A&E for that is AI judgement: sight can be lost within hours. Double vision, and sight lost in 1 eye for a short time that came back, are common warning signs, so they count too (the Cluster headaches page names double vision).
- `rf_ha_child_neuro`: The Tension headaches page says this for a child under 12. Using under 16 is AI judgement, because the age observations available are under 5 and under 16.
- `rf_ha_being_sick`: Taken directly from the Headaches page. Marked soft because the Migraine page lists feeling or being sick as a main symptom of a migraine attack. Needs clinical review.
- `rf_ha_child_worse_or_night`: The Tension headaches page says the same for a child under 12, and adds a headache when they wake up in the morning.
- `rf_ha_jaw_or_scalp`: The Temporal arteritis page says the same.
- `rf_ha_others_unwell`: The Carbon monoxide poisoning page says call 111 if you think you might have it, and 999 or A&E if someone is short of breath, confused, weak, has chest or muscle pain or has passed out.
- `rf_ha_pregnant`: The Migraine page says an urgent GP appointment or 111 for a migraine attack in someone pregnant or who has just had a baby. Applying it to any headache, because a headache can be a sign of pre-eclampsia (high blood pressure in pregnancy), is AI judgement. The pre-eclampsia condition card belongs to the women's health batch.
- `or_ha_worried`: The Headaches page says 'any other symptoms you're worried about'. Same reasoning as the sore throat rule: likely to over-triage, so soft.
- `or_ha_worse_over_time`: For a child, the urgent rule above applies instead.
- `or_ha_painkillers`: The Migraine page warns that painkillers on more than 2 days a week can cause more headaches. The Tension headaches page says see a GP if painkillers do not help.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Brain tumour warning signs | 126952004 | rare | Headache getting worse over days or weeks: strongly supports; Headache wakes them at night, or is worst on waking: supports; Changes in personality or behaviour: supports; Being sick: supports; Has had a seizure (fit): supports; Weakness that started gradually or is slowly getting worse: supports; Headache feels different from usual headaches: supports; Change in sight or loss of vision: supports |
| Poisoning by carbon monoxide, a gas from a faulty boiler, fire or car | 17383000 | rare | Others at home, or pets, unwell with similar symptoms: strongly supports; Better when away from home, worse on returning: strongly supports; Headache: strongly supports; Dizzy or off-balance: supports; Feels sick or has been sick: supports |
| Cluster headaches | 193031009 | rare | Severe sharp or burning pain around one eye, with a red or watering eye: strongly supports; Gets headaches regularly: supports; One eyelid drooping, or one pupil smaller, for the first time: supports; Smokes, or has smoked in the past: supports; Headache: strongly supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Encephalitis (swelling of the brain) | 45170000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Suddenly confused: strongly supports; Changes in personality or behaviour: supports; Has had a seizure (fit): supports; Difficulty speaking: supports; So drowsy they are hard to wake or cannot stay awake: supports; Headache: supports; Weakness, or cannot move part of the body (paralysis): supports |
| Swollen blood vessels in the head (temporal arteritis) | 414341000 | rare | Jaw pain when eating, or a sore or tender scalp or temple: strongly supports; Change in sight or loss of vision: supports; Headache feels different from usual headaches: supports; Feels very tired: supports; Aching body: supports; Losing weight without trying: supports; Headache: strongly supports; Double vision: supports; Feels very unwell: supports; Pain and stiffness in both shoulders or both hips, worst in the morning: supports; Lost the sight in 1 eye for a short time, then it came back: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Headache from taking painkillers too often | 698803006 | uncommon | Taking painkillers for headaches on more than 2 days a week: strongly supports; Gets headaches regularly: strongly supports; Headache wakes them at night, or is worst on waking: supports |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Bleeding on the brain (subarachnoid haemorrhage) | 21454007 | rare | Headache that came on suddenly and is extremely painful: strongly supports; Headache: strongly supports; Stiff neck: supports; Being sick: supports; Bright lights hurt the eyes or are bothering you: supports; So drowsy they are hard to wake or cannot stay awake: supports; Passed out (fainted): supports; Has had a seizure (fit): supports; Suddenly confused: supports |
| Tension headache | 398057008 | common | Feels like pressing or tightening on both sides of the head: strongly supports; Going through a stressful time or big life change: supports; Gets headaches regularly: supports; Getting less sleep than needed: supports; Having a lot of caffeine or alcohol: supports |
| Flu | 6142004 | uncommon | Very high temperature, or feels hot, cold or shivery: strongly supports; Aching body: strongly supports; Feels very tired: supports; Dry cough: supports; Feels very unwell: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Pre-eclampsia (high blood pressure in pregnancy that can cause serious problems) | 398254007 | very rare | Pain just below the ribs: strongly supports; Severe headache that painkillers do not help: strongly supports; Change in sight or loss of vision: strongly supports; Sudden swelling of the face, hands or feet: supports; Feels sick or has been sick: supports; Feels very unwell: supports; Pregnant, or gave birth in the last 6 weeks: strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Swelling is severe, painful or came on suddenly: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
