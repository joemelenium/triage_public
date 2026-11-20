# Review pack: Something in the eye

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
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | 2026-11-19 |  | Page last reviewed: 12 November 2024 |
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

## Something in the eye red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sie_chemical`<br>A strong chemical, such as oven cleaner or bleach, in the eye | "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Keep rinsing the eye with water, and go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_sie_pierced_or_fast`<br>A sharp object has pierced the eye, or something hit it at high speed | "Something sharp cut or pierced the eye" OR "Something hit the eye at high speed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999. Do not try to remove anything stuck in the eye.* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_sie_stuck`<br>Something stuck in the eye that rinsing has not removed, such as glass or grit<br>**Note:** The Eye pain and Dry eyes pages say the same. Reading 'stuck' as not removed by rinsing is AI judgement; the Eye injuries page says to wash the eye with clean water first. | "Something stuck in the eye that rinsing has not removed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_sie_after_injury`<br>Changes to the sight, severe pain, sensitivity to light, being sick, or cannot move the eye or keep it open, after something got in the eye<br>**Note:** The Eye injuries page lists each of these as a reason to go to A&E after an eye injury. Applying it to grit or an eyelash is AI reading. Soft, because a scratch on the surface of the eye or arc eye can cause pain and light sensitivity and are usually treated the same day outside A&E; the firm urgent rule below is its floor. | "Change in sight or loss of vision" OR "Severe eye pain" OR "Bright lights hurt the eyes or are bothering you" OR "Feels sick or has been sick" OR "Hard or painful to move the eye" OR "Cannot open the eye or keep it open" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |

## Something in the eye red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sie_after_injury_urgent`<br>Severe pain, sensitivity to light, changes to the sight, or cannot keep the eye open, after something got in the eye<br>**Note:** The firm floor under the soft emergency rule above. The page says urgent if an eye injury is very painful. | "Change in sight or loss of vision" OR "Severe eye pain" OR "Bright lights hurt the eyes or are bothering you" OR "Hard or painful to move the eye" OR "Cannot open the eye or keep it open" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. You could also visit an optician.* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_sie_not_better`<br>An eye injury, or something in the eye, not getting better after 24 hours | "Eye injury or something in the eye not better after 24 hours" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. You could also visit an optician.* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_sie_injury`<br>Something in the eye after an injury, or something hit the eye<br>**Note:** The page says get urgent help if you are worried about an eye injury, particularly in a child, and that minor injuries often get better within a day. Soft, so that a likely bit of dust can lower it. | "Injured eye, or something hit the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. You could also visit an optician.* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_sie_lenses`<br>Feels like something in the eye in someone who wears contact lenses<br>**Note:** The Red eye page says a red eye in someone who wears contact lenses could be an eye infection. Applying it to a painful eye is AI judgement. | "Wears contact lenses" AND ("Red or bloodshot eye" OR "Eye pain") | Urgent (help today)<br>Urgent care<br>Today<br>*Take your lenses out. Ask for an urgent GP or optician appointment, or get help from NHS 111.* | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| `rf_sie_welding`<br>Painful, gritty eyes after welding or a sunbed without eye protection: possible arc eye<br>**Note:** Clinical knowledge: arc eye is a burn to the surface of the eye. It is very painful, usually heals in a day or two, and should be checked the same day to rule out a metal fragment. | "Welding, or a sunbed, without eye protection in the last day" AND ("Eye pain" OR "Red or bloodshot eye" OR "Watering eyes") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Something in the eye: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Something in the eye, such as dust or an eyelash, with nothing that needs more help: wash it out**
- Outcome: Self-manageable, Self-care, No appointment needed. *Wash your eye with clean water. Minor eye injuries often get better within a day.*
- Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feels like something is in the eye | Does it feel like there is something in your eye, such as dust, an eyelash or grit? | 605954641000119109 | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
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
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Hard or painful to move the eye | Is it hard to move your eye, or does it not move as far as the other eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Cannot open the eye or keep it open | Is your eye so swollen or sore that you cannot open it or keep it open? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Eye injury or something in the eye not better after 24 hours | Has the feeling of something in your eye, or the injury, not got better after 24 hours? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Wears contact lenses | Do you wear contact lenses? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Red or bloodshot eye | Is the white of your eye red or bloodshot, in 1 or both eyes? | 703630003 | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Welding, or a sunbed, without eye protection in the last day | In the last day, have you been welding or near welding, or used a sunbed or sun lamp, without eye protection? |  | **AI judgement, needs clinical review** | |
| Watering eyes | Do your eyes keep watering? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |

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

### `advice_something_in_eye_self_care`

**What to do:** Wash your eye with clean water to get rid of dust, grit or an eyelash. Minor eye injuries often get better within a day.

**Look out for:**
- Something still in your eye after rinsing
- Changes to your sight
- Severe pain, or it hurting to look at light

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if it is not better after 24 hours. You could also see an optician.
- Go to A&E or call 999 if something is stuck in your eye or your sight changes

**Where to go:** You do not need an appointment now.

**What you can do yourself:**
- Hold your eye open and run clean water over it. Use tap water or bottled water that is not hot.
- Do not rub your eye
- Do not wear contact lenses or make-up around the eye until it is better
- Take paracetamol or ibuprofen for any pain

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sie_stuck`: The Eye pain and Dry eyes pages say the same. Reading 'stuck' as not removed by rinsing is AI judgement; the Eye injuries page says to wash the eye with clean water first.
- `rf_sie_after_injury`: The Eye injuries page lists each of these as a reason to go to A&E after an eye injury. Applying it to grit or an eyelash is AI reading. Soft, because a scratch on the surface of the eye or arc eye can cause pain and light sensitivity and are usually treated the same day outside A&E; the firm urgent rule below is its floor.
- `rf_sie_after_injury_urgent`: The firm floor under the soft emergency rule above. The page says urgent if an eye injury is very painful.
- `rf_sie_injury`: The page says get urgent help if you are worried about an eye injury, particularly in a child, and that minor injuries often get better within a day. Soft, so that a likely bit of dust can lower it.
- `rf_sie_lenses`: The Red eye page says a red eye in someone who wears contact lenses could be an eye infection. Applying it to a painful eye is AI judgement.
- `rf_sie_welding`: Clinical knowledge: arc eye is a burn to the surface of the eye. It is very painful, usually heals in a day or two, and should be checked the same day to rule out a metal fragment.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Arc eye (a burn to the surface of the eye from welding or sunbed light) | 1714005 | very rare | Welding, or a sunbed, without eye protection in the last day: strongly supports; Both eyes affected: strongly supports; Gritty, scratchy or burning feeling in the eye: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports |
| Chemical in the eye |  | very rare | Chemical or other harmful liquid in the eye: strongly supports; Eye pain: supports; Red or bloodshot eye: supports; Watering eyes: supports |
| Conjunctivitis (a red, sticky eye infection) | 299699004 | uncommon | Sticky discharge (pus) from the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Red or bloodshot eye: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Watering eyes: supports; Cough or runny nose: supports |
| Scratch on the clear front of the eye (corneal abrasion) | 85848002 | rare | Injured eye, or something hit the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Feels like something is in the eye: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| Eyelid turning outwards or inwards, or eyelashes rubbing the eye |  | rare | Eyelid has changed shape, turns inwards or droops away from the eye: strongly supports; Eyelashes grow inwards and rub the eye: strongly supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Eye waters all the time, with tears running down the cheek: supports; Red or bloodshot eye: supports |
| Something on the surface of the eye, such as dust, grit or an eyelash | 450671000124109 | uncommon | Feels like something is in the eye: strongly supports; Watering eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Red or bloodshot eye: supports |
| Keratitis or an eye ulcer (a sore on the clear front of the eye), often from contact lenses | 5888003 | rare | Wears contact lenses: strongly supports; Front of the eye looks cloudy, or has a white spot: strongly supports; Eye pain: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Red or bloodshot eye: supports; Watering eyes: supports; Blurred, cloudy or misty sight: supports; Feels like something is in the eye: supports |
| A cut through the eye, or something inside the eye |  | very rare | Something sharp cut or pierced the eye: strongly supports; Something hit the eye at high speed: strongly supports; Injured eye, or something hit the eye: strongly supports; Change in sight or loss of vision: supports; Eye pain: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
