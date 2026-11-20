# Review pack: Eating problems

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
| [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | 2026-11-19 |  | Page last reviewed: 23 October 2026 |
| [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/) | 2026-11-19 |  | Page last reviewed: 18 January 2024 |
| [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/) | 2026-11-19 |  | Page last reviewed: 23 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
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

## Eating problems red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ep_fainted`<br>An eating problem and has passed out (fainted)<br>**Note:** The Eating disorders page lists fainting or feeling faint as a physical sign. Clinical knowledge: fainting with an eating problem can mean a dangerous heart rhythm or very low blood sugar or salts, and needs checking the same day in hospital. | "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_ep_weak`<br>An eating problem and so weak it is hard to stand up, climb stairs or get up from sitting<br>**Note:** Clinical knowledge: muscle weakness this severe is a sign of dangerous starvation. | "So weak it is hard to stand up, climb stairs or get up from sitting" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_ep_fit`<br>An eating problem and has had a seizure (fit)<br>**Note:** Clinical knowledge: a fit can be caused by very low blood sugar or salts from not eating, being sick or taking laxatives. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_ep_slow_heartbeat`<br>An eating problem and the heart beating very slowly<br>**Note:** Clinical knowledge: a very slow heartbeat is a sign of dangerous starvation. | "Heart beating very slowly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_ep_cannot_keep_safe`<br>Cannot keep themselves or someone else safe right now | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |

## Eating problems red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ep_being_sick`<br>Being sick several times a day, or cannot keep drinks down<br>**Note:** Clinical knowledge: being sick many times a day can make salts in the blood (such as potassium) dangerously low, which can affect the heart. | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |
| `rf_ep_dehydration`<br>An eating problem with signs of dehydration<br>**Note:** Clinical knowledge. The Anorexia page says call 111 if someone needs urgent medical help. | "Signs of dehydration" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |

## Eating problems: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ep_weight_loss`<br>Lost a lot of weight quickly, or very thin<br>**Note:** The page says see a GP as soon as you can if you think you may have anorexia. Mapping 'as soon as you can' to within a few days for someone who has lost a lot of weight is AI judgement. | "Lost a lot of weight quickly, or very underweight" OR "Lost a lot of weight quickly" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP as soon as you can, within a few days* | [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/) | |
| `or_ep_child_restricting`<br>A child or young person under 16 eating very little to control their weight<br>**Note:** The page says children with anorexia may not grow as expected, and to see a GP as soon as you can. Within a few days is AI judgement. | "Under 16 years old" AND "Eating very little or skipping meals to control weight" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP as soon as you can, within a few days* | [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/) | |

## Default outcome

Used when no rule fires.

- **Worried about eating, weight or body shape, with no danger signs: see a GP**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP as soon as you can. The source gives no fixed time.*
- Source: [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Worried about eating, weight or body shape | Are you worried about your eating, or about your weight or body shape? For example, eating very little, making yourself sick, or eating large amounts and feeling out of control. |  | [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| So weak it is hard to stand up, climb stairs or get up from sitting | Do you feel so weak that it is hard to stand up, climb stairs or get up from sitting? |  | **AI judgement, needs clinical review** | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Heart beating very slowly | Is your heart beating much more slowly than usual? | 48867003 | **AI judgement, needs clinical review** | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Lost a lot of weight quickly, or very underweight | Have you lost a lot of weight quickly, or do people say you are very thin? |  | [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/) | |
| Lost a lot of weight quickly | Have you lost a lot of weight in the last few months, such as a stone (6kg) or more, or your clothes no longer fit? |  | **AI judgement, needs clinical review** | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Eating very little or skipping meals to control weight | Are you eating very little, or skipping meals, to control your weight? |  | [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/) | |

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

### `advice_eating_ae`

**What to do:** Go to A&E now, or call 999. Fainting, a fit, a very slow heartbeat or severe weakness with an eating problem can mean your body is in danger and needs checking straight away.

**Look out for:**
- Chest pain, or a heartbeat that is very slow, racing or uneven
- Becoming confused or very sleepy

**Get more help when:**
- Call 999 if the person stops responding, has a fit, or you cannot get to A&E safely
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or call NHS 111 and choose option 2 for mental health

**Where to go:** Go to A&E or call 999. Do not drive yourself. Ask someone to take you. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/), [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/)

### `advice_mh_cannot_keep_safe`

**What to do:** Call 999 or go to A&E now. A mental health emergency is as serious as a physical one. You will not be wasting anyone's time.

**Look out for:**
- Feeling that you may act on thoughts of ending your life or harming yourself
- Feeling that you cannot keep yourself or someone else safe

**Get more help when:**
- Call 999 now if you have seriously hurt yourself or taken an overdose
- While you wait, call Samaritans free on 116 123, day or night. Or text SHOUT to 85258.
- If you have a crisis team, you can also call them

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to take you, or call 999 for an ambulance. If you can, stay with other people and move away from anything you could use to harm yourself.

**What you can do yourself:**
- Try to get to a safe place, like a friend's house, and be around other people
- Stay away from alcohol and drug use, and from anything you could use to harm yourself
- Focus on getting through the next few minutes and hours, not the future

Source: [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/), [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

### `advice_eating_urgent`

**What to do:** Ask your GP surgery for an urgent appointment, or call NHS 111, today. Being sick a lot, or not drinking enough, can upset the salts in your blood and affect your heart.

**Look out for:**
- Fainting, or feeling very dizzy or weak
- Your heart racing, beating unevenly, or beating very slowly
- Chest pain, or muscle cramps or twitching

**Get more help when:**
- Go to A&E or call 999 if you faint, have chest pain, have a fit, or are too weak to stand
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or call NHS 111 and choose option 2 for mental health. Call 999 if your life is in danger.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online, today.

**What you can do yourself:**
- Sip water or other drinks often
- You can talk in confidence to the eating problems charity Beat on 0808 801 0677

Source: [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/), [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/)

### `advice_eating_soon`

**What to do:** See a GP as soon as you can, within the next few days. Getting help early gives you the best chance of recovering.

**Look out for:**
- Fainting, feeling dizzy, or being too weak to stand
- Your heart racing, beating unevenly, or beating very slowly
- Being sick several times a day

**Get more help when:**
- Go to A&E or call 999 if you faint, have chest pain, have a fit, or are too weak to stand
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or NHS 111 and choose option 2. Call 999 if your life is in danger.

**Where to go:** Make an appointment with a GP in the next few days. It may help to bring someone you trust.

**What you can do yourself:**
- You can talk in confidence to the eating problems charity Beat on 0808 801 0677

Source: [Anorexia: symptoms](https://www.nhs.uk/mental-health/conditions/anorexia/symptoms/), [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/)

### `advice_eating_gp`

**What to do:** See a GP as soon as you can. They will ask about your eating and how you feel, and can refer you to specialist help. Most people recover with treatment.

**Look out for:**
- Losing a lot of weight quickly
- Fainting, feeling dizzy, or being very weak
- Being sick several times a day

**Get more help when:**
- Go to A&E or call 999 if you faint, have chest pain, have a fit, or are too weak to stand
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or NHS 111 and choose option 2. Call 999 if your life is in danger.

**Where to go:** Make an appointment with a GP. It may help to bring someone you trust.

**What you can do yourself:**
- You can talk in confidence to the eating problems charity Beat on 0808 801 0677
- If you are worried about someone else, tell them gently that you are worried, and offer to go to the GP with them

Source: [Eating disorders: overview](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ep_fainted`: The Eating disorders page lists fainting or feeling faint as a physical sign. Clinical knowledge: fainting with an eating problem can mean a dangerous heart rhythm or very low blood sugar or salts, and needs checking the same day in hospital.
- `rf_ep_weak`: Clinical knowledge: muscle weakness this severe is a sign of dangerous starvation.
- `rf_ep_fit`: Clinical knowledge: a fit can be caused by very low blood sugar or salts from not eating, being sick or taking laxatives.
- `rf_ep_slow_heartbeat`: Clinical knowledge: a very slow heartbeat is a sign of dangerous starvation.
- `rf_ep_being_sick`: Clinical knowledge: being sick many times a day can make salts in the blood (such as potassium) dangerously low, which can affect the heart.
- `rf_ep_dehydration`: Clinical knowledge. The Anorexia page says call 111 if someone needs urgent medical help.
- `or_ep_weight_loss`: The page says see a GP as soon as you can if you think you may have anorexia. Mapping 'as soon as you can' to within a few days for someone who has lost a lot of weight is AI judgement.
- `or_ep_child_restricting`: The page says children with anorexia may not grow as expected, and to see a GP as soon as you can. Within a few days is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anorexia (eating very little to keep weight low) | 56882008 | very rare | Eating very little or skipping meals to control weight: strongly supports; Very afraid of putting on weight: strongly supports; Lost a lot of weight quickly, or very underweight: strongly supports; Exercising too much to control weight: supports; So weak it is hard to stand up, climb stairs or get up from sitting: supports |
| Binge eating (often eating very large amounts and feeling out of control) | 439960005 | common | Eats large amounts very quickly and feels out of control: strongly supports; Eats in secret, or feels ashamed after eating: strongly supports; Feels worthless or very guilty: supports; Feeling low, sad or depressed: supports |
| Bulimia (eating a lot, then making yourself sick to stay thin) | 78004001 | common | Makes themselves sick, or takes laxatives, to control weight: strongly supports; Eats large amounts very quickly and feels out of control: strongly supports; Very afraid of putting on weight: supports; Keeps being sick and cannot keep fluids down: supports; Eats in secret, or feels ashamed after eating: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
