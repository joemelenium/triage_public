# Review pack: Vomiting blood

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
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Alcohol-related liver disease](https://www.nhs.uk/conditions/alcohol-related-liver-disease-arld/) | 2026-11-19 |  | Page last reviewed: 15 July 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Liver disease](https://www.nhs.uk/conditions/liver-disease/) | 2026-11-19 |  | Page last reviewed: 09 August 2023 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |

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

## Vomiting blood red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_vb_with_other_symptoms`<br>Vomiting blood and feeling generally unwell, faint or dizzy, breathing fast or shallowly, cold, clammy pale skin, tummy pain or black poo<br>**Note:** Feeling confused is in the universal checks. | "Feels very unwell" OR "Feels light-headed" OR "Passed out (fainted)" OR "Breathing very fast" OR "Cold, clammy and pale skin" OR "Stomach ache" OR "Black, sticky poo, or dark red poo" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| `rf_vb_large_or_ongoing`<br>Still being sick with blood, or a lot of blood<br>**Note:** The Diarrhoea and vomiting, Stomach ulcer and Gastritis pages say 999 or A&E for vomiting blood. The Vomiting blood page allows an urgent GP appointment only when it has stopped. Treating a large amount as an emergency is AI judgement. | "A lot of blood, or still being sick with blood" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_vb_liver_or_alcohol`<br>Vomiting blood in someone with liver problems or who drinks a lot of alcohol<br>**Note:** The Alcohol-related liver disease page says 999 or A&E if you are worried alcohol may be affecting your liver and you vomit blood. Swollen veins in the food pipe can bleed heavily. | "Has liver problems, such as scarring of the liver" OR "Drinks a lot of alcohol" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Alcohol-related liver disease](https://www.nhs.uk/conditions/alcohol-related-liver-disease-arld/) | |
| `rf_vb_blood_thinners`<br>Vomiting blood while taking medicine to prevent blood clots<br>**Note:** Clinical knowledge: bleeding is harder to stop in people taking these medicines. The Vomiting blood page lists them as a cause. | "Takes medicine that thins the blood, or bleeds easily" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Vomiting blood: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Vomited blood that has stopped, with no other symptoms**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment, call 111 or get help from 111 online*
- Source: [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Cold, clammy and pale skin | Is your skin cold, clammy and pale? |  | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| A lot of blood, or still being sick with blood | Are you still being sick with blood, or was there a lot of blood, such as a cupful or more? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Has liver problems, such as scarring of the liver | Has a doctor told you that you have a liver problem? For example, scarring of the liver (cirrhosis), or harm from alcohol. |  | [Alcohol-related liver disease](https://www.nhs.uk/conditions/alcohol-related-liver-disease-arld/) | |
| Drinks a lot of alcohol | Do you usually drink more than 14 units of alcohol a week, or have you drunk a lot in the last few days? 14 units is about 6 pints of beer or 6 medium glasses of wine. |  | [Liver disease](https://www.nhs.uk/conditions/liver-disease/) | |
| Takes medicine that thins the blood, or bleeds easily | Do you take medicine that thins your blood, such as warfarin, apixaban or rivaroxaban? Or do you have a condition that makes you bleed more easily? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |

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

### `advice_vomiting_blood_urgent`

**What to do:** Ask for an urgent GP appointment, call 111 or get help from 111 online today. You should always get medical help if you have been sick with blood, even if it has stopped.

**Look out for:**
- Being sick with blood again
- Feeling faint, dizzy or confused, or cold, clammy, pale skin
- Tummy pain, or black, sticky poo

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Until you have been checked, do not drink alcohol. Do not take ibuprofen or aspirin.

Source: [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_vb_with_other_symptoms`: Feeling confused is in the universal checks.
- `rf_vb_large_or_ongoing`: The Diarrhoea and vomiting, Stomach ulcer and Gastritis pages say 999 or A&E for vomiting blood. The Vomiting blood page allows an urgent GP appointment only when it has stopped. Treating a large amount as an emergency is AI judgement.
- `rf_vb_liver_or_alcohol`: The Alcohol-related liver disease page says 999 or A&E if you are worried alcohol may be affecting your liver and you vomit blood. Swollen veins in the food pipe can bleed heavily.
- `rf_vb_blood_thinners`: Clinical knowledge: bleeding is harder to stop in people taking these medicines. The Vomiting blood page lists them as a cause.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bleeding from the stomach or food pipe, for example from an ulcer | 37372002 | uncommon | Black, sticky poo, or dark red poo: strongly supports; Being sick with blood in it (vomiting blood): strongly supports; A lot of blood, or still being sick with blood: supports; Feels light-headed: supports; Passed out (fainted): supports; Cold, clammy and pale skin: supports; Stomach ache: supports; Feels very unwell: supports |
| Bleeding from swollen veins in the food pipe, caused by liver problems (varices) | 17709002 | rare | Drinks a lot of alcohol: strongly supports; A lot of blood, or still being sick with blood: strongly supports; Yellow skin or yellow whites of the eyes (jaundice): supports; Black, sticky poo, or dark red poo: supports; Feels light-headed: supports; Tummy looks swollen or much bigger than usual: supports |
| A small tear in the food pipe from being sick or retching (Mallory-Weiss tear) | 35265002 | common | The blood came up only after being sick or retching many times: strongly supports; Keeps being sick: supports; Drinks a lot of alcohol: supports; Feeling sick (nausea): supports |
| Gastritis (swelling of the stomach lining) | 4556007 | uncommon | Pain in the upper middle of the tummy, below the breastbone: strongly supports; Indigestion or heartburn: strongly supports; Feeling sick (nausea): supports; Tummy pain that comes on after eating, especially fatty food: supports; Not feeling hungry, or eating much less than usual: supports; Heartburn or a sour taste in the mouth: supports |
| Stomach or food pipe cancer warning signs | 363349007 | rare | Losing weight without trying: strongly supports; Keeps getting indigestion: strongly supports; Problems swallowing: supports; Feels full after eating only a little: supports; Not feeling hungry, or eating much less than usual: supports; Black, sticky poo, or dark red poo: supports; Keeps being sick: supports; A lump or swelling in the tummy or groin: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
