# Review pack: Watering eyes

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
| [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | 2026-11-19 |  | Page last reviewed: 12 November 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
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

## Watering eyes red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_we_vision`<br>Watering eyes with any changes to the sight, such as loss of vision | "Change in sight or loss of vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| `rf_we_severe_pain`<br>Watering eyes with severe eye pain | "Severe eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |

## Watering eyes: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_we_daily_life`<br>Eyes keep watering and it is stopping everyday activities | "Watering stops them doing everyday things" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| `or_we_eyelid`<br>Eyelid turning inwards or drooping away from the eye | "Eyelid has changed shape, turns inwards or droops away from the eye" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| `or_we_lump`<br>Lumps or swellings around the eyes not better with treatment from a pharmacist | "Eyelid lump lasting weeks, or not better with pharmacy treatment" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| `or_we_worried`<br>Worried about the watering<br>**Note:** The Watering eyes page has no rule for being worried. The Red eye page says see a GP or optician if you are worried about your eyes; applying it here is AI judgement. | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **Watering eyes with nothing that needs more help: often get better on their own**
- Outcome: Self-manageable, Self-care, No appointment needed. *Watering eyes often get better on their own. A pharmacist can help.*
- Source: [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Watering eyes | Do your eyes keep watering? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Watering stops them doing everyday things | Is the watering stopping you doing everyday things, such as reading or driving? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Eyelid has changed shape, turns inwards or droops away from the eye | Has the shape of your eyelid changed, or is it turning inwards or drooping away from the eye? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
| Eyelid lump lasting weeks, or not better with pharmacy treatment | Has the lump lasted more than a few weeks, or not got better with treatment from a pharmacist? |  | [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/) | |
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

### `advice_watering_gp`

**What to do:** See a GP. They can find out why your eyes keep watering and suggest treatment.

**Look out for:**
- Changes to your sight
- Severe eye pain

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your sight changes or you get severe eye pain

**Where to go:** Make an appointment with a GP. A pharmacist can also give advice.

Source: [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/)

### `advice_watering_self_care`

**What to do:** Watering eyes are common and often get better on their own. A pharmacist can help.

**Look out for:**
- Changes to your sight
- Severe eye pain
- Watering that stops you doing everyday things

**Get more help when:**
- See a GP if the watering stops you doing everyday things, or your eyelid turns in or droops away from the eye
- Ask for an urgent GP appointment or call 111 if your sight changes or you get severe pain

**Where to go:** You do not need an appointment now. A pharmacist can tell you what you can buy to help.

**What you can do yourself:**
- Eyes often water in the cold, wind or smoke. Wear glasses or sunglasses outside.
- Babies often have watering eyes in the first weeks. Gently wipe them with cotton wool soaked in cooled boiled water.

Source: [Watering eyes](https://www.nhs.uk/symptoms/watering-eyes/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `or_we_worried`: The Watering eyes page has no rule for being worried. The Red eye page says see a GP or optician if you are worried about your eyes; applying it here is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Eye allergy, for example from hay fever (allergic conjunctivitis) | 473460002 | uncommon | Itchy eyes: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Both eyes affected: supports; Has eczema, hay fever or a food allergy: supports; Watering eyes: supports; Swollen eyelid: supports; Red or bloodshot eye: supports |
| Arc eye (a burn to the surface of the eye from welding or sunbed light) | 1714005 | very rare | Welding, or a sunbed, without eye protection in the last day: strongly supports; Both eyes affected: strongly supports; Gritty, scratchy or burning feeling in the eye: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports |
| Blepharitis (swollen, itchy, crusty eyelid edges) | 41446000 | uncommon | Itchy, sore or crusty eyelid edges: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Sticky discharge (pus) from the eye: supports; Dry eyes: supports |
| Blocked tear duct (the small tube that drains tears is blocked) | 314022009 | uncommon | Baby with a watery or slightly sticky eye since the first weeks of life: strongly supports; Eye waters all the time, with tears running down the cheek: strongly supports; Sticky discharge (pus) from the eye: supports; Watering stops them doing everyday things: supports |
| Conjunctivitis (a red, sticky eye infection) | 299699004 | uncommon | Sticky discharge (pus) from the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Red or bloodshot eye: strongly supports; Both eyes affected: supports; Itchy eyes: supports; Watering eyes: supports; Cough or runny nose: supports |
| Scratch on the clear front of the eye (corneal abrasion) | 85848002 | rare | Injured eye, or something hit the eye: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Feels like something is in the eye: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Red or bloodshot eye: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| Eyelid turning outwards or inwards, or eyelashes rubbing the eye |  | rare | Eyelid has changed shape, turns inwards or droops away from the eye: strongly supports; Eyelashes grow inwards and rub the eye: strongly supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Eye waters all the time, with tears running down the cheek: supports; Red or bloodshot eye: supports |
| Something on the surface of the eye, such as dust, grit or an eyelash | 450671000124109 | uncommon | Feels like something is in the eye: strongly supports; Watering eyes: supports; Gritty, scratchy or burning feeling in the eye: supports; Red or bloodshot eye: supports |
| Herpes simplex eye infection (an eye infection caused by the cold sore virus) | 9389005 | rare | Has had cold sores or a herpes eye infection: strongly supports; Blisters or a rash on the eyelid or skin around the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: supports; Bright lights hurt the eyes or are bothering you: supports; Watering eyes: supports; Weakened immune system: supports; Swollen eyelid: supports |
| Keratitis or an eye ulcer (a sore on the clear front of the eye), often from contact lenses | 5888003 | rare | Wears contact lenses: strongly supports; Front of the eye looks cloudy, or has a white spot: strongly supports; Eye pain: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Red or bloodshot eye: supports; Watering eyes: supports; Blurred, cloudy or misty sight: supports; Feels like something is in the eye: supports |
| Iritis or uveitis (swelling inside the eye that makes it red, sore and hurt in bright light) | 128473001 | rare | Bright lights hurt the eyes or are bothering you: strongly supports; Redness worst in a ring around the coloured part of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: strongly supports; Deep, boring ache in the eye: supports; Blurred, cloudy or misty sight: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Floaters or flashes in the eyes: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
