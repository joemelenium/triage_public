# Review pack: Dry eyes

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
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | 2026-11-19 |  | Page last reviewed: 12 November 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
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

## Dry eyes red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_de_pierced_or_stuck`<br>Injured or pierced eye, something stuck in the eye, or a chemical in the eye | "Something sharp cut or pierced the eye" OR "Something hit the eye at high speed" OR "Something stuck in the eye that rinsing has not removed" OR "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_red_headache_sick`<br>Red eye, severe headache and feeling sick | "Red or bloodshot eye" AND "Very painful headache" AND "Feels sick or has been sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_vision`<br>Any changes to the sight, like wavy lines, flashing or loss of vision<br>**Note:** Source difference: the Dry eyes page says call 999 or go to A&E, but lists blurry eyes as a dry eye symptom. The Vision loss and Conjunctivitis pages say urgent for changes in sight. Soft, with the firm urgent rule below as its floor. | "Change in sight or loss of vision" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_light`<br>It hurts to look at light<br>**Note:** Source difference: the page lists sensitivity to light as a dry eye symptom, and pain looking at light as a reason to call 999. The Eye pain page says urgent. Soft, with the firm urgent rule below as its floor. | "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_very_dark_red`<br>Eye or eyes very dark red<br>**Note:** Same as the red eye rule: the Eyelid problems page says urgent for a very red eye. | "Eye very dark red" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_injury`<br>An injury to the eye<br>**Note:** Source difference: the Eye injuries page says minor injuries often get better within a day. Soft, with the firm urgent rule below as its floor. | "Injured eye, or something hit the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |

## Dry eyes red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_de_vision_or_light_urgent`<br>Changes to the sight, pain looking at light, or an eye injury<br>**Note:** The firm floor under the soft emergency rules above. | "Change in sight or loss of vision" OR "Bright lights hurt the eyes or are bothering you" OR "Injured eye, or something hit the eye" OR "White of the eye very red" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_de_painful_red`<br>The eye is painful and red | "Red or bloodshot eye" AND "Eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `rf_de_red_lenses`<br>Red eye in someone who wears contact lenses: could be an eye infection | "Red or bloodshot eye" AND "Wears contact lenses" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. Take your lenses out.* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |

## Dry eyes: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_de_weeks`<br>Still dry after trying home treatments for a few weeks | "Still dry after trying home treatment for a few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See an optician or GP. No fixed time is given.* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `or_de_eyelid_shape`<br>Any change in the shape of the eyelids | "Eyelid has changed shape, turns inwards or droops away from the eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See an optician or GP. No fixed time is given.* | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| `or_de_worried`<br>Worried about the eyes | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See an optician or GP. No fixed time is given.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |

## Default outcome

Used when no rule fires.

- **Dry eyes with nothing that needs more help: treat them yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Dry eyes are not usually serious. A pharmacist can help.*
- Source: [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Dry eyes | Do your eyes feel dry? | 162290004 | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Something sharp cut or pierced the eye | Has something sharp cut or pierced your eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something hit the eye at high speed | Did something hit your eye at high speed? For example, while hammering, drilling, grinding, using power tools or mowing. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Something stuck in the eye that rinsing has not removed | Is something stuck in your eye that rinsing with water has not removed, such as a piece of glass, metal or grit? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Chemical or other harmful liquid in the eye | Has a chemical or other harmful liquid got in your eye? For example, bleach, oven cleaner, cement or plaster. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Eye very dark red | Is your eye very dark red, rather than pink or bright red? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| White of the eye very red | Is the white of your eye very red, in part or all over? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Wears contact lenses | Do you wear contact lenses? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Still dry after trying home treatment for a few weeks | Have your eyes still felt dry after trying home treatments, such as eye drops, for a few weeks? |  | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |
| Eyelid has changed shape, turns inwards or droops away from the eye | Has the shape of your eyelid changed, or is it turning inwards or drooping away from the eye? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_eye_contact_lens_urgent`

**What to do:** Take your contact lenses out and get your eye checked today. A red or painful eye when you wear lenses could be an infection on the clear front of the eye, which can harm your sight.

**Look out for:**
- Changes to your sight, or a white spot on the eye
- It hurting to look at light
- Pain getting worse

**Get more help when:**
- Go to A&E or call 999 if you have eye pain and your sight gets worse

**Where to go:** Ask your GP surgery or an optician for an urgent appointment, or call 111 or use 111 online. Take your lenses and their case with you.

**What you can do yourself:**
- Do not put your lenses back in until your eye has been checked
- Wear glasses instead

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

### `advice_dry_eyes_gp`

**What to do:** See an optician or GP. They can check what is causing your dry eyes and suggest treatment.

**Look out for:**
- Your eye becoming painful and red
- Any changes to your sight

**Get more help when:**
- Ask for an urgent appointment or call 111 if your eye becomes painful and red
- Call 999 or go to A&E if your sight changes or it hurts to look at light

**Where to go:** Book an appointment with an optician or a GP.

**What you can do yourself:**
- Clean your eyelids every day with a warm, damp flannel
- Take breaks from screens, and keep your screen just below eye level

Source: [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

### `advice_dry_eyes_self_care`

**What to do:** Dry eyes are not usually serious. There are things you can do to help, and a pharmacist can suggest eye drops.

**Look out for:**
- Your eye becoming painful and red
- Any changes to your sight
- Dry eyes that do not get better after a few weeks

**Get more help when:**
- See an optician or GP if your eyes are still dry after a few weeks of home treatment
- Ask for an urgent appointment or call 111 if your eye becomes painful and red

**Where to go:** You do not need an appointment now. A pharmacist can help with eye drops, gels or ointments.

**What you can do yourself:**
- Clean your eyelids every day. Press a warm, damp flannel on your eyes, then gently wipe your eyelids.
- Take breaks from screens, and keep your screen just below eye level
- If you wear contact lenses, take them out and wear glasses to rest your eyes
- Do not smoke, and avoid smoky, dry or dusty places

Source: [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_de_vision`: Source difference: the Dry eyes page says call 999 or go to A&E, but lists blurry eyes as a dry eye symptom. The Vision loss and Conjunctivitis pages say urgent for changes in sight. Soft, with the firm urgent rule below as its floor.
- `rf_de_light`: Source difference: the page lists sensitivity to light as a dry eye symptom, and pain looking at light as a reason to call 999. The Eye pain page says urgent. Soft, with the firm urgent rule below as its floor.
- `rf_de_very_dark_red`: Same as the red eye rule: the Eyelid problems page says urgent for a very red eye.
- `rf_de_injury`: Source difference: the Eye injuries page says minor injuries often get better within a day. Soft, with the firm urgent rule below as its floor.
- `rf_de_vision_or_light_urgent`: The firm floor under the soft emergency rules above.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Blepharitis (swollen, itchy, crusty eyelid edges) | 41446000 | uncommon | Itchy, sore or crusty eyelid edges: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Sticky discharge (pus) from the eye: supports; Dry eyes: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| Eyelid turning outwards or inwards, or eyelashes rubbing the eye |  | rare | Eyelid has changed shape, turns inwards or droops away from the eye: strongly supports; Eyelashes grow inwards and rub the eye: strongly supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Eye waters all the time, with tears running down the cheek: supports; Red or bloodshot eye: supports |
| Thyroid eye problems (swelling behind the eyes linked to a thyroid condition) | 276177000 | rare | Has a thyroid problem, such as an overactive thyroid: strongly supports; Bulging eyes: strongly supports; Both eyes affected: supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Double vision: supports; Swollen eyelid: supports; Smokes, or has smoked in the past: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
