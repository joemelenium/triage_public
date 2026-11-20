# Review pack: Heart palpitations

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
| [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/) | 2026-11-18 |  | Page last reviewed: 13 January 2025 |
| [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | 2026-11-18 |  | Page last reviewed: 17 March 2026 |
| [Supraventricular tachycardia (SVT)](https://www.nhs.uk/conditions/supraventricular-tachycardia-svt/) | 2026-11-18 |  | Page last reviewed: 12 June 2024 |
| [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | 2026-11-18 |  | Page last reviewed: 26 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
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

## Heart palpitations red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_palp_now_with_symptoms`<br>Heart racing or fluttering right now, with chest pain, shortness of breath, sweating, feeling sick, or feeling faint or fainting<br>**Note:** Source difference: the Heart palpitations page says call 999 or go to A&E for palpitations now with chest pain, shortness of breath or feeling faint. The Atrial fibrillation and SVT pages say call 999, and the Atrial fibrillation page adds sweating and feeling or being sick. The more urgent is used. The Atrial fibrillation page also lists a severe headache, which has no observation yet. | "Heart racing, pounding or fluttering right now" AND ("Chest pain" OR "Short of breath" OR "Feels light-headed" OR "Passed out (fainted)" OR "Feels sweaty" OR "Feels sick or has been sick") | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/) | |
| `rf_palp_not_going_away`<br>Heart racing or fluttering right now that has gone on for more than a few minutes<br>**Note:** AI reading of 'you currently have heart palpitations and they do not go away'. The page gives no time, so 'more than a few minutes' is used, from its advice to see a GP if they last longer than a few minutes. Marked soft because ongoing palpitations from a panic attack or caffeine are common. | "Heart racing, pounding or fluttering right now" AND "Each episode lasts longer than a few minutes" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `rf_palp_rhythm_episode_long`<br>A diagnosed heart rhythm problem and this episode has lasted longer than usual<br>**Note:** The SVT page says this for diagnosed SVT. Applying it to other diagnosed heart rhythm problems is AI judgement. | "Has a heart rhythm problem, such as atrial fibrillation or SVT" AND "Episode of fast heartbeat lasting longer than usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Supraventricular tachycardia (SVT)](https://www.nhs.uk/conditions/supraventricular-tachycardia-svt/) | |
| `rf_palp_very_slow_heartbeat`<br>Heart beating very slowly, with feeling faint, passing out, chest pain or breathlessness<br>**Note:** AI judgement from clinical knowledge: a very slow heartbeat with these signs can mean the heart is not pumping enough blood (for example heart block). Added after the pilot check. | "Heart beating very slowly" AND ("Feels light-headed" OR "Passed out (fainted)" OR "Chest pain" OR "Short of breath") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Heart palpitations red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_palp_stopped_with_symptoms`<br>Heart palpitations that came with chest pain, shortness of breath, or feeling faint or fainting, and have now stopped<br>**Note:** If the palpitations are still happening, the emergency rule above applies instead. The question about symptoms that came with the palpitations, even if they have stopped, was added in the breathing batch: before it, chest pain or feeling faint that had settled could not be reported. | "Chest pain" OR "Short of breath" OR "Feels light-headed" OR "Passed out (fainted)" OR "Palpitations came with chest pain, breathlessness or feeling faint, even if they have stopped" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, call 111 or get help from 111 online* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `rf_palp_irregular_now`<br>An irregular heartbeat right now<br>**Note:** Clinical knowledge: an irregular heartbeat happening now may be atrial fibrillation, which is best caught on a heart tracing (ECG) while it is happening. The Atrial fibrillation page says see a GP (non-urgent) if you think you have it. | "Heart racing, pounding or fluttering right now" AND "Heartbeat feels irregular, with no steady rhythm" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_palp_fast_now`<br>A very fast heartbeat right now<br>**Note:** Clinical knowledge: a very fast heartbeat happening now is best caught on a heart tracing (ECG). If it goes on for more than a few minutes, the emergency rule above applies. | "Heart racing, pounding or fluttering right now" AND "Heart beating very fast" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_palp_during_exercise`<br>Heart racing or fluttering that comes on while exercising<br>**Note:** Clinical knowledge: palpitations brought on by exercise can be a sign of a heart problem and should be checked promptly. No NHS page in the source log gives an urgency for this. Needs clinical review. | "Heart racing or fluttering comes on during exercise" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |

## Heart palpitations: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_palp_keep_coming_back`<br>Palpitations that keep coming back or are happening more often | "Keep coming back, or happening more often" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `or_palp_last_minutes`<br>Palpitations that last longer than a few minutes | "Each episode lasts longer than a few minutes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `or_palp_heart_condition`<br>Palpitations in someone with a heart condition | "Has a heart condition" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `or_palp_family_history`<br>Palpitations and a history of heart problems in the family<br>**Note:** The page says 'a history of heart problems in your family'. The existing observation asks about heart problems in a close relative before 60, which is narrower. Needs review. | "Aged 16 or over" AND "Close relative had a heart attack or angina before 60" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| `or_palp_irregular`<br>A heartbeat that feels irregular (possible atrial fibrillation) | "Heartbeat feels irregular, with no steady rhythm" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/) | |
| `or_palp_pale`<br>Palpitations with skin paler than usual (possible anaemia) | "Skin paler than usual for weeks or longer" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |

## Default outcome

Used when no rule fires.

- **Palpitations in someone who feels well, with nothing that needs more help: usually harmless**
- Outcome: Self-manageable, Self-care, No appointment needed. *Heart palpitations are usually harmless. Avoid things that can trigger them.*
- Source: [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/)
- **Note:** The page says palpitations are common and usually harmless, and to get help if they keep coming back or come with other symptoms. Self-care as the default is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Heart racing, slow, skipping or fluttering | Does your heart feel like it is racing, going too slowly, skipping a beat or fluttering? | 80313002 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Heart racing, pounding or fluttering right now | Is your heart racing, pounding, fluttering or skipping beats right now? |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels sweaty | Do you feel sweaty? | 415690000 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Each episode lasts longer than a few minutes | Does your heart racing or fluttering last longer than a few minutes each time? |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Has a heart rhythm problem, such as atrial fibrillation or SVT | Has a doctor told you that you have a heart rhythm problem? For example, atrial fibrillation (an irregular heartbeat), or SVT (episodes of a very fast heartbeat). |  | [Supraventricular tachycardia (SVT)](https://www.nhs.uk/conditions/supraventricular-tachycardia-svt/) | |
| Episode of fast heartbeat lasting longer than usual | Has your fast heartbeat gone on for longer than it usually does this time? |  | [Supraventricular tachycardia (SVT)](https://www.nhs.uk/conditions/supraventricular-tachycardia-svt/) | |
| Heart beating very slowly | Is your heart beating much more slowly than usual? | 48867003 | **AI judgement, needs clinical review** | |
| Palpitations came with chest pain, breathlessness or feeling faint, even if they have stopped | When your heart was racing or fluttering, did you also have chest pain, feel short of breath, feel faint or faint? Answer yes even if this has stopped now. |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Heartbeat feels irregular, with no steady rhythm | Does your heartbeat feel irregular, as if it has no steady rhythm? | 361137007 | [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Heart racing or fluttering comes on during exercise | Does your heart racing or fluttering come on while you are exercising? |  | **AI judgement, needs clinical review** | |
| Keep coming back, or happening more often | Does your heart racing or fluttering keep coming back, or is it happening more often? |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Has a heart condition | Has a doctor told you that you have a heart condition? For example, heart failure, a heart valve problem or a heart rhythm problem. |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Aged 16 or over | Is the person who is unwell aged 16 or over? |  | **AI judgement, needs clinical review** | |
| Close relative had a heart attack or angina before 60 | Has a close relative had heart problems before the age of 60? For example, a heart attack, or angina (chest pain caused by narrowed blood vessels to the heart). |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Skin paler than usual for weeks or longer | Has your skin been paler than usual for weeks or longer? |  | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |

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

### `advice_palpitations_999`

**What to do:** Call 999 now. A fast or uneven heartbeat with these symptoms needs treatment in hospital straight away.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- Sit or lie down and rest while you wait

Source: [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/), [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/), [Supraventricular tachycardia (SVT)](https://www.nhs.uk/conditions/supraventricular-tachycardia-svt/)

### `advice_palpitations_ae`

**What to do:** Call 999 or go to A&E now. Your heart palpitations are not going away and need to be checked.

**Look out for:**
- Chest pain
- Shortness of breath
- Feeling faint, or fainting

**Get more help when:**
- Call 999 straight away if you get any of the signs above, or you get worse while you wait

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Sit down and rest while you wait

Source: [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/)

### `advice_palpitations_urgent`

**What to do:** Ask your GP surgery for an urgent appointment, or get help from NHS 111 today. You can call 111 or use 111 online.

**Look out for:**
- Palpitations that come back and do not go away
- Chest pain or shortness of breath while your heart is racing
- Feeling faint, or fainting

**Get more help when:**
- Call 999 or go to A&E if your palpitations come back with any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999 or go to A&E. Do not drive yourself to A&E.

**What you can do yourself:**
- Write down when the palpitations happen and how long they last. This helps the doctor.
- Avoid caffeine, alcohol and smoking until you have been checked

Source: [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/), [Atrial fibrillation](https://www.nhs.uk/conditions/atrial-fibrillation/)

### `advice_palpitations_gp`

**What to do:** See a GP about your heart palpitations. They are usually harmless, but it is important to get them checked.

**Look out for:**
- Palpitations that do not go away
- Chest pain or shortness of breath
- Feeling faint, or fainting

**Get more help when:**
- Call 999 or go to A&E if you have palpitations now with any of the signs above, or they do not go away
- Ask for an urgent GP appointment or call 111 if you had these signs with palpitations that have now stopped

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Write down when the palpitations happen and how long they last
- Avoid things that can set them off, such as caffeine, alcohol, smoking and stress

Source: [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/)

### `advice_palpitations_self_care`

**What to do:** Heart palpitations are common and usually harmless. You do not need to see anyone now if you feel well.

**Look out for:**
- Palpitations that keep coming back, or happen more often
- Palpitations that last longer than a few minutes
- Chest pain, shortness of breath, feeling faint or fainting

**Get more help when:**
- See a GP if they keep coming back, last longer than a few minutes, or you have a heart condition
- Call 999 or go to A&E if you have palpitations now that do not go away. Do the same if they come with chest pain, shortness of breath or feeling faint.

**Where to go:** You do not need an appointment now. For advice see a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Cut down on caffeine, alcohol and smoking
- Try to get enough sleep and find ways to manage stress
- Check the leaflet of any medicine you take, in case it can cause palpitations

Source: [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_palp_now_with_symptoms`: Source difference: the Heart palpitations page says call 999 or go to A&E for palpitations now with chest pain, shortness of breath or feeling faint. The Atrial fibrillation and SVT pages say call 999, and the Atrial fibrillation page adds sweating and feeling or being sick. The more urgent is used. The Atrial fibrillation page also lists a severe headache, which has no observation yet.
- `rf_palp_not_going_away`: AI reading of 'you currently have heart palpitations and they do not go away'. The page gives no time, so 'more than a few minutes' is used, from its advice to see a GP if they last longer than a few minutes. Marked soft because ongoing palpitations from a panic attack or caffeine are common.
- `rf_palp_rhythm_episode_long`: The SVT page says this for diagnosed SVT. Applying it to other diagnosed heart rhythm problems is AI judgement.
- `rf_palp_very_slow_heartbeat`: AI judgement from clinical knowledge: a very slow heartbeat with these signs can mean the heart is not pumping enough blood (for example heart block). Added after the pilot check.
- `rf_palp_stopped_with_symptoms`: If the palpitations are still happening, the emergency rule above applies instead. The question about symptoms that came with the palpitations, even if they have stopped, was added in the breathing batch: before it, chest pain or feeling faint that had settled could not be reported.
- `rf_palp_irregular_now`: Clinical knowledge: an irregular heartbeat happening now may be atrial fibrillation, which is best caught on a heart tracing (ECG) while it is happening. The Atrial fibrillation page says see a GP (non-urgent) if you think you have it.
- `rf_palp_fast_now`: Clinical knowledge: a very fast heartbeat happening now is best caught on a heart tracing (ECG). If it goes on for more than a few minutes, the emergency rule above applies.
- `rf_palp_during_exercise`: Clinical knowledge: palpitations brought on by exercise can be a sign of a heart problem and should be checked promptly. No NHS page in the source log gives an urgency for this. Needs clinical review.
- `or_palp_family_history`: The page says 'a history of heart problems in your family'. The existing observation asks about heart problems in a close relative before 60, which is narrower. Needs review.
- `palpitations default outcome`: The page says palpitations are common and usually harmless, and to get help if they keep coming back or come with other symptoms. Self-care as the default is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anxiety or panic attack | 48694002 | common | Sudden rush of intense fear or panic: strongly supports; Pain triggered by worry or stress: strongly supports; Tingling or pins and needles in the fingers or around the mouth: supports; Breathing very fast: supports; Heart beating very fast: supports; Heart racing, slow, skipping or fluttering: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Short of breath: supports |
| Irregular heartbeat (atrial fibrillation) | 49436004 | rare | Heart racing, slow, skipping or fluttering: strongly supports; Heartbeat feels irregular, with no steady rhythm: strongly supports; Each episode lasts longer than a few minutes: supports; Heart racing, pounding or fluttering right now: supports; Heart beating very fast: supports; Short of breath: supports; Feels very tired: supports |
| A dangerous heart rhythm (very fast or very slow) or another heart problem that can cause fainting | 698247007 | very rare | Passed out (fainted): strongly supports; Heart beating very slowly: strongly supports; Heart beating very fast: supports; Heart racing, pounding or fluttering right now: supports; Feels light-headed: supports; Chest pain: supports; Short of breath: supports; Heart racing or fluttering comes on during exercise: supports; Has a heart condition: supports; Close relative had a heart attack or angina before 60: supports; Fainted while exercising: strongly supports; Heart racing, slow, skipping or fluttering: strongly supports; Fainted with no warning at all: strongly supports; Fainted while lying down: supports; Family member died suddenly under 40, or has an inherited heart condition: supports |
| Harmless extra or skipped heartbeats (ectopic beats) | 29717002 | common | Heart racing, slow, skipping or fluttering: strongly supports; Feels like a skipped beat or extra thump, then back to normal: strongly supports; Comes on after caffeine, alcohol, smoking, stress or poor sleep: supports; Keep coming back, or happening more often: supports; Heartbeat feels irregular, with no steady rhythm: supports |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Swelling of the heart muscle (myocarditis) | 50920009 | rare | Cold, flu, COVID-19 or a similar illness in the last few weeks: strongly supports; Short of breath: supports; Heart racing, slow, skipping or fluttering: supports; Heart beating very fast: supports; Feels very tired: supports; Out of breath doing everyday things: supports; Chest pain is there now: strongly supports |
| Episodes of a very fast heartbeat (supraventricular tachycardia, SVT) | 6456007 | uncommon | Heart racing, slow, skipping or fluttering: strongly supports; Heart beating very fast: strongly supports; Fast heartbeat starts and stops suddenly: strongly supports; Heart racing, pounding or fluttering right now: strongly supports; Each episode lasts longer than a few minutes: supports; Keep coming back, or happening more often: supports; Feels light-headed: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
