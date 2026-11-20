# Review pack: Head injury

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
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | 2026-11-19 |  | Page last reviewed: 30 May 2025 |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | 2026-11-19 |  | Page last reviewed: 21 April 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |

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

## Head injury red flags: Emergency (help now)

Most of these are asked together as one question: *"Since the head injury, do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hi_drowsy`<br>Cannot stay awake or keep their eyes open after a head injury | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_fit`<br>A fit (seizure) after a head injury | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_high_force`<br>Fell from more than 1 metre or 5 stairs, or hit the head at high speed | "Fell from more than 1 metre or 5 stairs, or hit the head at high speed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999. Do not move the person if they may have hurt their neck, unless they are in danger.* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_vision_or_hearing`<br>Problems with vision or hearing after a head injury<br>**Note:** Double vision is a separate observation from other changes in sight, so it is named too. The Double vision page also says 999 or A&E for double vision after a head injury. | "Change in sight or loss of vision" OR "Double vision" OR ("Hearing loss or a change in hearing" OR "Tinnitus (ringing or buzzing in the ears)") | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_skull`<br>Signs of a broken skull: fluid or blood from the ears or nose, bruising behind the ears, a black eye without hitting the eye, a dent, or something in a wound | "Fluid or blood from the ears or nose, bruising behind the ears or a black eye, a dent or something in a wound" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_numb_or_weak`<br>New numbness or weakness in any part of the body after a head injury | "Numbness or weakness in the face, arms or legs" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_walk_speak_understand`<br>Problems with walking, balance, understanding or speaking after a head injury | "Finding it hard to balance or walk" OR "Difficulty speaking" OR "Suddenly confused" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_behaviour`<br>Behaviour has changed since the head injury | "Behaviour changed since the head injury" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_baby`<br>A baby under 1 with a bruise, swelling or large cut on the head | "Under 1 year old" AND "A bruise, swelling or large cut on the head" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_knocked_out`<br>Knocked out by the head injury, even for a short time<br>**Note:** The Head injury page says call 999 if the person was knocked out and has not woken up (the universal red flag for passing out covers that). It does not mention someone who was knocked out briefly and has woken. Clinical knowledge: being knocked out at all is a reason to be checked in hospital for bleeding. Needs clinical review. | "Knocked out by the head injury, even briefly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now. Do not drive yourself.* | **AI judgement, needs clinical review** | |
| `rf_hi_blood_thinners_ae`<br>A head injury in someone who takes blood thinners or bleeds easily<br>**Note:** Source difference: the Head injury page says get help from 111. Clinical knowledge: people on blood thinners are much more likely to bleed inside the head, even after a minor knock, and usually need a scan. Soft, with the urgent rule below as its floor. Needs clinical review. | "Takes medicine that thins the blood, or bleeds easily" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E today. Do not drive yourself.* | **AI judgement, needs clinical review** | |

## Head injury red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hi_being_sick`<br>Being sick after a head injury | "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_dizzy`<br>Feeling dizzy after a head injury | "Dizzy or off-balance" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_blood_thinners`<br>A head injury in someone who takes blood thinners or has a condition that thins the blood | "Takes medicine that thins the blood, or bleeds easily" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_hi_alcohol`<br>Drinking alcohol or taking other substances at the time of the head injury | "Drinking alcohol or taking substances at the time of the head injury" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |

## Head injury: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_hi_worried`<br>A head injury and worried about other symptoms | "Worried about symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `or_hi_over_2_weeks`<br>Symptoms of a head injury lasting more than 2 weeks | "Symptoms from the head injury lasting more than 2 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |

## Default outcome

Used when no rule fires.

- **A minor head injury with nothing that needs more help: look after yourself at home**
- Outcome: Self-manageable, Self-care, No appointment needed. *You can usually look after a minor head injury at home. Make sure an adult stays with you for the first 24 hours.*
- Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Fell from more than 1 metre or 5 stairs, or hit the head at high speed | Did you fall from higher than 1 metre or 5 stairs, or hit your head at high speed, such as in a road accident? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Hearing loss or a change in hearing | Have you lost some or all of your hearing, or has your hearing changed? |  | [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | |
| Tinnitus (ringing or buzzing in the ears) | Can you hear noises like ringing, buzzing or humming that do not come from around you? This is called tinnitus. | 60862001 | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Fluid or blood from the ears or nose, bruising behind the ears or a black eye, a dent or something in a wound | Since the head injury, is clear fluid or blood coming from the ears or nose? Or is there a bruise behind the ears, a black eye (but the eye was not hit), a dent in the head, or something stuck in a cut? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Numbness or weakness in the face, arms or legs | Do you have numbness or weakness in your face, arms or legs? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Finding it hard to balance or walk | Are you finding it hard to balance or walk, or are you falling over? | 22631008 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Behaviour changed since the head injury | Since the head injury, has the person's behaviour changed? For example, they are more irritable or distracted, or have lost interest in things around them. |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| A bruise, swelling or large cut on the head | Is there a bruise, swelling or large cut on the head? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Knocked out by the head injury, even briefly | Were you knocked out (unconscious) by the head injury, even for a short time? |  | **AI judgement, needs clinical review** | |
| Takes medicine that thins the blood, or bleeds easily | Do you take medicine that thins your blood, such as warfarin, apixaban or rivaroxaban? Or do you have a condition that makes you bleed more easily? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Dizzy or off-balance | Do you feel dizzy or off-balance, or like you or the room is spinning? | 404640003 | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| Drinking alcohol or taking substances at the time of the head injury | When you hurt your head, had you been drinking alcohol? Or taking things like cannabis or cocaine? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Symptoms from the head injury lasting more than 2 weeks | Have the symptoms from the head injury lasted more than 2 weeks? |  | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |

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

### `advice_head_injury_999`

**What to do:** Call 999 now. These signs after a head injury need to be checked in hospital straight away.

**Look out for:**
- The person stops responding, or their breathing changes
- A fit (seizure)
- Being very hard to wake
- Being sick again and again

**Get more help when:**
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.
- Call 999 again if they get worse before help arrives

**Where to go:** Call 999. Do not drive them to A&E yourself. If they may have hurt their neck, do not move them unless they are in danger.

**What you can do yourself:**
- Do not move the person if they may have hurt their neck or back

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

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

### `advice_head_injury_urgent`

**What to do:** Get help from NHS 111 now. After a head injury, these symptoms need to be checked today.

**Look out for:**
- Getting drowsy or hard to wake
- A fit (seizure)
- Problems with vision, hearing, walking, balance or speaking
- Clear fluid or blood coming from the ears or nose
- A headache that will not go away

**Get more help when:**
- Call 999 if you get any of the signs above
- Call 999 if the person is knocked out, has a fit, or cannot stay awake

**Where to go:** Call 111 or use 111 online. Call 111 for a child under 5. If you are told to go to A&E, do not drive yourself.

**What you can do yourself:**
- Make sure an adult stays with you for at least the first 24 hours
- Rest, and do not drink alcohol

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_head_injury_gp`

**What to do:** See a GP. Symptoms after a head injury that last more than 2 weeks should be checked.

**Look out for:**
- Headaches getting worse, being sick, or getting drowsy
- Confusion, or trouble walking or speaking

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Ask your GP before you drive, go back to work or school, or play sport

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_head_injury_self_care`

**What to do:** You can usually look after a minor head injury at home. You may have symptoms such as a mild headache for up to 2 weeks.

**Look out for:**
- Being sick, or feeling dizzy
- Getting drowsy, or not being able to stay awake
- Problems with vision, walking, balance, understanding or speaking
- A fit (seizure), or changes in behaviour

**Get more help when:**
- Get help from 111 if you are being sick or feel dizzy
- Call 999 if you get any of the other signs above
- See a GP if your symptoms last more than 2 weeks

**Where to go:** You do not need an appointment now. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Hold an ice pack wrapped in a tea towel to the area for short periods, to bring down swelling
- Rest, and take paracetamol for a headache
- Make sure an adult stays with you for at least the first 24 hours
- Do not drink alcohol, take sleeping pills or play contact sports until you feel better

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hi_vision_or_hearing`: Double vision is a separate observation from other changes in sight, so it is named too. The Double vision page also says 999 or A&E for double vision after a head injury.
- `rf_hi_knocked_out`: The Head injury page says call 999 if the person was knocked out and has not woken up (the universal red flag for passing out covers that). It does not mention someone who was knocked out briefly and has woken. Clinical knowledge: being knocked out at all is a reason to be checked in hospital for bleeding. Needs clinical review.
- `rf_hi_blood_thinners_ae`: Source difference: the Head injury page says get help from 111. Clinical knowledge: people on blood thinners are much more likely to bleed inside the head, even after a minor knock, and usually need a scan. Soft, with the urgent rule below as its floor. Needs clinical review.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bleeding in the brain, or a broken skull, after a head injury | 450410005 | rare | Knocked out by the head injury, even briefly: strongly supports; So drowsy they are hard to wake or cannot stay awake: strongly supports; Child limp, floppy, hard to wake or not responding as usual: strongly supports; Being sick: supports; Headache: supports; Has had a seizure (fit): supports; Suddenly confused: supports; Behaviour changed since the head injury: supports; Fluid or blood from the ears or nose, bruising behind the ears or a black eye, a dent or something in a wound: supports; Weakness, or cannot move part of the body (paralysis): supports; Difficulty speaking: supports |
| Minor head injury or concussion (the brain is shaken by a knock to the head) | 110030002 | very common | A bruise, swelling or large cut on the head: supports; Headache: supports; Dizzy or off-balance: supports; Feels sick or has been sick: supports; Bright lights hurt the eyes or are bothering you: supports; Feels very tired: supports |
| Symptoms that carry on after a head injury (post-concussion syndrome) | 40425004 | uncommon | Symptoms from the head injury lasting more than 2 weeks: strongly supports; Headache: supports; Dizzy or off-balance: supports; Feels very tired: supports; Bright lights hurt the eyes or are bothering you: supports |
| Broken skull (a crack or break in the bone of the head) | 71642004 | rare | Fluid or blood from the ears or nose, bruising behind the ears or a black eye, a dent or something in a wound: strongly supports; Fell from more than 1 metre or 5 stairs, or hit the head at high speed: supports; A bruise, swelling or large cut on the head: supports; Hearing loss or a change in hearing: supports; Headache: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
