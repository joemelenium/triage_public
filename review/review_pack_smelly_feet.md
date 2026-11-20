# Review pack: Smelly feet

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
| [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/) | 2026-11-19 |  | Page last reviewed: 16 July 2025 |
| [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/) | 2026-11-19 |  | Page last reviewed: 29 April 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
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

## Smelly feet red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sf_foot_infection`<br>Smelly feet with a foot or leg that is painful, hot and swollen<br>**Note:** The Athlete's foot page says see a GP if your foot or leg is hot, painful and red, as this could be a more serious infection. The Cellulitis page says urgent help. | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_sf_wound_pus`<br>Smelly feet with pus or fluid leaking from a sore or wound on the foot<br>**Note:** AI judgement: a smelly foot with pus can be an infected sore or ulcer, especially with diabetes. | "Pus or fluid leaking" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Smelly feet: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sf_gp`<br>Smelly feet not better after self-care, or affecting daily life | "Not better after treating it yourself, or keeps coming back" OR "Affecting daily life, mood or self-esteem" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/) | |
| `or_sf_diabetes_athletes_foot`<br>Athlete's foot in someone with diabetes or a weakened immune system | "Weakened immune system" AND "Itchy, white or flaky skin between the toes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/) | |

## Default outcome

Used when no rule fires.

- **Smelly feet you can treat yourself, and a pharmacist can help**
- Outcome: Self-manageable, Self-care, No appointment needed. *You can usually treat smelly feet yourself*
- Source: [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Smelly feet | Do your feet smell? |  | [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Pus or fluid leaking | Is pus or fluid leaking from it? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Not better after treating it yourself, or keeps coming back | Has it not got better after treating it yourself, or does it keep coming back? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Affecting daily life, mood or self-esteem | Is it affecting your daily life, your mood or how you feel about yourself? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Itchy, white or flaky skin between the toes | Do you have itchy, white, flaky or cracked skin between your toes? | 6020002 | [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/) | |

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

### `advice_smelly_feet_gp`

**What to do:** See a GP about your smelly feet. The source gives no fixed time. They can check for a fungal infection or heavy sweating that needs treatment.

**Look out for:**
- Your foot or leg becoming hot, painful, swollen and red
- A sore or cut on your foot that is not healing, especially if you have diabetes

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your foot becomes hot, painful and swollen

**Where to go:** Book an appointment with your GP surgery, or a podiatrist.

**What you can do yourself:**
- Wash your feet at least once a day and dry between your toes
- Do not wear the same socks or shoes 2 days in a row

Source: [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/)

### `advice_smelly_feet_self_care`

**What to do:** You can usually treat smelly feet yourself by keeping them clean and dry. A pharmacist can suggest antibacterial soaps, foot powders or treatment for athlete's foot.

**Look out for:**
- Smelly feet that do not get better after treating them yourself
- Itchy, flaky skin between your toes that does not clear up
- Your foot becoming hot, painful and swollen

**Get more help when:**
- See a GP if your feet do not get better or it affects your daily life
- Ask for an urgent GP appointment or call 111 if your foot becomes hot, painful and swollen

**Where to go:** Treat it yourself at home. A pharmacy can help.

**What you can do yourself:**
- Wash your feet at least once a day, and dry between your toes
- Wear cotton socks, and let shoes dry out before wearing them again
- Do not wear the same socks or shoes 2 days in a row

Source: [Smelly feet](https://www.nhs.uk/symptoms/smelly-feet/), [Athlete's foot](https://www.nhs.uk/conditions/athletes-foot/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sf_foot_infection`: The Athlete's foot page says see a GP if your foot or leg is hot, painful and red, as this could be a more serious infection. The Cellulitis page says urgent help.
- `rf_sf_wound_pus`: AI judgement: a smelly foot with pus can be an infected sore or ulcer, especially with diabetes.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Fungal skin infection (such as ringworm or athlete's foot) | 47382004 | common | Itchy, dry, ring-shaped patch: strongly supports; Itchy, white or flaky skin between the toes: strongly supports; Itchy, flaky or scaly scalp: supports; Round or oval bald patches: supports; Rash is itchy: supports |
| Hyperhidrosis (sweating more than the body needs to, with no other cause) | 312230002 | uncommon | Sweating mainly in the armpits, hands, feet or face: strongly supports; Sweating too much for at least 6 months: supports; Sweating too much runs in the family: supports; Feet sweat a lot: supports |
| Smell from sweat and bacteria on the skin |  | very common | Smell is worse after sweating, exercise or hot weather: strongly supports; Feet sweat a lot: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
