# Review pack: Earache

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
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Earache](https://www.nhs.uk/symptoms/earache/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Ear infections](https://www.nhs.uk/conditions/ear-infections/) | 2026-11-19 |  | Page last reviewed: 16 January 2025 |
| [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | 2026-11-19 |  | Page last reviewed: 04 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | 2026-11-19 |  | Page last reviewed: 30 May 2025 |
| [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | 2026-11-19 |  | Page last reviewed: 03 October 2023 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Vertigo](https://www.nhs.uk/conditions/vertigo/) | 2026-11-19 |  | Page last reviewed: 02 May 2023 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Mastoiditis](https://www.nhs.uk/conditions/mastoiditis/) | 2026-11-19 |  | Page last reviewed: 17 August 2026 |
| [Mumps](https://www.nhs.uk/conditions/mumps/) | 2026-11-19 |  | Page last reviewed: 09 July 2025 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |

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

## Earache red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ea_meningitis_signs`<br>Earache with a very bad headache and a stiff neck, or bright light hurting the eyes<br>**Note:** Clinical knowledge: an ear infection can rarely spread to the lining of the brain (meningitis). The Mastoiditis page names meningitis as a complication, and the Mumps page says go to A&E or call 999 for a very bad headache with a stiff neck. | "Very painful headache" AND ("Stiff neck" OR "Bright lights hurt the eyes or are bothering you") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_ea_child_floppy`<br>A child with earache who is limp, floppy, hard to wake or not responding as usual | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ea_rash_not_fading`<br>Earache with a rash that does not fade when a glass is pressed on it | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_ea_head_injury`<br>Earache, or fluid from the ear, that started after a head injury<br>**Note:** AI reading of the Tinnitus page, which says go to A&E for tinnitus after a head injury. Ear pain, bleeding or fluid from the ear after a head injury can be a sign of a skull injury. | "Head injury in the last month" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Earache red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ea_over_2_to_3_days`<br>Earache for more than 2 to 3 days<br>**Note:** Source difference: the Earache page says an urgent GP appointment or 111 for earache lasting more than 2 to 3 days. The Ear infections page says see a GP (not urgent) for earache that does not get better after 3 days. The more urgent is used, marked soft. | "Earache for more than 2 to 3 days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_unwell`<br>Earache and feeling generally unwell | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_high_temperature`<br>Earache with a very high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_swelling_around_ear`<br>Earache with swelling around or behind the ear<br>**Note:** The Mastoiditis page also says an urgent GP appointment or 111 for redness or swelling behind the ear. | "Swelling, redness or tenderness around or behind the ear" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_discharge`<br>Earache with fluid coming from the ear | "Fluid or pus coming out of the ear" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_hearing_change`<br>Earache with hearing loss or a change in hearing | "Hearing loss or a change in hearing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_object`<br>Earache with something stuck in the ear | "Something stuck in the ear" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_child_under_2_both_ears`<br>A child under 2 with earache in both ears<br>**Note:** The Ear infections page says under 12 months; the Earache page says under 2. The wider age is used. | "Under 2 years old" AND "Earache in both ears" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `rf_ea_sick_or_dizzy`<br>Earache with feeling sick or being sick, or feeling dizzy | "Feels sick or has been sick" OR "Feels like you or the room is spinning (vertigo)" OR "Feels light-headed" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Ear infections](https://www.nhs.uk/conditions/ear-infections/) | |
| `rf_ea_long_term_condition`<br>Earache in someone with diabetes, a heart, lung, kidney or brain condition, or a weakened immune system | "Has a long-term health condition" OR "Weakened immune system" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Ear infections](https://www.nhs.uk/conditions/ear-infections/) | |
| `rf_ea_facial_weakness`<br>Earache with weakness or drooping of one side of the face<br>**Note:** The Bell's palsy page says an urgent GP appointment or 111, because treatment works best if started within 72 hours. Signs of a stroke are checked for everyone first. A face that is weak with ear pain or a rash in the ear can also be shingles of the ear. | "One side of the face weak or drooping" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today* | [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | |
| `rf_ea_rash_on_ear`<br>Earache with a painful rash or blisters in or around the ear<br>**Note:** Clinical knowledge: blisters in the ear can be shingles of the ear, which can weaken the face and affect hearing. Treatment works best if started early. The Shingles page says see a GP urgently for shingles near the eye; applying it to the ear is AI judgement. | "Painful rash or blisters in or around the ear" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111 today* | **AI judgement, needs clinical review** | |

## Earache: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ea_keeps_coming_back`<br>Keeps getting earache or ear infections | "Keeps getting earache or ear infections" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| `or_ea_baby_under_1`<br>A baby under 12 months with earache<br>**Note:** The Ear infections page says see a GP if your child is under 12 months and you think they have an ear infection. A pharmacist can treat children aged 1 to 17. | "Under 1 year old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Ear infections](https://www.nhs.uk/conditions/ear-infections/) | |

## Default outcome

Used when no rule fires.

- **Earache with nothing that needs more help: most earaches get better on their own within 3 days**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most earaches get better on their own within 2 to 3 days. A pharmacist can help.*
- Source: [Earache](https://www.nhs.uk/symptoms/earache/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Earache | Do you have earache or pain in your ear? | 301354004 | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Earache for more than 2 to 3 days | Have you had earache for more than 2 to 3 days? |  | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swelling, redness or tenderness around or behind the ear | Is there swelling, redness or tenderness around or behind the ear? The ear may stick out more than usual. |  | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Fluid or pus coming out of the ear | Is fluid or pus coming out of your ear? | 300132001 | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Hearing loss or a change in hearing | Have you lost some or all of your hearing, or has your hearing changed? |  | [Deafness](https://www.nhs.uk/conditions/hearing-loss/) | |
| Something stuck in the ear | Is there something stuck in the ear? |  | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Under 2 years old | Is the person who is unwell under 2 years old? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Earache in both ears | Is the pain in both ears? |  | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels like you or the room is spinning (vertigo) | Does it feel like you, or everything around you, is spinning? | 399153001 | [Vertigo](https://www.nhs.uk/conditions/vertigo/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Has a long-term health condition | Do you have a long-term health condition? For example, diabetes, or a heart, lung or kidney condition. |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| One side of the face weak or drooping | Is one side of your face weak or drooping? For example, your eye will not close or the corner of your mouth droops. | 95666008 | [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | |
| Painful rash or blisters in or around the ear | Do you have a painful rash or blisters in or around your ear? |  | **AI judgement, needs clinical review** | |
| Keeps getting earache or ear infections | Do you keep getting earache or ear infections? |  | [Earache](https://www.nhs.uk/symptoms/earache/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |

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

### `advice_earache_ae`

**What to do:** Call 999 or go to A&E now. An ear infection can rarely spread, and this needs checking in hospital.

**Look out for:**
- A very bad headache, a stiff neck, or bright light hurting the eyes
- A rash that does not fade when you press a glass against it
- Being very sleepy, confused or hard to wake

**Get more help when:**
- Call 999 if the person gets worse before you reach A&E, or you cannot get there safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Mastoiditis](https://www.nhs.uk/conditions/mastoiditis/), [Mumps](https://www.nhs.uk/conditions/mumps/), [Earache](https://www.nhs.uk/symptoms/earache/)

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

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

### `advice_earache_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You can call 111 or use 111 online. Call 111 if you need advice for a child under 5.

**Look out for:**
- Swelling, redness or pain behind the ear, or the ear sticking out
- A very bad headache with a stiff neck
- One side of the face becoming weak or drooping
- A child who is floppy, very sleepy or hard to wake

**Get more help when:**
- Call 999 or go to A&E if you or your child has a very bad headache with a stiff neck, or a rash that does not fade when pressed
- Call 999 if a child is floppy or will not wake up

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Hold a warm flannel against the ear
- Do not put anything inside the ear, such as cotton buds
- Do not let water get inside the ear

Source: [Earache](https://www.nhs.uk/symptoms/earache/), [Ear infections](https://www.nhs.uk/conditions/ear-infections/), [Mastoiditis](https://www.nhs.uk/conditions/mastoiditis/)

### `advice_object_stuck_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Do not try to take the object out yourself. You could push it further in.

**Look out for:**
- Pain, bleeding or fluid coming from the ear or nose
- Difficulty breathing
- A button battery or magnet, which can cause damage within hours

**Get more help when:**
- Go to A&E now if it is a button battery or magnet, or if the person is in a lot of pain
- Call 999 if the person finds it hard to breathe

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. A minor injuries unit or urgent treatment centre can also help.

Source: [Earache](https://www.nhs.uk/symptoms/earache/)

### `advice_earache_gp`

**What to do:** See a GP. They can look inside the ear and check what is causing the earache.

**Look out for:**
- A very high temperature, or feeling hot, cold or shivery
- Fluid coming from the ear, or swelling around the ear
- Hearing loss or a change in hearing
- Earache that lasts more than 2 to 3 days

**Get more help when:**
- Ask for an urgent GP appointment or get help from 111 if you get any of the signs above. Do the same if you feel unwell.
- Call 999 or go to A&E for a very bad headache with a stiff neck

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Hold a warm flannel against the ear
- Do not put anything inside the ear, such as cotton buds

Source: [Earache](https://www.nhs.uk/symptoms/earache/), [Ear infections](https://www.nhs.uk/conditions/ear-infections/)

### `advice_earache_self_care`

**What to do:** Most earaches get better on their own within 2 to 3 days. You can ease the pain yourself. A pharmacist can help, and can treat a middle ear infection in children aged 1 to 17.

**Look out for:**
- Earache that is not better after 2 to 3 days
- A very high temperature, or feeling hot, cold or shivery
- Swelling around the ear, or fluid coming from the ear
- Hearing loss, feeling dizzy, or being sick

**Get more help when:**
- Ask for an urgent GP appointment or get help from 111 if you get any of the signs above. Do the same if you feel unwell.
- See a GP if you or your child keep getting earache
- Call 999 or go to A&E for a very bad headache with a stiff neck

**Where to go:** You do not need an appointment now. A pharmacist can help. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Hold a warm flannel against the ear
- Do not put anything inside the ear, such as cotton buds
- Do not try to remove earwax, and do not let water get inside the ear

Source: [Earache](https://www.nhs.uk/symptoms/earache/), [Ear infections](https://www.nhs.uk/conditions/ear-infections/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ea_meningitis_signs`: Clinical knowledge: an ear infection can rarely spread to the lining of the brain (meningitis). The Mastoiditis page names meningitis as a complication, and the Mumps page says go to A&E or call 999 for a very bad headache with a stiff neck.
- `rf_ea_head_injury`: AI reading of the Tinnitus page, which says go to A&E for tinnitus after a head injury. Ear pain, bleeding or fluid from the ear after a head injury can be a sign of a skull injury.
- `rf_ea_over_2_to_3_days`: Source difference: the Earache page says an urgent GP appointment or 111 for earache lasting more than 2 to 3 days. The Ear infections page says see a GP (not urgent) for earache that does not get better after 3 days. The more urgent is used, marked soft.
- `rf_ea_swelling_around_ear`: The Mastoiditis page also says an urgent GP appointment or 111 for redness or swelling behind the ear.
- `rf_ea_child_under_2_both_ears`: The Ear infections page says under 12 months; the Earache page says under 2. The wider age is used.
- `rf_ea_facial_weakness`: The Bell's palsy page says an urgent GP appointment or 111, because treatment works best if started within 72 hours. Signs of a stroke are checked for everyone first. A face that is weak with ear pain or a rash in the ear can also be shingles of the ear.
- `rf_ea_rash_on_ear`: Clinical knowledge: blisters in the ear can be shingles of the ear, which can weaken the face and affect hearing. Treatment works best if started early. The Shingles page says see a GP urgently for shingles near the eye; applying it to the ear is AI judgement.
- `or_ea_baby_under_1`: The Ear infections page says see a GP if your child is under 12 months and you think they have an ear infection. A pharmacist can treat children aged 1 to 17.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Common cold | 82272006 | very common | Blocked or runny nose: strongly supports; Hoarse voice: supports; Dry cough: supports; Phlegm dripping down the back of the throat from the nose: supports |
| Cholesteatoma (a growth of skin deep inside the ear that can damage hearing) | 363668000 | rare | Smelly ear discharge, or discharge that keeps coming back: strongly supports; Hearing loss in one ear only: supports; Hearing getting slowly worse over months or years: supports; Keeps getting earache or ear infections: supports |
| Dental abscess (a pocket of pus in a tooth or gum) | 299709002 | common | Intense, throbbing tooth or gum pain: strongly supports; Swollen face, cheek or jaw: strongly supports; Toothache: strongly supports; Bad taste in the mouth: supports; Tooth hurts when biting or chewing: supports; Very high temperature, or feels hot, cold or shivery: supports; Swollen glands in the neck: supports; Sharp tooth pain with hot, cold or sweet things: supports |
| Earwax build-up | 18070006 | common | Ear feels blocked or full: strongly supports; Hearing loss in one ear only: supports; Itchy ear, or flaky skin in or around the ear: supports; Hearing loss or a change in hearing: supports; Tinnitus (ringing or buzzing in the ears): supports; Recent swimming, water in the ear, cotton buds or earplugs: supports |
| Glue ear (fluid behind the eardrum that muffles hearing, common in children) | 232255003 | uncommon | Hearing loss or a change in hearing: strongly supports; Ear feels blocked or full: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Tinnitus (ringing or buzzing in the ears): supports; Earache: supports |
| Jaw joint problem (pain and clicking in the joint just in front of the ear) |  | uncommon | Jaw aching, clicking, popping or locking: strongly supports; Teeth grinding or jaw clenching: supports; Feeling anxious, worried or panicky: supports; Jaw locking, or too painful to eat or drink: supports; Earache: supports |
| Mastoiditis (an infection of the bone behind the ear) | 52404001 | rare | Swelling, redness or tenderness around or behind the ear: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Fluid or pus coming out of the ear: supports; Feels very unwell: supports; Earache for more than 2 to 3 days: supports; Hearing loss or a change in hearing: supports |
| Middle ear infection (an infection behind the eardrum) | 3110003 | common | Earache: strongly supports; Young child rubbing or pulling their ear: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Young child irritable, restless or off their food: supports; Ear feels blocked or full: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Fluid or pus coming out of the ear: supports; Hearing loss or a change in hearing: supports |
| Mumps (a virus that causes painful swelling at the side of the face) | 36989005 | rare | Swelling on the side of the face, in front of and below the ear: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Aching body: supports; Feels very tired: supports; Earache: supports |
| Something stuck in the ear | 75441006 | rare | Something stuck in the ear: strongly supports; Hearing loss in one ear only: supports; Fluid or pus coming out of the ear: supports; Ear feels blocked or full: supports |
| Outer ear infection (an infection in the tube that goes into the ear) | 3135009 | common | Earache: strongly supports; Ear hurts more when touched or pulled: strongly supports; Itchy ear, or flaky skin in or around the ear: strongly supports; Recent swimming, water in the ear, cotton buds or earplugs: supports; Fluid or pus coming out of the ear: supports; Ear feels blocked or full: supports |
| Perforated eardrum (a hole or tear in the eardrum) | 60442001 | uncommon | Started suddenly after a loud noise, a blow to the ear, flying or diving: strongly supports; Fluid or pus coming out of the ear: supports; Earache: supports; Hearing loss in one ear only: supports; Hearing loss that came on suddenly: supports; Tinnitus (ringing or buzzing in the ears): supports |
| Shingles of the ear (a painful rash in or around the ear that can weaken one side of the face) | 21954000 | rare | Painful rash or blisters in or around the ear: strongly supports; One side of the face weak or drooping: strongly supports; Feels like you or the room is spinning (vertigo): supports; Hearing loss or a change in hearing: supports; Tinnitus (ringing or buzzing in the ears): supports; Earache: supports |
| Serious infection in the tube of the ear that spreads to the bone. It mostly affects older people or people with diabetes. | 94146005 | rare | Earache for more than 2 to 3 days: strongly supports; Fluid or pus coming out of the ear: strongly supports; Ear hurts more when touched or pulled: supports; One side of the face weak or drooping: supports; Swelling, redness or tenderness around or behind the ear: supports |
| Teething (a baby's tooth coming through) | 8004003 | rare | Signs of teething in a baby or young child: strongly supports; Young child rubbing or pulling their ear: supports; Young child irritable, restless or off their food: supports; Gums painful, swollen or bleeding: supports |
| Tonsillitis (infected tonsils at the back of the throat) | 90176007 | common | Pus-filled spots on the tonsils: supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Often gets sore throats: supports; Lump in the mouth or neck: supports; Swollen glands in the neck: supports; Feels very tired: supports; Cough or runny nose: argues against |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
