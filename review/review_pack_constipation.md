# Review pack: Constipation

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
| [Diverticular disease and diverticulitis](https://www.nhs.uk/conditions/diverticular-disease-and-diverticulitis/) | 2026-11-19 |  | Page last reviewed: 07 September 2023 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Bloating](https://www.nhs.uk/symptoms/bloating/) | 2026-11-19 |  | Page last reviewed: 21 January 2026 |
| [Soiling (child pooing their pants)](https://www.nhs.uk/symptoms/soiling-child-pooing-their-pants/) | 2026-11-19 |  | Page last reviewed: 22 November 2023 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Constipation in children](https://www.nhs.uk/baby/health/constipation-in-children/) | 2026-11-19 |  | Page last reviewed: 2 August 2023 |
| [Constipation](https://www.nhs.uk/conditions/constipation/) | 2026-11-19 |  | Page last reviewed: 26 October 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
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

## Constipation red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_con_blocked_bowel`<br>Cannot poo or fart at all, with being sick or a swollen tummy: possible blocked bowel<br>**Note:** The Diverticulitis page says 999 or A&E for severe tummy pain with being sick, a swollen tummy, or not being able to poo or fart. The Stomach ache page says 999 or A&E for a stomach ache with not being able to poo or fart, so a stomach ache is included: without it, the urgent rule below settled the outcome and the tummy pain was never asked about. | "Cannot poo or fart at all" AND ("Being sick" OR "Tummy looks swollen or much bigger than usual" OR "Stomach ache") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diverticular disease and diverticulitis](https://www.nhs.uk/conditions/diverticular-disease-and-diverticulitis/) | |
| `rf_con_sudden_severe_pain`<br>Constipation with a sudden, severe tummy ache | "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| `rf_con_nerve_signs`<br>Loss of feeling around the bottom or genitals, or weakness or numbness in both legs, or cannot pee: possible pressure on the nerves at the base of the spine<br>**Note:** The Back pain page says 999 or A&E for back pain with these signs (cauda equina syndrome). Applying them to constipation without back pain is AI judgement: changes in pooing can be the first sign. | "Numb or no feeling around the genitals or bottom" OR "Numbness or weakness in both legs" OR "Not able to pee at all for several hours" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Constipation red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_con_cannot_poo_or_fart`<br>Cannot poo or fart at all | "Cannot poo or fart at all" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_con_child_swollen_and_sick`<br>A child who is constipated or soiling, with a swollen tummy and being sick | "Under 16 years old" AND "Tummy looks swollen or much bigger than usual" AND "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Soiling (child pooing their pants)](https://www.nhs.uk/symptoms/soiling-child-pooing-their-pants/) | |
| `rf_con_swollen_or_sick`<br>Constipation with a swollen tummy, or with being sick<br>**Note:** The Bloating page says an urgent GP appointment or 111 for bloating with being sick or constipation. Using a swollen tummy for bloating is a reading of the source. | "Tummy looks swollen or much bigger than usual" OR "Being sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| `rf_con_black_poo`<br>Black or dark red poo<br>**Note:** Iron tablets can make poo dark. The question says so. | "Black, sticky poo, or dark red poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

## Constipation: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_con_child`<br>A child who may be constipated<br>**Note:** The Constipation in children page says take your child to a GP if you think they may be constipated, and get help early. | "Under 16 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*Take your child to see a GP. The source gives no fixed time.* | [Constipation in children](https://www.nhs.uk/baby/health/constipation-in-children/) | |
| `or_con_gp`<br>Constipation not getting better with treatment, regularly constipated, or with blood in poo, weight loss, tiredness, tummy pain, a medicine that causes it, or sudden changes in pooing<br>**Note:** The page says see a GP if you are regularly bloated. Using any bloating is AI judgement. | "Constipation not getting better with treatment" OR "Often constipated" OR "Bloating" OR "Bleeding from the bottom, or blood in poo" OR "Losing weight without trying" OR "Feels very tired" OR "Takes a medicine that can cause constipation" OR "Changes in pooing for 3 weeks or more" OR "Stomach ache" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Constipation](https://www.nhs.uk/conditions/constipation/) | |

## Default outcome

Used when no rule fires.

- **Constipation with nothing that needs more help: treat it with changes to diet and lifestyle, and ask a pharmacist if these do not help**
- Outcome: Self-manageable, Self-care, No appointment needed. *You may notice a difference within a few days*
- Source: [Constipation](https://www.nhs.uk/conditions/constipation/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Constipation | Are you constipated? This means pooing less often than usual, or finding it hard to poo. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot poo or fart at all | Are you unable to poo or fart at all? |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Tummy looks swollen or much bigger than usual | Does your tummy look swollen, or much bigger than usual? | 60728008 | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Not able to pee at all for several hours | Have you not been able to pee at all, not even a little, for 6 hours or more? |  | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Constipation not getting better with treatment | Is your constipation not getting better? For example, you have tried changes to what you eat and drink, or pharmacy medicines. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Often constipated | Do you often get constipated? |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Bloating | Do you feel bloated? This means your tummy feels full, tight or uncomfortable. | 116289008 | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Takes a medicine that can cause constipation | Do you take a medicine that can cause constipation? For example, strong painkillers such as codeine or morphine, or iron tablets. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Changes in pooing for 3 weeks or more | For 3 weeks or more, has your poo changed in a way that is not usual for you? For example, it is softer, thinner or runnier, you poo more often, or you are constipated. | 88111009 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

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

### `advice_nerve_emergency`

**What to do:** Call 999 or go to A&E now. Losing control of your bowels or bladder, with numbness around your bottom or weak legs, can mean pressure on the nerves at the base of the spine. It needs treatment within hours to prevent lasting damage.

**Look out for:**
- The numbness or weakness getting worse
- Not being able to pee

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive. Ask someone to drive you or call 999 and ask for an ambulance.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_constipation_urgent`

**What to do:** Ask for an urgent GP appointment or call NHS 111 today. Constipation with your other symptoms should be checked today.

**Look out for:**
- Not being able to fart at all
- A tummy that keeps swelling, or severe tummy pain
- Being sick, especially green sick

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Bloating](https://www.nhs.uk/symptoms/bloating/), [Soiling (child pooing their pants)](https://www.nhs.uk/symptoms/soiling-child-pooing-their-pants/)

### `advice_rectal_bleeding_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Black or dark red poo, or blood with diarrhoea, should be checked today.

**Look out for:**
- Bleeding that will not stop, or a lot of blood: the toilet water turns red or you see large clots
- Feeling faint or dizzy
- Being sick with blood

**Get more help when:**
- Go to A&E or call 999 if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Iron tablets and dark foods like liquorice or blueberries can turn poo dark. Tell the doctor if you have had them.

Source: [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/)

### `advice_constipation_child_gp`

**What to do:** Take your child to see a GP. The longer a child is constipated, the harder it can be to get back to normal, so get help early.

**Look out for:**
- A swollen tummy with being sick
- Numbness or weakness in both legs
- Blood in their poo

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your child has a swollen tummy and is being sick
- Call 999 or go to A&E if your child cannot poo or fart at all and has a swollen tummy or is being sick

**Where to go:** Make an appointment with a GP. A health visitor can also give advice. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Give your child plenty to drink, and lots of fruit and vegetables
- Help them sit on the potty or toilet after meals or before bed. Praise them, even if they do not poo.
- Stay calm and reassuring. Children do not get constipated on purpose.

Source: [Constipation in children](https://www.nhs.uk/baby/health/constipation-in-children/)

### `advice_constipation_gp`

**What to do:** See a GP about your constipation. They can look for the cause and may prescribe stronger laxatives (medicines that help you poo).

**Look out for:**
- Not being able to poo or fart at all
- A swollen tummy, or being sick
- Blood in your poo

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get a swollen tummy or start being sick
- Call 999 or go to A&E if you cannot poo or fart at all and have a swollen tummy or are being sick

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink plenty of water, and slowly add more fibre to your diet
- Try to be more active, for example a daily walk
- Speak to the GP before you stop taking any prescribed medicine

Source: [Constipation](https://www.nhs.uk/conditions/constipation/)

### `advice_constipation_self_care`

**What to do:** You can usually treat constipation with simple changes to your diet and lifestyle. Speak to a pharmacist if these do not help.

**Look out for:**
- Constipation that is not getting better
- Blood in your poo, or losing weight without trying
- A swollen tummy, or being sick

**Get more help when:**
- Speak to a pharmacist if diet and lifestyle changes are not helping. They can suggest a laxative (a medicine that helps you poo).
- See a GP if it is not getting better with treatment, keeps happening, or you have tummy pain
- Call 999 or go to A&E if you cannot poo or fart at all and have a swollen tummy or are being sick

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink plenty of water and other fluids, and avoid alcohol
- Slowly add more fibre, such as fruit, vegetables, oats or wheat bran
- Keep to a regular time for the toilet, and do not ignore the urge to poo
- Rest your feet on a low stool on the toilet, so your knees are above your hips
- Try to be more active, for example a daily walk

Source: [Constipation](https://www.nhs.uk/conditions/constipation/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_con_blocked_bowel`: The Diverticulitis page says 999 or A&E for severe tummy pain with being sick, a swollen tummy, or not being able to poo or fart. The Stomach ache page says 999 or A&E for a stomach ache with not being able to poo or fart, so a stomach ache is included: without it, the urgent rule below settled the outcome and the tummy pain was never asked about.
- `rf_con_nerve_signs`: The Back pain page says 999 or A&E for back pain with these signs (cauda equina syndrome). Applying them to constipation without back pain is AI judgement: changes in pooing can be the first sign.
- `rf_con_swollen_or_sick`: The Bloating page says an urgent GP appointment or 111 for bloating with being sick or constipation. Using a swollen tummy for bloating is a reading of the source.
- `rf_con_black_poo`: Iron tablets can make poo dark. The question says so.
- `or_con_child`: The Constipation in children page says take your child to a GP if you think they may be constipated, and get help early.
- `or_con_gp`: The page says see a GP if you are regularly bloated. Using any bloating is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Bowel cancer warning signs | 1286877004 | rare | Blood in poo for 3 weeks or more: strongly supports; Changes in pooing for 3 weeks or more: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Bleeding from the bottom, or blood in poo: supports |
| A blocked bowel (bowel obstruction) | 81060008 | rare | Cannot poo or fart at all: strongly supports; Tummy looks swollen or much bigger than usual: strongly supports; Being sick: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Green or yellow-green sick: supports; The lump is painful or firm, or cannot be pushed back in: supports; Constipation: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Irritable bowel syndrome (IBS) | 10743008 | common | Tummy pain eases after pooing or farting: strongly supports; Stomach ache that does not go away or keeps coming back: strongly supports; Pooing changes between diarrhoea and constipation: strongly supports; Bloating: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Slime (mucus) in poo: supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Constipation: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
