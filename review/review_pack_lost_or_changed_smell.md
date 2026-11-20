# Review pack: Lost or changed sense of smell

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
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |
| [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | 2026-11-18 |  | Page last reviewed: 31 January 2024 |
| [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/) | 2026-11-19 |  | Page last reviewed: 01 December 2023 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |

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

## Lost or changed sense of smell red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sm_fit`<br>A changed sense of smell with a seizure (fit)<br>**Note:** Clinical knowledge: the smell page says a changed sense of smell can rarely be caused by epilepsy. A new seizure needs checking in hospital. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_sm_meningitis_signs`<br>A lost sense of smell with a very bad headache and a stiff neck, or bright light hurting the eyes<br>**Note:** Clinical knowledge: a sinus infection can rarely spread to the lining of the brain (meningitis). | "Very painful headache" AND ("Stiff neck" OR "Bright lights hurt the eyes or are bothering you") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_sm_clear_fluid_after_injury`<br>Clear, watery fluid trickling from the nose after an injury | "Started after an injury to the nose or face" AND "Clear, watery fluid trickling from the nose after an injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |

## Lost or changed sense of smell red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sm_head_injury`<br>A lost sense of smell that started after a head injury<br>**Note:** Clinical knowledge: losing the sense of smell after a head injury can mean damage to the nerves of smell or a skull injury, and needs checking. | "Head injury in the last month" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | **AI judgement, needs clinical review** | |
| `rf_sm_very_unwell`<br>A lost sense of smell and feeling very unwell | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sinusitis](https://www.nhs.uk/conditions/sinusitis-sinus-infection/) | |

## Lost or changed sense of smell: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sm_not_back`<br>Sense of smell not back to normal after a few weeks | "Sense of smell not back to normal after a few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/) | |
| `or_sm_phantom`<br>Smelling things that are not there<br>**Note:** AI reading of the smell page, which says this can rarely be caused by conditions like epilepsy. It is often harmless after a cold, so seeing a GP with no fixed time is used. | "Smelling things that are not there" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **A lost or changed sense of smell with nothing that needs more help: it often gets better in a few weeks or months**
- Outcome: Self-manageable, Self-care, No appointment needed. *It is not usually serious and may get better in a few weeks or months*
- Source: [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Lost or changed sense of smell or taste | Have you lost your sense of smell or taste, or has it changed? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Started after an injury to the nose or face | Did this start after a blow or injury to your nose or face? |  | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| Clear, watery fluid trickling from the nose after an injury | Since the injury, is clear, watery fluid trickling from your nose? |  | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Sense of smell not back to normal after a few weeks | Has your sense of smell not gone back to normal after a few weeks? |  | [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/) | |
| Smelling things that are not there | Do you smell things that are not there, like smoke or burnt toast? |  | [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/) | |

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

### `advice_head_injury_ae`

**What to do:** Go to A&E now. After a head injury, you need to be checked in hospital for bleeding inside the head.

**Look out for:**
- Getting drowsy or hard to wake
- Being sick, or a headache that gets worse
- Confusion, or trouble walking or speaking
- Clear fluid or blood coming from the ear or nose
- Passing out, a seizure (fit), or problems speaking

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself if you have hit your head. Ask someone to take you, or call 999. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/), [Broken nose](https://www.nhs.uk/conditions/broken-nose/), [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

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

### `advice_smell_urgent`

**What to do:** Get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Clear, watery fluid trickling from your nose
- A very bad headache, being sick, or feeling very sleepy
- A seizure (fit)

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Call 111 or use 111 online today. In an emergency call 999 or go to A&E.

Source: [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/), [Broken nose](https://www.nhs.uk/conditions/broken-nose/)

### `advice_smell_gp`

**What to do:** See a GP. They will check for causes such as sinusitis (swollen spaces in the face) or nasal polyps (soft growths inside the nose), and may send you for tests.

**Look out for:**
- A blocked nose on one side that does not go away
- Nosebleeds, or problems with your eyesight
- A seizure (fit), or a very bad headache

**Get more help when:**
- Call 999 or go to A&E if you have a seizure or a very bad headache with a stiff neck

**Where to go:** Make an appointment with a GP.

**What you can do yourself:**
- Rinse your nose with salt water if a cold or allergy might be the cause
- Smell training can help some people
- Fit a smoke alarm and a gas alarm, and check use-by dates, as you may not smell gas, fire or food that has gone off

Source: [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/)

### `advice_smell_self_care`

**What to do:** A change in your sense of smell is not usually serious. It may get better in a few weeks or months, especially after a cold, flu or COVID-19.

**Look out for:**
- Your sense of smell not going back to normal after a few weeks
- Smelling things that are not there, like smoke or burnt toast
- A blocked nose on one side, or nosebleeds

**Get more help when:**
- See a GP if you get any of the signs above
- Call 999 or go to A&E if you have a seizure or a very bad headache with a stiff neck

**Where to go:** You do not need an appointment now. A pharmacist can suggest salt water nose rinses.

**What you can do yourself:**
- Rinse your nose with salt water if a cold or allergy might be the cause
- Stay at home if you have a high temperature or do not feel well enough to do your usual activities
- Fit a smoke alarm and a gas alarm, and check use-by dates, as you may not smell gas, fire or food that has gone off

Source: [Anosmia](https://www.nhs.uk/symptoms/lost-or-changed-sense-smell/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sm_fit`: Clinical knowledge: the smell page says a changed sense of smell can rarely be caused by epilepsy. A new seizure needs checking in hospital.
- `rf_sm_meningitis_signs`: Clinical knowledge: a sinus infection can rarely spread to the lining of the brain (meningitis).
- `rf_sm_head_injury`: Clinical knowledge: losing the sense of smell after a head injury can mean damage to the nerves of smell or a skull injury, and needs checking.
- `or_sm_phantom`: AI reading of the smell page, which says this can rarely be caused by conditions like epilepsy. It is often harmless after a cold, so seeing a GP with no fixed time is used.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Common cold | 82272006 | very common | Blocked or runny nose: strongly supports; Hoarse voice: supports; Dry cough: supports; Phlegm dripping down the back of the throat from the nose: supports |
| COVID-19 | 840539006 | uncommon | Lost or changed sense of smell or taste: supports; Very high temperature, or feels hot, cold or shivery: supports; Dry cough: supports; Aching body: supports; Feels very tired: supports; Blocked or runny nose: supports |
| Hay fever (an allergy to pollen) | 21719001 | uncommon | Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Blocked or runny nose: strongly supports; Has eczema, hay fever or a food allergy: supports; Dry cough: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Allergic rhinitis (a nose allergy, often all year) | 446096008 | common | Blocked or runny nose: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Nose symptoms all year round: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Has eczema, hay fever or a food allergy: supports; Blocked or runny nose for more than 3 weeks: supports |
| Nasal polyps (soft, harmless growths inside the nose) | 736500007 | uncommon | Blocked or runny nose: strongly supports; Lost or changed sense of smell or taste: strongly supports; Blocked or runny nose for more than 3 weeks: strongly supports; Phlegm dripping down the back of the throat from the nose: supports; Snoring: supports; Sense of smell faded slowly over months or years: supports |
| Cancer of the nose or sinuses (rare; sinuses are spaces in the face, behind the cheeks) |  | rare | Only one side of the nose blocked: strongly supports; Blocked or runny nose for more than 3 weeks: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Lost or changed sense of smell or taste: supports; Gets nosebleeds regularly: supports; Sight changed suddenly: supports; Nosebleed: supports |
| Loss of smell after a cold, flu or COVID-19 |  | very common | Cold, flu, COVID-19 or a similar illness in the last few weeks: strongly supports; Things smell different or unpleasant: supports; Smelling things that are not there: supports; Sense of smell not back to normal after a few weeks: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
