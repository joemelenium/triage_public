# Review pack: Metallic taste

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
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
| [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | 2026-11-19 |  | Page last reviewed: 20 April 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | 2026-11-19 |  | Page last reviewed: 05 June 2025 |

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

## Metallic taste red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_mt_allergic_swelling`<br>Lips, mouth, tongue or throat suddenly swollen | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_mt_throat_tight`<br>A metallic taste with the throat feeling tight or closed up<br>**Note:** Clinical knowledge: a sudden metallic taste can be an early sign of a severe allergic reaction. | "Throat feels tight" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |

## Metallic taste: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_mt_lasting`<br>A metallic taste that does not go away, or has no obvious cause | "Metallic taste that does not go away, with no clear cause" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/) | |
| `or_mt_gums`<br>A metallic taste with painful, swollen or bleeding gums | "Gums painful, swollen or bleeding" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |

## Default outcome

Used when no rule fires.

- **A metallic taste with nothing that needs more help: it often goes away by itself**
- Outcome: Self-manageable, Self-care, No appointment needed. *A metallic taste is not usually serious and will sometimes go away by itself*
- Source: [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Metallic taste in the mouth | Do you have a metallic taste in your mouth? | 11193009 | [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Metallic taste that does not go away, with no clear cause | Has the metallic taste not gone away, with no clear cause? |  | [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/) | |
| Gums painful, swollen or bleeding | Are your gums painful, swollen or red, or do they bleed when you brush your teeth? |  | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |

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

### `advice_anaphylaxis_999`

**What to do:** Call 999 now and say you think it is anaphylaxis, a severe allergic reaction. Use an adrenaline auto-injector (such as an EpiPen) straight away if you have one.

**Look out for:**
- Swelling of the lips, mouth, tongue or throat
- Struggling to breathe, or very wheezy
- Skin, tongue or lips turning blue, grey or pale
- Feeling faint, very confused or drowsy

**Get more help when:**
- If you are no better after 5 minutes, use a second auto-injector if you have one
- Call 999 again if the person gets worse or stops responding

**Where to go:** Call 999 for an ambulance. Do not drive to A&E. Stay with the person until help arrives.

**What you can do yourself:**
- Lie down. You can raise your legs. If you are struggling to breathe, sit up slowly.
- If you are pregnant, lie on your left side
- If you were stung by an insect, try to remove the sting if it is still in the skin
- Do not stand or walk at any time, even if you feel better

Source: [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/)

### `advice_metallic_taste_gp`

**What to do:** See a GP. They can look for a cause. Do not stop a prescribed medicine without getting advice first.

**Look out for:**
- Lips, tongue or throat suddenly swelling, or finding it hard to breathe
- Sore or bleeding gums

**Get more help when:**
- Call 999 if your lips, tongue or throat suddenly swell or you find it hard to breathe
- See a dentist for sore or bleeding gums

**Where to go:** Make an appointment with a GP. A pharmacist can advise if you think a medicine is the cause.

Source: [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/)

### `advice_bad_breath_dentist`

**What to do:** See a dentist. Bad breath and sore or bleeding gums are often caused by gum problems or tooth decay, which a dentist can treat.

**Look out for:**
- Very sore and swollen gums, or teeth becoming loose
- A swollen face or jaw, or a throbbing toothache

**Get more help when:**
- Ask for an urgent dentist appointment if you get any of the signs above
- Go to A&E if swelling spreads to your eye or neck, or you find it hard to breathe or swallow

**Where to go:** Make an appointment with a dentist. If you do not have one, find a dentist near you or call 111.

**What you can do yourself:**
- Brush your teeth and gums twice a day for 2 minutes with fluoride toothpaste
- Clean between your teeth with floss or small brushes once a day
- Clean your tongue once a day with a tongue scraper
- Do not smoke

Source: [Bad breath](https://www.nhs.uk/symptoms/bad-breath/), [Gum disease](https://www.nhs.uk/conditions/gum-disease/)

### `advice_metallic_taste_self_care`

**What to do:** A metallic taste is not usually serious. It will sometimes go away by itself, for example after a cold clears up or during pregnancy.

**Look out for:**
- A metallic taste that does not go away, or has no obvious cause
- Sore or bleeding gums
- Lips, tongue or throat suddenly swelling

**Get more help when:**
- See a GP if the taste does not go away or has no obvious cause
- Call 999 if your lips, tongue or throat suddenly swell or you find it hard to breathe

**Where to go:** You do not need an appointment now. Speak to a pharmacist if you think a medicine is causing it.

**What you can do yourself:**
- Brush your teeth and gums twice a day and floss, and have regular dental check-ups
- Do not stop taking a prescribed medicine without advice

Source: [Metallic taste](https://www.nhs.uk/symptoms/metallic-taste/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_mt_throat_tight`: Clinical knowledge: a sudden metallic taste can be an early sign of a severe allergic reaction.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Common cold | 82272006 | very common | Blocked or runny nose: strongly supports; Hoarse voice: supports; Dry cough: supports; Phlegm dripping down the back of the throat from the nose: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Gum infection, with sore, swollen or bleeding gums | 2556008 | common | Gums painful, swollen or bleeding: strongly supports; Bad breath: supports; Bad taste in the mouth: supports; Gums very sore and swollen, or teeth loose or falling out: supports; Metallic taste in the mouth: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
