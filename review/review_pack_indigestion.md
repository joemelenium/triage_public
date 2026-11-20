# Review pack: Indigestion and heartburn

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
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Gastritis](https://www.nhs.uk/conditions/gastritis/) | 2026-11-19 |  | Page last reviewed: 05 August 2026 |
| [Hiatus hernia](https://www.nhs.uk/conditions/hiatus-hernia/) | 2026-11-19 |  | Page last reviewed: 08 May 2024 |
| [Indigestion](https://www.nhs.uk/conditions/indigestion/) | 2026-11-19 |  | Page last reviewed: 05 May 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |
| [Hernia](https://www.nhs.uk/conditions/hernia/) | 2026-11-19 |  | Page last reviewed: 19 May 2026 |
| [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | 2026-11-19 |  | Page last reviewed: 09 August 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Heartburn and acid reflux](https://www.nhs.uk/conditions/heartburn-and-acid-reflux/) | 2026-11-18 |  | Page last reviewed: 20 November 2023 |

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

## Indigestion and heartburn red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ind_heart_attack_signs`<br>Indigestion with the chest feeling tight, squeezed or heavy: possible heart attack<br>**Note:** The Chest pain page says chest pain that feels like squeezing or pressure, burning or indigestion may be a heart attack: call 999. Applying it to indigestion is AI judgement. Any chest pain also brings in the chest pain rules. | "Chest feels tight or squeezed" OR "Chest feels heavy" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_ind_sweaty_or_breathless`<br>Indigestion with feeling sweaty or short of breath, aged 45 or over: possible heart attack<br>**Note:** The Chest pain page says chest pain or discomfort that can feel like burning or indigestion, with feeling sweaty or short of breath, may be a heart attack: call 999. Applying it to indigestion is AI judgement. Kept firm from 45, when a heart attack becomes more common (DECISIONS 169). | ("Feels sweaty" OR "Short of breath") AND "Aged 45 or over" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_ind_sweaty_or_breathless_under_45`<br>Indigestion with feeling sweaty or short of breath, under 45: possible heart attack<br>**Note:** As the rule above, but soft under 45: a clearly likely milder cause, from what the patient said, can lower it. An independent check found sweating alone gave 999 for any age (DECISIONS 169). | ("Feels sweaty" OR "Short of breath") AND NOT "Aged 45 or over" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_ind_blood`<br>Indigestion with vomiting blood, or black, sticky poo<br>**Note:** Source difference: the Gastritis and Stomach ulcer pages say 999 or A&E. The Indigestion page says see a GP for bloody sick or poo. The more urgent is used. | "Being sick with blood in it (vomiting blood)" OR "Black, sticky poo, or dark red poo" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Gastritis](https://www.nhs.uk/conditions/gastritis/) | |
| `rf_ind_sudden_severe`<br>Severe tummy or chest pain that started suddenly | "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Gastritis](https://www.nhs.uk/conditions/gastritis/) | |

## Indigestion and heartburn red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ind_warning_signs`<br>Indigestion with weight loss, difficulty swallowing, being sick again and again, feeling full after a little food, or a lump in the tummy<br>**Note:** Source difference: the Hiatus hernia, Stomach ulcer and Gastritis pages say an urgent GP appointment or 111. The Indigestion page says see a GP (non-urgent). The more urgent is used. These can be signs of something more serious, such as cancer. | "Losing weight without trying" OR "Problems swallowing" OR "Keeps being sick" OR "Feels full after eating only a little" OR "A lump or swelling in the tummy or groin" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hiatus hernia](https://www.nhs.uk/conditions/hiatus-hernia/) | |
| `rf_ind_upper_tummy_pain`<br>Indigestion with pain in the upper tummy<br>**Note:** The Hiatus hernia page says urgent for indigestion with pain in the upper tummy. The Indigestion page says stomach ache is not usually a symptom of indigestion. Marked soft. | "Pain in the upper middle of the tummy, below the breastbone" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hiatus hernia](https://www.nhs.uk/conditions/hiatus-hernia/) | |

## Indigestion and heartburn: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ind_keeps_happening`<br>Keeps getting indigestion, or it has not gone away with pharmacy medicine | "Keeps getting indigestion" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Indigestion](https://www.nhs.uk/conditions/indigestion/) | |
| `or_ind_severe_pain`<br>Indigestion with severe pain<br>**Note:** A severe stomach ache also brings in the stomach ache rules, which say 999 or A&E. | "Severe stomach ache" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Indigestion](https://www.nhs.uk/conditions/indigestion/) | |

## Default outcome

Used when no rule fires.

- **Indigestion or heartburn with nothing that needs more help: treat it at home, and a pharmacist can help**
- Outcome: Self-manageable, Self-care, No appointment needed. *There is usually no need to see a GP*
- Source: [Indigestion](https://www.nhs.uk/conditions/indigestion/)
- **Note:** The Heartburn page gives the same self-care advice.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Indigestion or heartburn | Do you have indigestion or heartburn? This is a burning feeling in your chest or upper tummy, or feeling full, often after eating. |  | [Indigestion](https://www.nhs.uk/conditions/indigestion/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chest feels tight or squeezed | Does your chest feel tight, or like it is being squeezed? | 23924001 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Chest feels heavy | Does your chest feel heavy? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Feels sweaty | Do you feel sweaty? | 415690000 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Aged 45 or over | Is the person who is unwell aged 45 or over? |  | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Keeps being sick | Do you keep being sick, again and again? |  | [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | |
| Feels full after eating only a little | Do you feel full after eating only a small amount of food? |  | [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | |
| A lump or swelling in the tummy or groin | Do you have a lump or swelling in your tummy or groin? It may go away when you lie down. |  | [Hernia](https://www.nhs.uk/conditions/hernia/) | |
| Pain in the upper middle of the tummy, below the breastbone | Is the pain in the middle of your upper tummy, just below your breastbone? | 79922009 | [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | |
| Keeps getting indigestion | Do you keep getting indigestion? Or has it not gone away with pharmacy medicine? |  | [Indigestion](https://www.nhs.uk/conditions/indigestion/) | |
| Severe stomach ache | Is the pain in your tummy severe? This means it is there all the time and so bad it is hard to think or talk, you cannot sleep, or it is very hard to move. |  | [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | |

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

### `advice_indigestion_999`

**What to do:** Call 999 now. Indigestion with chest tightness, sweating or shortness of breath could be a heart attack.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- Sit and rest while you wait for help
- Take aspirin (300mg) if you have any, unless you are allergic to it

Source: [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/)

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

### `advice_indigestion_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Indigestion with these symptoms should be checked quickly.

**Look out for:**
- Being sick with blood, or sick that looks like ground coffee
- Black, sticky poo
- Severe tummy or chest pain that starts suddenly

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Hiatus hernia](https://www.nhs.uk/conditions/hiatus-hernia/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/), [Gastritis](https://www.nhs.uk/conditions/gastritis/)

### `advice_indigestion_gp`

**What to do:** See a GP. They can look for the cause of your indigestion and suggest treatment.

**Look out for:**
- Losing weight without trying, or difficulty swallowing
- Being sick again and again
- Being sick with blood, or black, sticky poo

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you lose weight, find it hard to swallow or keep being sick
- Call 999 or go to A&E if you are sick with blood or have black, sticky poo

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Do not take ibuprofen or aspirin unless a doctor has told you to

Source: [Indigestion](https://www.nhs.uk/conditions/indigestion/)

### `advice_indigestion_self_care`

**What to do:** You can usually treat indigestion and heartburn yourself. A pharmacist can suggest medicines to ease the burning or pain.

**Look out for:**
- Indigestion that keeps coming back
- Losing weight without trying, or difficulty swallowing
- Being sick with blood, or black, sticky poo

**Get more help when:**
- See a GP if you keep getting indigestion
- Ask for an urgent GP appointment or call 111 if you lose weight, find it hard to swallow or keep being sick
- Call 999 if you get chest pain that feels tight or heavy, or spreads to your arms, neck, jaw or back

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Eat smaller meals, and do not eat 3 to 4 hours before bed
- Cut down on tea, coffee, cola, alcohol, and rich, spicy or fatty food
- Raise your head and shoulders up in bed
- Do not smoke, and lose weight if you are overweight

Source: [Indigestion](https://www.nhs.uk/conditions/indigestion/), [Heartburn and acid reflux](https://www.nhs.uk/conditions/heartburn-and-acid-reflux/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ind_heart_attack_signs`: The Chest pain page says chest pain that feels like squeezing or pressure, burning or indigestion may be a heart attack: call 999. Applying it to indigestion is AI judgement. Any chest pain also brings in the chest pain rules.
- `rf_ind_sweaty_or_breathless`: The Chest pain page says chest pain or discomfort that can feel like burning or indigestion, with feeling sweaty or short of breath, may be a heart attack: call 999. Applying it to indigestion is AI judgement. Kept firm from 45, when a heart attack becomes more common (DECISIONS 169).
- `rf_ind_sweaty_or_breathless_under_45`: As the rule above, but soft under 45: a clearly likely milder cause, from what the patient said, can lower it. An independent check found sweating alone gave 999 for any age (DECISIONS 169).
- `rf_ind_blood`: Source difference: the Gastritis and Stomach ulcer pages say 999 or A&E. The Indigestion page says see a GP for bloody sick or poo. The more urgent is used.
- `rf_ind_warning_signs`: Source difference: the Hiatus hernia, Stomach ulcer and Gastritis pages say an urgent GP appointment or 111. The Indigestion page says see a GP (non-urgent). The more urgent is used. These can be signs of something more serious, such as cancer.
- `rf_ind_upper_tummy_pain`: The Hiatus hernia page says urgent for indigestion with pain in the upper tummy. The Indigestion page says stomach ache is not usually a symptom of indigestion. Marked soft.
- `or_ind_severe_pain`: A severe stomach ache also brings in the stomach ache rules, which say 999 or A&E.
- `indigestion default outcome`: The Heartburn page gives the same self-care advice.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Heart attack | 22298006 | very rare | Chest feels tight or squeezed: strongly supports; Sudden chest pain that does not go away: strongly supports; Chest feels heavy: supports; Chest pain is there now: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feels light-headed: supports; Short of breath: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Close relative had a heart attack or angina before 60: supports; Chest pain worse when breathing in: argues against; Chest hurts more when pressed: argues against |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Gallstones (small stones in the gallbladder that can cause attacks of pain) | 235919008 | uncommon | Pain in the upper right of the tummy, just under the ribs: strongly supports; Tummy pain that comes on after eating, especially fatty food: strongly supports; Severe stomach ache: supports; Tummy pain that spreads to the back: supports; Feeling sick (nausea): supports; Being sick: supports |
| Gastritis (swelling of the stomach lining) | 4556007 | uncommon | Pain in the upper middle of the tummy, below the breastbone: strongly supports; Indigestion or heartburn: strongly supports; Feeling sick (nausea): supports; Tummy pain that comes on after eating, especially fatty food: supports; Not feeling hungry, or eating much less than usual: supports; Heartburn or a sour taste in the mouth: supports |
| Stomach or food pipe cancer warning signs | 363349007 | rare | Losing weight without trying: strongly supports; Keeps getting indigestion: strongly supports; Problems swallowing: supports; Feels full after eating only a little: supports; Not feeling hungry, or eating much less than usual: supports; Black, sticky poo, or dark red poo: supports; Keeps being sick: supports; A lump or swelling in the tummy or groin: supports |
| Stomach ulcer (an open sore in the lining of the stomach) | 397825006 | uncommon | Pain in the upper middle of the tummy, below the breastbone: strongly supports; Indigestion or heartburn: strongly supports; Tummy pain that comes on after eating, especially fatty food: supports; Feeling sick (nausea): supports; Not feeling hungry, or eating much less than usual: supports; Black, sticky poo, or dark red poo: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
