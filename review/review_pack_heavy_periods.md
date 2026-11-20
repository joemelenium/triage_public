# Review pack: Heavy periods

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
| [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | 2026-11-19 |  | Page last reviewed: 24 November 2025 |
| [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | 2026-11-19 |  | Page last reviewed: 19 September 2024 |
| [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | 2026-11-18 |  | Page last reviewed: 26 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | 2026-11-19 |  | Page last reviewed: 09 August 2024 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | 2026-11-19 |  | Page last reviewed: 13 August 2024 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Anal fissure](https://www.nhs.uk/conditions/anal-fissure/) | 2026-11-19 |  | Page last reviewed: 26 June 2025 |
| [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | 2026-11-19 |  | Page last reviewed: 17 December 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | 2026-11-19 |  | Page last reviewed: 18 November 2024 |

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

## Heavy periods red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hp_heavy_and_faint`<br>Very heavy bleeding with feeling faint, dizzy or light-headed, or passing out<br>**Note:** Clinical knowledge: very heavy bleeding with feeling faint can mean a lot of blood has been lost. | "Heavy bleeding from the vagina" AND ("Feels light-headed" OR "Passed out (fainted)") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_hp_fainted`<br>Heavy periods and passed out (fainted) | "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_hp_pregnant_heavy`<br>Heavy bleeding in someone who is pregnant: possible miscarriage | "Pregnant (a positive test, or told by a midwife or doctor)" AND "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |
| `rf_hp_may_be_pregnant_heavy`<br>Heavy bleeding in someone who could be pregnant<br>**Note:** The Miscarriage page says call 999 for heavy bleeding in pregnancy. Applying it to someone who only could be pregnant is AI judgement. | "Pregnant, or could be pregnant" AND "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |
| `rf_hp_severe_pain_or_shoulder`<br>Heavy bleeding with severe tummy pain, or pain in the tip of the shoulder<br>**Note:** The Pelvic pain page: pelvic pain with heavy bleeding, or pain in the tip of the shoulder, needs 999 or A&E. | "Severe stomach ache" OR "Pain in the tip of the shoulder" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |

## Heavy periods red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hp_may_be_pregnant`<br>Heavy or unusual bleeding in someone who is or could be pregnant<br>**Note:** The Miscarriage page says get urgent help for any bleeding in pregnancy. | "Pregnant, or could be pregnant" OR "Pregnant (a positive test, or told by a midwife or doctor)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |
| `rf_hp_light_headed`<br>Heavy periods with feeling light-headed or dizzy<br>**Note:** Clinical knowledge: feeling light-headed with heavy bleeding can be a sign of losing a lot of blood, or of anaemia. | "Feels light-headed" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_hp_breathless_or_palpitations`<br>Heavy periods with breathlessness or a racing heart: possible anaemia<br>**Note:** Clinical knowledge: these can be signs of severe anaemia from blood loss. The Heavy periods page lists feeling tired or short of breath a lot as part of heavy periods, so soft. | "Short of breath" OR "Heart racing, slow, skipping or fluttering" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_hp_painkillers_not_helping`<br>Heavy periods with severe pain, or pain worse than usual, that painkillers have not helped<br>**Note:** The Period pain page says an urgent GP appointment or 111 for pelvic or period pain that is severe or worse than usual, and painkillers have not helped. Firm, as in the Period pain entry symptom. It was bundled with any pelvic pain in one soft rule. | "Severe pain, or worse than usual, and painkillers have not helped" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |
| `rf_hp_pelvic_pain`<br>Heavy periods with pelvic pain<br>**Note:** Including any pelvic pain is an AI reading of the Period pain page, so soft. | "Pelvic pain (pain low down in the tummy)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |

## Heavy periods: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_hp_affecting_life`<br>Heavy periods that affect daily life, or have lasted for some time | "Heavy periods affect daily life" OR "Heavy periods for some time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | |
| `or_hp_severe_pain_or_changed`<br>Heavy periods with severe period pain, or periods that have changed | "Period pain stops usual daily activities" OR "Periods have changed: irregular, heavier, more painful or stopped" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | |
| `or_hp_other_symptoms`<br>Heavy periods with bleeding between periods or after sex, or pain when peeing, pooing or having sex | "Vaginal bleeding between periods or after sex" OR "Pain, burning or stinging when peeing" OR "Pain when pooing" OR "Pain deep inside during or after sex" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | |

## Default outcome

Used when no rule fires.

- **Heavy periods that are not affecting daily life, with nothing that needs more help**
- Outcome: Self-manageable, Self-care, No appointment needed. *Heavy periods can be normal. See a GP if they affect your life.*
- Source: [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/)
- **Note:** The page says heavy periods may be normal, and to see a GP if they affect your life or have lasted for some time. Likely conditions (for example anaemia or fibroids) can raise this.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Heavy periods | Do you have heavy periods? | 386692008 | [Iron deficiency anaemia](https://www.nhs.uk/conditions/iron-deficiency-anaemia/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Pregnant (a positive test, or told by a midwife or doctor) | Are you pregnant? Answer yes if you have had a positive pregnancy test, or a midwife or doctor has told you. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Pregnant, or could be pregnant | Are you pregnant, or could you be? For example, your period is late, or you have had sex without contraception since your last period. |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Severe stomach ache | Is the pain in your tummy severe? This means it is there all the time and so bad it is hard to think or talk, you cannot sleep, or it is very hard to move. |  | [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | |
| Pain in the tip of the shoulder | Do you have pain in the tip of your shoulder, where your arm meets your shoulder? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heart racing, slow, skipping or fluttering | Does your heart feel like it is racing, going too slowly, skipping a beat or fluttering? | 80313002 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Severe pain, or worse than usual, and painkillers have not helped | Is the pain severe or worse than usual, and have painkillers not helped? |  | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |
| Pelvic pain (pain low down in the tummy) | Do you have pain low down in your tummy, between your hips (your pelvis)? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Heavy periods affect daily life | Are your heavy periods affecting your daily life? For example, you avoid exercise or take time off work. |  | [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | |
| Heavy periods for some time | Have you had heavy periods for several months or more? |  | [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/) | |
| Period pain stops usual daily activities | Does your period pain stop you doing your usual daily activities, such as work or school? |  | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |
| Periods have changed: irregular, heavier, more painful or stopped | Have your periods changed? For example, they have become irregular, heavier or more painful, or they have stopped. |  | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |
| Vaginal bleeding between periods or after sex | Are you bleeding from your vagina between periods or after sex? |  | [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Pain when pooing | Does it hurt when you poo? |  | [Anal fissure](https://www.nhs.uk/conditions/anal-fissure/) | |
| Pain deep inside during or after sex | Do you get pain deep inside during or after sex? | 247419003 | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |

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

### `advice_heavy_bleeding_emergency`

**What to do:** Go to A&E now, or call 999. Heavy bleeding with feeling faint or dizzy can mean you have lost a lot of blood.

**Look out for:**
- Passing out, or feeling very faint
- Lips or skin very pale, blue or grey

**Get more help when:**
- Call 999 if you pass out, or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Lie down while you wait for help

Source: **AI judgement, needs clinical review**

### `advice_pregnancy_999`

**What to do:** Call 999 now. You need treatment straight away.

**Look out for:**
- Passing out, or feeling very faint
- Bleeding getting heavier

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself. Bring your maternity notes if you have them.

**What you can do yourself:**
- Lie down while you wait for help

Source: [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/), [Miscarriage](https://www.nhs.uk/conditions/miscarriage/), [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/)

### `advice_possible_ectopic_emergency`

**What to do:** Call 999 or go to A&E now. These signs could mean an ectopic pregnancy has burst, where a pregnancy growing outside the womb splits open. This needs treatment straight away.

**Look out for:**
- Feeling very dizzy, or passing out
- Looking very pale
- Pain getting worse

**Get more help when:**
- Call 999 for an ambulance if you pass out, feel very faint, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E now. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance.

Source: [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/)

### `advice_pelvic_pain_emergency`

**What to do:** Call 999 or go to A&E now. Pelvic pain with these signs can mean something serious that needs treatment straight away.

**Look out for:**
- Feeling faint, dizzy or light-headed, or passing out
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina
- Pain that gets worse very quickly

**Get more help when:**
- Call 999 if you pass out, feel very faint, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/)

### `advice_possible_ectopic_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment or call NHS 111. Tummy pain or unusual bleeding when you could be pregnant needs checking as soon as possible. It could be an ectopic pregnancy, where a pregnancy grows outside the womb.

**Look out for:**
- A sharp, sudden and very bad pain in your tummy
- Feeling very dizzy or faint, or passing out
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina

**Get more help when:**
- Call 999 or go to A&E straight away if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you are under the care of an early pregnancy unit or maternity unit, you can call them.

**What you can do yourself:**
- Do a pregnancy test if you have not done one, but get help even if it is negative

Source: [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/), [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/)

### `advice_heavy_periods_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment or call NHS 111.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Bleeding that soaks a pad soon after putting it on
- Severe tummy pain, or pain in the tip of your shoulder

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

Source: **AI judgement, needs clinical review**, [Miscarriage](https://www.nhs.uk/conditions/miscarriage/), [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/)

### `advice_period_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Severe pain that painkillers have not helped needs checking.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Pain in the tip of your shoulder
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if the pain becomes very bad, or you feel faint or pass out

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Use a heat pad or hot water bottle on your tummy
- Take paracetamol or ibuprofen as the packet says

Source: [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/)

### `advice_heavy_periods_gp`

**What to do:** See a GP about your heavy periods. There are treatments that can help. A GP may check for a cause, such as fibroids (growths in the womb), and test your blood for a lack of iron.

**Look out for:**
- Feeling tired, short of breath or pale
- Bleeding between periods or after sex
- Severe pain during your periods

**Get more help when:**
- Go to A&E or call 999 if you bleed very heavily and feel faint or dizzy

**Where to go:** Ask your GP surgery for an appointment. The source gives no fixed time.

**What you can do yourself:**
- Keep a diary of your periods: how long they last and how many pads or tampons you use
- Paracetamol or ibuprofen can help with pain

Source: [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/)

### `advice_heavy_periods_self_care`

**What to do:** Heavy periods can be normal for you. Treatment can help if they start to affect your daily life.

**Look out for:**
- Heavy periods that affect your daily life, or go on for months
- Severe pain during your periods
- Bleeding between periods or after sex
- Feeling tired or short of breath a lot

**Get more help when:**
- See a GP if you get any of these
- Go to A&E or call 999 if you bleed very heavily and feel faint or dizzy

**Where to go:** You can look after this yourself for now. See a GP if anything changes.

**What you can do yourself:**
- Keep a diary of your periods, so you notice any change
- Eat foods with plenty of iron, such as green vegetables, beans and meat

Source: [Heavy periods](https://www.nhs.uk/conditions/heavy-periods/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hp_heavy_and_faint`: Clinical knowledge: very heavy bleeding with feeling faint can mean a lot of blood has been lost.
- `rf_hp_may_be_pregnant_heavy`: The Miscarriage page says call 999 for heavy bleeding in pregnancy. Applying it to someone who only could be pregnant is AI judgement.
- `rf_hp_severe_pain_or_shoulder`: The Pelvic pain page: pelvic pain with heavy bleeding, or pain in the tip of the shoulder, needs 999 or A&E.
- `rf_hp_may_be_pregnant`: The Miscarriage page says get urgent help for any bleeding in pregnancy.
- `rf_hp_light_headed`: Clinical knowledge: feeling light-headed with heavy bleeding can be a sign of losing a lot of blood, or of anaemia.
- `rf_hp_breathless_or_palpitations`: Clinical knowledge: these can be signs of severe anaemia from blood loss. The Heavy periods page lists feeling tired or short of breath a lot as part of heavy periods, so soft.
- `rf_hp_painkillers_not_helping`: The Period pain page says an urgent GP appointment or 111 for pelvic or period pain that is severe or worse than usual, and painkillers have not helped. Firm, as in the Period pain entry symptom. It was bundled with any pelvic pain in one soft rule.
- `rf_hp_pelvic_pain`: Including any pelvic pain is an AI reading of the Period pain page, so soft.
- `heavy_periods default outcome`: The page says heavy periods may be normal, and to see a GP if they affect your life or have lasted for some time. Likely conditions (for example anaemia or fibroids) can raise this.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Adenomyosis (tissue like the lining of the womb growing into the wall of the womb) | 784314006 | uncommon | Heavy periods: strongly supports; Period pain: strongly supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Bloated regularly, or it does not go away: supports; Pain deep inside during or after sex: supports; Passing blood clots bigger than a 10p coin: supports |
| Ectopic pregnancy (a pregnancy growing outside the womb) | 34801009 | very rare | Pain low down on one side of the tummy: strongly supports; Pelvic pain (pain low down in the tummy): strongly supports; Vaginal bleeding between periods or after sex: supports; Missed or late period: supports; Stomach pain in pregnancy: supports; Vaginal bleeding in pregnancy: supports; Pregnant, or could be pregnant: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: supports; Pain in the tip of the shoulder: supports; Feels light-headed: supports; Passed out (fainted): supports; Pain when pooing: supports |
| Endometriosis (tissue like the lining of the womb growing in other places) | 129103003 | uncommon | Period pain stops usual daily activities: strongly supports; Tummy or pelvic pain that keeps coming back or does not go away: strongly supports; Period pain: strongly supports; Pain deep inside during or after sex: supports; Pain when pooing: supports; Feels very tired: supports; Struggling to get pregnant: supports; Pelvic pain (pain low down in the tummy): supports |
| Fibroids (non-cancerous growths in or around the womb) | 95315005 | uncommon | Heavy periods: strongly supports; Passing blood clots bigger than a 10p coin: supports; Peeing more often than usual: supports; Bloated regularly, or it does not go away: supports; Pain in the lower back: supports; Pain deep inside during or after sex: supports; Periods last more than 7 days: supports; Period pain: supports |
| Heavy periods with no clear cause |  | very common | Heavy periods for some time: strongly supports; Passing blood clots bigger than a 10p coin: supports; Heavy periods affect daily life: supports |
| Perimenopause or menopause (when periods change and then stop) | 289903006 | uncommon | Hot flushes: strongly supports; Trouble sleeping (insomnia): supports; Feeling low, sad or depressed: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports; Feels very tired: supports; Night sweats: supports; Vaginal dryness: supports; Irregular periods: supports; Periods stopped for 12 months or more (the menopause): supports |
| Miscarriage (loss of a pregnancy before 24 weeks) | 17369002 | very rare | Pink, grey or white lumps coming from the vagina: strongly supports; Vaginal bleeding in pregnancy: strongly supports; Stomach pain in pregnancy: supports; Heavy bleeding from the vagina: supports; Vaginal bleeding between periods or after sex: supports; Pelvic pain (pain low down in the tummy): supports; Missed or late period: supports |
| Pelvic infection (infection of the womb, tubes or ovaries) | 198130006 | rare | Pelvic pain (pain low down in the tummy): strongly supports; Vaginal discharge that is unusual: supports; Pain deep inside during or after sex: supports; Very high temperature, or feels hot, cold or shivery: supports; Vaginal bleeding between periods or after sex: supports; Sex without a condom with a new partner in the last 3 months: supports; A sexual partner has a sexually transmitted infection: supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: strongly supports; Pain, burning or stinging when peeing: supports; Feels very unwell: supports |
| Periods not settled yet after starting (puberty) |  | rare | Periods started in the last 2 years: strongly supports; Irregular periods: supports; Missed or late period: supports; Heavy periods: supports |
| Womb cancer (cancer of the lining of the womb) | 93781006 | very rare | Vaginal bleeding after the menopause: strongly supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports; Pain in the lower back: supports; Pain deep inside during or after sex: supports; Losing weight without trying: supports; Bleeding between periods: supports; Heavy bleeding from the vagina: supports |
| Polyps (small soft growths) or a thickened lining in the womb |  | uncommon | Bleeding between periods: strongly supports; Vaginal bleeding after the menopause: strongly supports; Heavy periods: supports; Takes the combined pill or HRT: supports; Periods last more than 7 days: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
