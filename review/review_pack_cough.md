# Review pack: Cough

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
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Croup](https://www.nhs.uk/conditions/croup/) | 2026-11-18 |  | Page last reviewed: 02 August 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | 2026-11-18 |  | Page last reviewed: 17 July 2026 |
| [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | 2026-11-18 |  | Page last reviewed: 26 June 2026 |
| [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | 2026-11-18 |  | Page last reviewed: 11 June 2025 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | 2026-11-18 |  | Page last reviewed: 2 November 2026 |
| [Asthma](https://www.nhs.uk/conditions/asthma/) | 2026-11-18 |  | Page last reviewed: 07 April 2025 |
| [Chest infection](https://www.nhs.uk/conditions/chest-infection/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | 2026-11-18 |  | Page last reviewed: 10 September 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Lung cancer symptoms](https://www.nhs.uk/conditions/lung-cancer/symptoms/) | 2026-11-18 |  | Page last reviewed: 20 August 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Bronchitis](https://www.nhs.uk/conditions/bronchitis/) | 2026-11-18 |  | Page last reviewed: 18 August 2026 |

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

## Cough red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cough_cannot_talk`<br>Cough and so short of breath that cannot say a short sentence when resting<br>**Note:** The Pneumonia and Bronchitis pages say call 999 for struggling to breathe, choking, gasping and unable to speak. That more severe case is caught by the universal red flag for severe difficulty breathing. | "Too breathless to say a short sentence" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| `rf_cough_sudden_breathlessness`<br>Cough with breathing that came on suddenly or suddenly got much worse | "Breathlessness came on suddenly, or suddenly got much worse" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| `rf_cough_child_struggling`<br>A child with a cough who is struggling to breathe: grunting, or tummy sucking in under the ribs | "Under 16 years old" AND "Child struggling to breathe (grunting, or tummy sucking in under the ribs)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_cough_child_floppy`<br>A child with a cough who is limp, floppy, hard to wake or not responding as usual<br>**Note:** The Pneumonia page gives the same advice for a baby who cannot be woken or feels floppy. The Bronchitis page says call 999 for that. | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_cough_stridor`<br>Cough with a high-pitched sound when breathing in<br>**Note:** Source difference: the Sore throat page says call 999 or go to A&E for a high-pitched sound when breathing. The Croup page lists it as a croup symptom and says an urgent GP appointment or 111, unless the child is struggling to breathe. The more urgent is used, marked soft. Needs clinical review. | "High-pitched sound when breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_cough_blotchy_skin`<br>Cough with blotchy or mottled skin: possible sepsis | "Blotchy or mottled skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_rash_not_fading`<br>Cough with a rash that does not fade when a glass is pressed on it<br>**Note:** The Sepsis page gives the same advice. | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| `rf_cough_fit`<br>Cough with a seizure (fit)<br>**Note:** The COVID-19 page gives the same advice for a first fit. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| `rf_cough_seriously_unwell`<br>Very unwell and getting worse, or feels something is seriously wrong<br>**Note:** Taken from the COVID-19 page. The Sepsis and Bronchiolitis pages also say to trust your instincts. Marked soft because it depends on how worried the person is, not on a specific sign. | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| `rf_cough_choked`<br>Cough that started suddenly after choking on something<br>**Note:** Clinical knowledge: something breathed into the airway needs to be checked and removed in hospital. No NHS symptom page in the source log covers this. | "Started after choking on something" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_cough_pauses_in_breathing`<br>A young child with a cough and pauses in their breathing | "Under 5 years old" AND "Pauses in a young child's breathing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_cough_child_restless`<br>A young child who is very upset or restless, struggling to breathe and cannot be calmed | "Under 5 years old" AND "Child very upset or restless, struggling to breathe and cannot be calmed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_cough_sepsis_signs`<br>Cough with very fast breathing and a high temperature or feeling very unwell: possible sepsis<br>**Note:** Requiring a high temperature or feeling very unwell is AI judgement, so that fast breathing from a panic attack is not sent to A&E on its own. | "Breathing very fast" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_young_child_breathing_fast`<br>A child under 5 with a cough who is breathing very fast | "Under 5 years old" AND "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_baby_high_temperature`<br>A baby under 3 months with 38C or more, or 3 to 6 months with 39C or more<br>**Note:** Source difference: the COVID-19 and Bronchiolitis pages say an urgent GP appointment or 111 for this temperature. The Sepsis page says call 999 or go to A&E. The more urgent is used. | "Under 1 year old" AND "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_young_child_not_peeing`<br>A child under 5 with a cough who has not had a pee for 12 hours or more<br>**Note:** Source difference: the Bronchiolitis page says an urgent GP appointment or 111 for a dry nappy for 12 hours. The more urgent Sepsis page advice is used. | "Under 5 years old" AND "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_whooping_chest_pain`<br>Coughing fits with chest pain that is worse when breathing or coughing<br>**Note:** The Whooping cough page says this could be a sign of pneumonia. Limiting it to people with coughing fits is an AI reading: the Pneumonia and Bronchitis pages give an urgent GP appointment or 111 for the same pain with other coughs. | "Chest pain worse when breathing in" AND "Coughing fits, sometimes with a whoop" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| `rf_cough_child_sit_up_or_drooling`<br>A child who is drooling more than usual, or wants to sit up rather than lie down and has a high-pitched sound when breathing<br>**Note:** The Croup page says call 999 or go to A&E if a child is unwell and drooling more than usual, finding it hard to swallow, or wants to sit rather than lie down. Requiring a high-pitched sound when breathing with wanting to sit up is AI judgement, so that a child with a blocked nose who sleeps propped up is not sent to A&E. Added in the breathing batch after test-case authors found no question for it. | "Under 16 years old" AND ("Drooling" OR ("Child wants to sit up rather than lie down" AND "High-pitched sound when breathing")) | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_cough_sepsis_cold_or_shivery`<br>Feeling cold to the touch or shivery, with feeling very unwell or breathing very fast: possible sepsis, even without a high temperature<br>**Note:** The Sepsis page says call 999 or go to A&E for an adult who feels hot or cold to the touch or is shivery, and says a high temperature is less common in older adults with sepsis. Requiring feeling very unwell or breathing very fast is AI judgement, so that everyone with a shivery cold is not sent to A&E. Soft, so that likely flu can lower it; sepsis itself, if likely, keeps the outcome at emergency. | "Feels cold to the touch, or shivery" AND ("Feels very unwell" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_cough_young_child_cold_or_shivery`<br>A child under 5 who feels cold to the touch or is shivery<br>**Note:** Source difference: the Sepsis page says call 999 or go to A&E for a child under 5 who feels cold to the touch or is shivery. The Bronchiolitis page says an urgent GP appointment or 111 for a child who feels hot or cold to the touch or is shivering. The more urgent is used, marked soft, with the urgent high temperature rule as its floor. | "Under 5 years old" AND "Feels cold to the touch, or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Cough red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cough_very_bad`<br>A very bad cough, or one that is quickly getting worse<br>**Note:** The Whooping cough and Bronchiectasis pages give the same advice. | "Cough very bad or getting worse quickly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_very_unwell`<br>Cough and feeling very unwell | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_chest_pain`<br>Cough with chest pain<br>**Note:** The chest pain entry symptom also applies once chest pain is reported, with its own red flags. The Flu and COVID-19 pages say call 999 or go to A&E for sudden chest pain; that is covered by the chest pain red flag for sudden pain that does not go away. | "Chest pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_worse_breathing_in`<br>Cough with chest pain that is worse when breathing or coughing<br>**Note:** The Bronchitis and Pleurisy pages give the same advice. | "Chest pain worse when breathing in" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | |
| `rf_cough_short_of_breath`<br>Cough and short of breath<br>**Note:** The Cough page says 'you find it hard to breathe'. The Pneumonia and Bronchitis pages say 'you're feeling short of breath'. The breathlessness entry symptom also applies once this is reported. Made soft after development cases showed over-triage; the firm rule below keeps difficulty breathing at urgent. | "Short of breath" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_difficulty_breathing`<br>Cough and finding it hard to breathe<br>**Note:** The Cough page says to get help if 'you find it hard to breathe'. | "Difficulty breathing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_coughing_up_blood`<br>Cough and coughing up blood<br>**Note:** The coughing up blood entry symptom also applies once this is reported, with its own emergency rules. | "Coughing up blood" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_swollen_neck_glands`<br>Cough with a swollen, painful side of the neck (swollen glands) | "Swollen glands in the neck" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `rf_cough_yellow_green_phlegm`<br>Cough with yellow or green phlegm, and a high temperature, breathlessness or feeling very unwell<br>**Note:** Source difference: the Pneumonia page says an urgent GP appointment or 111. The Chest infection page lists yellow or green phlegm as a usual symptom that gets better on its own in 7 to 10 days. The more urgent is used, marked soft. Requiring a high temperature, breathlessness or feeling very unwell (signs of a chest infection that needs checking) is AI judgement, so a cold with green phlegm is not sent for urgent care. Changed after the pilot check. | "Yellow or green phlegm" AND ("Very high temperature, or feels hot, cold or shivery" OR "Short of breath" OR "Feels very unwell") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | |
| `rf_cough_frothy_pink_phlegm`<br>Coughing up frothy pink phlegm | "Frothy pink phlegm" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| `rf_cough_lots_of_phlegm`<br>Coughing up a lot of phlegm every day<br>**Note:** AI reading: the Bronchiectasis page gives this as an example of a cough that is very bad or quickly getting worse. For someone whose usual cough is like this, it may not be urgent. | "Coughs up a lot of phlegm every day" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| `rf_cough_croup`<br>A child with a barking cough (possible croup)<br>**Note:** The Croup page says to call 111 or see a GP if you think your child may have croup, because they may need medicine. | "Under 16 years old" AND "Barking cough" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_cough_whooping_baby`<br>A baby with coughing fits (possible whooping cough)<br>**Note:** The page says babies under 6 months. Under 1 year is used because there is no finer age band yet; this is more cautious. | "Under 1 year old" AND "Coughing fits, sometimes with a whoop" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| `rf_cough_whooping_contact_pregnant`<br>Pregnant, or recently given birth, and in contact with whooping cough<br>**Note:** The page says pregnant. Including people who gave birth in the last 6 weeks comes from how the observation is worded; it is more cautious. | "Pregnant, or gave birth in the last 6 weeks" AND "In contact with someone who has whooping cough" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| `rf_cough_high_temp_higher_chance`<br>Cough with a high temperature in someone more likely to get seriously ill: 65 or over, pregnant, a long-term condition, or a weakened immune system<br>**Note:** Source difference: the Flu and Bronchitis pages say an urgent GP appointment or 111 for these groups. The Chest infection page says see a GP (non-urgent). The more urgent is used. Requiring a high temperature, to mark flu or a chest infection, is AI judgement. | "Very high temperature, or feels hot, cold or shivery" AND ("Aged 65 or over" OR "Pregnant, or gave birth in the last 6 weeks" OR "Has a long-term health condition" OR "Weakened immune system") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Flu](https://www.nhs.uk/conditions/flu/) | |
| `rf_cough_not_peed`<br>Cough and no pee for 12 hours or more<br>**Note:** For children under 5 the more urgent Sepsis page rule above applies. | "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_cough_child_feeding_less`<br>A baby or young child with a cough who is feeding or eating much less than usual | "Under 5 years old" AND "Baby or young child feeding or eating much less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_cough_copd_flare_up`<br>COPD that is worse than usual | "Aged 16 or over" AND "Diagnosed with COPD" AND "COPD worse than usual (a flare-up)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| `rf_cough_more_than_usual`<br>A long-term lung or heart condition, and more short of breath than usual<br>**Note:** The Bronchiectasis and COPD pages say an urgent GP appointment or 111 for being more short of breath than usual. The Shortness of breath page says contact 111 for difficulty breathing, 'you may be more short of breath than usual'. Applying it to any long-term lung or heart condition is AI judgement. Added in the breathing batch: before this it could only be reached through a question about COPD. | "More short of breath than usual, with a long-term lung or heart condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| `rf_cough_young_child_worse`<br>A child under 5 whose symptoms are getting worse, or not getting better<br>**Note:** The Bronchiolitis page says an urgent GP appointment or 111 if a child has had a cold and it is getting worse. The Croup page says the same for a child getting worse or not getting better. | "Under 5 years old" AND "Symptoms getting worse, or not getting better after about a week" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_cough_baby_born_early_or_heart_lung`<br>A baby under 1 who was born early, or has a heart or lung condition or a weak immune system<br>**Note:** AI judgement. The Bronchiolitis page says these babies have a higher chance of getting seriously ill, but gives no action for it on its own. A same-day check for a baby like this with breathing symptoms is a reading of that. Needs clinical review. | "Under 1 year old" AND "Young child born early, or with a heart or lung condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | **AI judgement, needs clinical review** | |
| `rf_cough_bronchiectasis_infection`<br>Diagnosed bronchiectasis, with signs of a chest infection: a high temperature, or chest pain when breathing<br>**Note:** Someone with bronchiectasis has a long-term lung condition, so the question about one is asked first, to keep the number of questions down. | ("Very high temperature, or feels hot, cold or shivery" OR "Chest pain worse when breathing in") AND "Has a long-term health condition" AND "Diagnosed with bronchiectasis" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| `rf_cough_flu_like_higher_chance`<br>Flu-like symptoms (a high temperature or aching all over) in someone more likely to get seriously ill: 65 or over, pregnant, a long-term condition, or a weakened immune system<br>**Note:** The Flu page gives this advice for flu symptoms in these groups. A test is not needed. Added after development cases showed the rule had only fired with a positive test. | ("Very high temperature, or feels hot, cold or shivery" OR "Aching body") AND ("Aged 65 or over" OR "Pregnant, or gave birth in the last 6 weeks" OR "Has a long-term health condition" OR "Weakened immune system") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Flu](https://www.nhs.uk/conditions/flu/) | |
| `rf_cough_positive_test_higher_chance`<br>A positive COVID-19 or flu test in someone more likely to get seriously ill: 65 or over, pregnant, a long-term condition, or a weakened immune system<br>**Note:** Kept firm, not soft: likely flu must not lower it, because the Flu page gives this advice for people with flu. The Flu page says an urgent GP appointment or 111 for flu symptoms in these groups. The COVID-19 page says it is particularly important to get help if you are at higher chance of getting ill, and that people who can have COVID-19 treatment should test as soon as they get symptoms. Using a positive test to mark flu or COVID-19 is AI judgement. The page's age for COVID-19 is 60; the existing age band of 65 is used. | ("Tested positive for COVID-19" OR "Tested positive for flu") AND ("Aged 65 or over" OR "Pregnant, or gave birth in the last 6 weeks" OR "Has a long-term health condition" OR "Weakened immune system") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Flu](https://www.nhs.uk/conditions/flu/) | |
| `rf_cough_symptoms_worse`<br>A cough of less than 3 weeks with symptoms getting worse, or not getting better<br>**Note:** Source difference: the COVID-19 page says an urgent GP appointment or 111 if symptoms are getting worse or not getting better, and the Flu page if they do not improve after 7 days. The Common cold and Chest infection pages say see a GP (non-urgent). The more urgent is used, marked soft, with the firm GP rule below as its floor. Limited to a cough of less than 3 weeks (AI judgement): these pages describe a short illness, and a cough of 3 weeks or more has its own rule (see a GP) on the Cough page. | "Symptoms getting worse, or not getting better after about a week" AND NOT "Cough for 3 weeks or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |

## Cough: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_cough_asthma_attack_recovered`<br>Diagnosed asthma, and an asthma attack in the last few days that has now settled<br>**Note:** The Asthma page says: if you've had an asthma attack and have recovered, see a GP within 2 days. Added in the breathing batch after test-case authors found no question for it. | "Diagnosed with asthma" AND "Had an asthma attack recently that has now settled" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within 2 days, even if you feel better* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| `or_cough_symptoms_worse`<br>Cough with symptoms getting worse, or not getting better<br>**Note:** The Chest infection page says see a GP if your symptoms get worse. The Common cold page says see a GP if cold symptoms get worse or do not get better after 10 days. | "Symptoms getting worse, or not getting better after about a week" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Chest infection](https://www.nhs.uk/conditions/chest-infection/) | |
| `or_cough_3_weeks`<br>A cough for 3 weeks or more<br>**Note:** The Bronchitis page says an urgent GP appointment or 111 for a cough of more than 3 weeks that is not getting better. The Cough, Lung cancer, COPD and Tuberculosis pages say see a GP. The Cough page is used, as the page for the symptom itself. | "Cough for 3 weeks or more" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `or_cough_weight_loss`<br>Cough and losing weight for no reason | "Losing weight without trying" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `or_cough_weak_immune_system`<br>Cough in someone with a weakened immune system | "Weakened immune system" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| `or_cough_night_sweats`<br>Cough with night sweats | "Night sweats" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| `or_cough_tb_contact`<br>Cough after a lot of time with someone who has TB, or living where TB is common<br>**Note:** The page covers contact with someone who has TB. Including having lived where TB is common is AI judgement. | "Close contact with TB, or lived where TB is common" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| `or_cough_frequent_chest_infections`<br>Keeps getting chest infections, or has one that is not getting better<br>**Note:** The Lung cancer and Bronchiectasis pages also list this. | "Keeps getting chest infections, or one that is not getting better" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| `or_cough_asthma_not_controlled`<br>Asthma needing the reliever more often, or waking at night | "Diagnosed with asthma" AND "Asthma needing the reliever more often, or waking at night" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |

## Default outcome

Used when no rule fires.

- **Cough with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *A cough usually clears up on its own within 3 to 4 weeks*
- Source: [Cough](https://www.nhs.uk/symptoms/cough/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Cough | Do you have a cough? | 49727002 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Too breathless to say a short sentence | Are you so short of breath that you cannot say a short sentence, even when resting? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Breathlessness came on suddenly, or suddenly got much worse | Did your breathing problem come on suddenly? Or has it suddenly got much worse? |  | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child struggling to breathe (grunting, or tummy sucking in under the ribs) | Is the person who is unwell struggling to breathe? You may hear grunting noises, or see their tummy sucking in under their ribs. |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| High-pitched sound when breathing | Are you making a high-pitched sound when you breathe? | 70407001 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Started after choking on something | Did this start suddenly after choking on something, such as food or a small object? | 249489001 | **AI judgement, needs clinical review** | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pauses in a young child's breathing | Are there pauses in the child's breathing, where they stop breathing for a few seconds? | 1023001 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Child very upset or restless, struggling to breathe and cannot be calmed | Is the child very upset or restless, finding it hard to breathe, and cannot be calmed down? |  | [Croup](https://www.nhs.uk/conditions/croup/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Chest pain worse when breathing in | Is the chest pain worse when you breathe in? | 2237002 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Coughing fits, sometimes with a whoop | Do you get coughing fits that last a few minutes? You may make a "whoop" sound when you breathe in between coughs. | 43025008 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Drooling | Are you drooling? This can be a sign of not being able to swallow. | 62718007 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Child wants to sit up rather than lie down | Does the child want to sit up rather than lie down, because it is easier to breathe? |  | [Croup](https://www.nhs.uk/conditions/croup/) | |
| Feels cold to the touch, or shivery | Do you feel cold to the touch, or are you shivering or shivery? This can happen even without a high temperature. |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Cough very bad or getting worse quickly | Is your cough very bad, or getting worse quickly? For example, a hacking cough, or you cannot stop coughing. |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Coughing up blood | Are you coughing up blood? | 66857006 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Swollen glands in the neck | Do you have swollen glands in your neck? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Yellow or green phlegm | Is the phlegm (mucus) you cough up yellow or green? | 42192008 | [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | |
| Frothy pink phlegm | Are you coughing up frothy, pink phlegm (mucus)? |  | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| Coughs up a lot of phlegm every day | Do you cough up a lot of phlegm (mucus) every day? |  | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| Barking cough | Does the cough sound like a bark, like a seal? | 17986004 | [Croup](https://www.nhs.uk/conditions/croup/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| In contact with someone who has whooping cough | Have you been in contact with someone who has whooping cough? |  | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Has a long-term health condition | Do you have a long-term health condition? For example, diabetes, or a heart, lung or kidney condition. |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Aged 16 or over | Is the person who is unwell aged 16 or over? |  | **AI judgement, needs clinical review** | |
| Diagnosed with COPD | Has a doctor told you that you have COPD? This is a long-term lung condition that causes coughing and breathlessness. |  | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| COPD worse than usual (a flare-up) | Is your COPD worse than usual? For example, you are more short of breath than usual, or coughing up more phlegm (mucus). |  | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| More short of breath than usual, with a long-term lung or heart condition | Do you have a long-term lung condition or heart condition, such as COPD, asthma, bronchiectasis or heart failure? And are you more short of breath than you usually are? |  | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| Symptoms getting worse, or not getting better after about a week | Are your symptoms getting worse? Or have they not started to get better after about a week? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Young child born early, or with a heart or lung condition | Was the child born early (premature)? Or do they have a heart or lung condition, or a weak immune system that makes it harder to fight infection? |  | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Diagnosed with bronchiectasis | Has a doctor told you that you have bronchiectasis? This is a long-term condition where the airways in the lungs are damaged and make a lot of phlegm (mucus). | 939431000000108 | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| Aching body | Does your body ache all over? | 68962001 | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Tested positive for COVID-19 | Have you done a COVID-19 test that was positive in the last few days? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Tested positive for flu | Have you had a test for flu that was positive in the last few days? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Cough for 3 weeks or more | Have you had the cough for 3 weeks or more? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Diagnosed with asthma | Has a doctor told you that you have asthma? | 161527007 | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Had an asthma attack recently that has now settled | Have you had an asthma attack in the last few days that has now settled? This is when your symptoms were severe and it was hard to breathe. |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Night sweats | Do you have night sweats, where you wake up very sweaty? | 42984000 | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| Close contact with TB, or lived where TB is common | Have you spent a lot of time with someone who has TB (tuberculosis)? Or have you lived in a country where TB is common? |  | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| Keeps getting chest infections, or one that is not getting better | Do you keep getting chest infections? Or do you have a chest infection that is not getting better? |  | [Lung cancer symptoms](https://www.nhs.uk/conditions/lung-cancer/symptoms/) | |
| Asthma needing the reliever more often, or waking at night | Have you needed your reliever inhaler more often than usual? Or is your asthma waking you at night, or stopping you doing your usual activities? |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |

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

### `advice_cough_emergency`

**What to do:** Call 999 or go to A&E now. This could be a sign of a serious problem.

**Look out for:**
- Struggling to breathe, choking or gasping
- Skin, lips or tongue turning blue, grey, pale or blotchy
- Feeling suddenly confused, or being very sleepy or hard to wake
- Coughing up more than a few streaks of blood

**Get more help when:**
- Call 999 straight away if you get any of the signs above, or you get worse while you wait

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Cough](https://www.nhs.uk/symptoms/cough/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/), [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/), [Pneumonia](https://www.nhs.uk/conditions/pneumonia/)

### `advice_child_breathing_emergency`

**What to do:** Call 999 or go to A&E now. Your child needs to be checked in hospital straight away.

**Look out for:**
- Grunting noises, or their tummy sucking in under their ribs
- Pauses in their breathing
- Lips, tongue or skin turning blue, grey, pale or blotchy
- Being limp, floppy or hard to wake

**Get more help when:**
- Call 999 straight away if your child gets any of the signs above, or gets worse while you wait
- Trust your own judgement. If you think your child is seriously unwell, call 999.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines your child takes.

**What you can do yourself:**
- Keep your child upright and try to keep them calm. Crying can make breathing harder.
- Do not put your child in a steamy room or get them to breathe in steam

Source: [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/), [Croup](https://www.nhs.uk/conditions/croup/), [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

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

### `advice_child_breathing_999`

**What to do:** Call 999 now. Your child needs emergency help.

**Look out for:**
- Keep checking that your child is still responding and breathing
- If they stop responding and stop breathing, the 999 call handler will tell you how to start CPR. This means you press hard and fast on the middle of their chest.

**Get more help when:**
- Call 999 again if your child's condition changes before help arrives

**Where to go:** Call 999. Do not drive your child to A&E. Stay with your child until help arrives.

**What you can do yourself:**
- Keep your child upright if they are awake, and try to keep them calm

Source: [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/), [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/)

### `advice_cough_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Struggling to breathe, or so short of breath you cannot say a short sentence
- Skin, lips or tongue turning blue, grey, pale or blotchy
- Feeling suddenly confused, or a child who is floppy or hard to wake
- Coughing up more than a few streaks of blood, or sudden chest pain

**Get more help when:**
- Call 999 or go to A&E now if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Take paracetamol or ibuprofen for any pain or a high temperature. Check the leaflet first.
- Do not take cough medicine if you might have a chest infection. Coughing helps clear it.

Source: [Cough](https://www.nhs.uk/symptoms/cough/), [Pneumonia](https://www.nhs.uk/conditions/pneumonia/), [Bronchitis](https://www.nhs.uk/conditions/bronchitis/)

### `advice_croup_urgent`

**What to do:** Ask for an urgent GP appointment or call NHS 111 today. A barking cough in a child can be croup, and a doctor may give medicine to help.

**Look out for:**
- Struggling to breathe: grunting, or the tummy sucking in under the ribs
- Blue, grey, pale or blotchy skin, lips or tongue
- Being sleepier than usual, hard to wake, or unusually quiet and still
- Drooling, finding it hard to swallow, or wanting to sit rather than lie down

**Get more help when:**
- Call 999 or go to A&E now if your child gets any of the signs above. Do the same if they are very upset, struggle to breathe and cannot be calmed.
- Call 111 again if your child is not getting better after seeing a doctor

**Where to go:** Ask your GP surgery for an urgent appointment or call 111. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Sit your child upright and try not to let them lie down
- Comfort them and try to keep them calm. Crying can make it worse.
- Give them plenty of fluids, and check on them often, including at night
- Do not put your child in a steamy room or get them to breathe in steam

Source: [Croup](https://www.nhs.uk/conditions/croup/)

### `advice_whooping_cough_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. This could be whooping cough, which can be serious in young babies.

**Look out for:**
- Lips, tongue, face or skin suddenly turning blue or grey
- Finding it hard to breathe, or shallow breathing
- Chest pain that is worse when breathing or coughing
- A seizure (fit)

**Get more help when:**
- Call 999 or go to A&E now if you or your child get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111. For children aged 5 or over you can also use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Get plenty of rest and drink lots of fluids
- Do not give aspirin to children under 16
- Stay off school, work or nursery for 2 days after starting antibiotics. With no antibiotics, stay off for 3 weeks after the cough started.

Source: [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/)

### `advice_copd_flare_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your COPD, a long-term lung condition, is worse than usual.

**Look out for:**
- Severe difficulty breathing, such as gasping, choking or not being able to get words out
- Your chest feeling tight or heavy
- Lips or skin turning very pale, blue or grey
- Feeling suddenly confused

**Get more help when:**
- Call 999 or go to A&E now if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999 or go to A&E. Do not drive yourself to A&E.

**What you can do yourself:**
- Use your inhalers as your care team told you
- If you have a rescue pack of medicines at home, follow the instructions you were given
- Avoid smoke and strong smells, such as cleaning products or perfume

Source: [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/)

### `advice_cough_flu_higher_risk`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You may be more likely to get seriously ill with flu, and treatment can help if it is started early.

**Look out for:**
- Sudden chest pain
- Difficulty breathing
- Coughing up blood
- Symptoms getting worse, or not getting better after a week

**Get more help when:**
- Call 999 or go to A&E if you get sudden chest pain, find it hard to breathe, or start coughing up a lot of blood

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Rest and sleep
- Keep warm
- Drink plenty of water to avoid dehydration (peeing less than usual can be a sign)

Source: [Flu](https://www.nhs.uk/conditions/flu/)

### `advice_asthma_attack_recovered`

**What to do:** See a GP within 2 days of your asthma attack, even if you feel better now. They will check your treatment and help stop it happening again.

**Look out for:**
- Your symptoms come back, or you need your reliever inhaler more than usual
- Another asthma attack: severe symptoms that make it hard to breathe
- Not being able to say a short sentence because you are so short of breath

**Get more help when:**
- Use your reliever inhaler if symptoms come back. Sit up straight and try to stay calm.
- Call 999 if you have another attack and get worse, your inhaler does not help, or you do not have it

**Where to go:** Ask your GP surgery for an appointment in the next 2 days. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Always have your reliever inhaler with you
- Follow your asthma action plan if you have one
- Try to avoid things that set off your asthma, such as smoke, pollen or animals

Source: [Asthma](https://www.nhs.uk/conditions/asthma/)

### `advice_cough_gp`

**What to do:** See a GP about your cough. It is rarely a sign of something serious, but it should be checked.

**Look out for:**
- A cough that is very bad or quickly getting worse
- Coughing up blood
- Chest pain, or finding it hard to breathe
- Feeling very unwell, or a swollen, painful side of the neck

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if you are struggling to breathe or your lips or skin turn blue or grey

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Rest and drink plenty of fluids
- If you smoke, stopping will help

Source: [Cough](https://www.nhs.uk/symptoms/cough/), [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/), [Lung cancer symptoms](https://www.nhs.uk/conditions/lung-cancer/symptoms/)

### `advice_asthma_gp`

**What to do:** See a GP or asthma nurse. Your asthma may need a change of treatment.

**Look out for:**
- Needing your reliever inhaler more and more
- Symptoms that wake you at night or stop you doing your usual activities
- An asthma attack: severe symptoms that make it hard to breathe

**Get more help when:**
- After any asthma attack, see a GP within 2 days, even if you feel better
- Call 999 if you have an asthma attack and get worse. Also call 999 if your inhaler does not help, or you do not have it.

**Where to go:** Make an appointment with a GP or asthma nurse. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Always have your reliever inhaler with you
- Use your inhalers as your care team told you. A pharmacist can check you are using them the right way.
- Try to avoid things that set off your asthma, such as smoke, pollen or animals

Source: [Asthma](https://www.nhs.uk/conditions/asthma/)

### `advice_cough_self_care`

**What to do:** You can treat this yourself. A cough usually clears up on its own within 3 to 4 weeks.

**Look out for:**
- A cough that lasts more than 3 weeks
- A cough that is very bad or quickly getting worse
- Chest pain, finding it hard to breathe, or coughing up blood
- Feeling very unwell

**Get more help when:**
- See a pharmacist if you would like help, such as cough sweets or syrup
- See a GP if you have had a cough for more than 3 weeks, or you are losing weight for no reason
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if you are struggling to breathe or your lips or skin turn blue or grey

**Where to go:** You do not need an appointment now. A pharmacist can help if you need it. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Try to stay at home if you have a high temperature or do not feel well enough to do your usual things
- Take paracetamol or ibuprofen for any pain
- Try hot lemon and honey. Do not give honey to babies under 1, and do not give hot drinks to small children.
- Some medicines are not safe for everyone, for example if you are pregnant. Check the leaflet or ask a pharmacist.

Source: [Cough](https://www.nhs.uk/symptoms/cough/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cough_cannot_talk`: The Pneumonia and Bronchitis pages say call 999 for struggling to breathe, choking, gasping and unable to speak. That more severe case is caught by the universal red flag for severe difficulty breathing.
- `rf_cough_child_floppy`: The Pneumonia page gives the same advice for a baby who cannot be woken or feels floppy. The Bronchitis page says call 999 for that.
- `rf_cough_stridor`: Source difference: the Sore throat page says call 999 or go to A&E for a high-pitched sound when breathing. The Croup page lists it as a croup symptom and says an urgent GP appointment or 111, unless the child is struggling to breathe. The more urgent is used, marked soft. Needs clinical review.
- `rf_cough_rash_not_fading`: The Sepsis page gives the same advice.
- `rf_cough_fit`: The COVID-19 page gives the same advice for a first fit.
- `rf_cough_seriously_unwell`: Taken from the COVID-19 page. The Sepsis and Bronchiolitis pages also say to trust your instincts. Marked soft because it depends on how worried the person is, not on a specific sign.
- `rf_cough_choked`: Clinical knowledge: something breathed into the airway needs to be checked and removed in hospital. No NHS symptom page in the source log covers this.
- `rf_cough_sepsis_signs`: Requiring a high temperature or feeling very unwell is AI judgement, so that fast breathing from a panic attack is not sent to A&E on its own.
- `rf_cough_baby_high_temperature`: Source difference: the COVID-19 and Bronchiolitis pages say an urgent GP appointment or 111 for this temperature. The Sepsis page says call 999 or go to A&E. The more urgent is used.
- `rf_cough_young_child_not_peeing`: Source difference: the Bronchiolitis page says an urgent GP appointment or 111 for a dry nappy for 12 hours. The more urgent Sepsis page advice is used.
- `rf_cough_whooping_chest_pain`: The Whooping cough page says this could be a sign of pneumonia. Limiting it to people with coughing fits is an AI reading: the Pneumonia and Bronchitis pages give an urgent GP appointment or 111 for the same pain with other coughs.
- `rf_cough_child_sit_up_or_drooling`: The Croup page says call 999 or go to A&E if a child is unwell and drooling more than usual, finding it hard to swallow, or wants to sit rather than lie down. Requiring a high-pitched sound when breathing with wanting to sit up is AI judgement, so that a child with a blocked nose who sleeps propped up is not sent to A&E. Added in the breathing batch after test-case authors found no question for it.
- `rf_cough_sepsis_cold_or_shivery`: The Sepsis page says call 999 or go to A&E for an adult who feels hot or cold to the touch or is shivery, and says a high temperature is less common in older adults with sepsis. Requiring feeling very unwell or breathing very fast is AI judgement, so that everyone with a shivery cold is not sent to A&E. Soft, so that likely flu can lower it; sepsis itself, if likely, keeps the outcome at emergency.
- `rf_cough_young_child_cold_or_shivery`: Source difference: the Sepsis page says call 999 or go to A&E for a child under 5 who feels cold to the touch or is shivery. The Bronchiolitis page says an urgent GP appointment or 111 for a child who feels hot or cold to the touch or is shivering. The more urgent is used, marked soft, with the urgent high temperature rule as its floor.
- `rf_cough_very_bad`: The Whooping cough and Bronchiectasis pages give the same advice.
- `rf_cough_chest_pain`: The chest pain entry symptom also applies once chest pain is reported, with its own red flags. The Flu and COVID-19 pages say call 999 or go to A&E for sudden chest pain; that is covered by the chest pain red flag for sudden pain that does not go away.
- `rf_cough_worse_breathing_in`: The Bronchitis and Pleurisy pages give the same advice.
- `rf_cough_short_of_breath`: The Cough page says 'you find it hard to breathe'. The Pneumonia and Bronchitis pages say 'you're feeling short of breath'. The breathlessness entry symptom also applies once this is reported. Made soft after development cases showed over-triage; the firm rule below keeps difficulty breathing at urgent.
- `rf_cough_difficulty_breathing`: The Cough page says to get help if 'you find it hard to breathe'.
- `rf_cough_coughing_up_blood`: The coughing up blood entry symptom also applies once this is reported, with its own emergency rules.
- `rf_cough_yellow_green_phlegm`: Source difference: the Pneumonia page says an urgent GP appointment or 111. The Chest infection page lists yellow or green phlegm as a usual symptom that gets better on its own in 7 to 10 days. The more urgent is used, marked soft. Requiring a high temperature, breathlessness or feeling very unwell (signs of a chest infection that needs checking) is AI judgement, so a cold with green phlegm is not sent for urgent care. Changed after the pilot check.
- `rf_cough_lots_of_phlegm`: AI reading: the Bronchiectasis page gives this as an example of a cough that is very bad or quickly getting worse. For someone whose usual cough is like this, it may not be urgent.
- `rf_cough_croup`: The Croup page says to call 111 or see a GP if you think your child may have croup, because they may need medicine.
- `rf_cough_whooping_baby`: The page says babies under 6 months. Under 1 year is used because there is no finer age band yet; this is more cautious.
- `rf_cough_whooping_contact_pregnant`: The page says pregnant. Including people who gave birth in the last 6 weeks comes from how the observation is worded; it is more cautious.
- `rf_cough_high_temp_higher_chance`: Source difference: the Flu and Bronchitis pages say an urgent GP appointment or 111 for these groups. The Chest infection page says see a GP (non-urgent). The more urgent is used. Requiring a high temperature, to mark flu or a chest infection, is AI judgement.
- `rf_cough_not_peed`: For children under 5 the more urgent Sepsis page rule above applies.
- `rf_cough_more_than_usual`: The Bronchiectasis and COPD pages say an urgent GP appointment or 111 for being more short of breath than usual. The Shortness of breath page says contact 111 for difficulty breathing, 'you may be more short of breath than usual'. Applying it to any long-term lung or heart condition is AI judgement. Added in the breathing batch: before this it could only be reached through a question about COPD.
- `rf_cough_young_child_worse`: The Bronchiolitis page says an urgent GP appointment or 111 if a child has had a cold and it is getting worse. The Croup page says the same for a child getting worse or not getting better.
- `rf_cough_baby_born_early_or_heart_lung`: AI judgement. The Bronchiolitis page says these babies have a higher chance of getting seriously ill, but gives no action for it on its own. A same-day check for a baby like this with breathing symptoms is a reading of that. Needs clinical review.
- `rf_cough_bronchiectasis_infection`: Someone with bronchiectasis has a long-term lung condition, so the question about one is asked first, to keep the number of questions down.
- `rf_cough_flu_like_higher_chance`: The Flu page gives this advice for flu symptoms in these groups. A test is not needed. Added after development cases showed the rule had only fired with a positive test.
- `rf_cough_positive_test_higher_chance`: Kept firm, not soft: likely flu must not lower it, because the Flu page gives this advice for people with flu. The Flu page says an urgent GP appointment or 111 for flu symptoms in these groups. The COVID-19 page says it is particularly important to get help if you are at higher chance of getting ill, and that people who can have COVID-19 treatment should test as soon as they get symptoms. Using a positive test to mark flu or COVID-19 is AI judgement. The page's age for COVID-19 is 60; the existing age band of 65 is used.
- `rf_cough_symptoms_worse`: Source difference: the COVID-19 page says an urgent GP appointment or 111 if symptoms are getting worse or not getting better, and the Flu page if they do not improve after 7 days. The Common cold and Chest infection pages say see a GP (non-urgent). The more urgent is used, marked soft, with the firm GP rule below as its floor. Limited to a cough of less than 3 weeks (AI judgement): these pages describe a short illness, and a cough of 3 weeks or more has its own rule (see a GP) on the Cough page.
- `or_cough_asthma_attack_recovered`: The Asthma page says: if you've had an asthma attack and have recovered, see a GP within 2 days. Added in the breathing batch after test-case authors found no question for it.
- `or_cough_symptoms_worse`: The Chest infection page says see a GP if your symptoms get worse. The Common cold page says see a GP if cold symptoms get worse or do not get better after 10 days.
- `or_cough_3_weeks`: The Bronchitis page says an urgent GP appointment or 111 for a cough of more than 3 weeks that is not getting better. The Cough, Lung cancer, COPD and Tuberculosis pages say see a GP. The Cough page is used, as the page for the symptom itself.
- `or_cough_tb_contact`: The page covers contact with someone who has TB. Including having lived where TB is common is AI judgement.
- `or_cough_frequent_chest_infections`: The Lung cancer and Bronchiectasis pages also list this.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bronchitis (a short-term infection of the airways in the lungs) | 10509002 | common | Cough: strongly supports; Coughing up phlegm: supports; Blocked or runny nose: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Wheezing: supports; Chest pain worse when breathing in: supports |
| Asthma (a long-term condition that makes the airways narrow), or an asthma attack | 195967001 | uncommon | Wheezing comes and goes, often worse at night or early morning: strongly supports; Wheezing brought on by exercise or cold air: supports; Symptoms come on around pollen, dust, mould or animals: supports; Cough worse at night: supports; Has eczema, hay fever or a food allergy: supports; Chest feels tight or squeezed: supports |
| Bronchiectasis (damaged airways in the lungs that make a lot of phlegm) | 12295008 | very rare | Coughs up a lot of phlegm every day: strongly supports; Coughing up phlegm: strongly supports; Cough for 3 weeks or more: strongly supports; Keeps getting chest infections, or one that is not getting better: strongly supports; Wheezing: supports; Feels very tired: supports; Coughing up blood: supports; More short of breath than usual, with a long-term lung or heart condition: supports |
| Bronchiolitis (a chest infection that babies get) | 4120002 | rare | Blocked or runny nose: strongly supports; Cough: supports; Wheezing: supports; Breathing very fast: supports; Baby or young child feeding or eating much less than usual: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Chest infection that may need treatment from a GP | 50417007 | common | Cough: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Coughing up phlegm: strongly supports; Yellow or green phlegm: strongly supports; Symptoms getting worse, or not getting better after about a week: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Very high temperature, or feels hot, cold or shivery: supports; Chest pain worse when breathing in: supports; Short of breath: supports |
| Common cold | 82272006 | very common | Blocked or runny nose: strongly supports; Hoarse voice: supports; Dry cough: supports; Phlegm dripping down the back of the throat from the nose: supports |
| A flare-up of COPD (a long-term lung condition that makes it hard to breathe) | 195951007 | rare | COPD worse than usual (a flare-up): strongly supports; More short of breath than usual, with a long-term lung or heart condition: strongly supports; Yellow or green phlegm: supports; Cough very bad or getting worse quickly: supports; Short of breath at rest: supports |
| COVID-19 | 840539006 | uncommon | Lost or changed sense of smell or taste: supports; Very high temperature, or feels hot, cold or shivery: supports; Dry cough: supports; Aching body: supports; Feels very tired: supports; Blocked or runny nose: supports |
| Croup (an infection of the airways in young children that causes a barking cough) | 71186008 | rare | Barking cough: strongly supports; High-pitched sound when breathing: strongly supports; Hoarse voice: supports; Cough worse at night: supports; Blocked or runny nose: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Flu | 6142004 | uncommon | Very high temperature, or feels hot, cold or shivery: strongly supports; Aching body: strongly supports; Feels very tired: supports; Dry cough: supports; Feels very unwell: supports |
| Hay fever (an allergy to pollen) | 21719001 | uncommon | Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Blocked or runny nose: strongly supports; Has eczema, hay fever or a food allergy: supports; Dry cough: supports |
| Something breathed into the airway or lungs, such as food or a small toy | 262599003 | rare | Started after choking on something: strongly supports; Cough: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: supports; Wheezing: supports; High-pitched sound when breathing: supports |
| Lung cancer | 363358000 | very rare | Smokes, or has smoked in the past: strongly supports; Cough for 3 weeks or more: strongly supports; Losing weight without trying: supports; Coughing up blood: supports; Keeps getting chest infections, or one that is not getting better: supports; Hoarse voice: supports; Fingertips wider or rounder, with nails curving over (clubbing): supports; Feels very tired: supports; Short of breath: supports |
| Pneumonia (an infection deep in the lungs) | 233604007 | uncommon | Cough: strongly supports; Short of breath: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Chest pain worse when breathing in: supports; Yellow or green phlegm: supports; Aching body: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Scarring of the lungs (pulmonary fibrosis) | 51615001 | very rare | Breathlessness has come on slowly over weeks or months: strongly supports; Out of breath doing everyday things: strongly supports; Dry cough: strongly supports; Short of breath: strongly supports; Cough for 3 weeks or more: supports; Fingertips wider or rounder, with nails curving over (clubbing): supports; Feels very tired: supports; Has breathed in dust, fumes or chemicals for a long time: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Tuberculosis (TB), an infection that usually affects the lungs | 154283005 | very rare | Cough for 3 weeks or more: strongly supports; Night sweats: strongly supports; Close contact with TB, or lived where TB is common: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Very high temperature, or feels hot, cold or shivery: supports; Coughing up blood: supports |
| Whooping cough (an infection that causes long coughing fits) | 27836007 | uncommon | Coughing fits, sometimes with a whoop: strongly supports; Has been sick after coughing: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Blocked or runny nose: supports |
| Heart failure (the heart cannot pump blood as well as it should), or a flare of it | 84114007 | rare | Short of breath: strongly supports; Out of breath doing everyday things: strongly supports; Short of breath when lying flat: strongly supports; Swollen feet, ankles or legs: supports; Suddenly put on weight: supports; Heart failure symptoms worse than usual: supports; Frothy pink phlegm: supports; Cough worse at night: supports; Feels very tired: supports |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
