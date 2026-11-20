# Review pack: Itchy skin

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
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Stevens-Johnson syndrome](https://www.nhs.uk/conditions/stevens-johnson-syndrome/) | 2026-11-19 |  | Page last reviewed: 04 March 2026 |
| [Jaundice](https://www.nhs.uk/conditions/jaundice/) | 2026-11-19 |  | Page last reviewed: 22 January 2024 |
| [Itching and intrahepatic cholestasis of pregnancy](https://www.nhs.uk/pregnancy/complications/itching-and-intrahepatic-cholestasis/) | 2026-11-19 |  | Page last reviewed: 24 February 2026 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | 2026-11-19 |  | Page last reviewed: 6 September 2024 |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [Scabies](https://www.nhs.uk/conditions/scabies/) | 2026-11-19 |  | Page last reviewed: 21 November 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Rashes in babies and children](https://www.nhs.uk/symptoms/rashes-babies-and-children/) | 2026-11-19 |  | Page last reviewed: 03 October 2024 |
| [Lumps](https://www.nhs.uk/symptoms/lumps/) | 2026-11-19 |  | Page last reviewed: 05 February 2024 |
| [Angioedema](https://www.nhs.uk/conditions/angioedema/) | 2026-11-19 |  | Page last reviewed: 25 August 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Hepatitis](https://www.nhs.uk/conditions/hepatitis/) | 2026-11-19 |  | Page last reviewed: 31 December 2025 |
| [Pancreatic cancer: symptoms](https://www.nhs.uk/conditions/pancreatic-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 9 June 2023 |
| [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/) | 2026-11-19 |  | Page last reviewed: 04 August 2025 |

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

## Itchy skin red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_it_allergic_swelling`<br>Itching with sudden swelling of the lips, mouth, tongue or throat, or the throat feeling tight | "Lips, mouth, tongue or throat suddenly swollen" OR "Throat feels tight" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_it_non_fading_rash`<br>Itching with a rash that does not fade when a glass is pressed on it<br>**Note:** Same as the rash rule. The rash entry symptom, brought in by the rash, holds the firm urgent floor. | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_it_skin_peeling`<br>Itchy or painful skin that is blistering or peeling over a large area | "Skin blistering or peeling over a large area" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Stevens-Johnson syndrome](https://www.nhs.uk/conditions/stevens-johnson-syndrome/) | |

## Itchy skin red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_it_jaundice`<br>Itching with yellow skin or yellow whites of the eyes | "Yellow skin or yellow whites of the eyes (jaundice)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| `rf_it_pregnancy_cholestasis`<br>Pregnant with itchy palms or soles, very itchy skin, or itching worse at night (possible cholestasis of pregnancy) | "Pregnant, or gave birth in the last 6 weeks" AND ("Itchy palms or soles in pregnancy" OR "Severe itching, for example keeping you awake" OR "Itching worse at night") | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit now. If you cannot contact them, call 111.* | [Itching and intrahepatic cholestasis of pregnancy](https://www.nhs.uk/pregnancy/complications/itching-and-intrahepatic-cholestasis/) | |
| `rf_it_skin_infection`<br>Itchy skin that has become painful, hot and swollen | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_it_eczema_infected`<br>Eczema that is leaking, crusty, painful or warm, or suddenly worse and painful with clusters of blisters | "Diagnosed with eczema" AND ("Eczema weeping, crusty, painful or warm, or with spots of pus" OR "Eczema suddenly much worse and painful, with clusters of blisters or open sores") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | |
| `rf_it_eczema_high_temperature`<br>Eczema with a high temperature or feeling generally unwell | "Diagnosed with eczema" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | |

## Itchy skin: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_it_gp`<br>Itching that affects daily life, is not better with self-care, is all over the body, or is severe | "Affecting daily life, mood or self-esteem" OR "Not better after treating it yourself, or keeps coming back" OR "Itching all over the body, without a rash" OR "Severe itching, for example keeping you awake" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| `or_it_pregnancy`<br>Itchy skin during pregnancy | "Pregnant, or gave birth in the last 6 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or midwife. The source gives no fixed time.* | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| `or_it_worried_rash_or_lump`<br>Itching caused by a new rash, lump or swelling that you are worried about | "Worried about symptoms" AND ("Rash or spots on the skin" OR "Lump or growth on or under the skin" OR "Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals") | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |

## Default outcome

Used when no rule fires.

- **Itchy skin with nothing that needs more help: treat it yourself, and a pharmacist can advise**
- Outcome: Self-manageable, Self-care, No appointment needed. *You can often treat itchy skin yourself. It usually goes away after a few weeks.*
- Source: [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Itchy skin | Is your skin itchy? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Skin blistering or peeling over a large area | Is the skin blistering or peeling over a large area? Or does it come away easily? |  | [Stevens-Johnson syndrome](https://www.nhs.uk/conditions/stevens-johnson-syndrome/) | |
| Yellow skin or yellow whites of the eyes (jaundice) | Have your skin or the whites of your eyes turned yellow? | 18165001 | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Itchy palms or soles in pregnancy | Are the palms of your hands or the soles of your feet itchy? |  | [Itching and intrahepatic cholestasis of pregnancy](https://www.nhs.uk/pregnancy/complications/itching-and-intrahepatic-cholestasis/) | |
| Severe itching, for example keeping you awake | Is the itching severe? For example, does it keep you awake at night? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Itching worse at night | Is the itching worse at night? |  | [Scabies](https://www.nhs.uk/conditions/scabies/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Diagnosed with eczema | Has a doctor told you that you have eczema? |  | [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | |
| Eczema weeping, crusty, painful or warm, or with spots of pus | Is your eczema leaking fluid, crusty, painful, swollen or warm? Or does it have spots filled with pus? |  | [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | |
| Eczema suddenly much worse and painful, with clusters of blisters or open sores | Has your eczema suddenly got much worse and painful? Are there groups of small blisters or open sores? |  | [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Affecting daily life, mood or self-esteem | Is it affecting your daily life, your mood or how you feel about yourself? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Not better after treating it yourself, or keeps coming back | Has it not got better after treating it yourself, or does it keep coming back? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Itching all over the body, without a rash | Are you itchy all over your body, without a rash? | 418290006 | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Rash or spots on the skin | Do you have a rash or spots on your skin? | 271807003 | [Rashes in babies and children](https://www.nhs.uk/symptoms/rashes-babies-and-children/) | |
| Lump or growth on or under the skin | Do you have a lump, bump or growth on or under your skin? |  | [Lumps](https://www.nhs.uk/symptoms/lumps/) | |
| Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals | Has part of your body suddenly become swollen, such as your eyelids, hands, feet or genitals? |  | [Angioedema](https://www.nhs.uk/conditions/angioedema/) | |

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

### `advice_rash_non_fading_emergency`

**What to do:** Call 999 or go to A&E now. A rash with these signs can mean a serious infection, such as meningitis (an infection of the layers around the brain) or sepsis (a life-threatening reaction to an infection).

**Look out for:**
- A rash that does not fade when you press a glass against it. On brown or black skin, check paler areas such as the palms, soles, inside the eyelids or the roof of the mouth.
- Being very sleepy, hard to wake, confused, or floppy
- Skin, lips or tongue that look pale, blue, grey or blotchy

**Get more help when:**
- Call 999 if the person gets worse while you wait, or you cannot get to A&E safely
- Trust your instincts. Get help straight away if you think something is seriously wrong.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines the person takes.

**What you can do yourself:**
- Do not wait for a rash to appear if the person seems very unwell

Source: [Meningitis](https://www.nhs.uk/conditions/meningitis/), [Rashes in babies and children](https://www.nhs.uk/symptoms/rashes-babies-and-children/)

### `advice_skin_reaction_emergency`

**What to do:** Call 999 or go to A&E now. A rash with blisters, peeling skin, or sores in the mouth or eyes can be a serious reaction to a medicine or an infection. It needs treatment in hospital.

**Look out for:**
- Skin that blisters, peels or comes away easily
- Sore, swollen mouth, lips, eyes or genitals
- Wheezing, a tight chest or throat, or trouble breathing or talking

**Get more help when:**
- Call 999 if breathing gets harder or the person gets worse

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Bring any medicines you take, including any you started recently.

**What you can do yourself:**
- Do not take any more doses of a new medicine until a doctor has checked you

Source: [Stevens-Johnson syndrome](https://www.nhs.uk/conditions/stevens-johnson-syndrome/)

### `advice_jaundice_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Yellow skin or yellow whites of the eyes (jaundice) can be a sign of something serious, such as a liver problem, and needs checking today.

**Look out for:**
- Tummy pain, especially under the ribs on the right
- A very high temperature, or feeling hot, cold or shivery
- Being confused or very sleepy

**Get more help when:**
- Call 999 or go to A&E if you get tummy pain, a very high temperature, or become confused

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5.

**What you can do yourself:**
- Do not drink alcohol until you have been checked

Source: [Jaundice](https://www.nhs.uk/conditions/jaundice/), [Hepatitis](https://www.nhs.uk/conditions/hepatitis/), [Pancreatic cancer: symptoms](https://www.nhs.uk/conditions/pancreatic-cancer/symptoms/), [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/)

### `advice_itch_pregnancy_urgent`

**What to do:** Call your maternity unit now. If you cannot contact them, call 111. Very itchy skin in pregnancy can be a liver problem called ICP (intrahepatic cholestasis of pregnancy). So can itchy palms or soles, or itching that is worse at night. It needs urgent treatment.

**Look out for:**
- Your skin or the whites of your eyes turning yellow
- Dark pee or pale poo
- Your baby moving less than usual

**Get more help when:**
- Call your maternity unit straight away if your baby is moving less than usual

**Where to go:** Call your maternity unit if you have the number. If not, call 111.

**What you can do yourself:**
- Have cool or warm (not hot) baths or showers
- Use an unperfumed moisturiser, and wear loose cotton clothing

Source: [Itching and intrahepatic cholestasis of pregnancy](https://www.nhs.uk/pregnancy/complications/itching-and-intrahepatic-cholestasis/)

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

### `advice_eczema_infected_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Your eczema may be infected. Or it may be a more serious problem called eczema herpeticum. You may need medicine to treat it.

**Look out for:**
- Clusters of small blisters or open sores that spread quickly
- A high temperature, or feeling generally unwell
- Sores near the eyes

**Get more help when:**
- Call 999 or go to A&E if they get very unwell, very sleepy or confused

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5.

**What you can do yourself:**
- Do not scratch, and keep nails short
- Do not share towels or creams. Use a spoon or pump to take cream out of a pot.

Source: [Atopic eczema](https://www.nhs.uk/conditions/atopic-eczema/)

### `advice_itchy_skin_gp`

**What to do:** See a GP about your itchy skin. The source gives no fixed time. They will look at your skin, and may arrange a blood test to find the cause.

**Look out for:**
- A rash that spreads or becomes painful, hot and swollen
- Your skin or the whites of your eyes turning yellow
- Losing weight without trying, or night sweats

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your skin or eyes turn yellow
- Call 999 if your lips, mouth or throat suddenly swell

**Where to go:** Book an appointment with your GP surgery. A pharmacist can suggest treatments in the meantime.

**What you can do yourself:**
- Pat or tap your skin instead of scratching it
- Put on a moisturiser with no perfume often. Have cool or warm baths or showers, not hot ones.
- Wear loose cotton or silk clothing

Source: [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/)

### `advice_itchy_skin_self_care`

**What to do:** You can usually treat itchy skin yourself, and it often goes away after a few weeks. A pharmacist can suggest products, such as antihistamines or cooling creams.

**Look out for:**
- Itching that affects your daily life, is severe, or is all over your body
- Itching that does not get better with self-care, or keeps coming back
- A new rash, lump or swelling you are worried about

**Get more help when:**
- See a GP if any of these happen, or you are pregnant
- Ask for an urgent GP appointment or call 111 if your skin or eyes turn yellow

**Where to go:** Treat it yourself at home. A pharmacy can help. See a GP if it does not get better.

**What you can do yourself:**
- Pat or tap your skin instead of scratching it, and keep your nails short
- Hold something cool on your skin, like a damp towel
- Use an unperfumed moisturiser regularly
- Do not wear tight clothes or wool, and do not use perfumed soaps

Source: [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_it_non_fading_rash`: Same as the rash rule. The rash entry symptom, brought in by the rash, holds the firm urgent floor.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Shingles (an infection that causes a painful rash on one side of the body) | 4740000 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Chest pain is there now: supports; Chest pain is sharp or stabbing: supports; Pain in the upper back: supports; Blisters or fluid-filled spots: supports; Shingles rash on or near the eye or nose, or changes to vision: supports; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Eczema (a common skin condition that makes skin itchy, dry and cracked) | 24079001 | common | Dry, cracked, scaly skin: strongly supports; Rash is itchy: strongly supports; Rash in the skin creases (inside elbows, behind knees, neck), or on a baby's face: supports; Rash comes and goes, with flare-ups: supports; Has eczema, hay fever or a food allergy: supports |
| Chickenpox (itchy spots that turn into blisters) | 38907003 | rare | Small itchy spots that turn into blisters, then scabs: strongly supports; Blisters or fluid-filled spots: strongly supports; Rash is itchy: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Close contact with someone who has chickenpox or shingles: supports; Aching body: supports |
| A liver problem in pregnancy that causes itching (ICP) | 235888006 | very rare | Itchy palms or soles in pregnancy: strongly supports; Itching worse at night: supports; Itching all over the body, without a rash: supports; Pale poo and dark pee: supports; Severe itching, for example keeping you awake: supports |
| Contact dermatitis (a reaction to something on the skin) | 40275004 | common | Rash where the skin touched something, such as a soap, metal, plant or chemical: strongly supports; Rash is itchy: supports; Dry, cracked, scaly skin: supports; Blisters or fluid-filled spots: supports |
| Dry skin |  | common | Dry skin: strongly supports; Itching all over the body, without a rash: supports |
| Eczema herpeticum (eczema infected with the cold sore virus) | 186535001 | very rare | Eczema suddenly much worse and painful, with clusters of blisters or open sores: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Blisters or fluid-filled spots: supports; Rash is sore or painful: supports |
| Fungal skin infection (such as ringworm or athlete's foot) | 47382004 | common | Itchy, dry, ring-shaped patch: strongly supports; Itchy, white or flaky skin between the toes: strongly supports; Itchy, flaky or scaly scalp: supports; Round or oval bald patches: supports; Rash is itchy: supports |
| Head lice |  | uncommon | Lice or eggs (nits) seen in the hair: strongly supports; Itchy, flaky or scaly scalp: strongly supports; Other people at home or in close contact are itchy too: supports |
| Heat rash (prickly heat) | 63951004 | uncommon | Small itchy or prickly spots after being hot or sweaty: strongly supports; Rash is itchy: supports; Feels sweaty: supports |
| Hives (a raised, itchy rash, often from an allergy or a virus) | 402408009 | uncommon | Raised, itchy or swollen rash (hives): strongly supports; Raised patches move around and each fades within a day: strongly supports; Rash is itchy: supports; Started soon after a food, medicine or insect sting: supports; Sudden swelling of part of the body, such as the eyelids, hands, feet or genitals: supports |
| Impetigo (a skin infection that causes crusty sores) | 48277006 | uncommon | Sores or blisters that burst and leave crusty, golden-brown patches: strongly supports; Blisters or fluid-filled spots: supports; Rash is itchy: supports; Rash spreading: supports; Diagnosed with eczema: supports |
| Infected eczema (eczema with a bacterial skin infection) |  | very rare | Eczema weeping, crusty, painful or warm, or with spots of pus: strongly supports; Sores or blisters that burst and leave crusty, golden-brown patches: supports; Pus or fluid leaking: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Itching caused by another health problem |  | rare | Itching all over the body, without a rash: strongly supports; Feels very tired: supports; Losing weight without trying: supports; Night sweats: supports; Pale poo and dark pee: supports |
| Rash caused by a medicine | 28926001 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Rash is itchy: supports; Rash spreading: supports; Raised, itchy or swollen rash (hives): supports |
| Pityriasis rosea (a harmless rash that starts with one large patch) | 77252004 | rare | One larger scaly patch first, then many smaller patches: strongly supports; Rash is itchy: supports; Aching body: supports |
| Psoriasis (flaky patches of skin with silvery scales) | 9014002 | uncommon | Raised patches with silvery-white scales: strongly supports; Patches on the outside of the elbows or knees, or on the scalp: strongly supports; Small dents or pits in the nails: supports; Rash is itchy: supports; Painful or swollen joints: supports |
| Scabies (tiny mites that burrow into the skin and cause very itchy spots) | 128869009 | uncommon | Itching worse at night: strongly supports; Very itchy spots between the fingers or on the wrists, sometimes with tiny lines: strongly supports; Other people at home or in close contact are itchy too: supports; Rash is itchy: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
