# Review pack: Bulging eyes

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
| [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | 2026-11-19 |  | Page last reviewed: 20 June 2023 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
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

## Bulging eyes red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_be_child_new`<br>A child's eye or eyes have just started bulging | "Under 16 years old" AND "Bulging has just started" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| `rf_be_new_with_vision`<br>Eyes have started bulging, with changes to the sight like wavy lines, flashing or loss of vision<br>**Note:** Including double vision is AI judgement: it is a change in sight. | "Bulging has just started" AND ("Change in sight or loss of vision" OR "Floaters or flashes in the eyes" OR "Double vision") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| `rf_be_new_with_headache`<br>Eyes have started bulging, with a severe headache or feeling sick | "Bulging has just started" AND ("Very painful headache" OR "Feels sick or has been sick") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| `rf_be_severe_pain`<br>Severe eye pain, or severe eye pain that started suddenly | "Severe eye pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| `rf_be_infection`<br>Bulging eye with a red, hot, swollen eyelid, or an eye that is hard to move: possible infection behind the eye<br>**Note:** The page lists infection around or behind the eye as a cause. The Cellulitis page says cellulitis in the eye is very serious. The signs used are AI judgement. | "Swollen eyelid that is red, hot, painful, tender or blistered" OR "Hard or painful to move the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |

## Bulging eyes red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_be_vision_urgent`<br>Bulging eyes with blurred or double vision that is not new<br>**Note:** The page lists blurred or double vision as symptoms of bulging eyes and says vision can be affected. Clinical knowledge: changes in sight with thyroid eye problems can mean the nerve to the eye is being squeezed, which needs checking the same day. | "Change in sight or loss of vision" OR "Double vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Bulging eyes: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Bulging eyes with nothing that needs more urgent help: get them checked quickly**
- Outcome: Soon (help within a few days), General practice, Within a few days. *See a GP within a few days*
- Source: [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/)
- **Note:** The page says 'See a GP' (non-urgent) for a bulging eye, and at the top says to get it checked quickly as your vision can be affected. 'Soon' (within a few days) is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Bulging eyes | Do your eyes look like they are bulging or sticking out more than usual? You may see more of the whites of your eyes. | 301919003 | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Bulging has just started | Has the bulging just started, in the last few days? |  | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Floaters or flashes in the eyes | Are you seeing floaters or flashes? Floaters are small dark dots, lines, rings or cobwebs that drift across your sight. Flashes are sudden flashes of light. |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Swollen eyelid that is red, hot, painful, tender or blistered | Is the swollen eyelid hot, painful, tender, blistered or red? Redness may be harder to see on brown or black skin. |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Hard or painful to move the eye | Is it hard to move your eye, or does it not move as far as the other eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |

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

### `advice_bulging_ae`

**What to do:** Call 999 or go to A&E now. Eyes that have started bulging with these symptoms need to be checked in hospital straight away.

**Look out for:**
- Your sight getting worse
- Pain getting worse, or a very high temperature

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/)

### `advice_eye_infection_spreading`

**What to do:** Go to A&E now, or call 999. Your answers suggest an infection that may be spreading behind the eye. This is very serious and needs treatment in hospital.

**Look out for:**
- Your eye bulging or becoming harder to move
- Changes to your sight
- Feeling very unwell, confused, dizzy or faint
- Cold, clammy or pale skin

**Get more help when:**
- Call 999 if you get worse quickly or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/), [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/), [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

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

### `advice_bulging_soon`

**What to do:** See a GP in the next few days. Bulging eyes can be a sign of a problem with your thyroid gland. It can be treated, but get it checked quickly as your sight can be affected.

**Look out for:**
- Any changes to your sight, like wavy lines, flashing, blurring or double vision
- Severe eye pain
- A severe headache or feeling sick

**Get more help when:**
- Call 999 or go to A&E if your sight changes, or you get severe eye pain or a severe headache

**Where to go:** Make an appointment with a GP for the next few days.

**What you can do yourself:**
- Use pillows to keep your head raised when lying down
- Wear sunglasses if your eyes are sensitive to bright light
- If you wear contact lenses, take them out and wear glasses to rest your eyes
- Do not smoke

Source: [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_be_new_with_vision`: Including double vision is AI judgement: it is a change in sight.
- `rf_be_infection`: The page lists infection around or behind the eye as a cause. The Cellulitis page says cellulitis in the eye is very serious. The signs used are AI judgement.
- `rf_be_vision_urgent`: The page lists blurred or double vision as symptoms of bulging eyes and says vision can be affected. Clinical knowledge: changes in sight with thyroid eye problems can mean the nerve to the eye is being squeezed, which needs checking the same day.
- `bulging_eyes default outcome`: The page says 'See a GP' (non-urgent) for a bulging eye, and at the top says to get it checked quickly as your vision can be affected. 'Soon' (within a few days) is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A growth, swelling or bleeding behind the eye |  | rare | Only 1 eye bulging: strongly supports; Bulging has just started: supports; Double vision: supports; Eye pain: supports; Change in sight or loss of vision: supports |
| Infection behind the eye (orbital cellulitis) | 194005002 | very rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Hard or painful to move the eye: strongly supports; Swollen eyelid: strongly supports; Bulging eyes: supports; Eye hurts more when moving it: supports; Very high temperature, or feels hot, cold or shivery: supports; Change in sight or loss of vision: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |
| Thyroid eye problems (swelling behind the eyes linked to a thyroid condition) | 276177000 | rare | Has a thyroid problem, such as an overactive thyroid: strongly supports; Bulging eyes: strongly supports; Both eyes affected: supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Double vision: supports; Swollen eyelid: supports; Smokes, or has smoked in the past: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
