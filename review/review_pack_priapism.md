# Review pack: Priapism (painful erections)

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
| [Sickle cell disease](https://www.nhs.uk/conditions/sickle-cell-disease/) | 2026-11-19 |  | Page last reviewed: 22 September 2026 |
| [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | 2026-11-19 |  | Page last reviewed: 05 December 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
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

## Priapism (painful erections) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pr_sickle_cell`<br>An erection that is painful or will not go away, in someone with sickle cell or another inherited blood condition<br>**Note:** Source difference: the Sickle cell page says call 999 for an erection that is painful or does not go away. The Priapism page says call 999 or go to A&E for a painful erection lasting more than 1 hour with sickle cell. The more urgent is used. Including other inherited blood conditions such as thalassaemia comes from the Priapism page's list of causes; it is AI judgement. | "Has sickle cell or another inherited blood condition" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Sickle cell disease](https://www.nhs.uk/conditions/sickle-cell-disease/) | |
| `rf_pr_over_3_hours`<br>An erection that has lasted more than 3 hours<br>**Note:** The page says more than 3 to 4 hours. The lower figure is used, to be cautious. | "Erection lasting more than 3 hours" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | |
| `rf_pr_painful_over_1_hour`<br>A painful erection that has lasted more than 1 hour<br>**Note:** Clinical knowledge: a painful erection usually means blood is trapped in the penis, which causes damage within hours. The page gives 3 to 4 hours for any erection; earlier help for a painful one is AI judgement. | "The erection is painful" AND "Erection lasting more than 1 hour" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |

## Priapism (painful erections): other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **An erection that will not go away, for less than 3 hours: try things to make it go down, and get help now**
- Outcome: Urgent (help today), Urgent care, Today. *Get help from NHS 111 now. Go to A&E if it lasts 3 hours.*
- Source: **AI judgement, needs clinical review**
- **Note:** The Priapism page gives things to try at home and says go to A&E after 3 to 4 hours. Getting advice from 111 before then is AI judgement.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Erection that will not go away, or is painful | Do you have an erection that will not go away, or that is painful? |  | [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Has sickle cell or another inherited blood condition | Do you have sickle cell, or a blood condition like it that runs in families? For example, thalassaemia. |  | [Sickle cell disease](https://www.nhs.uk/conditions/sickle-cell-disease/) | |
| Erection lasting more than 3 hours | Has the erection lasted more than 3 hours? |  | [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | |
| The erection is painful | Is the erection painful? |  | [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | |
| Erection lasting more than 1 hour | Has the erection lasted more than 1 hour? |  | [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/) | |

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

### `advice_priapism_999`

**What to do:** Call 999 now. With sickle cell, an erection that is painful or will not go away needs treatment in hospital straight away.

**Look out for:**
- Severe pain anywhere, or a sickle cell crisis
- A high temperature
- Difficulty breathing

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. The person you speak to will tell you what to do.

**What you can do yourself:**
- Do not put ice or cold water on your penis. It can make things worse with sickle cell.
- Drink lots of water and try to pee

Source: [Sickle cell disease](https://www.nhs.uk/conditions/sickle-cell-disease/), [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/)

### `advice_priapism_ae`

**What to do:** Call 999 or go to A&E now. An erection that lasts this long needs treatment in hospital as soon as possible to stop permanent damage to your penis.

**Look out for:**
- Pain getting worse
- The penis changing colour

**Get more help when:**
- Call 999 if you cannot get to A&E quickly

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not put ice packs or cold water on your penis
- Do not have sex or masturbate. It will not make the erection go away.

Source: [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/)

### `advice_priapism_urgent`

**What to do:** Get help from NHS 111 now. Try the things below to make the erection go down. If it lasts 3 hours, go to A&E.

**Look out for:**
- The erection lasting 3 hours or more
- The erection becoming very painful

**Get more help when:**
- Call 999 or go to A&E if it lasts more than 3 hours
- If you have sickle cell, call 999 now

**Where to go:** Call 111 or use 111 online now. Go to A&E if it lasts 3 hours.

**What you can do yourself:**
- Try to go for a pee
- Have a warm bath or shower, and drink lots of water
- Go for a gentle walk, or try squats or running on the spot
- Take paracetamol if you need to
- Do not put ice or cold water on your penis, and do not drink alcohol or smoke

Source: [Priapism (painful erections)](https://www.nhs.uk/symptoms/priapism-painful-erections/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_pr_sickle_cell`: Source difference: the Sickle cell page says call 999 for an erection that is painful or does not go away. The Priapism page says call 999 or go to A&E for a painful erection lasting more than 1 hour with sickle cell. The more urgent is used. Including other inherited blood conditions such as thalassaemia comes from the Priapism page's list of causes; it is AI judgement.
- `rf_pr_over_3_hours`: The page says more than 3 to 4 hours. The lower figure is used, to be cautious.
- `rf_pr_painful_over_1_hour`: Clinical knowledge: a painful erection usually means blood is trapped in the penis, which causes damage within hours. The page gives 3 to 4 hours for any erection; earlier help for a painful one is AI judgement.
- `priapism default outcome`: The Priapism page gives things to try at home and says go to A&E after 3 to 4 hours. Getting advice from 111 before then is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Priapism (an erection that will not go away and needs hospital treatment) | 6273006 | uncommon | Erection lasting more than 3 hours: strongly supports; The erection is painful: strongly supports; Erection lasting more than 1 hour: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
