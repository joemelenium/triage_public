# Review pack: Hives (a raised, itchy rash)

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
| [Hives](https://www.nhs.uk/conditions/hives/) | 2026-11-19 |  | Page last reviewed: 26 April 2024 |
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Angioedema](https://www.nhs.uk/conditions/angioedema/) | 2026-11-19 |  | Page last reviewed: 25 August 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
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

## Hives (a raised, itchy rash) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hv_swelling_or_tight_throat`<br>Hives with lips, mouth, tongue or throat suddenly swollen, the throat feeling tight, or struggling to swallow | "Lips, mouth, tongue or throat suddenly swollen" OR "Throat feels tight" OR "Unable to swallow" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_breathing`<br>Hives with breathing very fast, or struggling to breathe | "Difficulty breathing" OR "Breathing very fast" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_child_floppy`<br>A child with hives who is limp, floppy or not responding as usual | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_confused_or_drowsy`<br>Feeling very confused or drowsy, which can be a serious allergic reaction<br>**Note:** The page says call 999 if you suddenly become very confused, drowsy or dizzy. Confusion is also checked for everyone, but that check gives A&E, not an ambulance. | "Suddenly confused" OR "So drowsy they are hard to wake or cannot stay awake" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_dizzy`<br>Hives with feeling suddenly dizzy or light-headed<br>**Note:** The Hives page says call 999 if you suddenly become very confused, drowsy or dizzy. The question asks about feeling light-headed, which is milder, so the rule is soft. Sudden confusion is checked for everyone. | "Feels light-headed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Hives](https://www.nhs.uk/conditions/hives/) | |

## Hives (a raised, itchy rash) red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hv_swelling_under_skin`<br>Hives with swelling under the skin, such as the eyelids, hands, feet or genitals (possible angioedema) | "Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_not_better`<br>Hives not better after 2 days, spreading, or keeps coming back<br>**Note:** The Hives page labels this box 'non-urgent advice' but says to ask for an urgent GP appointment or get help from 111. The urgent wording is used, marked soft because of the label. | "Hives not getting better after 2 days" OR "Rash spreading" OR "Hives keeps coming back" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_temperature_unwell`<br>Hives with a high temperature and feeling unwell | "Very high temperature, or feels hot, cold or shivery" AND "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hives](https://www.nhs.uk/conditions/hives/) | |
| `rf_hv_after_trigger`<br>Hives that came on soon after a food, medicine or insect sting, with no signs of a severe reaction<br>**Note:** AI judgement: a reaction to a new trigger can get worse over the next hours, and the person may need advice on avoiding it. Soft, so a mild reaction that looks like ordinary hives can be lowered. | "Started soon after a food, medicine or insect sting" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | **AI judgement, needs clinical review** | |

## Hives (a raised, itchy rash): other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_hv_worried_child`<br>Worried about a child's hives | "Under 16 years old" AND "Worried about symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hives](https://www.nhs.uk/conditions/hives/) | |

## Default outcome

Used when no rule fires.

- **Hives with nothing that needs more help: a pharmacist can advise on antihistamines**
- Outcome: Routine (help needed, timing not critical), Community pharmacy, No fixed time given in the source. *Speak to a pharmacist. Hives usually get better within a few days.*
- Source: [Hives](https://www.nhs.uk/conditions/hives/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Raised, itchy or swollen rash (hives) | Do you have a raised, itchy or swollen rash? | 126485001 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals | Has part of your body suddenly become swollen, such as your eyelids, hands, feet or genitals? |  | [Angioedema](https://www.nhs.uk/conditions/angioedema/) | |
| Hives not getting better after 2 days | Has the raised, itchy rash not got better after 2 days? |  | [Hives](https://www.nhs.uk/conditions/hives/) | |
| Rash spreading | Is the rash spreading? |  | [Hives](https://www.nhs.uk/conditions/hives/) | |
| Hives keeps coming back | Does the raised, itchy rash keep coming back? |  | [Hives](https://www.nhs.uk/conditions/hives/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Started soon after a food, medicine or insect sting | Did this start soon after eating a food, taking a medicine or being stung by an insect? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
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

### `advice_hives_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. The hives or swelling need checking, and you may need medicine such as antihistamines or steroid tablets.

**Look out for:**
- Swelling of the lips, mouth, tongue or throat
- Struggling to breathe, or very wheezy
- Feeling suddenly very confused, drowsy or dizzy

**Get more help when:**
- Call 999 straight away if you get any of these signs. Use an adrenaline auto-injector if you have one.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Try to work out what set it off, such as a food, medicine, plant or heat, so you can avoid it
- Do not scratch, and wear loose clothes

Source: [Hives](https://www.nhs.uk/conditions/hives/), [Angioedema](https://www.nhs.uk/conditions/angioedema/)

### `advice_hives_pharmacy`

**What to do:** Speak to a pharmacist about antihistamine treatment. Hives usually get better within a few days. Tell the pharmacist if you have a long-term condition.

**Look out for:**
- Hives not getting better after 2 days, spreading, or coming back
- Swelling under the skin, such as the eyelids, hands or feet
- A high temperature with feeling unwell

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if any of these happen
- Call 999 if your lips, mouth, throat or tongue suddenly swell, or you struggle to breathe

**Where to go:** Go to a pharmacy. You do not need an appointment.

**What you can do yourself:**
- Try to find out what sets your hives off, so you can avoid it
- Keep cool and wear loose clothing

Source: [Hives](https://www.nhs.uk/conditions/hives/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hv_confused_or_drowsy`: The page says call 999 if you suddenly become very confused, drowsy or dizzy. Confusion is also checked for everyone, but that check gives A&E, not an ambulance.
- `rf_hv_dizzy`: The Hives page says call 999 if you suddenly become very confused, drowsy or dizzy. The question asks about feeling light-headed, which is milder, so the rule is soft. Sudden confusion is checked for everyone.
- `rf_hv_not_better`: The Hives page labels this box 'non-urgent advice' but says to ask for an urgent GP appointment or get help from 111. The urgent wording is used, marked soft because of the label.
- `rf_hv_after_trigger`: AI judgement: a reaction to a new trigger can get worse over the next hours, and the person may need advice on avoiding it. Soft, so a mild reaction that looks like ordinary hives can be lowered.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Angioedema (sudden swelling under the skin) | 41291007 | uncommon | Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals: strongly supports; Lips, mouth, tongue or throat suddenly swollen: supports; Started soon after a food, medicine or insect sting: strongly supports; Started a new medicine or changed a dose in the last few weeks: supports; Raised, itchy or swollen rash (hives): supports; Swelling is severe, painful or came on suddenly: supports; Has eczema, hay fever or a food allergy: supports |
| Hives (a raised, itchy rash, often from an allergy or a virus) | 402408009 | uncommon | Raised, itchy or swollen rash (hives): strongly supports; Raised patches move around and each fades within a day: strongly supports; Rash is itchy: supports; Started soon after a food, medicine or insect sting: supports; Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals: supports |
| Rash caused by a medicine | 28926001 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Rash is itchy: supports; Rash spreading: supports; Raised, itchy or swollen rash (hives): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
