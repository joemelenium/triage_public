# Review pack: Tinnitus

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
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | 2026-11-19 |  | Page last reviewed: 04 July 2023 |
| [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | 2026-11-19 |  | Page last reviewed: 30 May 2025 |
| [Vertigo](https://www.nhs.uk/conditions/vertigo/) | 2026-11-19 |  | Page last reviewed: 02 May 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |
| [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/) | 2026-11-19 |  | Page last reviewed: 11 September 2026 |

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

## Tinnitus red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tn_head_injury`<br>Tinnitus after a head injury | "Head injury in the last month" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| `rf_tn_facial_weakness`<br>Tinnitus with weakness in the muscles of the face | "One side of the face weak or drooping" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| `rf_tn_sudden_hearing_loss`<br>Tinnitus with sudden hearing loss<br>**Note:** Source difference: the Tinnitus page says go to A&E or call 999 for tinnitus with sudden hearing loss. The Hearing loss and Labyrinthitis pages say an urgent GP appointment or 111 for sudden hearing loss. The more urgent is used, marked soft; the hearing loss rules keep it at least urgent. | "Hearing loss that came on suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| `rf_tn_vertigo`<br>Tinnitus with a spinning feeling (vertigo)<br>**Note:** Source difference: the Tinnitus page says go to A&E or call 999 for tinnitus with vertigo. The Meniere's disease page says see a GP for attacks of vertigo, tinnitus and hearing loss, and the Labyrinthitis page says see a GP. The more urgent is used, marked soft, so that likely Meniere's or labyrinthitis can lower it. | "Feels like you or the room is spinning (vertigo)" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |

## Tinnitus red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tn_pulsing`<br>Tinnitus that beats in time with the pulse | "Tinnitus that beats in time with the pulse" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |

## Tinnitus: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_tn_regular`<br>Tinnitus regularly or all the time | "Tinnitus regularly or all the time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| `or_tn_worse`<br>Tinnitus that is getting worse | "Tinnitus getting worse" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| `or_tn_bothering`<br>Tinnitus affecting sleep or concentration, or causing anxiety or low mood | "Tinnitus affecting sleep, concentration or mood" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |

## Default outcome

Used when no rule fires.

- **Tinnitus with nothing that needs more help: it is not usually serious and may get better by itself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Tinnitus is not usually a sign of anything serious and may get better by itself*
- Source: [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Tinnitus (ringing or buzzing in the ears) | Can you hear noises like ringing, buzzing or humming that do not come from around you? This is called tinnitus. | 60862001 | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| One side of the face weak or drooping | Is one side of your face weak or drooping? For example, your eye will not close or the corner of your mouth droops. | 95666008 | [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | |
| Hearing loss that came on suddenly | Did the hearing loss come on suddenly, over a few hours or a few days? |  | [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | |
| Feels like you or the room is spinning (vertigo) | Does it feel like you, or everything around you, is spinning? | 399153001 | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| Tinnitus that beats in time with the pulse | Does the noise beat in time with your heartbeat, like a pulse? |  | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Tinnitus regularly or all the time | Do you hear the noise regularly or all the time? |  | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Tinnitus getting worse | Is the noise getting worse? |  | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |
| Tinnitus affecting sleep, concentration or mood | Is the noise affecting your sleep or concentration, or making you feel anxious or low? |  | [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | |

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

### `advice_head_injury_ae`

**What to do:** Go to A&E now. After a head injury, you need to be checked in hospital for bleeding inside the head.

**Look out for:**
- Getting drowsy or hard to wake
- Being sick, or a headache that gets worse
- Confusion, or trouble walking or speaking
- Clear fluid or blood coming from the ear or nose
- Passing out, a seizure (fit), or problems speaking

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself if you have hit your head. Ask someone to take you, or call 999. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/), [Broken nose](https://www.nhs.uk/conditions/broken-nose/), [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

### `advice_tinnitus_ae`

**What to do:** Go to A&E or call 999. Ringing or buzzing in the ears (tinnitus) with sudden hearing loss, weakness in the face or a spinning feeling needs checking straight away.

**Look out for:**
- Signs of a stroke: the face drooping on one side, not being able to lift both arms, or slurred speech
- Feeling very off balance, or being sick

**Get more help when:**
- Call 999 straight away if you see any signs of a stroke

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Tinnitus](https://www.nhs.uk/conditions/tinnitus/), [Meniere's disease](https://www.nhs.uk/conditions/menieres-disease/)

### `advice_tinnitus_urgent`

**What to do:** Ask for an urgent GP appointment. Ringing or whooshing in the ears (tinnitus) that beats in time with your pulse needs checking.

**Look out for:**
- Sudden hearing loss
- Weakness in the face, or a spinning feeling (vertigo)
- A very bad headache, or problems with your eyesight

**Get more help when:**
- Go to A&E or call 999 if you get sudden hearing loss, weakness in your face, or a spinning feeling

**Where to go:** Ask your GP surgery for an urgent appointment. If you cannot get one, call 111 or use 111 online.

Source: [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

### `advice_tinnitus_gp`

**What to do:** See a GP. They will look in your ears for something they can treat, such as an ear infection or earwax, and may check your hearing. Tinnitus means hearing ringing or buzzing that does not come from outside.

**Look out for:**
- A noise that beats in time with your pulse
- Sudden hearing loss, weakness in your face, or a spinning feeling

**Get more help when:**
- Ask for an urgent GP appointment if the noise beats in time with your pulse
- Go to A&E or call 999 for sudden hearing loss, weakness in your face, or a spinning feeling

**Where to go:** Make an appointment with a GP. The Tinnitus UK helpline is free on 0800 018 0527.

**What you can do yourself:**
- Try to relax. Deep breathing or yoga may help.
- Try to improve your sleep, for example with a bedtime routine and less caffeine
- Avoid total silence. Soft music or sounds may help take your mind off the noise.

Source: [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

### `advice_tinnitus_self_care`

**What to do:** Ringing or buzzing in your ears (tinnitus) is not usually a sign of anything serious, and it may get better by itself. There are things you can do to help you cope.

**Look out for:**
- Tinnitus that you hear all the time, or that is getting worse
- Tinnitus that affects your sleep or concentration, or makes you feel anxious or low
- A noise that beats in time with your pulse

**Get more help when:**
- See a GP if you get any of the first two signs above
- Ask for an urgent GP appointment if the noise beats in time with your pulse
- Go to A&E or call 999 for sudden hearing loss, weakness in your face, or a spinning feeling

**Where to go:** You do not need an appointment now. The Tinnitus UK helpline is free on 0800 018 0527.

**What you can do yourself:**
- Try to relax. Deep breathing or yoga may help.
- Try to avoid stress and loud background noise
- Avoid total silence. Soft music or sounds may help take your mind off the noise.
- Do not focus on it. Hobbies and activities may help.

Source: [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_tn_sudden_hearing_loss`: Source difference: the Tinnitus page says go to A&E or call 999 for tinnitus with sudden hearing loss. The Hearing loss and Labyrinthitis pages say an urgent GP appointment or 111 for sudden hearing loss. The more urgent is used, marked soft; the hearing loss rules keep it at least urgent.
- `rf_tn_vertigo`: Source difference: the Tinnitus page says go to A&E or call 999 for tinnitus with vertigo. The Meniere's disease page says see a GP for attacks of vertigo, tinnitus and hearing loss, and the Labyrinthitis page says see a GP. The more urgent is used, marked soft, so that likely Meniere's or labyrinthitis can lower it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Acoustic neuroma (a slow-growing growth on the hearing nerve that is not cancer) | 126949007 | rare | Hearing loss in one ear only: strongly supports; Tinnitus in one ear only: strongly supports; Hearing getting slowly worse over months or years: supports; Feels like you or the room is spinning (vertigo): supports; Tinnitus (ringing or buzzing in the ears): supports; Hearing loss or a change in hearing: supports |
| A blood vessel problem near the ear, causing a noise that beats with the pulse | 232322006 | rare | Tinnitus that beats in time with the pulse: strongly supports; Tinnitus in one ear only: supports; Tinnitus regularly or all the time: supports; Sight changed suddenly: supports |
| Earwax build-up | 18070006 | common | Ear feels blocked or full: strongly supports; Hearing loss in one ear only: supports; Itchy ear, or flaky skin in or around the ear: supports; Hearing loss or a change in hearing: supports; Tinnitus (ringing or buzzing in the ears): supports; Recent swimming, water in the ear, cotton buds or earplugs: supports |
| Hearing loss from getting older or from loud noise over many years |  | common | Hearing getting slowly worse over months or years: strongly supports; Hearing loss or a change in hearing: strongly supports; Around a lot of loud noise over the years: supports; Tinnitus (ringing or buzzing in the ears): supports |
| Labyrinthitis (an ear infection that affects balance) | 23919004 | uncommon | Feels like you or the room is spinning (vertigo): strongly supports; Feels sick or has been sick: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Hearing loss that came on suddenly: supports; Tinnitus (ringing or buzzing in the ears): supports; Hearing loss or a change in hearing: supports; Dizziness there all the time since it started: strongly supports; Being sick: supports; Finding it hard to balance or walk: supports |
| Meniere's (a condition deep in the ear that causes bouts of spinning, hearing loss and ringing) | 13445001 | rare | Symptoms come in attacks lasting minutes to hours: strongly supports; Feels like you or the room is spinning (vertigo): strongly supports; Ear feels blocked or full: supports; Hearing loss or a change in hearing: strongly supports; Tinnitus (ringing or buzzing in the ears): strongly supports; Feels sick or has been sick: supports; Dizziness keeps coming back, or will not go away: strongly supports |
| Perforated eardrum (a hole or tear in the eardrum) | 60442001 | uncommon | Started suddenly after a loud noise, a blow to the ear, flying or diving: strongly supports; Fluid or pus coming out of the ear: supports; Earache: supports; Hearing loss in one ear only: supports; Hearing loss that came on suddenly: supports; Tinnitus (ringing or buzzing in the ears): supports |
| Sudden hearing loss from the inner ear or hearing nerve, which needs treatment quickly | 715239002 | uncommon | Hearing loss that came on suddenly: strongly supports; Hearing loss in one ear only: strongly supports; Tinnitus (ringing or buzzing in the ears): supports; Ear feels blocked or full: supports; Feels like you or the room is spinning (vertigo): supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
