# Review pack: Swollen arms or hands

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
| [Angioedema](https://www.nhs.uk/conditions/angioedema/) | 2026-11-19 |  | Page last reviewed: 25 August 2026 |
| [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | 2026-11-19 |  | Page last reviewed: 01 October 2025 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | 2026-11-19 |  | Page last reviewed: 23 March 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | 2026-11-19 |  | Page last reviewed: 03 January 2024 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | 2026-11-19 |  | Page last reviewed: 30 April 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |

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

## Swollen arms or hands red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sa_allergic_swelling`<br>A swollen arm or hand with lips, mouth, tongue or throat suddenly swollen, or the throat feeling tight: possible anaphylaxis | "Lips, mouth, tongue or throat suddenly swollen" OR "Throat feels tight" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Angioedema](https://www.nhs.uk/conditions/angioedema/) | |
| `rf_sa_breathless_or_chest`<br>A swollen arm or hand with breathlessness, or a tight, heavy or painful chest | "Short of breath" OR "Difficulty breathing" OR "Chest pain" OR "Chest feels tight or squeezed" OR "Chest feels heavy" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_sa_cellulitis_spreading`<br>A red, hot swollen arm or hand with a fast heartbeat, fast breathing, feeling faint, or cold, clammy or blotchy skin | "Swollen area is red or hot to touch" AND ("Heart beating very fast" OR "Breathing very fast" OR "Feels light-headed" OR "Hands and feet, or skin, unusually cold to touch" OR "Blotchy or mottled skin") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_sa_cellulitis_temperature`<br>A red, hot swollen arm or hand with a high temperature, or feeling hot, cold or shivery<br>**Note:** Source difference, as for the swollen legs rule: the Cellulitis page says 999 or A&E, the Swollen arms page says urgent. The more urgent is used, marked soft. | "Swollen area is red or hot to touch" AND "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Swollen arms or hands red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sa_severe_or_sudden`<br>Swelling that is severe, painful or came on suddenly | "Swelling is severe, painful or came on suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_sa_red_hot`<br>The swollen area is red or feels hot | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_swollen_arms_high_temperature`<br>A swollen arm or hand with a high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_sa_swelling_elsewhere`<br>Swelling in the arms or hands and other parts of the body | "Swelling in other parts of the body too, such as the face or tummy" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_sa_diabetes`<br>A swollen arm or hand in someone with diabetes | "Has diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| `rf_sa_pregnancy`<br>Pregnant or recently given birth, with swollen hands and a severe headache, vision problems or pain below the ribs | "Pregnant, or gave birth in the last 6 weeks" AND (("Severe headache that painkillers do not help" OR "Change in sight or loss of vision" OR "Pain just below the ribs") OR "Swelling in other parts of the body too, such as the face or tummy" OR "Swelling is severe, painful or came on suddenly") | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit now, or call 111 if you cannot* | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |

## Swollen arms or hands: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sa_not_improving`<br>Swelling that does not go away | "Swelling not better after a few days of home treatment" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |

## Default outcome

Used when no rule fires.

- **Swelling in an arm or hand with no obvious cause: get it checked today**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Swollen arm or hand | Is one or both of your arms or hands swollen or puffy? |  | [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Chest feels tight or squeezed | Does your chest feel tight, or like it is being squeezed? | 23924001 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Chest feels heavy | Does your chest feel heavy? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Hands and feet, or skin, unusually cold to touch | Are your hands and feet, or your skin, unusually cold to touch, or cold and damp (clammy)? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swelling is severe, painful or came on suddenly | Is the swelling severe or painful, or did it come on suddenly? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Swelling in other parts of the body too, such as the face or tummy | Do you also have swelling in other parts of your body, such as your face, around your eyes, or your tummy? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Severe headache that painkillers do not help | Do you have a severe headache that does not go away with painkillers? |  | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Pain just below the ribs | Do you have pain just below your ribs, especially on the right side? |  | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| Swelling not better after a few days of home treatment | Has the swelling not improved after a few days of treating it at home, or is it getting worse? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |

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

### `advice_swelling_999`

**What to do:** Call 999 now. Swelling with breathlessness or chest pain can mean a blood clot in the lung, which needs treatment in hospital straight away.

**Look out for:**
- Breathing that gets harder
- Chest pain that gets worse
- Lips or skin turning blue, grey or pale
- Passing out

**Get more help when:**
- Call 999 again if you get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/), [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/), [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/)

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

### `advice_swelling_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your swelling needs to be checked.

**Look out for:**
- Feeling short of breath, or your chest feeling tight, heavy or painful
- Coughing up blood
- The swollen area getting redder, hotter or more painful
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 if you get short of breath, chest pain, or cough up blood. You could have a blood clot in the lung.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Raise the swollen arm or leg on pillows when you can
- Do not wear clothes, socks or shoes that are too tight

Source: [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/), [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/), [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/), [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

### `advice_pre_eclampsia_urgent`

**What to do:** Get urgent medical help now. Call your maternity unit. These can be signs of pre-eclampsia, a condition that causes high blood pressure in pregnancy. It needs checking straight away.

**Look out for:**
- A fit (seizure)
- A severe headache that does not go away, or your headache getting worse
- Blurred vision, flashing lights, or your vision getting worse
- Pain just below the ribs
- Being sick, or sudden swelling of the face, hands or feet

**Get more help when:**
- Call 999 if you have a fit, or feel very unwell

**Where to go:** Call your maternity unit. If you have recently given birth, or cannot reach your maternity unit, call 111.

Source: [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/)

### `advice_swelling_gp`

**What to do:** See a GP. They can find what is causing the swelling and help with treatment.

**Look out for:**
- Swelling in only one leg, or swelling that is painful, red or hot
- Swelling that spreads to your face or tummy
- Feeling short of breath

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 if you get short of breath, chest pain, or cough up blood

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Raise your legs or the swollen area on pillows when you can
- Get some gentle exercise, like walking, to help your blood flow
- Do not stand or sit still for long periods

Source: [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/), [Swollen arms and hands (oedema)](https://www.nhs.uk/conditions/swollen-arms-and-hands-oedema/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sa_cellulitis_temperature`: Source difference, as for the swollen legs rule: the Cellulitis page says 999 or A&E, the Swollen arms page says urgent. The more urgent is used, marked soft.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Blood clot in a vein, usually in the leg (deep vein thrombosis, DVT) | 128053003 | uncommon | Pain or swelling in one leg: strongly supports; Swelling is severe, painful or came on suddenly: supports; Swollen area is red or hot to touch: supports; One leg swollen, warm and painful, often in the calf: strongly supports; Swelling of the painful area: supports; Skin over the painful area has changed colour: supports |
| Fluid build-up from standing, heat, salty food or a medicine |  | very common | Swelling comes on with heat or staying in one position, and goes down with rest: strongly supports; Started a new medicine or changed a dose in the last few weeks: supports; Knows what caused the swelling: supports |
| Lymphoedema (long-term swelling from a problem with the lymph glands) | 234097001 | rare | Swelling there for 3 months or more: strongly supports; Swelling not better after a few days of home treatment: supports; Swelling comes on with heat or staying in one position, and goes down with rest: supports |
| Angioedema (sudden swelling under the skin) | 41291007 | uncommon | Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals: strongly supports; Lips, mouth, tongue or throat suddenly swollen: supports; Started soon after a food, medicine or insect sting: strongly supports; Started a new medicine or changed a dose in the last few weeks: supports; Raised, itchy or swollen rash (hives): supports; Swelling is severe, painful or came on suddenly: supports; Has eczema, hay fever or a food allergy: supports |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Pre-eclampsia (high blood pressure in pregnancy that can cause serious problems) | 398254007 | very rare | Pain just below the ribs: strongly supports; Severe headache that painkillers do not help: strongly supports; Change in sight or loss of vision: strongly supports; Sudden swelling of the face, hands or feet: supports; Feels sick or has been sick: supports; Feels very unwell: supports; Pregnant, or gave birth in the last 6 weeks: strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Swelling is severe, painful or came on suddenly: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
