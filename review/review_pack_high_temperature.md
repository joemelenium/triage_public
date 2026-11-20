# Review pack: High temperature

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
| [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | 2026-11-19 |  | Page last reviewed: 03 January 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | 2026-11-19 |  | Page last reviewed: 28 May 2026 |
| [Fever in adults](https://www.nhs.uk/symptoms/fever-in-adults/) | 2026-11-19 |  | Page last reviewed: 19 October 2026 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Malaria](https://www.nhs.uk/conditions/malaria/) | 2026-11-19 |  | Page last reviewed: 29 July 2025 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Rashes in babies and children](https://www.nhs.uk/symptoms/rashes-babies-and-children/) | 2026-11-19 |  | Page last reviewed: 03 October 2024 |
| [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | 2026-11-19 |  | Page last reviewed: 16 October 2023 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | 2026-11-19 |  | Page last reviewed: 21 June 2023 |
| [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | 2026-11-19 |  | Page last reviewed: 6 August 2026 |

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

## High temperature red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ht_child_meningitis_signs`<br>A child with a high temperature and a stiff neck, a rash that does not fade when pressed, or bothered by light | "Under 16 years old" AND ("Stiff neck" OR "Rash that does not fade when pressed" OR "Bright lights hurt the eyes or are bothering you") | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_fit`<br>A child with a high temperature who has had a fit (seizure)<br>**Note:** The Fever in children page says call 999 for a first fit. The Febrile seizures page says 999 or A&E for a first fit, a fit lasting more than 5 minutes, or more than one in 24 hours. Applying it to every fit, not only the first, is AI judgement: the engine cannot tell a first fit from a repeat with confidence, and a carer is rarely sure it was a simple febrile fit. | "Under 16 years old" AND "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_floppy`<br>A child with a high temperature who is floppy, drowsy, hard to wake or not responding as usual | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_not_feeding_or_playing`<br>A child with a high temperature who is not interested in feeding or anything around them | "Under 16 years old" AND "Child not interested in feeding or anything around them" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_crying`<br>A child with a high temperature who is extremely agitated, will not stop crying, or has a weak, high-pitched cry<br>**Note:** The Fever in children page lists extreme agitation or crying that will not stop. The Sepsis and Meningitis pages add a weak, high-pitched or continuous cry. | "Under 16 years old" AND "Child extremely agitated, crying and will not stop, or a weak or high-pitched cry" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_cold_hands`<br>A child with a high temperature and unusually cold hands and feet | "Under 16 years old" AND "Hands and feet, or skin, unusually cold to touch" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_skin_colour`<br>A child with a high temperature and blotchy or mottled skin<br>**Note:** Blue, grey or pale skin, lips or tongue is caught for everyone by the universal red flag. | "Under 16 years old" AND "Blotchy or mottled skin" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_breathing`<br>A child with a high temperature who is struggling to breathe, grunting, or breathing very fast<br>**Note:** The page says difficulty breathing (grunting, or the stomach sucking in under the ribs), breathlessness or breathing very fast. Uses the general difficulty breathing question, which covers a child struggling to breathe, so a yes to either fires it. | "Under 16 years old" AND ("Difficulty breathing" OR "Breathing very fast") | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_baby_high_temperature`<br>A baby under 3 months with 38C or more, or 3 to 6 months with 39C or more<br>**Note:** Source difference: the Fever in children page says call 111 for these temperatures. The Sepsis, Meningitis and 'Is your baby seriously ill' pages say call 999 or go to A&E. The more urgent is used. Any baby under 3 months with a high temperature, measured or not, gets at least urgent from the rule below. | "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_bulging_soft_spot`<br>A baby with a high temperature and a bulging soft spot on top of the head<br>**Note:** Clinical knowledge: a bulging soft spot with a high temperature can be a sign of meningitis in a baby. No NHS page in the source log lists it with an action. | "Baby's soft spot on top of the head bulging" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_ht_young_child_not_peed`<br>A child under 5 with a high temperature who has not had a pee for 12 hours | "Under 5 years old" AND "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_meningitis_signs`<br>A high temperature with a stiff neck, a rash that does not fade when pressed, or bothered by bright light<br>**Note:** For children the rule above sends an ambulance, as the Fever in children page says call 999. | "Stiff neck" OR "Rash that does not fade when pressed" OR "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_ht_fit`<br>A high temperature and a fit (seizure) | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_ht_drowsy`<br>A high temperature and so drowsy they are hard to wake or cannot stay awake | "So drowsy they are hard to wake or cannot stay awake" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_breathing_very_fast`<br>A high temperature and breathing very fast: possible sepsis | "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_skin_blotchy`<br>A high temperature and blotchy or mottled skin: possible sepsis | "Blotchy or mottled skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_cold_hands`<br>A high temperature with hands and feet, or skin, unusually cold or clammy<br>**Note:** The Sepsis and Meningitis pages say call 999 or go to A&E for an adult who feels hot or cold to the touch. Marked soft for adults, as in the breathlessness rules, so that likely flu with aching can lower it. The rule for children above is firm. | "Hands and feet, or skin, unusually cold to touch" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_very_painful_headache`<br>A high temperature and a very painful headache<br>**Note:** Taken from the Meningitis page. Marked soft because a bad headache is common with flu; meningitis itself, if likely, keeps the outcome at emergency. | "Very painful headache" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_ht_seriously_unwell`<br>Very unwell and getting worse, or feels something is seriously wrong<br>**Note:** The Sepsis page says get help immediately if you think something is seriously wrong. Soft, as in the cough and breathlessness rules. | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ht_chemotherapy`<br>A high temperature during or soon after chemotherapy<br>**Note:** Clinical knowledge: a high temperature during chemotherapy can be sepsis with a very weak immune system, which needs antibiotics within the hour. No NHS page in the source log gives the action. | "Having chemotherapy now or in the last 6 weeks" | Emergency (help now)<br>Emergency department<br>Now<br>*Call your cancer care team's 24-hour line now, or go to A&E* | **AI judgement, needs clinical review** | |
| `rf_ht_heatstroke`<br>Hot skin that is not sweating, or still unwell after 30 minutes of cooling down: possible heatstroke | "Hot skin that is not sweating" OR "Still unwell after 30 minutes of cooling down" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |

## High temperature red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ht_under_3_months`<br>A baby under 3 months with a high temperature, or thought to have one<br>**Note:** The Fever in children page says call 111 for a baby under 3 months with 38C or more, or if you think they have a high temperature. A measured 38C or more gives emergency through the rule above. The 'serious infection in a young baby' card can also raise this. | "Baby under 3 months old" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_under_6_months`<br>A baby 3 to 6 months old with a high temperature, or thought to have one | "Baby under 6 months old" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_5_days`<br>A high temperature that has lasted 5 days or more<br>**Note:** The Fever in children page says call 111. Applying it to adults is AI judgement; the Fever in adults page says get urgent help when a high temperature is not getting better, which a temperature for 5 days usually is. | "High temperature for 5 days or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_not_getting_better`<br>A high temperature that is not getting better with treatment at home, or is getting worse | "High temperature not getting better with treatment at home" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Fever in adults](https://www.nhs.uk/symptoms/fever-in-adults/) | |
| `rf_ht_child_not_usual_self`<br>A child with a high temperature who is not their usual self or not wanting to eat or feed, and the carer is worried | "Under 16 years old" AND ("Child not their usual self, or not wanting to eat, and the carer is worried" OR "Baby or young child feeding or eating much less than usual") | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_child_rash`<br>A child with a high temperature and another sign of illness, such as a rash<br>**Note:** A rash that does not fade when pressed is an emergency (rules above). | "Under 16 years old" AND "Rash or spots on the skin" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_dehydrated`<br>A high temperature with signs of not having enough water in the body<br>**Note:** The Fever in children page says call 111 for a dehydrated child. The Dehydration page gives the same level for adults with dark pee or peeing less. | "Signs of dehydration" OR "Child with dry nappies, sunken eyes or no tears" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 or ask for an urgent GP appointment* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_ht_not_peed`<br>A high temperature and no pee for 12 hours or more<br>**Note:** The Kidney infection page says an urgent GP appointment or 111 for not having a pee all day. For children under 5 the more urgent sepsis rule above applies. | "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | |
| `rf_ht_weakened_immune_system`<br>A high temperature in someone with a weakened immune system<br>**Note:** The UTI and Sore throat pages say urgent help for a weakened immune system. Chemotherapy, the most dangerous case, is an emergency above. | "Weakened immune system" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_ht_malaria_area`<br>A high temperature after being somewhere malaria is found in the last 12 months | "Been to a country where malaria is found in the last year" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today. Say where you have been.* | [Malaria](https://www.nhs.uk/conditions/malaria/) | |

## High temperature: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ht_pain_peeing`<br>A high temperature with pain or burning when peeing: possible kidney or urine infection<br>**Note:** The UTI page says an urgent GP appointment or 111 for a UTI with a very high temperature or feeling hot, cold or shivering, or in a child. | "Pain, burning or stinging when peeing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `or_ht_pain_back_or_side`<br>A high temperature with pain in the lower tummy or the back just under the ribs | "Pain in the back or side, just under the ribs" OR "Pain low down in the tummy, below the belly button" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | |

## Default outcome

Used when no rule fires.

- **A high temperature with nothing that needs more help: look after it at home**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most high temperatures get better on their own within 1 to 4 days*
- Source: [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/)
- **Note:** Both NHS pages say a high temperature can usually be looked after at home. Not a floor: likely conditions (for example a urine infection or pneumonia) can raise it.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Child not interested in feeding or anything around them | Has the child stopped feeding? Or have they lost all interest in what is going on around them? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Child extremely agitated, crying and will not stop, or a weak or high-pitched cry | Is the child extremely agitated or crying and will not stop? Or do they have a weak, high-pitched cry that does not sound like their usual cry? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Hands and feet, or skin, unusually cold to touch | Are your hands and feet, or your skin, unusually cold to touch, or cold and damp (clammy)? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Baby's soft spot on top of the head bulging | Is the soft spot on top of your baby's head (fontanelle) bulging or tight? |  | **AI judgement, needs clinical review** | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Having chemotherapy now or in the last 6 weeks | Are you having chemotherapy (a treatment for cancer), or have you had it in the last 6 weeks? |  | **AI judgement, needs clinical review** | |
| Hot skin that is not sweating | Is the skin very hot but not sweating, and maybe red? |  | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |
| Still unwell after 30 minutes of cooling down | Is the person still unwell after 30 minutes of resting in a cool place, being cooled and drinking fluids? |  | [Heat exhaustion and heatstroke](https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/) | |
| Baby under 3 months old | Is the person who is unwell a baby under 3 months old? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Baby under 6 months old | Is the person who is unwell a baby under 6 months old? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| High temperature for 5 days or more | Has the high temperature lasted for 5 days or more? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| High temperature not getting better with treatment at home | Have you been treating the high temperature at home, but it is not getting better or is getting worse? |  | [Fever in adults](https://www.nhs.uk/symptoms/fever-in-adults/) | |
| Child not their usual self, or not wanting to eat, and the carer is worried | Is the child not their usual self, or not wanting to eat, and are you worried about them? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Rash or spots on the skin | Do you have a rash or spots on your skin? | 271807003 | [Rashes in babies and children](https://www.nhs.uk/symptoms/rashes-babies-and-children/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Child with dry nappies, sunken eyes or no tears | Does the child have signs of not having enough water in their body? For example, dry nappies, sunken eyes, or no tears when crying. |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Been to a country where malaria is found in the last year | In the last 12 months, have you been to a country where malaria (an infection spread by mosquito bites) is found? |  | [Malaria](https://www.nhs.uk/conditions/malaria/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Pain in the back or side, just under the ribs | Do you have pain in your back or side, just under the ribs? | 271857006 | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| Pain low down in the tummy, below the belly button | Is the pain low down in your tummy, below your belly button? | 54586004 | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |

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

### `advice_fever_child_999`

**What to do:** Call 999 now. Your child has a high temperature and a sign of serious illness, such as meningitis or sepsis (a life-threatening reaction to an infection).

**Look out for:**
- Your child becoming floppy, very sleepy or hard to wake
- Breathing that gets harder, with grunting or the tummy sucking in under the ribs
- Skin, lips or tongue turning blue, grey, pale or blotchy
- A fit (seizure)

**Get more help when:**
- Call 999 again if your child gets worse before help arrives
- If your child stops responding and stops breathing, the 999 call handler will tell you how to start CPR. This means you press hard and fast on the middle of their chest.

**Where to go:** Call 999. Do not drive your child to A&E yourself. Stay with your child until help arrives.

**What you can do yourself:**
- Do not give your child anything to eat or drink until a doctor has seen them, unless the 999 call handler says so
- Do not wrap your child up or sponge them down to cool them

Source: [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/), [Sepsis](https://www.nhs.uk/conditions/sepsis/), [Meningitis](https://www.nhs.uk/conditions/meningitis/)

### `advice_febrile_fit_999`

**What to do:** Call 999 now. Your child has had a fit (seizure) with a high temperature.

**Look out for:**
- A fit that lasts more than 5 minutes
- Difficulty breathing
- Stiffness or twitching on only one side of the body
- Being much sleepier than usual for more than an hour after the fit stops

**Get more help when:**
- Call 999 again if your child has another fit, or gets worse before help arrives

**Where to go:** Call 999. Do not take your child to A&E yourself while they are still having a fit or are not responding.

**What you can do yourself:**
- Put your child on their side on a soft surface, away from anything that could hurt them
- Do not put anything in their mouth
- Stay with them and note how long the fit lasts

Source: [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/), [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/)

### `advice_fever_baby_emergency`

**What to do:** Call 999 or go to A&E now. A baby this young with a high temperature needs to be checked in hospital straight away, even if they seem otherwise well.

**Look out for:**
- Your baby becoming floppy, very sleepy or hard to wake
- A weak, high-pitched or continuous cry
- Not feeding, or a dry nappy for 12 hours
- Skin, lips or tongue turning blue, grey, pale or blotchy, or a rash that does not fade when you press a glass on it

**Get more help when:**
- Call 999 if your baby gets worse or you cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive yourself if you need to watch your baby. Ask someone to drive you or call 999.

**What you can do yourself:**
- Keep breastfeeding or giving feeds if your baby will take them
- Do not give medicine for the temperature unless a doctor says so

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/), [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/)

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

### `advice_fever_chemo_emergency`

**What to do:** Call your cancer care team's 24-hour phone line now, or go to A&E. A high temperature during chemotherapy (a treatment for cancer) can mean a serious infection. The treatment makes it harder to fight infection.

**Look out for:**
- Shivering or feeling very cold
- Breathing very fast, or feeling confused or very sleepy
- Blotchy or very pale skin

**Get more help when:**
- Call 999 if you get worse quickly, or cannot reach your care team or get to A&E safely

**Where to go:** Use the 24-hour number your cancer team gave you, or go to A&E. Do not drive yourself. Take your treatment record or alert card with you.

**What you can do yourself:**
- Do not wait to see if the temperature goes down with paracetamol

Source: **AI judgement, needs clinical review**, [Sepsis](https://www.nhs.uk/conditions/sepsis/)

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

### `advice_fever_child_urgent`

**What to do:** Call 111 now, or ask for an urgent GP appointment. Your child's high temperature needs to be checked today.

**Look out for:**
- A rash that does not fade when you press a glass against it
- A stiff neck, or bright light hurting their eyes
- Being floppy, very sleepy or hard to wake, or not interested in feeding or playing
- Breathing very fast, grunting, or the tummy sucking in under the ribs
- Unusually cold hands and feet, or blotchy skin

**Get more help when:**
- Call 999 if your child gets any of the signs above, or has a fit
- Trust your instincts. If you think something is seriously wrong, call 999.

**Where to go:** Call 111 or use 111 online. Call 111 if you need advice for a child under 5. In an emergency call 999.

**What you can do yourself:**
- Give plenty of fluids. If your baby is breastfed, keep breastfeeding as usual.
- Check on your child regularly, including during the night
- Do not undress your child or sponge them down to cool them, and do not cover them in too many clothes or blankets
- Do not give a baby under 3 months ibuprofen. Do not give a baby under 2 months paracetamol.
- Never give aspirin to children under 16

Source: [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/)

### `advice_fever_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your high temperature needs to be checked.

**Look out for:**
- A rash that does not fade when you press a glass against it
- A stiff neck, or bright light hurting your eyes
- Breathing very fast, or feeling confused or very sleepy
- Blotchy skin, or hands and feet that feel cold

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above, or you feel something is seriously wrong

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Get lots of rest
- Drink plenty of fluids, so your pee is light yellow and clear
- Take paracetamol or ibuprofen if you feel uncomfortable

Source: [Fever in adults](https://www.nhs.uk/symptoms/fever-in-adults/), [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/), [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/), [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/)

### `advice_malaria_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Say where you have travelled. A high temperature after being somewhere malaria is found needs a blood test the same day.

**Look out for:**
- Feeling confused or very sleepy
- Breathing very fast, or finding it hard to breathe
- Yellow skin or eyes, or dark pee

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above, or get worse quickly
- Tell anyone you travelled with to get help straight away if they get symptoms

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Malaria](https://www.nhs.uk/conditions/malaria/)

### `advice_fever_self_care`

**What to do:** You can usually look after a high temperature at home. It should get better within 1 to 4 days.

**Look out for:**
- A rash that does not fade when you press a glass against it
- A stiff neck, or bright light hurting the eyes
- Being very sleepy or hard to wake, or confused
- Breathing very fast, or blotchy, blue or grey skin
- Signs of not having enough water in the body: peeing less, dark pee, or in children dry nappies or no tears

**Get more help when:**
- Call 999 if you or your child get any of the signs above
- Call 111 or ask for an urgent GP appointment if the high temperature lasts 5 days or more. Do the same if treating it at home is not helping.
- Call 111 if a child is not their usual self and you are worried

**Where to go:** You do not need an appointment now. A pharmacist can give advice about medicines. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Rest, and drink plenty of fluids. Keep breastfeeding a baby as usual.
- Take, or give, paracetamol or ibuprofen if you or your child are uncomfortable. Check the leaflet for the right dose for a child.
- Do not undress a child or sponge them down to cool them
- Check on a child regularly, including during the night
- Stay at home and avoid contact with other people until you do not have a high temperature

Source: [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/), [Fever in adults](https://www.nhs.uk/symptoms/fever-in-adults/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ht_child_fit`: The Fever in children page says call 999 for a first fit. The Febrile seizures page says 999 or A&E for a first fit, a fit lasting more than 5 minutes, or more than one in 24 hours. Applying it to every fit, not only the first, is AI judgement: the engine cannot tell a first fit from a repeat with confidence, and a carer is rarely sure it was a simple febrile fit.
- `rf_ht_child_crying`: The Fever in children page lists extreme agitation or crying that will not stop. The Sepsis and Meningitis pages add a weak, high-pitched or continuous cry.
- `rf_ht_child_skin_colour`: Blue, grey or pale skin, lips or tongue is caught for everyone by the universal red flag.
- `rf_ht_child_breathing`: The page says difficulty breathing (grunting, or the stomach sucking in under the ribs), breathlessness or breathing very fast. Uses the general difficulty breathing question, which covers a child struggling to breathe, so a yes to either fires it.
- `rf_ht_baby_high_temperature`: Source difference: the Fever in children page says call 111 for these temperatures. The Sepsis, Meningitis and 'Is your baby seriously ill' pages say call 999 or go to A&E. The more urgent is used. Any baby under 3 months with a high temperature, measured or not, gets at least urgent from the rule below.
- `rf_ht_bulging_soft_spot`: Clinical knowledge: a bulging soft spot with a high temperature can be a sign of meningitis in a baby. No NHS page in the source log lists it with an action.
- `rf_ht_meningitis_signs`: For children the rule above sends an ambulance, as the Fever in children page says call 999.
- `rf_ht_cold_hands`: The Sepsis and Meningitis pages say call 999 or go to A&E for an adult who feels hot or cold to the touch. Marked soft for adults, as in the breathlessness rules, so that likely flu with aching can lower it. The rule for children above is firm.
- `rf_ht_very_painful_headache`: Taken from the Meningitis page. Marked soft because a bad headache is common with flu; meningitis itself, if likely, keeps the outcome at emergency.
- `rf_ht_seriously_unwell`: The Sepsis page says get help immediately if you think something is seriously wrong. Soft, as in the cough and breathlessness rules.
- `rf_ht_chemotherapy`: Clinical knowledge: a high temperature during chemotherapy can be sepsis with a very weak immune system, which needs antibiotics within the hour. No NHS page in the source log gives the action.
- `rf_ht_under_3_months`: The Fever in children page says call 111 for a baby under 3 months with 38C or more, or if you think they have a high temperature. A measured 38C or more gives emergency through the rule above. The 'serious infection in a young baby' card can also raise this.
- `rf_ht_5_days`: The Fever in children page says call 111. Applying it to adults is AI judgement; the Fever in adults page says get urgent help when a high temperature is not getting better, which a temperature for 5 days usually is.
- `rf_ht_child_rash`: A rash that does not fade when pressed is an emergency (rules above).
- `rf_ht_dehydrated`: The Fever in children page says call 111 for a dehydrated child. The Dehydration page gives the same level for adults with dark pee or peeing less.
- `rf_ht_not_peed`: The Kidney infection page says an urgent GP appointment or 111 for not having a pee all day. For children under 5 the more urgent sepsis rule above applies.
- `rf_ht_weakened_immune_system`: The UTI and Sore throat pages say urgent help for a weakened immune system. Chemotherapy, the most dangerous case, is an emergency above.
- `or_ht_pain_peeing`: The UTI page says an urgent GP appointment or 111 for a UTI with a very high temperature or feeling hot, cold or shivering, or in a child.
- `high_temperature default outcome`: Both NHS pages say a high temperature can usually be looked after at home. Not a floor: likely conditions (for example a urine infection or pneumonia) can raise it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| Bronchiolitis (a chest infection that babies get) | 4120002 | rare | Blocked or runny nose: strongly supports; Cough: supports; Wheezing: supports; Breathing very fast: supports; Baby or young child feeding or eating much less than usual: supports; Very high temperature, or feels hot, cold or shivery: supports |
| COVID-19 | 840539006 | uncommon | Lost or changed sense of smell or taste: supports; Very high temperature, or feels hot, cold or shivery: supports; Dry cough: supports; Aching body: supports; Feels very tired: supports; Blocked or runny nose: supports |
| Flu | 6142004 | uncommon | Very high temperature, or feels hot, cold or shivery: strongly supports; Aching body: strongly supports; Feels very tired: supports; Dry cough: supports; Feels very unwell: supports |
| Pneumonia (an infection deep in the lungs) | 233604007 | uncommon | Cough: strongly supports; Short of breath: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Chest pain worse when breathing in: supports; Yellow or green phlegm: supports; Aching body: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Glandular fever (a virus that causes a sore throat, swollen glands and tiredness) | 271558008 | uncommon | Feels very tired: strongly supports; Swollen glands in the neck: strongly supports; Sore throat not improved after a week: supports; Very high temperature, or feels hot, cold or shivery: supports; Lump in the mouth or neck: supports; Swollen glands in the armpit or groin: supports; Aching body: supports |
| Middle ear infection (an infection behind the eardrum) | 3110003 | common | Earache: strongly supports; Young child rubbing or pulling their ear: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Young child irritable, restless or off their food: supports; Ear feels blocked or full: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Fluid or pus coming out of the ear: supports; Hearing loss or a change in hearing: supports |
| Tonsillitis (infected tonsils at the back of the throat) | 90176007 | common | Pus-filled spots on the tonsils: supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Often gets sore throats: supports; Lump in the mouth or neck: supports; Swollen glands in the neck: supports; Feels very tired: supports; Cough or runny nose: argues against |
| Heat exhaustion | 95868006 | uncommon | Unwell after being in the heat or exercising hard: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Feels sick or has been sick: supports; Feeling very thirsty all the time: supports; Feels very tired: supports; Signs of dehydration: supports |
| Heatstroke (the body overheating dangerously) | 52072009 | rare | Unwell after being in the heat or exercising hard: strongly supports; Hot skin that is not sweating: strongly supports; Still unwell after 30 minutes of cooling down: strongly supports; Suddenly confused: supports; Has had a seizure (fit): supports; Breathing very fast: supports; Heart beating very fast: supports |
| Kawasaki (a rare illness in young children, with a high temperature for 5 days or more) | 75053002 | very rare | High temperature for 5 days or more: strongly supports; Red or bloodshot eye: supports; Red, dry or cracked lips, or a red, swollen tongue: supports; Rash or spots on the skin: supports; Red, swollen hands or feet, or peeling skin on fingers or toes: supports; Swollen glands in the neck: supports |
| Malaria (an infection spread by mosquito bites) | 61462000 | rare | Been to a country where malaria is found in the last year: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels cold to the touch, or shivery: supports; Aching body: supports; Feels sick or has been sick: supports; Very painful headache: supports; Diarrhoea, or being sick: supports |
| Serious infection in a young baby (such as a blood, kidney or brain infection) |  | very rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Baby or young child feeding or eating much less than usual: strongly supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not their usual self, or not wanting to eat, and the carer is worried: supports; Blotchy or mottled skin: supports |
| Viral infection (such as a cold, a tummy bug or another virus) | 34014006 | common | Blocked or runny nose: strongly supports; Aching body: supports; Cough: supports; Diarrhoea, or being sick: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
