# Review pack: Eye pain

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
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/) | 2026-11-19 |  | Page last reviewed: 14 August 2023 |
| [Shingles](https://www.nhs.uk/conditions/shingles/) | 2026-11-18 |  | Page last reviewed: 23 November 2023 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | 2026-11-19 |  | Page last reviewed: 18 August 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | 2026-11-19 |  | Page last reviewed: 10 September 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |

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

## Eye pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ep_chemical`<br>A chemical or other harmful liquid in the eye | "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Rinse the eye with clean water for at least 20 minutes, then go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_ep_pierced_or_stuck`<br>An injured or pierced eye, something hit it at high speed, or something is stuck in it<br>**Note:** The Eye injuries page gives the same advice. | "Something sharp cut or pierced the eye" OR "Something hit the eye at high speed" OR "Something stuck in the eye that rinsing has not removed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go straight to A&E, or call 999* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_injury`<br>Eye pain after an injury to the eye<br>**Note:** Source difference: the Eye pain page says call 999 or go to A&E if you have injured your eye. The Eye injuries page says minor injuries often get better in a day, severe pain needs A&E, and an injury that is very painful or not better after 24 hours needs an urgent appointment. Soft, with the firm urgent rule below as its floor. | "Injured eye, or something hit the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go straight to A&E, or call 999* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_cannot_see`<br>Eye pain and cannot see (loss of vision) | "Cannot see out of 1 or both eyes, or a large part of the sight is missing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_keeps_awake`<br>Eye pain that keeps you awake at night | "Eye pain keeps them awake at night" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_sudden_severe`<br>Severe eye pain that started suddenly<br>**Note:** The Bulging eyes page says the same. | "Eye pain or other eye symptoms started suddenly" AND "Severe eye pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_ep_sudden`<br>Eye symptoms that started suddenly<br>**Note:** The page says call 999 or go to A&E if 'your eye symptoms start suddenly'. Read literally this covers grit or a scratch, which other pages treat as minor. Soft, with the firm urgent rule below as its floor. | "Eye pain or other eye symptoms started suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_lenses_and_vision`<br>Wears contact lenses, with eye pain and vision loss | "Wears contact lenses" AND "Change in sight or loss of vision" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E. Take your lenses out.* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_headache_red_sick`<br>Red eye, severe headache and feeling sick | "Red or bloodshot eye" AND "Very painful headache" AND "Feels sick or has been sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_after_surgery`<br>Severe pain or loss of vision after eye surgery or treatment in the last 4 weeks<br>**Note:** The page says severe pain or loss of vision. Including any change to the sight is AI judgement, from the Detached retina page, which says go to A&E if blurriness gets worse after surgery. | "Eye surgery or eye treatment in the last 4 weeks" AND ("Severe eye pain" OR "Change in sight or loss of vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E, or call the eye unit that treated you* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_gca_vision`<br>Eye pain with pain at the temples or jaw pain when eating, and changes to the sight or double vision: possible giant cell arteritis<br>**Note:** Clinical knowledge: giant cell arteritis with any sight symptom can cause permanent blindness within hours and needs same-day hospital treatment. The Giant cell arteritis page says an urgent GP appointment, and a same-day eye specialist if there are vision problems. | "Jaw pain when eating, or a sore or tender scalp or temple" AND ("Change in sight or loss of vision" OR "Double vision" OR "Lost the sight in 1 eye for a short time, then it came back") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Eye pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ep_severe`<br>Severe eye pain | "Severe eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_light`<br>Eye pain with sensitivity to light | "Bright lights hurt the eyes or are bothering you" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_vision`<br>Eye pain with changes to the sight, like blurring, how you see colour, or loss of vision | "Change in sight or loss of vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_very_red`<br>Eye pain and the eye is very red | "White of the eye very red" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_double_vision`<br>Eye pain and double vision | "Double vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_ep_injury_urgent`<br>Eye pain after an injury<br>**Note:** The firm floor under the soft emergency rule for an injury. | "Injured eye, or something hit the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. You could also see an optician.* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_ep_sudden_urgent`<br>Eye symptoms that started suddenly<br>**Note:** The firm floor under the soft emergency rule for sudden symptoms. AI reading. | "Eye pain or other eye symptoms started suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_ep_moving_eye`<br>Eye pain that is worse when moving the eye<br>**Note:** Clinical knowledge: pain on moving the eye can be optic neuritis or an infection behind the eye, which both need checking the same day. | "Eye hurts more when moving it" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_ep_gca`<br>Eye pain with pain at the temples or scalp, or jaw pain when eating: possible giant cell arteritis | "Jaw pain when eating, or a sore or tender scalp or temple" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/) | |
| `rf_ep_shingles`<br>Eye pain with blisters or a rash around the eye, such as shingles<br>**Note:** The Herpes simplex eye infections page says urgent for eye pain, and lists blisters around the eye. | "Blisters or a rash on the eyelid or skin around the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today* | [Shingles](https://www.nhs.uk/conditions/shingles/) | |

## Eye pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ep_lasting`<br>Eye pain lasting more than a few days, or eyelashes rubbing the eye<br>**Note:** The Eye pain page gives no routine advice. Seeing a GP or optician for pain that lasts is AI judgement, in line with the Red eye page. | "Eye pain lasting more than a few days" OR "Eyelashes grow inwards and rub the eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or optician. No fixed time is given.* | **AI judgement, needs clinical review** | |
| `or_ep_worried`<br>Worried about the eye pain | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or optician. No fixed time is given.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `or_ep_cluster`<br>Attacks of very bad pain around 1 eye: possible cluster headaches | "Severe sharp or burning pain around one eye, with a red or watering eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |

## Default outcome

Used when no rule fires.

- **Eye pain with nothing that needs more help: usually nothing to worry about**
- Outcome: Self-manageable, Self-care, No appointment needed. *Eye pain is common and usually nothing to worry about. A pharmacist can help.*
- Source: [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)
- **Note:** The page says eye pain is common and usually nothing to worry about, and gives no routine advice. Self-care as the default is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chemical or other harmful liquid in the eye | Has a chemical or other harmful liquid got in your eye? For example, bleach, oven cleaner, cement or plaster. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something sharp cut or pierced the eye | Has something sharp cut or pierced your eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something hit the eye at high speed | Did something hit your eye at high speed? For example, while hammering, drilling, grinding, using power tools or mowing. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something stuck in the eye that rinsing has not removed | Is something stuck in your eye that rinsing with water has not removed, such as a piece of glass, metal or grit? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Eye pain keeps them awake at night | Is the eye pain bad enough to keep you awake at night? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Eye pain or other eye symptoms started suddenly | Did the pain or other eye symptoms start suddenly, over minutes or a few hours? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Wears contact lenses | Do you wear contact lenses? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Eye surgery or eye treatment in the last 4 weeks | Have you had eye surgery or eye treatment, such as an injection in the eye, in the last 4 weeks? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Lost the sight in 1 eye for a short time, then it came back | Did you lose the sight in 1 eye for a few seconds or minutes, like a curtain coming down, and then it came back? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| White of the eye very red | Is the white of your eye very red, in part or all over? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Eye hurts more when moving it | Does it hurt more when you move your eye? |  | **AI judgement, needs clinical review** | |
| Blisters or a rash on the eyelid or skin around the eye | Do you have blisters or a rash on your eyelid, or on the skin around your eye? |  | [Herpes simplex eye infections](https://www.nhs.uk/conditions/herpes-simplex-eye-infections/) | |
| Eye pain lasting more than a few days | Has the pain in or around your eye lasted more than a few days? |  | **AI judgement, needs clinical review** | |
| Eyelashes grow inwards and rub the eye | Do your eyelashes grow inwards and rub against your eye? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Severe sharp or burning pain around one eye, with a red or watering eye | Is it a very bad, sharp or burning pain around one eye? Is that eye red or watering, or that side of your nose blocked or runny? |  | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |

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

### `advice_chemical_eye`

**What to do:** Rinse your eye with lots of clean water straight away, for at least 20 minutes. Then go to A&E or call 999.

**Look out for:**
- Pain or redness getting worse
- Changes to your sight

**Get more help when:**
- Keep rinsing your eye with water while you wait for help, or on the way to hospital
- Call 999 if you cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Take the container of the chemical with you, as the label may help with treatment. Do not drive yourself.

**What you can do yourself:**
- Hold your eye open and run clean, cool water over the eyeball. The flow should not be too strong.
- Take out contact lenses if you can do it easily
- Do not rub your eye

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/)

### `advice_eye_injury_ae`

**What to do:** Go to A&E now, or call 999. An injury like this needs to be checked in hospital to protect your sight.

**Look out for:**
- Changes to your sight
- Blood or pus coming from your eye
- Feeling or being sick

**Get more help when:**
- Call 999 if you cannot get to A&E safely, or if there is heavy bleeding

**Where to go:** Go to A&E. Some areas have an eye casualty (an emergency eye department) you may be sent to. Do not drive yourself. Ask someone to drive you or call 999.

**What you can do yourself:**
- Do not try to remove anything that has pierced your eye or is stuck in it
- Do not rub or press on your eye
- If you can, cover the eye loosely with something clean, such as a paper cup taped in place
- Do not wear contact lenses

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/), [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

### `advice_eye_emergency`

**What to do:** Go to A&E or call 999 now. Your eye symptoms need to be checked in hospital straight away to protect your sight.

**Look out for:**
- Your sight getting worse
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech
- Pain getting worse, or feeling or being sick

**Get more help when:**
- Call 999 if you get any signs of a stroke, or you cannot get to A&E safely

**Where to go:** Go to A&E. If there is an eye casualty (an emergency eye department) near you, the 111 service or A&E may send you there. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

**What you can do yourself:**
- Do not rub your eye
- If you wear contact lenses, take them out and bring them with you

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/), [Vision loss](https://www.nhs.uk/conditions/vision-loss/), [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

### `advice_gca_emergency`

**What to do:** Go to A&E now, or call 999. Pain at the side of the head or in the jaw with changes to your sight can be giant cell arteritis (swollen blood vessels in the head). It needs treatment today to protect your sight.

**Look out for:**
- Losing sight in 1 or both eyes, even for a short time
- Double vision
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Call 999 if you lose your sight or get any signs of a stroke

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/)

### `advice_eye_urgent`

**What to do:** Get your eye checked today. Ask your GP surgery for an urgent appointment, or see an optician today if they can, or call 111.

**Look out for:**
- Any changes to your sight, like wavy lines, flashing or loss of vision
- It starting to hurt to look at light
- A severe headache and feeling sick
- Pain getting worse

**Get more help when:**
- Go to A&E or call 999 if you suddenly cannot see, or get sudden severe eye pain

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Many opticians can see eye problems on the same day, and some areas have a minor eye conditions service. In an emergency, go to A&E or call 999.

**What you can do yourself:**
- Do not rub your eye
- Do not wear contact lenses until your eye has been checked

Source: [Eye pain](https://www.nhs.uk/symptoms/eye-pain/), [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Conjunctivitis](https://www.nhs.uk/conditions/conjunctivitis/)

### `advice_gca_urgent`

**What to do:** Ask for an urgent GP appointment or call 111 today. Pain at the side of the head or scalp, or jaw pain when eating, can be giant cell arteritis (swollen blood vessels in the head). It needs treatment quickly.

**Look out for:**
- Any change to your sight, such as blurring, double vision or losing sight in 1 eye
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Go to A&E or call 999 if your sight changes, even for a short time

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

Source: [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/)

### `advice_shingles_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Shingles near the eye or nose, or with changes to your vision, needs checking quickly to protect your sight.

**Look out for:**
- Your eye becoming more red or painful
- Your vision getting worse
- The rash spreading, or you feeling very unwell

**Get more help when:**
- Medicine for shingles works best if you start it within 3 days of the rash appearing
- Call 999 if you get sudden chest pain. Call 999 if pain spreads to your arm, neck, jaw or back.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Take paracetamol to help with the pain
- Keep the rash clean and dry, and wear loose clothing
- Do not share towels. Keep away from babies and people who are pregnant until the blisters dry.

Source: [Shingles](https://www.nhs.uk/conditions/shingles/)

### `advice_eye_gp`

**What to do:** See a GP or an optician to find out what is causing your eye pain.

**Look out for:**
- The pain getting severe
- It hurting to look at light
- Any changes to your sight

**Get more help when:**
- Ask for an urgent appointment or call 111 if the pain gets worse or your sight changes
- Go to A&E or call 999 if you cannot see, or the pain keeps you awake at night

**Where to go:** Make an appointment with a GP, or see an optician.

Source: [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

### `advice_cluster_headache_gp`

**What to do:** See a GP. Attacks of very bad pain around 1 eye may be cluster headaches, which can be treated.

**Look out for:**
- An eyelid drooping for the first time. Or 1 pupil (the black circle in the middle of the eye) becoming smaller than the other.
- Changes to your sight

**Get more help when:**
- Call 999 or go to A&E if an eyelid droops for the first time. Also if 1 pupil (the black circle in the middle of the eye) gets smaller.

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

Source: [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/)

### `advice_eye_pain_self_care`

**What to do:** Eye pain is common and usually nothing to worry about. A pharmacist can help.

**Look out for:**
- The pain getting severe
- It hurting to look at light
- Any changes to your sight
- The eye becoming very red

**Get more help when:**
- See a GP or optician if the pain lasts more than a few days
- Ask for an urgent appointment or call 111 if the pain becomes severe or your sight changes
- Call 999 or go to A&E if you cannot see, or the pain keeps you awake at night

**Where to go:** You do not need an appointment now. A pharmacist can give advice.

**What you can do yourself:**
- Take paracetamol or ibuprofen for the pain
- Do not rub your eye, and do not wear contact lenses until it is better

Source: [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ep_pierced_or_stuck`: The Eye injuries page gives the same advice.
- `rf_ep_injury`: Source difference: the Eye pain page says call 999 or go to A&E if you have injured your eye. The Eye injuries page says minor injuries often get better in a day, severe pain needs A&E, and an injury that is very painful or not better after 24 hours needs an urgent appointment. Soft, with the firm urgent rule below as its floor.
- `rf_ep_sudden_severe`: The Bulging eyes page says the same.
- `rf_ep_sudden`: The page says call 999 or go to A&E if 'your eye symptoms start suddenly'. Read literally this covers grit or a scratch, which other pages treat as minor. Soft, with the firm urgent rule below as its floor.
- `rf_ep_after_surgery`: The page says severe pain or loss of vision. Including any change to the sight is AI judgement, from the Detached retina page, which says go to A&E if blurriness gets worse after surgery.
- `rf_ep_gca_vision`: Clinical knowledge: giant cell arteritis with any sight symptom can cause permanent blindness within hours and needs same-day hospital treatment. The Giant cell arteritis page says an urgent GP appointment, and a same-day eye specialist if there are vision problems.
- `rf_ep_injury_urgent`: The firm floor under the soft emergency rule for an injury.
- `rf_ep_sudden_urgent`: The firm floor under the soft emergency rule for sudden symptoms. AI reading.
- `rf_ep_moving_eye`: Clinical knowledge: pain on moving the eye can be optic neuritis or an infection behind the eye, which both need checking the same day.
- `rf_ep_shingles`: The Herpes simplex eye infections page says urgent for eye pain, and lists blisters around the eye.
- `or_ep_lasting`: The Eye pain page gives no routine advice. Seeing a GP or optician for pain that lasts is AI judgement, in line with the Red eye page.
- `eye_pain default outcome`: The page says eye pain is common and usually nothing to worry about, and gives no routine advice. Self-care as the default is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cluster headaches | 193031009 | rare | Severe sharp or burning pain around one eye, with a red or watering eye: strongly supports; Gets headaches regularly: supports; One eyelid drooping, or one pupil smaller, for the first time: supports; Smokes, or has smoked in the past: supports; Headache: strongly supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Swollen blood vessels in the head (temporal arteritis) | 414341000 | rare | Jaw pain when eating, or a sore or tender scalp or temple: strongly supports; Change in sight or loss of vision: supports; Headache feels different from usual headaches: supports; Feels very tired: supports; Aching body: supports; Losing weight without trying: supports; Headache: strongly supports; Double vision: supports; Feels very unwell: supports; Pain and stiffness in both shoulders or both hips, worst in the morning: supports; Lost the sight in 1 eye for a short time, then it came back: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Sudden glaucoma (a quick build-up of pressure inside the eye) |  | rare | Severe eye pain: strongly supports; Glowing rings (halos) around lights: strongly supports; Headache: strongly supports; Feels sick or has been sick: strongly supports; Very painful headache: supports; Blurred, cloudy or misty sight: supports; White of the eye very red: supports; Front of the eye looks cloudy, or has a white spot: supports; Eye pain or other eye symptoms started suddenly: supports; Red or bloodshot eye: supports |
| Arc eye (a burn to the surface of the eye from welding or sunbed light) | 1714005 | very rare | Welding, or a sunbed, without eye protection in the last day: strongly supports; Both eyes affected: strongly supports; Gritty, scratchy or burning feeling in the eye: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports |
| Serious injury from a blow to the eye (bleeding inside the eye or a broken eye socket) |  | very rare | Hit in the eye by something blunt: strongly supports; Injured eye, or something hit the eye: strongly supports; Double vision: supports; Hard or painful to move the eye: supports; Severe eye pain: supports; Feels sick or has been sick: supports; Change in sight or loss of vision: supports |
| Chemical in the eye |  | very rare | Chemical or other harmful liquid in the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Watering eyes: supports |
| Conjunctivitis (a red, sticky eye infection) | 299699004 | uncommon | Sticky discharge (pus) from the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Red or bloodshot eye: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Watering eyes: supports; Cough or runny nose: supports |
| Scratch on the clear front of the eye (corneal abrasion) | 85848002 | rare | Injured eye, or something hit the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Feels like something is in the eye: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| Episcleritis (a red patch on the white of the eye, with mild soreness) | 815008 | rare | Redness in one patch of the white of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports |
| Skin infection of the eyelid and the skin around the eye | 314516007 | rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Swollen eyelid: strongly supports; Red, painful lump near the edge of the eyelid: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Something on the surface of the eye, such as dust, grit or an eyelash | 450671000124109 | uncommon | Feels like something is in the eye: strongly supports; Watering eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Red or bloodshot eye: supports |
| Herpes simplex eye infection (an eye infection caused by the cold sore virus) | 9389005 | rare | Has had cold sores or a herpes eye infection: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Weakened immune system: supports; Swollen eyelid: supports |
| Infection inside the eye after surgery or an injection in the eye | 1847009 | very rare | Eye surgery or eye treatment in the last 4 weeks: strongly supports; Severe eye pain: strongly supports; Change in sight or loss of vision: strongly supports; Red or bloodshot eye: supports; Sticky discharge (pus) from the eye: supports |
| Keratitis or an eye ulcer (a sore on the clear front of the eye), often from contact lenses | 5888003 | rare | Wears contact lenses: strongly supports; Front of the eye looks cloudy, or has a white spot: strongly supports; Eye pain: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Red or bloodshot eye: supports; Watering eyes: supports; Blurred, cloudy or misty sight: supports; Feels like something is in the eye: supports |
| Optic neuritis (swelling of the nerve at the back of the eye) | 66760008 | rare | Eye hurts more when moving it: strongly supports; Sight got worse over a few days: strongly supports; Colours look faded or washed out: strongly supports; Eye pain: supports; Change in sight in 1 eye only: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports |
| Infection behind the eye (orbital cellulitis) | 194005002 | very rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Hard or painful to move the eye: strongly supports; Swollen eyelid: strongly supports; Bulging eyes: supports; Eye hurts more when moving it: supports; Very high temperature, or feels hot, cold or shivery: supports; Change in sight or loss of vision: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |
| A cut through the eye, or something inside the eye |  | very rare | Something sharp cut or pierced the eye: strongly supports; Something hit the eye at high speed: strongly supports; Injured eye, or something hit the eye: strongly supports; Change in sight or loss of vision: supports; Eye pain: supports |
| Scleritis (painful swelling of the white outer layer of the eye) | 78370002 | rare | Deep, boring ache in the eye: strongly supports; Eye very dark red: strongly supports; Eye pain keeps them awake at night: supports; Severe eye pain: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Redness in one patch of the white of the eye: supports |
| Shingles near the eye (a painful rash of blisters on one side of the forehead, eyelid or nose) | 87513003 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Shingles rash on or near the eye or nose, or changes to vision: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Swollen eyelid: supports |
| Stye (a small, painful lump on the eyelid) | 397513003 | rare | Red, painful lump near the edge of the eyelid: strongly supports; Lump on or in the eyelid: strongly supports; Swollen eyelid: supports; Watering eyes: supports |
| Iritis or uveitis (swelling inside the eye that makes it red, sore and hurt in bright light) | 128473001 | rare | Bright lights hurt the eyes or are bothering you: strongly supports; Redness worst in a ring around the coloured part of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: strongly supports; Deep, boring ache in the eye: supports; Blurred, cloudy or misty sight: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Floaters or flashes in the eyes: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
