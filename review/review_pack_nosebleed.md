# Review pack: Nosebleed

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
| [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | 2026-11-19 |  | Page last reviewed: 05 December 2023 |
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |
| [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | 2026-11-19 |  | Page last reviewed: 13 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | 2026-11-19 |  | Page last reviewed: 03 October 2023 |
| [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | 2026-11-18 |  | Page last reviewed: 26 January 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |

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

## Nosebleed red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_nb_over_15_minutes`<br>A nosebleed lasting longer than 10 to 15 minutes | "Nosebleed lasting longer than 10 to 15 minutes" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_heavy`<br>A nosebleed where the bleeding seems very heavy | "Nosebleed that seems very heavy" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_swallowing_blood`<br>Swallowing a large amount of blood that has made you sick | "Swallowing a lot of blood, which has made them sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_head_injury`<br>A nosebleed that started after a blow to the head | "Head injury in the last month" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_weak_or_dizzy`<br>A nosebleed with feeling weak or dizzy | "Feels light-headed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_breathing`<br>A nosebleed with difficulty breathing | "Difficulty breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `rf_nb_clear_fluid_after_injury`<br>Clear, watery fluid trickling from the nose after an injury | "Started after an injury to the nose or face" AND "Clear, watery fluid trickling from the nose after an injury" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |

## Nosebleed red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_nb_broken_nose`<br>After an injury, the nose is crooked, the swelling has not gone down after 3 days, or it is hard to breathe through | "Started after an injury to the nose or face" AND "Nose crooked, or not healing, after an injury" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| `rf_nb_child_bruising`<br>A child with nosebleeds who is bruising or bleeding easily, or for no reason | "Under 16 years old" AND "Bruising or bleeding easily, or for no reason" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |

## Nosebleed: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_nb_child_under_2`<br>A child under 2 who has had a nosebleed | "Under 2 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `or_nb_regular`<br>Regular nosebleeds | "Gets nosebleeds regularly" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `or_nb_anaemia`<br>Nosebleeds with signs of anaemia, such as skin paler than usual | "Skin paler than usual for weeks or longer" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `or_nb_blood_thinners`<br>A nosebleed in someone taking medicine to prevent blood clots, or with a blood clotting condition | "Takes medicine that thins the blood, or bleeds easily" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| `or_nb_bruising`<br>Nosebleeds with bruising or bleeding easily | "Bruising or bleeding easily, or for no reason" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |

## Default outcome

Used when no rule fires.

- **A nosebleed with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most nosebleeds can be treated at home and stop within 10 to 15 minutes*
- Source: [Nosebleed](https://www.nhs.uk/conditions/nosebleed/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Nosebleed | Do you have a nosebleed, or have you had one recently? |  | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Nosebleed lasting longer than 10 to 15 minutes | Has the nosebleed lasted longer than 10 to 15 minutes, even with pinching the soft part of your nose? |  | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| Nosebleed that seems very heavy | Does the bleeding from your nose seem very heavy? |  | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| Swallowing a lot of blood, which has made them sick | Are you swallowing a lot of blood, and has it made you sick? |  | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Started after an injury to the nose or face | Did this start after a blow or injury to your nose or face? |  | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| Clear, watery fluid trickling from the nose after an injury | Since the injury, is clear, watery fluid trickling from your nose? |  | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| Nose crooked, or not healing, after an injury | Since the injury, is your nose crooked, or is the swelling not going down after 3 days, or is it hard to breathe through your nose? |  | [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Bruising or bleeding easily, or for no reason | Have you been bruising or bleeding easily, or for no reason? | 424131007 | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |
| Under 2 years old | Is the person who is unwell under 2 years old? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Gets nosebleeds regularly | Do you get nosebleeds regularly? |  | [Nosebleed](https://www.nhs.uk/conditions/nosebleed/) | |
| Skin paler than usual for weeks or longer | Has your skin been paler than usual for weeks or longer? |  | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |
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

### `advice_nosebleed_ae`

**What to do:** Go to A&E now. Keep pinching the soft part of your nose on the way.

**Look out for:**
- Feeling weak, dizzy or faint
- Difficulty breathing
- Blood coming from the mouth as well as the nose

**Get more help when:**
- Call 999 if you pass out, find it hard to breathe, or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Sit down and lean forward, and pinch the soft part of your nose just above your nostrils
- Breathe through your mouth and spit out any blood

Source: [Nosebleed](https://www.nhs.uk/conditions/nosebleed/)

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

### `advice_broken_nose_urgent`

**What to do:** Get help from NHS 111 today. You may have broken your nose and it may need to be checked or straightened.

**Look out for:**
- A nosebleed that will not stop
- Clear, watery fluid trickling from your nose
- A very bad headache with blurred or double vision
- A purple swelling inside your nose

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above, or you are sick or pass out

**Where to go:** Call 111 or use 111 online today. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Hold an ice pack wrapped in a tea towel on your nose for up to 15 minutes, several times a day
- Take paracetamol or ibuprofen for pain
- Do not blow your nose or wear glasses until the swelling goes down

Source: [Broken nose](https://www.nhs.uk/conditions/broken-nose/)

### `advice_nosebleed_urgent`

**What to do:** Ask for an urgent GP appointment or call 111 today. Bruising or bleeding easily in a child needs checking.

**Look out for:**
- A nosebleed lasting longer than 10 to 15 minutes
- Being very pale, very tired or getting lots of infections
- Feeling weak or dizzy

**Get more help when:**
- Go to A&E if a nosebleed lasts longer than 10 to 15 minutes, or the child feels weak or dizzy

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 if you need advice for a child under 5.

**What you can do yourself:**
- For a nosebleed, sit down and lean forward, and pinch the soft part of the nose for 10 to 15 minutes

Source: [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/), [Nosebleed](https://www.nhs.uk/conditions/nosebleed/)

### `advice_nosebleed_gp`

**What to do:** See a GP. They may check for a cause, such as a problem with how your blood clots or a lack of iron.

**Look out for:**
- A nosebleed lasting longer than 10 to 15 minutes
- Bleeding that seems very heavy, or swallowing a lot of blood
- Feeling weak or dizzy

**Get more help when:**
- Go to A&E if you get any of the signs above

**Where to go:** Make an appointment with a GP. Do not stop a prescribed medicine to prevent blood clots without advice.

**What you can do yourself:**
- Sit down and lean forward, and pinch the soft part of your nose for 10 to 15 minutes
- Breathe through your mouth
- Afterwards, do not blow or pick your nose, or do heavy lifting, for 24 hours

Source: [Nosebleed](https://www.nhs.uk/conditions/nosebleed/)

### `advice_nosebleed_self_care`

**What to do:** Most nosebleeds are not serious and can be treated at home.

**Look out for:**
- A nosebleed lasting longer than 10 to 15 minutes
- Bleeding that seems very heavy, or swallowing a lot of blood that makes you sick
- Feeling weak or dizzy, or difficulty breathing
- Regular nosebleeds

**Get more help when:**
- Go to A&E if you get any of the first three signs above
- See a GP if you get nosebleeds regularly, or a child under 2 has had a nosebleed

**Where to go:** You do not need an appointment. A pharmacist can suggest a cream for the inside of the nose if it is dry.

**What you can do yourself:**
- Sit down and lean forward, and pinch the soft part of your nose just above your nostrils for 10 to 15 minutes
- Breathe through your mouth
- Put an ice pack wrapped in a tea towel on the top of your nose
- Afterwards, do not blow or pick your nose, or do heavy lifting, for 24 hours

Source: [Nosebleed](https://www.nhs.uk/conditions/nosebleed/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Broken nose | 263171005 | uncommon | Started after an injury to the nose or face: strongly supports; Nose crooked, or not healing, after an injury: supports; Swollen face, cheek or jaw: supports; Nosebleed: supports; Blocked or runny nose: supports |
| Leukaemia (a cancer of the blood) | 91855006 | rare | Bruising or bleeding easily, or for no reason: strongly supports; Skin paler than usual for weeks or longer: supports; Feels very tired: supports; Very high temperature, or feels hot, cold or shivery: supports; Night sweats: supports; Losing weight without trying: supports |
| Cancer of the nose or sinuses (rare; sinuses are spaces in the face, behind the cheeks) |  | rare | Only one side of the nose blocked: strongly supports; Blocked or runny nose for more than 3 weeks: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Lost or changed sense of smell or taste: supports; Gets nosebleeds regularly: supports; Sight changed suddenly: supports; Nosebleed: supports |
| Nosebleeds made worse by blood-thinning medicine or a blood clotting condition |  | rare | Gets nosebleeds regularly: strongly supports; Bruising or bleeding easily, or for no reason: strongly supports; Nosebleed lasting longer than 10 to 15 minutes: supports; Gums painful, swollen or bleeding: supports |
| Something stuck up the nose | 74699008 | rare | Something stuck up the nose: strongly supports; Only one side of the nose blocked: strongly supports; Nosebleed: supports; Bad breath: supports |
| Severe nosebleed from deeper inside the nose | 232355001 | uncommon | Nosebleed lasting longer than 10 to 15 minutes: strongly supports; Nosebleed that seems very heavy: supports; Swallowing a lot of blood, which has made them sick: supports; Feels light-headed: supports |
| Nosebleed from the front of the nose (the usual kind, not serious) | 232354002 | very common | Nosebleed after picking or blowing the nose, or a dry nose: strongly supports; Blocked or runny nose: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Gets nosebleeds regularly: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
