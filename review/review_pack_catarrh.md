# Review pack: Catarrh

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
| [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | 2026-11-18 |  | Page last reviewed: 31 January 2024 |
| [Catarrh](https://www.nhs.uk/conditions/catarrh/) | 2026-11-19 |  | Page last reviewed: 16 June 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Nasal polyps](https://www.nhs.uk/conditions/nasal-polyps/) | 2026-11-19 |  | Page last reviewed: 29 June 2023 |

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

## Catarrh red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ca_eye_swelling`<br>Catarrh with swelling, redness or pain around the eye<br>**Note:** Clinical knowledge: a sinus infection can rarely spread to the tissue around the eye, which needs treatment in hospital the same day. | "Swelling, redness or pain around the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_ca_vision`<br>Catarrh with sudden problems with eyesight<br>**Note:** Clinical knowledge: double or blurred vision with a sinus infection can mean it has spread to the eye socket. | "Sight changed suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_ca_meningitis_signs`<br>Catarrh with a very bad headache and a stiff neck, or bright light hurting the eyes<br>**Note:** Clinical knowledge: a sinus infection can rarely spread to the lining of the brain (meningitis). | "Very painful headache" AND ("Stiff neck" OR "Bright lights hurt the eyes or are bothering you") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Catarrh red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ca_very_unwell`<br>Catarrh or sinusitis and feeling very unwell | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |
| `rf_ca_sinus_pain_worse`<br>Face pain that is severe, getting worse, or not helped by painkillers | "Face pain that is severe, getting worse, or not helped by painkillers" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |
| `rf_ca_weak_immune_sinusitis`<br>Signs of sinusitis in someone with a weakened immune system | "Weakened immune system" AND "Pain or tenderness around the cheeks, eyes or forehead" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |

## Catarrh: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ca_few_weeks`<br>Catarrh for more than a few weeks | "Catarrh for more than a few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Catarrh](https://www.nhs.uk/conditions/catarrh/) | |
| `or_ca_new_symptoms`<br>Catarrh with new symptoms such as problems swallowing or a lost sense of smell<br>**Note:** The Catarrh page also lists a new sore throat. That is left to the sore throat rules, because a sore throat with catarrh is usually a cold. | "Problems swallowing" OR "Lost or changed sense of smell or taste" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Catarrh](https://www.nhs.uk/conditions/catarrh/) | |

## Default outcome

Used when no rule fires.

- **Catarrh with nothing that needs more help: it usually clears up by itself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Catarrh usually clears up by itself. A pharmacist can help.*
- Source: [Catarrh](https://www.nhs.uk/conditions/catarrh/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Catarrh (a build-up of phlegm in the nose or throat) | Do you have a build-up of phlegm in your nose or throat that you keep needing to clear? This is called catarrh. | 161959005 | [Catarrh](https://www.nhs.uk/conditions/catarrh/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Swelling, redness or pain around the eye | Is the skin around your eye swollen, red or painful, or is your eyelid swelling shut? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Sight changed suddenly | Did the change in your sight come on suddenly, over seconds, minutes or hours? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Face pain that is severe, getting worse, or not helped by painkillers | Is the pain in your face severe or getting worse, or not helped by painkillers? |  | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pain or tenderness around the cheeks, eyes or forehead | Do you have pain, swelling or tenderness around your cheeks, eyes or forehead? | 95668009 | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |
| Catarrh for more than a few weeks | Have you had the build-up of phlegm in your nose or throat for more than a few weeks? |  | [Catarrh](https://www.nhs.uk/conditions/catarrh/) | |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Lost or changed sense of smell or taste | Have you lost your sense of smell or taste, or has it changed? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |

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

### `advice_nose_ae`

**What to do:** Go to A&E now, or call 999. An infection in the sinuses (spaces in the face, behind the cheeks) can rarely spread to the eye or brain.

**Look out for:**
- Swelling or redness around the eye getting worse
- Double or blurred vision
- A very bad headache, a stiff neck, or feeling confused

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/), [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/)

### `advice_nose_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Call 111 if you need advice for a child under 5.

**Look out for:**
- Swelling or redness around the eye
- Double or blurred vision
- A very bad headache with a stiff neck

**Get more help when:**
- Go to A&E or call 999 if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Take paracetamol or ibuprofen for pain. Do not give aspirin to children under 16.
- Rinse your nose with salt water

Source: [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/)

### `advice_nose_gp`

**What to do:** See a GP. They can check for causes such as sinusitis (swollen spaces in the face) or nasal polyps (soft growths inside the nose).

**Look out for:**
- Pain in the face that is severe or getting worse
- Feeling very unwell
- Swelling around the eye, or problems with your eyesight

**Get more help when:**
- Ask for an urgent GP appointment or get help from 111 if the face pain gets worse or you feel very unwell
- Go to A&E or call 999 for swelling around the eye, problems with your eyesight, or a very bad headache with a stiff neck

**Where to go:** Make an appointment with a GP. A pharmacist can suggest treatments while you wait.

**What you can do yourself:**
- Drink plenty of water
- Rinse your nose with salt water
- Try not to smoke, and keep away from smoky places

Source: [Catarrh](https://www.nhs.uk/conditions/catarrh/), [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/), [Nasal polyps](https://www.nhs.uk/conditions/nasal-polyps/)

### `advice_catarrh_self_care`

**What to do:** Catarrh is a build-up of phlegm in your nose and throat. It usually clears up by itself. A pharmacist can help.

**Look out for:**
- Catarrh that lasts more than a few weeks
- New symptoms, such as problems swallowing or a lost sense of smell
- Pain in the face that is severe or getting worse, or feeling very unwell

**Get more help when:**
- See a GP if you get the first two signs above
- Ask for an urgent GP appointment or get help from 111 if face pain gets worse or you feel very unwell
- Go to A&E for swelling around the eye or problems with your eyesight

**Where to go:** You do not need an appointment. A pharmacist can suggest treatments, such as salt water nose rinses.

**What you can do yourself:**
- Drink plenty of water
- Sip ice-cold water when you need to clear your throat, rather than coughing
- Sit in the bathroom with a hot shower running to loosen the phlegm
- Rinse your nose with salt water, or gargle with salt water

Source: [Catarrh](https://www.nhs.uk/conditions/catarrh/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ca_eye_swelling`: Clinical knowledge: a sinus infection can rarely spread to the tissue around the eye, which needs treatment in hospital the same day.
- `rf_ca_vision`: Clinical knowledge: double or blurred vision with a sinus infection can mean it has spread to the eye socket.
- `rf_ca_meningitis_signs`: Clinical knowledge: a sinus infection can rarely spread to the lining of the brain (meningitis).
- `or_ca_new_symptoms`: The Catarrh page also lists a new sore throat. That is left to the sore throat rules, because a sore throat with catarrh is usually a cold.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Common cold | 82272006 | very common | Blocked or runny nose: strongly supports; Hoarse voice: supports; Dry cough: supports; Phlegm dripping down the back of the throat from the nose: supports |
| Hay fever (an allergy to pollen) | 21719001 | uncommon | Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Blocked or runny nose: strongly supports; Has eczema, hay fever or a food allergy: supports; Dry cough: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Allergic rhinitis (a nose allergy, often all year) | 446096008 | common | Blocked or runny nose: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Nose symptoms all year round: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Has eczema, hay fever or a food allergy: supports; Blocked or runny nose for more than 3 weeks: supports |
| A feeling of a lump in the throat with nothing actually stuck | 267103008 | common | Feels like a lump in the throat, though food goes down normally: strongly supports; Feeling anxious, worried or panicky: supports; Heartburn or a sour taste in the mouth: supports; Phlegm dripping down the back of the throat from the nose: supports |
| Nasal polyps (soft, harmless growths inside the nose) | 736500007 | uncommon | Blocked or runny nose: strongly supports; Lost or changed sense of smell or taste: strongly supports; Blocked or runny nose for more than 3 weeks: strongly supports; Phlegm dripping down the back of the throat from the nose: supports; Snoring: supports; Sense of smell faded slowly over months or years: supports |
| Non-allergic rhinitis (a blocked or runny nose that is not from an allergy or a cold) | 8229003 | uncommon | Blocked or runny nose: strongly supports; Nose worse with smoke, perfume, weather, alcohol or spicy food: strongly supports; Used a spray to unblock the nose for more than a week: strongly supports; Blocked or runny nose for more than 3 weeks: supports; Phlegm dripping down the back of the throat from the nose: supports |
| A sinus infection spreading to the eye or brain. Sinuses are spaces in the face, behind the cheeks. |  | rare | Swelling, redness or pain around the eye: strongly supports; Sight changed suddenly: strongly supports; Stiff neck: supports; Bright lights hurt the eyes or are bothering you: supports; Very high temperature, or feels hot, cold or shivery: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
