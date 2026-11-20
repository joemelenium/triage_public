# Review pack: Wheezing

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
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Asthma](https://www.nhs.uk/conditions/asthma/) | 2026-11-18 |  | Page last reviewed: 07 April 2025 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Croup](https://www.nhs.uk/conditions/croup/) | 2026-11-18 |  | Page last reviewed: 02 August 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | 2026-11-18 |  | Page last reviewed: 26 June 2026 |
| [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | 2026-11-18 |  | Page last reviewed: 2 November 2026 |
| [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | 2026-11-18 |  | Page last reviewed: 11 June 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
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

## Wheezing red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wh_allergic_swelling`<br>Wheezing with lips, mouth, tongue or throat suddenly swollen | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_wh_throat_tight`<br>Wheezing with the throat feeling tight | "Throat feels tight" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_wh_after_allergy_trigger`<br>Wheezing that started soon after a food, medicine or insect sting<br>**Note:** AI reading of the Anaphylaxis page, which says call 999 if you become very wheezy after contact with something you are allergic to. Kept firm, not soft, on purpose: missing a severe allergic reaction is life-threatening. Needs clinical review. | "Started soon after a food, medicine or insect sting" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_wh_cannot_talk`<br>Wheezing and so short of breath that cannot say a short sentence<br>**Note:** Clinical knowledge: not being able to finish a sentence is a sign of a severe asthma attack, which can be life-threatening. The COVID-19 page says call 999 or go to A&E for this; 999 is used because a severe asthma attack needs treatment on the way to hospital. | "Too breathless to say a short sentence" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_wh_sudden`<br>Wheezing with breathing that came on suddenly or suddenly got much worse<br>**Note:** The Pulmonary embolism and COVID-19 pages say call 999 or go to A&E for breathing problems that come on suddenly. Marked soft because asthma attacks often start quickly and can settle with a reliever inhaler. | "Breathlessness came on suddenly, or suddenly got much worse" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| `rf_wh_child_struggling`<br>A wheezy child struggling to breathe: grunting, or tummy sucking in under the ribs<br>**Note:** Source difference: the Bronchiolitis page says call 999. The Shortness of breath page says call 999 or go to A&E. The more urgent is used. | "Under 16 years old" AND "Child struggling to breathe (grunting, or tummy sucking in under the ribs)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_child_floppy`<br>A wheezy child who is limp, floppy, hard to wake or not responding as usual<br>**Note:** Source difference: the Bronchiolitis page says call 999 for a child who is floppy and will not wake up. The Shortness of breath page says call 999 or go to A&E for a child who is limp, floppy or not responding as usual. The more urgent is used. | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_pauses_in_breathing`<br>A young child with wheezing and pauses in their breathing | "Under 5 years old" AND "Pauses in a young child's breathing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_choked`<br>Wheezing that started suddenly after choking on something<br>**Note:** Clinical knowledge: something breathed into the airway can cause wheezing on one side and needs to be removed in hospital. | "Started after choking on something" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_wh_asthma_reliever_not_helping`<br>Asthma attack and no better after the most puffs of reliever inhaler allowed, or getting worse | "Diagnosed with asthma" AND "Having an asthma attack now" AND "No better after the most puffs of reliever inhaler allowed, or getting worse" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| `rf_wh_asthma_no_inhaler`<br>Asthma attack and no reliever inhaler | "Diagnosed with asthma" AND "Having an asthma attack now" AND "Asthma attack without a reliever inhaler" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| `rf_wh_young_child_breathing_fast`<br>A wheezy child under 5 who is breathing very fast<br>**Note:** The Bronchiolitis page says call 999 for difficulty breathing that includes breathing quickly. The Sepsis page says call 999 or go to A&E for breathing very fast. A&E is used for fast breathing alone; grunting or the tummy sucking in is sent to 999 above. | "Under 5 years old" AND "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_wh_baby_feeding_poorly`<br>A wheezy baby under 1 who is feeding much less than usual<br>**Note:** AI judgement from clinical knowledge: a wheezy baby who is not feeding may be tiring and needs checking in hospital. The Bronchiolitis page says an urgent GP appointment or 111, so the rule is soft, with the firm urgent rule below as its floor. | "Under 1 year old" AND "Baby or young child feeding or eating much less than usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_wh_baby_high_temperature`<br>A wheezy baby under 3 months with 38C or more, or 3 to 6 months with 39C or more<br>**Note:** Source difference: the Bronchiolitis page says an urgent GP appointment or 111. The Sepsis page says call 999 or go to A&E. The more urgent is used. | "Under 1 year old" AND "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_wh_young_child_not_peeing`<br>A wheezy child under 5 who has not had a pee for 12 hours or more<br>**Note:** Source difference: the Bronchiolitis page says an urgent GP appointment or 111 for a dry nappy for 12 hours. The more urgent Sepsis page advice is used. | "Under 5 years old" AND "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_wh_child_sit_up_or_drooling`<br>A child who is drooling more than usual, or wants to sit up rather than lie down and has a high-pitched sound when breathing<br>**Note:** The Croup page says call 999 or go to A&E if a child is unwell and drooling more than usual, finding it hard to swallow, or wants to sit rather than lie down. Requiring a high-pitched sound when breathing with wanting to sit up is AI judgement, so that a child with a blocked nose who sleeps propped up is not sent to A&E. Added in the breathing batch after test-case authors found no question for it. | "Under 16 years old" AND ("Drooling" OR ("Child wants to sit up rather than lie down" AND "High-pitched sound when breathing")) | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Croup](https://www.nhs.uk/conditions/croup/) | |
| `rf_wh_stridor`<br>A high-pitched sound when breathing in<br>**Note:** Same as the cough rule. Source difference: the Sore throat page says call 999 or go to A&E for a high-pitched sound when breathing. The Croup page lists it as a croup symptom and says an urgent GP appointment or 111. The more urgent is used, marked soft. | "High-pitched sound when breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_wh_sepsis_cold_or_shivery`<br>Feeling cold to the touch or shivery, with feeling very unwell or breathing very fast: possible sepsis, even without a high temperature<br>**Note:** The Sepsis page says call 999 or go to A&E for an adult who feels hot or cold to the touch or is shivery, and says a high temperature is less common in older adults with sepsis. Requiring feeling very unwell or breathing very fast is AI judgement, so that everyone with a shivery cold is not sent to A&E. Soft, so that likely flu can lower it; sepsis itself, if likely, keeps the outcome at emergency. | "Feels cold to the touch, or shivery" AND ("Feels very unwell" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_wh_young_child_cold_or_shivery`<br>A child under 5 who feels cold to the touch or is shivery<br>**Note:** Source difference: the Sepsis page says call 999 or go to A&E for a child under 5 who feels cold to the touch or is shivery. The Bronchiolitis page says an urgent GP appointment or 111 for a child who feels hot or cold to the touch or is shivering. The more urgent is used, marked soft, with the urgent high temperature rule as its floor. | "Under 5 years old" AND "Feels cold to the touch, or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Wheezing red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wh_difficulty_breathing`<br>Wheezing and finding it hard to breathe | "Difficulty breathing" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact NHS 111* | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| `rf_wh_asthma_attack`<br>Diagnosed asthma and having an asthma attack now<br>**Note:** AI reading of the Asthma page, which says to see a GP within 2 days of an asthma attack, even after recovering. Same-day help is used because the attack is happening now. | "Diagnosed with asthma" AND "Having an asthma attack now" | Urgent (help today)<br>Urgent care<br>Today<br>*Use your reliever inhaler now. Then get an urgent GP appointment, even if you feel better.* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| `rf_wh_very_unwell`<br>Wheezing and feeling very unwell, or a child who is very tired, irritable or not themselves<br>**Note:** The Cough page gives the same advice for feeling very unwell. | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_young_child_high_temperature`<br>A wheezy child under 5 with a high temperature, or feeling hot, cold or shivery | "Under 5 years old" AND "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_child_feeding_less`<br>A wheezy baby or young child feeding or eating much less than usual | "Under 5 years old" AND "Baby or young child feeding or eating much less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_not_peed`<br>Wheezing and no pee for 12 hours or more | "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_lying_flat`<br>Wheezing and short of breath when lying flat<br>**Note:** Source difference: the Heart failure page says an urgent GP appointment or 111. The Shortness of breath page says see a GP. The more urgent is used. Wheezing from fluid on the lungs can be a sign of heart failure. | "Short of breath when lying flat" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| `rf_wh_frothy_pink_phlegm`<br>Wheezing and coughing up frothy pink phlegm | "Frothy pink phlegm" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| `rf_wh_copd_flare_up`<br>COPD that is worse than usual | "Aged 16 or over" AND "Diagnosed with COPD" AND "COPD worse than usual (a flare-up)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| `rf_wh_more_than_usual`<br>A long-term lung or heart condition, and more short of breath than usual<br>**Note:** The Bronchiectasis and COPD pages say an urgent GP appointment or 111 for being more short of breath than usual. The Shortness of breath page says contact 111 for difficulty breathing, 'you may be more short of breath than usual'. Applying it to any long-term lung or heart condition is AI judgement. Added in the breathing batch: before this it could only be reached through a question about COPD. | "More short of breath than usual, with a long-term lung or heart condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| `rf_wh_young_child_worse`<br>A child under 5 whose symptoms are getting worse, or not getting better<br>**Note:** The Bronchiolitis page says an urgent GP appointment or 111 if a child has had a cold and it is getting worse. The Croup page says the same for a child getting worse or not getting better. | "Under 5 years old" AND "Symptoms getting worse, or not getting better after about a week" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_wh_baby_born_early_or_heart_lung`<br>A baby under 1 who was born early, or has a heart or lung condition or a weak immune system<br>**Note:** AI judgement. The Bronchiolitis page says these babies have a higher chance of getting seriously ill, but gives no action for it on its own. A same-day check for a baby like this with breathing symptoms is a reading of that. Needs clinical review. | "Under 1 year old" AND "Young child born early, or with a heart or lung condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | **AI judgement, needs clinical review** | |

## Wheezing: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_wh_asthma_attack_recovered`<br>Diagnosed asthma, and an asthma attack in the last few days that has now settled<br>**Note:** The Asthma page says: if you've had an asthma attack and have recovered, see a GP within 2 days. Added in the breathing batch after test-case authors found no question for it. | "Diagnosed with asthma" AND "Had an asthma attack recently that has now settled" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within 2 days, even if you feel better* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| `or_wh_asthma_not_controlled`<br>Asthma needing the reliever more often, or waking at night or stopping usual activities | "Diagnosed with asthma" AND "Asthma needing the reliever more often, or waking at night" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Asthma](https://www.nhs.uk/conditions/asthma/) | |

## Default outcome

Used when no rule fires.

- **Wheezing with nothing that needs more urgent help: see a GP to find the cause**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Asthma](https://www.nhs.uk/conditions/asthma/)
- **Note:** Wheezing is a main asthma symptom. Treating every new wheeze as needing a GP is a reading of the Asthma page; it can also be caused by a chest infection, bronchiolitis or COPD. People already diagnosed with asthma whose symptoms are as usual are handled by the exception below.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Wheezing | Are you wheezing? This is a whistling sound when you breathe. | 56018004 | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Started soon after a food, medicine or insect sting | Did this start soon after eating a food, taking a medicine or being stung by an insect? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Too breathless to say a short sentence | Are you so short of breath that you cannot say a short sentence, even when resting? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Breathlessness came on suddenly, or suddenly got much worse | Did your breathing problem come on suddenly? Or has it suddenly got much worse? |  | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child struggling to breathe (grunting, or tummy sucking in under the ribs) | Is the person who is unwell struggling to breathe? You may hear grunting noises, or see their tummy sucking in under their ribs. |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pauses in a young child's breathing | Are there pauses in the child's breathing, where they stop breathing for a few seconds? | 1023001 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Started after choking on something | Did this start suddenly after choking on something, such as food or a small object? | 249489001 | **AI judgement, needs clinical review** | |
| Diagnosed with asthma | Has a doctor told you that you have asthma? | 161527007 | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Having an asthma attack now | Are you having an asthma attack now? This is when your symptoms are severe and it is hard to breathe. |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| No better after the most puffs of reliever inhaler allowed, or getting worse | Have you taken the most puffs of your reliever inhaler that you are allowed, and you still do not feel better? Or are you getting worse? |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Asthma attack without a reliever inhaler | Are you without your reliever inhaler? For example, you do not have it with you, or it has run out. |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Drooling | Are you drooling? This can be a sign of not being able to swallow. | 62718007 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Child wants to sit up rather than lie down | Does the child want to sit up rather than lie down, because it is easier to breathe? |  | [Croup](https://www.nhs.uk/conditions/croup/) | |
| High-pitched sound when breathing | Are you making a high-pitched sound when you breathe? | 70407001 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels cold to the touch, or shivery | Do you feel cold to the touch, or are you shivering or shivery? This can happen even without a high temperature. |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Short of breath when lying flat | Do you get short of breath when you lie down flat? For example, you need extra pillows, or you wake up at night gasping for breath. | 62744007 | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| Frothy pink phlegm | Are you coughing up frothy, pink phlegm (mucus)? |  | [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | |
| Aged 16 or over | Is the person who is unwell aged 16 or over? |  | **AI judgement, needs clinical review** | |
| Diagnosed with COPD | Has a doctor told you that you have COPD? This is a long-term lung condition that causes coughing and breathlessness. |  | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| COPD worse than usual (a flare-up) | Is your COPD worse than usual? For example, you are more short of breath than usual, or coughing up more phlegm (mucus). |  | [COPD](https://www.nhs.uk/conditions/chronic-obstructive-pulmonary-disease-copd/) | |
| More short of breath than usual, with a long-term lung or heart condition | Do you have a long-term lung condition or heart condition, such as COPD, asthma, bronchiectasis or heart failure? And are you more short of breath than you usually are? |  | [Bronchiectasis](https://www.nhs.uk/conditions/bronchiectasis/) | |
| Symptoms getting worse, or not getting better after about a week | Are your symptoms getting worse? Or have they not started to get better after about a week? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Young child born early, or with a heart or lung condition | Was the child born early (premature)? Or do they have a heart or lung condition, or a weak immune system that makes it harder to fight infection? |  | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Had an asthma attack recently that has now settled | Have you had an asthma attack in the last few days that has now settled? This is when your symptoms were severe and it was hard to breathe. |  | [Asthma](https://www.nhs.uk/conditions/asthma/) | |
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

### `advice_asthma_attack_999`

**What to do:** Call 999 now. You may be having a severe asthma attack.

**Look out for:**
- Feeling worse at any time
- Lips or skin turning blue, grey or pale
- Feeling very tired, confused or drowsy

**Get more help when:**
- No better after 10 minutes and no ambulance yet? Use your reliever inhaler again. Take up to the same number of puffs.
- Call 999 again if you get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- Sit up straight and try to stay calm
- If you have a blue reliever inhaler, take 1 puff every 30 to 60 seconds, up to 10 puffs. Use a spacer if you have one.
- If you have an inhaler you use both to prevent and treat symptoms, take 1 puff every 1 to 3 minutes, up to 6 puffs
- If your asthma action plan says something different, follow your plan

Source: [Asthma](https://www.nhs.uk/conditions/asthma/)

### `advice_breathless_ae`

**What to do:** Call 999 or go to A&E now. Your breathing problem could be a sign of something serious.

**Look out for:**
- Severe difficulty breathing, such as gasping, choking or not being able to get words out
- Lips or skin turning very pale, blue or grey
- Feeling suddenly confused
- Passing out

**Get more help when:**
- Call 999 straight away if you get any of the signs above, or you get worse while you wait

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Sit upright. Try to stay calm and breathe slowly.
- If you have a reliever inhaler, use it as your care team told you

Source: [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

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

### `advice_wheezing_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Being so short of breath you cannot say a short sentence
- A child grunting, or their tummy sucking in under their ribs, or pauses in their breathing
- Lips, tongue or skin turning blue, grey or pale
- Swelling of the lips, mouth or throat

**Get more help when:**
- Call 999 now if you or your child get any of the signs above
- Trust your own judgement. If you think your child is seriously unwell, get help straight away.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Sit upright to help breathing. Keep a child upright as much as possible when they are awake.
- If you have a reliever inhaler, use it as your care team told you
- Give a baby smaller feeds more often
- Do not smoke around children

Source: [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/), [Asthma](https://www.nhs.uk/conditions/asthma/), [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/)

### `advice_asthma_attack_urgent`

**What to do:** Use your reliever inhaler now, as your asthma action plan says. Then ask for an urgent GP appointment or get help from NHS 111 today, even if you feel better.

**Look out for:**
- Feeling worse at any time
- Your inhaler not helping, even after the most puffs you can take
- Not being able to say a short sentence because you are so short of breath
- Lips or skin turning blue, grey or pale

**Get more help when:**
- Call 999 now if you get any of the signs above, or you do not have your inhaler
- See a GP within 2 days of any asthma attack to check your treatment

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999. Do not drive yourself to A&E.

**What you can do yourself:**
- Sit up straight and try to stay calm
- If you have a blue reliever inhaler, take 1 puff every 30 to 60 seconds, up to 10 puffs. Use a spacer if you have one.
- If you have an inhaler you use both to prevent and treat symptoms, take 1 puff every 1 to 3 minutes, up to 6 puffs

Source: [Asthma](https://www.nhs.uk/conditions/asthma/)

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

### `advice_wheezing_gp`

**What to do:** See a GP about the wheezing. It is often caused by asthma or a chest infection, and a GP can find the cause.

**Look out for:**
- Finding it hard to breathe, or wheezing that gets worse
- Being so short of breath you cannot say a short sentence
- Swelling of the lips, mouth or throat
- Lips, tongue or skin turning blue, grey or pale

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you find it hard to breathe or feel very unwell
- Call 999 if you cannot say a short sentence, your lips or skin turn blue or grey, or your lips, mouth or throat swell

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Try to avoid things that seem to set off the wheezing, such as smoke, pollen or animals
- If you smoke, stopping will help

Source: [Asthma](https://www.nhs.uk/conditions/asthma/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_wh_after_allergy_trigger`: AI reading of the Anaphylaxis page, which says call 999 if you become very wheezy after contact with something you are allergic to. Kept firm, not soft, on purpose: missing a severe allergic reaction is life-threatening. Needs clinical review.
- `rf_wh_cannot_talk`: Clinical knowledge: not being able to finish a sentence is a sign of a severe asthma attack, which can be life-threatening. The COVID-19 page says call 999 or go to A&E for this; 999 is used because a severe asthma attack needs treatment on the way to hospital.
- `rf_wh_sudden`: The Pulmonary embolism and COVID-19 pages say call 999 or go to A&E for breathing problems that come on suddenly. Marked soft because asthma attacks often start quickly and can settle with a reliever inhaler.
- `rf_wh_child_struggling`: Source difference: the Bronchiolitis page says call 999. The Shortness of breath page says call 999 or go to A&E. The more urgent is used.
- `rf_wh_child_floppy`: Source difference: the Bronchiolitis page says call 999 for a child who is floppy and will not wake up. The Shortness of breath page says call 999 or go to A&E for a child who is limp, floppy or not responding as usual. The more urgent is used.
- `rf_wh_choked`: Clinical knowledge: something breathed into the airway can cause wheezing on one side and needs to be removed in hospital.
- `rf_wh_young_child_breathing_fast`: The Bronchiolitis page says call 999 for difficulty breathing that includes breathing quickly. The Sepsis page says call 999 or go to A&E for breathing very fast. A&E is used for fast breathing alone; grunting or the tummy sucking in is sent to 999 above.
- `rf_wh_baby_feeding_poorly`: AI judgement from clinical knowledge: a wheezy baby who is not feeding may be tiring and needs checking in hospital. The Bronchiolitis page says an urgent GP appointment or 111, so the rule is soft, with the firm urgent rule below as its floor.
- `rf_wh_baby_high_temperature`: Source difference: the Bronchiolitis page says an urgent GP appointment or 111. The Sepsis page says call 999 or go to A&E. The more urgent is used.
- `rf_wh_young_child_not_peeing`: Source difference: the Bronchiolitis page says an urgent GP appointment or 111 for a dry nappy for 12 hours. The more urgent Sepsis page advice is used.
- `rf_wh_child_sit_up_or_drooling`: The Croup page says call 999 or go to A&E if a child is unwell and drooling more than usual, finding it hard to swallow, or wants to sit rather than lie down. Requiring a high-pitched sound when breathing with wanting to sit up is AI judgement, so that a child with a blocked nose who sleeps propped up is not sent to A&E. Added in the breathing batch after test-case authors found no question for it.
- `rf_wh_stridor`: Same as the cough rule. Source difference: the Sore throat page says call 999 or go to A&E for a high-pitched sound when breathing. The Croup page lists it as a croup symptom and says an urgent GP appointment or 111. The more urgent is used, marked soft.
- `rf_wh_sepsis_cold_or_shivery`: The Sepsis page says call 999 or go to A&E for an adult who feels hot or cold to the touch or is shivery, and says a high temperature is less common in older adults with sepsis. Requiring feeling very unwell or breathing very fast is AI judgement, so that everyone with a shivery cold is not sent to A&E. Soft, so that likely flu can lower it; sepsis itself, if likely, keeps the outcome at emergency.
- `rf_wh_young_child_cold_or_shivery`: Source difference: the Sepsis page says call 999 or go to A&E for a child under 5 who feels cold to the touch or is shivery. The Bronchiolitis page says an urgent GP appointment or 111 for a child who feels hot or cold to the touch or is shivering. The more urgent is used, marked soft, with the urgent high temperature rule as its floor.
- `rf_wh_asthma_attack`: AI reading of the Asthma page, which says to see a GP within 2 days of an asthma attack, even after recovering. Same-day help is used because the attack is happening now.
- `rf_wh_very_unwell`: The Cough page gives the same advice for feeling very unwell.
- `rf_wh_lying_flat`: Source difference: the Heart failure page says an urgent GP appointment or 111. The Shortness of breath page says see a GP. The more urgent is used. Wheezing from fluid on the lungs can be a sign of heart failure.
- `rf_wh_more_than_usual`: The Bronchiectasis and COPD pages say an urgent GP appointment or 111 for being more short of breath than usual. The Shortness of breath page says contact 111 for difficulty breathing, 'you may be more short of breath than usual'. Applying it to any long-term lung or heart condition is AI judgement. Added in the breathing batch: before this it could only be reached through a question about COPD.
- `rf_wh_young_child_worse`: The Bronchiolitis page says an urgent GP appointment or 111 if a child has had a cold and it is getting worse. The Croup page says the same for a child getting worse or not getting better.
- `rf_wh_baby_born_early_or_heart_lung`: AI judgement. The Bronchiolitis page says these babies have a higher chance of getting seriously ill, but gives no action for it on its own. A same-day check for a baby like this with breathing symptoms is a reading of that. Needs clinical review.
- `or_wh_asthma_attack_recovered`: The Asthma page says: if you've had an asthma attack and have recovered, see a GP within 2 days. Added in the breathing batch after test-case authors found no question for it.
- `wheezing default outcome`: Wheezing is a main asthma symptom. Treating every new wheeze as needing a GP is a reading of the Asthma page; it can also be caused by a chest infection, bronchiolitis or COPD. People already diagnosed with asthma whose symptoms are as usual are handled by the exception below.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bronchitis (a short-term infection of the airways in the lungs) | 10509002 | common | Cough: strongly supports; Coughing up phlegm: supports; Blocked or runny nose: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Wheezing: supports; Chest pain worse when breathing in: supports |
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Asthma (a long-term condition that makes the airways narrow), or an asthma attack | 195967001 | uncommon | Wheezing comes and goes, often worse at night or early morning: strongly supports; Wheezing brought on by exercise or cold air: supports; Symptoms come on around pollen, dust, mould or animals: supports; Cough worse at night: supports; Has eczema, hay fever or a food allergy: supports; Chest feels tight or squeezed: supports |
| Bronchiolitis (a chest infection that babies get) | 4120002 | rare | Blocked or runny nose: strongly supports; Cough: supports; Wheezing: supports; Breathing very fast: supports; Baby or young child feeding or eating much less than usual: supports; Very high temperature, or feels hot, cold or shivery: supports |
| A flare-up of COPD (a long-term lung condition that makes it hard to breathe) | 195951007 | rare | COPD worse than usual (a flare-up): strongly supports; More short of breath than usual, with a long-term lung or heart condition: strongly supports; Yellow or green phlegm: supports; Cough very bad or getting worse quickly: supports; Short of breath at rest: supports |
| Something breathed into the airway or lungs, such as food or a small toy | 262599003 | rare | Started after choking on something: strongly supports; Cough: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: supports; Wheezing: supports; High-pitched sound when breathing: supports |
| Heart failure (the heart cannot pump blood as well as it should), or a flare of it | 84114007 | rare | Short of breath: strongly supports; Out of breath doing everyday things: strongly supports; Short of breath when lying flat: strongly supports; Swollen feet, ankles or legs: supports; Suddenly put on weight: supports; Heart failure symptoms worse than usual: supports; Frothy pink phlegm: supports; Cough worse at night: supports; Feels very tired: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
