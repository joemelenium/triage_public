# Review pack: Diarrhoea and vomiting

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
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [C. difficile](https://www.nhs.uk/conditions/c-difficile/) | 2026-11-19 |  | Page last reviewed: 24 July 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |
| [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | 2026-11-19 |  | Page last reviewed: 09 August 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Norovirus](https://www.nhs.uk/conditions/norovirus/) | 2026-11-19 |  | Page last reviewed: 31 December 2024 |
| [Food poisoning](https://www.nhs.uk/conditions/food-poisoning/) | 2026-11-19 |  | Page last reviewed: 19 December 2024 |

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

## Diarrhoea and vomiting red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dv_vomiting_blood`<br>Being sick with blood, or sick that looks like ground coffee<br>**Note:** Source difference: the Diarrhoea and vomiting page says 999 or A&E. The Vomiting blood page says an urgent GP appointment or 111 if the bleeding has stopped and there are no other symptoms. The more urgent is used, marked soft. | "Being sick with blood in it (vomiting blood)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_green_vomit`<br>Green sick (adults), or yellow-green or green sick (children)<br>**Note:** For a baby, the Reflux in babies page says an urgent GP appointment or 111 for green or yellow sick. The Diarrhoea and vomiting page says 999 or A&E for children. The more urgent is used: in a baby it can mean a twisted bowel. | "Green or yellow-green sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_swallowed_poison`<br>May have swallowed something poisonous or harmful<br>**Note:** Adding button batteries and magnets to the question is AI judgement: both can cause serious harm inside the gut within hours. | "May have swallowed something poisonous or harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E. Take the packet or container with you.* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_meningitis_signs`<br>A stiff neck, or pain when looking at bright lights | "Stiff neck" OR "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_sudden_headache`<br>A sudden, severe headache | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_sudden_tummy_ache`<br>A sudden, severe tummy ache | "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_skin`<br>Blue, grey, pale or blotchy skin, lips or tongue<br>**Note:** Blue, grey or pale skin is in the universal checks. | "Blotchy or mottled skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_fast_breathing`<br>Taking lots of quick, short breaths | "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_child_not_responding`<br>A child who is limp, floppy, hard to wake or not responding as usual | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_rash_not_fading`<br>A rash that does not fade when a glass is pressed on it | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_dv_baby_high_temperature`<br>A baby under 3 months with 38C or more, or 3 to 6 months with 39C or more | "Under 1 year old" AND "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_dv_young_child_no_pee`<br>A child under 5 who has not had a pee (or a wet nappy) for 12 hours or more<br>**Note:** The Sepsis page lists not peeing for 12 hours in a child as a sign of sepsis. The Diarrhoea and vomiting page says 111 for fewer wet nappies (see the urgent rule). No pee at all for 12 hours is taken as the more serious sign, as in the cough rules. | "Under 5 years old" AND "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_dv_dka_ketones`<br>Diabetes, with high ketones or a high blood sugar that insulin is not bringing down | "Has diabetes" AND "High ketones, or high blood sugar that insulin is not bringing down" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_dv_dka_signs`<br>Very thirsty and peeing a lot, with being sick, fruity breath or very fast breathing: possible diabetic ketoacidosis<br>**Note:** Being sick with diarrhoea usually means peeing less, not more. Thirst with peeing more than usual points to high blood sugar. | ("Feeling very thirsty all the time" AND "Peeing more often than usual") AND ("Being sick" OR "Breath smells fruity" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |

## Diarrhoea and vomiting red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dv_cannot_keep_fluids`<br>Keeps being sick and cannot keep fluids down | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_blood`<br>Bloody diarrhoea or bleeding from the bottom | "Bleeding from the bottom, or blood in poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_long_lasting`<br>Diarrhoea for more than 7 days, or being sick for more than 2 days | "Diarrhoea for more than 7 days" OR "Being sick for more than 2 days" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_young_child_dehydrated`<br>A child under 5 with signs of dehydration, such as fewer wet nappies | "Under 5 years old" AND "Signs of dehydration" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_child_stopped_feeding`<br>A baby or young child who has stopped feeding, or is eating much less, while ill | "Under 5 years old" AND "Baby or young child feeding or eating much less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_baby`<br>A baby under 12 months with diarrhoea or being sick<br>**Note:** The page says call 111 if you're worried about a baby under 12 months. Applying it to every baby is a reading of the source, so it is soft: likely reflux or a mild cause can lower it. | "Under 1 year old" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_baby_diarrhoea`<br>A baby under 12 months with diarrhoea<br>**Note:** Kept firm, not soft: babies can become dehydrated quickly, so a likely stomach bug must not lower it. Bringing up milk alone is left to the soft rule above, so a baby with reflux is not always sent for urgent help. Where to draw this line is AI judgement. | "Under 1 year old" AND "Diarrhoea" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_antibiotics`<br>Diarrhoea while taking, or soon after taking, antibiotics | "Diarrhoea" AND "Taking antibiotics now, or took them recently" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [C. difficile](https://www.nhs.uk/conditions/c-difficile/) | |
| `rf_dv_older_child_adult_no_pee`<br>Aged 5 or over and no pee for 12 hours or more<br>**Note:** The page says call 111 if signs of dehydration carry on after rehydration sachets. Not peeing for 12 hours is taken as dehydration that needs more than a pharmacy. AI judgement. | NOT "Under 5 years old" AND "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_dv_diabetes`<br>Diabetes, and being sick<br>**Note:** Being sick when you have diabetes can quickly lead to diabetic ketoacidosis. Using being sick as the trigger is AI judgement. | "Has diabetes" AND "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your diabetes care team now or get help from NHS 111* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_dv_thirsty_peeing`<br>Very thirsty and peeing much more than usual: possible diabetes<br>**Note:** Clinical knowledge: being sick with thirst and peeing more can be the first sign of type 1 diabetes. | "Feeling very thirsty all the time" AND "Peeing more often than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |

## Diarrhoea and vomiting: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_dv_dehydrated_pharmacy`<br>Aged 5 or over with signs of dehydration: a pharmacist can help with rehydration sachets | NOT "Under 5 years old" AND "Signs of dehydration" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*Speak to a pharmacist today. Call 111 if signs of dehydration carry on after rehydration sachets.* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `or_dv_higher_chance_dehydration`<br>An older person, or someone with a weakened immune system or other health condition: more likely to get dehydrated | "Aged 65 or over" OR "Weakened immune system" OR "Has a long-term health condition" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*Speak to a pharmacist. The source gives no fixed time.* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |

## Default outcome

Used when no rule fires.

- **Diarrhoea or being sick with nothing that needs more help: treat it at home**
- Outcome: Self-manageable, Self-care, No appointment needed. *Diarrhoea usually stops within 5 to 7 days, and being sick within 1 or 2 days*
- Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Diarrhoea, or being sick | Do you have diarrhoea, or have you been sick? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Green or yellow-green sick | Have you been sick, and was the sick green or yellow-green? | 71419002 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| May have swallowed something poisonous or harmful | Could you have swallowed something poisonous? For example, a cleaning product, a plant, or someone else's medicine. Or a button battery or magnets? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| High ketones, or high blood sugar that insulin is not bringing down | Have you tested your ketones and they are high (over 3mmol/L in blood, or over 2+ in pee)? Or is your blood sugar high and your insulin is not bringing it down? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Diarrhoea for more than 7 days | Have you had diarrhoea for more than 7 days? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Being sick for more than 2 days | Have you been sick on and off for more than 2 days? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Diarrhoea | Do you have diarrhoea? This means passing watery or runny poo more often than usual. | 62315008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Taking antibiotics now, or took them recently | Are you taking antibiotics, or have you taken them in the last few weeks? |  | [C. difficile](https://www.nhs.uk/conditions/c-difficile/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Has a long-term health condition | Do you have a long-term health condition? For example, diabetes, or a heart, lung or kidney condition. |  | [Flu](https://www.nhs.uk/conditions/flu/) | |

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

### `advice_vomiting_blood_ae`

**What to do:** Call 999 or go to A&E now. Being sick with blood can be a sign of bleeding in your stomach or food pipe. It needs to be checked in hospital straight away.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Cold, clammy, pale skin, or fast or shallow breathing
- Black, sticky poo

**Get more help when:**
- Call 999 if you get worse, keep being sick with blood, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat or drink anything until a doctor has checked you
- If you can, keep a sample or a photo of the sick to show the doctor

Source: [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/), [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

### `advice_dv_ae`

**What to do:** Call 999 or go to A&E now. This needs to be checked in hospital straight away.

**Look out for:**
- Being very sleepy, confused or not responding as usual
- Blue, grey, pale or blotchy skin, lips or tongue
- Finding it hard to breathe

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. If you may have swallowed something harmful, bring the packet or container.

**What you can do yourself:**
- If you have swallowed something harmful, do not try to make yourself sick

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/)

### `advice_stomach_ache_ae`

**What to do:** Call 999 or go to A&E now. Your tummy pain needs to be checked in hospital straight away.

**Look out for:**
- Pain getting worse, or spreading across your tummy
- Feeling faint, passing out, or cold, clammy, pale skin
- Being sick with blood, or green sick

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat anything until a doctor has checked you. Small sips of water are fine.
- Do not take ibuprofen or aspirin. They can make some tummy problems worse.

Source: [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/), [Appendicitis](https://www.nhs.uk/conditions/appendicitis/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

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

### `advice_child_tummy_emergency`

**What to do:** Call 999 or go to A&E now. Your child needs to be checked in hospital straight away.

**Look out for:**
- Your child becoming more sleepy, floppy or hard to wake
- Blue, grey, pale or blotchy skin, lips or tongue
- Green sick, or blood in their poo

**Get more help when:**
- Call 999 if your child gets worse or you cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive if you are on your own with your child. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Do not give your child anything to eat until a doctor has checked them

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_dka_ae`

**What to do:** Call 999 or go to A&E now. These can be signs of diabetic ketoacidosis (DKA), a serious problem caused by a lack of insulin. It needs treatment in hospital straight away.

**Look out for:**
- Being sick, and not able to keep fluids down
- Feeling very sleepy or confused
- Breathing deeply or fast

**Get more help when:**
- Call 999 if the person gets worse, is hard to wake, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive. Bring your insulin, your blood sugar meter and any other medicines you take.

**What you can do yourself:**
- Keep taking your insulin. Do not stop it, even if you are not eating.
- Keep having sips of water

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/)

### `advice_dv_urgent`

**What to do:** Call NHS 111 now. They will tell you what to do, and can arrange a call from a nurse or doctor if you need one.

**Look out for:**
- Signs of dehydration. This means not having enough water in the body. Look for dark, smelly pee, peeing less, or fewer wet nappies.
- Being sick with blood, or green sick
- A sudden, severe tummy ache or headache, or a stiff neck
- A baby or child who is very sleepy, floppy or not responding as usual

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above, other than dehydration
- Call 999 or go to A&E if a child has not had a wet nappy or a pee for 12 hours

**Where to go:** Call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink lots of fluids. Take small sips if you feel sick.
- Carry on breast or bottle feeding your baby. Give small feeds more often than usual.
- Do not give children under 12 medicine to stop diarrhoea

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [C. difficile](https://www.nhs.uk/conditions/c-difficile/)

### `advice_dka_urgent`

**What to do:** Call your diabetes care team now, or get help from NHS 111. Being unwell or being sick when you have diabetes can quickly make your blood sugar and ketones go up.

**Look out for:**
- Ketones over 3mmol/L in your blood, or over 2+ in your pee
- Feeling very thirsty and peeing a lot, or breath that smells fruity
- Feeling very sleepy or confused, or breathing fast

**Get more help when:**
- Call 999 or go to A&E if your ketones are high, or you get any of the signs above

**Where to go:** Call your diabetes care team, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Check your blood sugar and ketones more often, as your diabetes team has told you
- Keep taking your insulin, and drink plenty of sugar-free fluids
- Follow your sick day rules if you have them

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/)

### `advice_dv_pharmacy`

**What to do:** Speak to a pharmacist. They can give you rehydration sachets to mix with water, to replace lost fluids. This helps with dehydration (not having enough water in the body).

**Look out for:**
- Still peeing less, or dark pee, after using the sachets
- Being sick so often you cannot keep fluids down
- Blood in your poo

**Get more help when:**
- Call 111 if you are still peeing less, or your pee is still dark, after using the sachets
- Call 111 if diarrhoea lasts more than 7 days, or being sick lasts more than 2 days
- Call 999 or go to A&E if you are sick with blood, or have a sudden, severe tummy ache

**Where to go:** Go to a pharmacy. You do not need an appointment. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink lots of fluids, such as water or squash. Take small sips if you feel sick.
- Avoid fruit juice and fizzy drinks, which can make diarrhoea worse

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/)

### `advice_dv_self_care`

**What to do:** You can usually treat diarrhoea and being sick at home. The most important thing is to drink lots of fluids to avoid dehydration (not having enough water in the body).

**Look out for:**
- Signs of dehydration, such as dark, smelly pee or peeing less than usual
- Being sick so often you cannot keep fluids down
- Blood in your poo, or diarrhoea for more than 7 days

**Get more help when:**
- Speak to a pharmacist if you have signs of dehydration
- Call 111 if you cannot keep fluids down, have blood in your poo, or diarrhoea lasts more than 7 days or being sick more than 2 days
- Call 999 or go to A&E if you are sick with blood, or have a sudden, severe tummy ache or headache

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Stay at home and get plenty of rest
- Drink lots of fluids, such as water or squash. Take small sips if you feel sick.
- Eat when you feel able to
- Stay off school or work until you have not been sick or had diarrhoea for 2 days
- Wash your hands with soap and water often, and do not prepare food for others

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Norovirus](https://www.nhs.uk/conditions/norovirus/), [Food poisoning](https://www.nhs.uk/conditions/food-poisoning/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_dv_vomiting_blood`: Source difference: the Diarrhoea and vomiting page says 999 or A&E. The Vomiting blood page says an urgent GP appointment or 111 if the bleeding has stopped and there are no other symptoms. The more urgent is used, marked soft.
- `rf_dv_green_vomit`: For a baby, the Reflux in babies page says an urgent GP appointment or 111 for green or yellow sick. The Diarrhoea and vomiting page says 999 or A&E for children. The more urgent is used: in a baby it can mean a twisted bowel.
- `rf_dv_swallowed_poison`: Adding button batteries and magnets to the question is AI judgement: both can cause serious harm inside the gut within hours.
- `rf_dv_skin`: Blue, grey or pale skin is in the universal checks.
- `rf_dv_young_child_no_pee`: The Sepsis page lists not peeing for 12 hours in a child as a sign of sepsis. The Diarrhoea and vomiting page says 111 for fewer wet nappies (see the urgent rule). No pee at all for 12 hours is taken as the more serious sign, as in the cough rules.
- `rf_dv_dka_signs`: Being sick with diarrhoea usually means peeing less, not more. Thirst with peeing more than usual points to high blood sugar.
- `rf_dv_baby`: The page says call 111 if you're worried about a baby under 12 months. Applying it to every baby is a reading of the source, so it is soft: likely reflux or a mild cause can lower it.
- `rf_dv_baby_diarrhoea`: Kept firm, not soft: babies can become dehydrated quickly, so a likely stomach bug must not lower it. Bringing up milk alone is left to the soft rule above, so a baby with reflux is not always sent for urgent help. Where to draw this line is AI judgement.
- `rf_dv_older_child_adult_no_pee`: The page says call 111 if signs of dehydration carry on after rehydration sachets. Not peeing for 12 hours is taken as dehydration that needs more than a pharmacy. AI judgement.
- `rf_dv_diabetes`: Being sick when you have diabetes can quickly lead to diabetic ketoacidosis. Using being sick as the trigger is AI judgement.
- `rf_dv_thirsty_peeing`: Clinical knowledge: being sick with thirst and peeing more can be the first sign of type 1 diabetes.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Diabetic ketoacidosis (DKA). This is when a lack of insulin makes you very ill. | 420422005 | rare | Breath smells fruity: strongly supports; Breathing faster and more deeply than usual: strongly supports; Blood sugar high and not coming down, or ketones raised: strongly supports; Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Keeps being sick and cannot keep fluids down: supports; Stomach ache: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Being sick: strongly supports; High ketones, or high blood sugar that insulin is not bringing down: strongly supports; Breathing very fast: supports; Losing weight without trying: supports; Feels very tired: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Appendicitis (a swollen appendix, a pouch on the bowel) | 74400008 | uncommon | Pain started around the belly button and moved to the lower right: strongly supports; Pain in the lower right side of the tummy: strongly supports; Tummy pain worse when moving, coughing or going over bumps: strongly supports; Not feeling hungry, or eating much less than usual: strongly supports; Stomach ache: strongly supports; Stomach ache gradually getting worse: supports; Feeling sick (nausea): supports; Being sick: supports; Very high temperature, or feels hot, cold or shivery: supports |
| A blocked bowel (bowel obstruction) | 81060008 | rare | Cannot poo or fart at all: strongly supports; Tummy looks swollen or much bigger than usual: strongly supports; Being sick: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Green or yellow-green sick: supports; The lump is painful or firm, or cannot be pushed back in: supports; Constipation: supports |
| A bowel infection after antibiotics (C. difficile) |  | rare | Taking antibiotics now, or took them recently: strongly supports; Diarrhoea: supports; Diarrhoea for more than 7 days: supports; Cramping tummy pain that comes and goes in waves: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports |
| Coeliac condition (the body reacts to gluten, which damages the gut) | 396331005 | uncommon | Symptoms come on after foods with wheat, barley or rye: strongly supports; Bloating: supports; Diarrhoea: supports; Farting a lot, or smelly farts: supports; Feels very tired: supports; Losing weight without trying: supports |
| Cows' milk allergy in a baby | 782555009 | very rare | Has eczema, hay fever or a food allergy: strongly supports; Raised, itchy or swollen rash (hives): supports; Diarrhoea: supports; Bleeding from the bottom, or blood in poo: supports; Baby coughing, gulping or unsettled during feeds: supports; Baby not gaining weight, or losing weight: supports |
| Food poisoning | 75258004 | common | Started after eating food that may have been off, or others who ate it are ill: strongly supports; Diarrhoea: strongly supports; Being sick: strongly supports; Others nearby have the same symptoms: supports; Cramping tummy pain that comes and goes in waves: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Stomach bug (gastroenteritis) | 69776003 | very common | Diarrhoea: strongly supports; Being sick: strongly supports; Others nearby have the same symptoms: supports; Cramping tummy pain that comes and goes in waves: supports; Very high temperature, or feels hot, cold or shivery: supports; Feeling sick (nausea): supports |
| Crohn's or ulcerative colitis (long-term swelling of the gut) | 24526004 | rare | Diarrhoea for more than 7 days: strongly supports; Bleeding from the bottom, or blood in poo: strongly supports; Slime (mucus) in poo: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Cramping tummy pain that comes and goes in waves: supports; Diarrhoea: supports; Changes in pooing for 3 weeks or more: supports |
| The bowel sliding into itself in a child (intussusception) | 49723003 | very rare | Young child with bouts of screaming and knees drawn up, pale or floppy between bouts: strongly supports; Being sick: strongly supports; Bleeding from the bottom, or blood in poo: supports; Slime (mucus) in poo: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Cramping tummy pain that comes and goes in waves: supports |
| Irritable bowel syndrome (IBS) | 10743008 | common | Tummy pain eases after pooing or farting: strongly supports; Stomach ache that does not go away or keeps coming back: strongly supports; Pooing changes between diarrhoea and constipation: strongly supports; Bloating: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Slime (mucus) in poo: supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Constipation: supports |
| Lactose intolerance (cannot easily digest the sugar in milk) | 782415009 | uncommon | Symptoms come on after milk or dairy foods: strongly supports; Bloating: strongly supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Cramping tummy pain that comes and goes in waves: supports; Feeling sick (nausea): supports |
| Motion sickness (travel sickness) | 37031009 | uncommon | Started while travelling by car, boat, plane or on a ride: strongly supports; Feels light-headed: supports; Being sick: supports |
| Sickness in pregnancy (morning sickness) | 51885006 | uncommon | Pregnant, or could be pregnant: strongly supports; Pregnant, or gave birth in the last 6 weeks: supports; Being sick: supports |
| A narrowed stomach outlet in a baby (pyloric stenosis) | 48644003 | very rare | Being sick with great force (projectile): strongly supports; Baby seems hungry straight after being sick: strongly supports; Baby not gaining weight, or losing weight: supports; Signs of dehydration: supports |
| A twisted bowel in a baby (malrotation with volvulus) | 458422009 | very rare | Green or yellow-green sick: strongly supports; Tummy looks swollen or much bigger than usual: strongly supports; Bleeding from the bottom, or blood in poo: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Baby will not stop crying and is very distressed: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |
| Severe sickness in pregnancy (hyperemesis gravidarum) | 14094001 | rare | Keeps being sick and cannot keep fluids down: strongly supports; Pregnant, or could be pregnant: strongly supports; Feels sick or has been sick: strongly supports; Signs of dehydration: strongly supports; Losing weight without trying: supports; Feels light-headed: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
