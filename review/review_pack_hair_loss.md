# Review pack: Hair loss

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
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Hair loss](https://www.nhs.uk/symptoms/hair-loss/) | 2026-11-19 |  | Page last reviewed: 24 January 2024 |
| [Ringworm](https://www.nhs.uk/conditions/ringworm/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | 2026-11-18 |  | Page last reviewed: 26 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | 2026-11-19 |  | Page last reviewed: 12 March 2024 |
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

## Hair loss red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hl_scalp_infection`<br>Hair loss with a painful, hot, swollen patch of scalp<br>**Note:** AI reading: a painful, swollen, pus-filled patch on the scalp can be a severe ringworm or skin infection, and the Cellulitis page says urgent help for painful, hot, swollen skin. | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Hair loss: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_hl_worried`<br>Worried about hair loss, or it is affecting your wellbeing | "Worried about symptoms" OR "Affecting daily life, mood or self-esteem" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Hair loss](https://www.nhs.uk/symptoms/hair-loss/) | |
| `or_hl_patches_or_scalp`<br>Bald patches, or an itchy, flaky or scaly scalp (possible alopecia areata or ringworm of the scalp)<br>**Note:** The Ringworm page says see a GP for ringworm on the scalp, which needs prescription treatment. A GP visit for bald patches is AI judgement. | "Round or oval bald patches" OR "Itchy, flaky or scaly scalp" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Ringworm](https://www.nhs.uk/conditions/ringworm/) | |
| `or_hl_anaemia_signs`<br>Hair loss with skin paler than usual for weeks, or very tired (possible lack of iron) | "Skin paler than usual for weeks or longer" OR "Nails curve inwards like a spoon" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |

## Default outcome

Used when no rule fires.

- **Hair loss that is not worrying you: often temporary or part of getting older**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP if you want to find out the cause. The source gives no fixed time.*
- Source: [Hair loss](https://www.nhs.uk/symptoms/hair-loss/)
- **Note:** The Hair loss page says hair loss is not usually anything to worry about, and to see a GP before going to a commercial hair clinic. Not a floor: likely pattern hair loss or shedding after an illness can lower this to self-care.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Hair loss | Are you losing hair, or has your hair become thinner? | 56317004 | [Hair loss](https://www.nhs.uk/symptoms/hair-loss/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Affecting daily life, mood or self-esteem | Is it affecting your daily life, your mood or how you feel about yourself? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Round or oval bald patches | Are there round or oval bald patches, rather than thinning all over? | 68225006 | [Hair loss](https://www.nhs.uk/symptoms/hair-loss/) | |
| Itchy, flaky or scaly scalp | Is your scalp itchy, flaky or scaly? |  | [Ringworm](https://www.nhs.uk/conditions/ringworm/) | |
| Skin paler than usual for weeks or longer | Has your skin been paler than usual for weeks or longer? |  | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |
| Nails curve inwards like a spoon | Do your nails curve inwards, like a spoon? | 66270006 | [Nail problems](https://www.nhs.uk/symptoms/nail-problems/) | |

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

### `advice_skin_infection_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Painful, hot, swollen skin can be a skin infection called cellulitis. Early treatment with antibiotics can stop it becoming more serious.

**Look out for:**
- The redness or swelling spreading
- A very high temperature, or feeling hot, cold or shivery
- A fast heartbeat, fast breathing, or feeling dizzy or faint
- Purple patches on the skin, or cold, clammy, pale skin

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs, or become confused
- Contact your GP if you do not start to feel better 2 to 3 days after starting antibiotics

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Raise the affected area on a pillow or chair to reduce swelling
- Take paracetamol or ibuprofen for the pain
- Drink plenty of fluids

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

### `advice_hair_loss_gp`

**What to do:** See a GP if you are worried about your hair loss, or want to know the cause. The source gives no fixed time. Most hair loss is not a sign of anything serious.

**Look out for:**
- Bald patches, or an itchy, flaky or scaly scalp
- Feeling very tired, or skin paler than usual
- Hair loss affecting your mood or wellbeing

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if a patch of scalp becomes painful, hot and swollen

**Where to go:** Book an appointment with your GP surgery. See a GP before going to a private hair clinic.

**What you can do yourself:**
- Hair loss after an illness or stress usually grows back by itself
- If your hair loss is upsetting you, a GP may be able to help you get counselling or support

Source: [Hair loss](https://www.nhs.uk/symptoms/hair-loss/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hl_scalp_infection`: AI reading: a painful, swollen, pus-filled patch on the scalp can be a severe ringworm or skin infection, and the Cellulitis page says urgent help for painful, hot, swollen skin.
- `or_hl_patches_or_scalp`: The Ringworm page says see a GP for ringworm on the scalp, which needs prescription treatment. A GP visit for bald patches is AI judgement.
- `hair_loss default outcome`: The Hair loss page says hair loss is not usually anything to worry about, and to see a GP before going to a commercial hair clinic. Not a floor: likely pattern hair loss or shedding after an illness can lower this to self-care.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Alopecia areata (bald patches on the head) |  | uncommon | Round or oval bald patches: strongly supports; Small dents or pits in the nails: supports |
| Fungal skin infection (such as ringworm or athlete's foot) | 47382004 | common | Itchy, dry, ring-shaped patch: strongly supports; Itchy, white or flaky skin between the toes: strongly supports; Itchy, flaky or scaly scalp: supports; Round or oval bald patches: supports; Rash is itchy: supports |
| Male or female pattern hair loss | 87872006 | common | Hair thinning slowly on the top of the head or at the temples: strongly supports; Hair loss runs in the family: supports |
| Hair shedding after an illness, stress, having a baby or weight loss |  | common | Lots of hair falling out a few months after an illness, stress, giving birth or losing weight: strongly supports; Pregnant, or gave birth in the last 6 weeks: supports; Losing weight without trying: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
