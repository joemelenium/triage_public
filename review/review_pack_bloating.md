# Review pack: Bloating

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
| [Bloating](https://www.nhs.uk/symptoms/bloating/) | 2026-11-19 |  | Page last reviewed: 21 January 2026 |
| [Diverticular disease and diverticulitis](https://www.nhs.uk/conditions/diverticular-disease-and-diverticulitis/) | 2026-11-19 |  | Page last reviewed: 07 September 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Constipation](https://www.nhs.uk/conditions/constipation/) | 2026-11-19 |  | Page last reviewed: 26 October 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Hernia](https://www.nhs.uk/conditions/hernia/) | 2026-11-19 |  | Page last reviewed: 19 May 2026 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Heartburn and acid reflux](https://www.nhs.uk/conditions/heartburn-and-acid-reflux/) | 2026-11-18 |  | Page last reviewed: 20 November 2023 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | 2026-11-19 |  | Page last reviewed: 09 August 2024 |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |

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

## Bloating red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bl_sudden_severe`<br>Bloating with a stomach ache that is severe and came on very suddenly | "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_vomiting_blood`<br>Bloating and being sick with blood, or sick that looks like ground coffee | "Being sick with blood in it (vomiting blood)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_blocked_bowel`<br>Bloating, cannot poo or fart at all, and a swollen tummy or being sick: possible blocked bowel<br>**Note:** The Bloating page says urgent for not being able to poo or fart. With a swollen tummy or being sick, the Diverticulitis and Stomach ache pages say 999 or A&E. The more urgent is used. | "Cannot poo or fart at all" AND ("Tummy looks swollen or much bigger than usual" OR "Being sick") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diverticular disease and diverticulitis](https://www.nhs.uk/conditions/diverticular-disease-and-diverticulitis/) | |

## Bloating red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bl_stomach_ache`<br>Bloating with a stomach ache<br>**Note:** Source difference: the Bloating page says urgent. The Stomach ache and Farting pages say see a GP for bloating with a stomach ache that does not go away, and list trapped wind as a common cause. The more urgent is used, marked soft. | "Stomach ache" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_d_and_v_or_constipation`<br>Bloating with being sick, diarrhoea or constipation<br>**Note:** Source difference: the Bloating page says urgent. The Constipation page lists bloating as a usual part of constipation and says see a GP (non-urgent) if regularly bloated. The more urgent is used, marked soft. | "Diarrhoea, or being sick" OR "Constipation" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_high_temperature`<br>Bloating with a high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_lump`<br>Bloating with a swelling or lump in the tummy | "A lump or swelling in the tummy or groin" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_cannot_pee_poo_fart`<br>Bloating and cannot pee, poo or fart<br>**Note:** The Stomach ache page says 999 or A&E for not being able to pee at all with a stomach ache. Saying yes to a stomach ache brings in that rule. | "Not able to pee at all for several hours" OR "Cannot poo or fart at all" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_bl_acid_reflux`<br>Bloating with a burning feeling in the chest from acid reflux<br>**Note:** Source difference: the Bloating page says urgent. The Heartburn and Indigestion pages say a pharmacist can help. The more urgent is used, marked soft. | "Heartburn or a sour taste in the mouth" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |

## Bloating: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bl_gp`<br>Bloating regularly or that does not go away, or with weight loss or blood in poo | "Bloated regularly, or it does not go away" OR "Losing weight without trying" OR "Bleeding from the bottom, or blood in poo" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |

## Default outcome

Used when no rule fires.

- **Bloating with nothing that needs more help: try things to ease it, and a pharmacist can help**
- Outcome: Self-manageable, Self-care, No appointment needed. *Bloating is very common and usually eases with simple changes*
- Source: [Bloating](https://www.nhs.uk/symptoms/bloating/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Bloating | Do you feel bloated? This means your tummy feels full, tight or uncomfortable. | 116289008 | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Cannot poo or fart at all | Are you unable to poo or fart at all? |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Tummy looks swollen or much bigger than usual | Does your tummy look swollen, or much bigger than usual? | 60728008 | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Diarrhoea, or being sick | Do you have diarrhoea, or have you been sick? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Constipation | Are you constipated? This means pooing less often than usual, or finding it hard to poo. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| A lump or swelling in the tummy or groin | Do you have a lump or swelling in your tummy or groin? It may go away when you lie down. |  | [Hernia](https://www.nhs.uk/conditions/hernia/) | |
| Not able to pee at all for several hours | Have you not been able to pee at all, not even a little, for 6 hours or more? |  | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Heartburn or a sour taste in the mouth | Do you get heartburn (a burning feeling in the middle of your chest), or a sour taste in your mouth? |  | [Heartburn and acid reflux](https://www.nhs.uk/conditions/heartburn-and-acid-reflux/) | |
| Bloated regularly, or it does not go away | Have you felt bloated, or had a swollen tummy, most days, or on and off for 3 weeks or more? Or does it not go away, even when you change what you eat? |  | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

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

### `advice_stomach_ache_ae`

**What to do:** Call 999 or go to A&E now. Your tummy pain needs to be checked in hospital straight away.

**Look out for:**
- Pain getting worse, or spreading across your tummy
- Feeling faint, passing out, or cold, clammy, pale skin
- Being sick with blood, or green sick

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat anything until a doctor has checked you. Small sips of water are fine.
- Do not take ibuprofen or aspirin. They can make some tummy problems worse.

Source: [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/), [Appendicitis](https://www.nhs.uk/conditions/appendicitis/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

### `advice_vomiting_blood_ae`

**What to do:** Call 999 or go to A&E now. Being sick with blood can be a sign of bleeding in your stomach or food pipe. It needs to be checked in hospital straight away.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Cold, clammy, pale skin, or fast or shallow breathing
- Black, sticky poo

**Get more help when:**
- Call 999 if you get worse, keep being sick with blood, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat or drink anything until a doctor has checked you
- If you can, keep a sample or a photo of the sick to show the doctor

Source: [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/), [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

### `advice_constipation_ae`

**What to do:** Call 999 or go to A&E now. Not being able to poo or fart, with a swollen tummy or being sick, can mean your bowel is blocked.

**Look out for:**
- Being sick, especially green sick
- The tummy pain getting worse

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat until a doctor has checked you. Do not take laxatives (medicines that help you poo) until you have been told it is safe.

Source: [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/), [Diverticular disease and diverticulitis](https://www.nhs.uk/conditions/diverticular-disease-and-diverticulitis/)

### `advice_bloating_urgent`

**What to do:** Ask for an urgent GP appointment or call NHS 111 today. Bloating with your other symptoms should be checked today.

**Look out for:**
- A stomach ache that is severe and came on very suddenly
- Being sick with blood, or sick that looks like ground coffee
- Severe difficulty breathing

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Bloating](https://www.nhs.uk/symptoms/bloating/)

### `advice_bloating_gp`

**What to do:** See a GP. They can look for the cause of your bloating, and may suggest tests or a dietitian.

**Look out for:**
- A stomach ache, being sick, diarrhoea or constipation
- A high temperature, or a lump in your tummy

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if you get a severe stomach ache that comes on very suddenly

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep a diary of what you eat and when you feel bloated

Source: [Bloating](https://www.nhs.uk/symptoms/bloating/)

### `advice_bloating_self_care`

**What to do:** Bloating is very common. There are things you can do to ease it, and a pharmacist can help.

**Look out for:**
- Bloating that does not go away, or keeps coming back
- A stomach ache, being sick, diarrhoea or constipation
- Losing weight without trying, or blood in your poo

**Get more help when:**
- See a GP if you feel bloated regularly, or changing your diet has not helped
- Get help today if you get a stomach ache, a high temperature or a lump in your tummy. Call 111 or ask for an urgent GP appointment.
- Call 999 or go to A&E if you get a severe stomach ache that comes on very suddenly

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Exercise regularly, and eat smaller meals more often
- Chew with your mouth closed, so you do not swallow air
- Cut down on fizzy drinks, alcohol, coffee and foods that cause gas, like beans or cabbage
- Massage your tummy gently from right to left to release trapped wind

Source: [Bloating](https://www.nhs.uk/symptoms/bloating/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bl_blocked_bowel`: The Bloating page says urgent for not being able to poo or fart. With a swollen tummy or being sick, the Diverticulitis and Stomach ache pages say 999 or A&E. The more urgent is used.
- `rf_bl_stomach_ache`: Source difference: the Bloating page says urgent. The Stomach ache and Farting pages say see a GP for bloating with a stomach ache that does not go away, and list trapped wind as a common cause. The more urgent is used, marked soft.
- `rf_bl_d_and_v_or_constipation`: Source difference: the Bloating page says urgent. The Constipation page lists bloating as a usual part of constipation and says see a GP (non-urgent) if regularly bloated. The more urgent is used, marked soft.
- `rf_bl_cannot_pee_poo_fart`: The Stomach ache page says 999 or A&E for not being able to pee at all with a stomach ache. Saying yes to a stomach ache brings in that rule.
- `rf_bl_acid_reflux`: Source difference: the Bloating page says urgent. The Heartburn and Indigestion pages say a pharmacist can help. The more urgent is used, marked soft.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Bowel cancer warning signs | 1286877004 | rare | Blood in poo for 3 weeks or more: strongly supports; Changes in pooing for 3 weeks or more: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Bleeding from the bottom, or blood in poo: supports |
| A blocked bowel (bowel obstruction) | 81060008 | rare | Cannot poo or fart at all: strongly supports; Tummy looks swollen or much bigger than usual: strongly supports; Being sick: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Green or yellow-green sick: supports; The lump is painful or firm, or cannot be pushed back in: supports; Constipation: supports |
| Coeliac condition (the body reacts to gluten, which damages the gut) | 396331005 | uncommon | Symptoms come on after foods with wheat, barley or rye: strongly supports; Bloating: supports; Diarrhoea: supports; Farting a lot, or smelly farts: supports; Feels very tired: supports; Losing weight without trying: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Irritable bowel syndrome (IBS) | 10743008 | common | Tummy pain eases after pooing or farting: strongly supports; Stomach ache that does not go away or keeps coming back: strongly supports; Pooing changes between diarrhoea and constipation: strongly supports; Bloating: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Slime (mucus) in poo: supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Constipation: supports |
| Lactose intolerance (cannot easily digest the sugar in milk) | 782415009 | uncommon | Symptoms come on after milk or dairy foods: strongly supports; Bloating: strongly supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Cramping tummy pain that comes and goes in waves: supports; Feeling sick (nausea): supports |
| Trapped wind |  | common | Farting a lot, or smelly farts: strongly supports; Bloating: strongly supports; Tummy pain eases after pooing or farting: strongly supports; Cramping tummy pain that comes and goes in waves: supports |
| Ovarian cancer | 363443007 | very rare | Bloated regularly, or it does not go away: strongly supports; Feels full quickly or has no appetite: strongly supports; Peeing more often than usual: supports; Losing weight without trying: supports; Feels very tired: supports; Changes in pooing for 3 weeks or more: supports; Pelvic pain (pain low down in the tummy): supports; Feels full after eating only a little: supports; Pain low down in the tummy, below the belly button: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
