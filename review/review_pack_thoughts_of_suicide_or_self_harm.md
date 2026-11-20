# Review pack: Thoughts of suicide or self-harm

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
| [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/) | 2026-11-19 |  | Page last reviewed: 23 August 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Poisoning](https://www.nhs.uk/conditions/poisoning/) | 2026-11-19 |  | Page last reviewed: 12 June 2025 |

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

## Thoughts of suicide or self-harm red flags: Emergency (help now)

Most of these are asked together as one question: *"Thank you for telling us. You are not alone, and help is available. Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sh_plan`<br>Has a plan to end their life, or feels they may act on thoughts of suicide soon<br>**Note:** The page says call 999 or go to A&E if you feel you may be about to harm yourself. Reading a plan, or feeling you may act soon, as that is AI judgement. | "Has a plan to end their life, or may act on the thoughts soon" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| `rf_sh_preparing`<br>Has done something to prepare to end their life<br>**Note:** Clinical knowledge: preparing (a note, giving things away, gathering the means) is a sign of high immediate danger. Treated like the source's 'about to harm yourself'. | "Has done something to prepare to end their life" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_sh_cannot_keep_safe`<br>Cannot keep themselves or someone else safe right now | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_sh_overdose`<br>Has taken an overdose or swallowed something harmful, even if they feel well<br>**Note:** The Poisoning page says the same, and that symptoms may take hours or days to start. | "Taken an overdose, or swallowed something harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| `rf_sh_serious_injury`<br>A serious injury from self-harm: deep, gaping, bleeding a lot, or a bad burn | "Serious injury from self-harm: deep, bleeding a lot, or a bad burn" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_sh_voices_harm`<br>Hearing voices telling them to harm themselves or someone else<br>**Note:** Clinical knowledge: voices telling someone to harm themselves or others, together with thoughts of suicide or self-harm, need assessment now. | "Voices telling them to harm themselves or someone else" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Thoughts of suicide or self-harm red flags: Urgent (help today)

Most of these are asked together as one question: *"These questions help us find the right help for you. Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sh_suicidal_thoughts`<br>Thoughts of ending their life, without immediate danger<br>**Note:** The page lists a GP emergency appointment, NHS 111 and the crisis team for help that is not an immediate danger. The Where to get urgent help for mental health page says 111 or an urgent GP appointment. | "Thoughts of ending their life" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), ask your GP surgery for an emergency appointment, or contact your crisis team if you have one, today* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| `rf_sh_harm_others`<br>Thoughts of harming someone else, including a baby or child<br>**Note:** Clinical knowledge. If they feel they cannot keep someone safe, the emergency rule applies. | "Thoughts of harming someone else" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | **AI judgement, needs clinical review** | |
| `rf_sh_getting_worse`<br>Self-harm happening more often, or injuries getting more serious<br>**Note:** Clinical knowledge: self-harm that is getting worse raises the chance of serious harm or suicide. The Self-harm page says some people who self-harm are at a higher chance of suicide, and to get support as soon as possible. | "Self-harm happening more often or getting more serious" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | **AI judgement, needs clinical review** | |
| `rf_sh_wound_infected`<br>A wound from self-harm that may be infected<br>**Note:** The Self-harm page says speak to a GP about minor injuries because of the chance of infection. Making an infected-looking wound same-day is AI judgement. | "Self-harm wound may be infected" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |

## Thoughts of suicide or self-harm: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sh_self_harmed`<br>Has harmed themselves on purpose, with no sign of immediate danger | "Has harmed themselves on purpose" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*Speak to a GP. The source gives no fixed time, but it is important to get support as soon as possible.* | [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/) | |

## Default outcome

Used when no rule fires.

- **Thoughts of self-harm, or has self-harmed, with no thoughts of suicide and no sign of immediate danger**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *Speak to a GP. The source gives no fixed time, but it is important to get support as soon as possible.*
- Source: [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/)
- **Note:** Thoughts of ending your life are handled by the urgent rule above. A 'not sure' to that question keeps the outcome urgent.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Thoughts of suicide or self-harm, or has self-harmed | Have you had thoughts of ending your life, or of harming yourself? Or have you harmed yourself on purpose? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Has a plan to end their life, or may act on the thoughts soon | Have you made a plan to end your life? Or do you feel you might act on these thoughts soon? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Has done something to prepare to end their life | Have you done anything to prepare to end your life? For example, writing a note, giving things away, or getting hold of pills or something else to harm yourself with. |  | **AI judgement, needs clinical review** | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Taken an overdose, or swallowed something harmful | In the last few days, have you taken an overdose of a medicine or a drug, or swallowed something harmful? Answer yes even if you feel well. |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Serious injury from self-harm: deep, bleeding a lot, or a bad burn | Have you hurt yourself and the injury is deep, gaping open or bleeding a lot? Or have you burned yourself badly? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Voices telling them to harm themselves or someone else | Are the voices telling you to harm yourself or someone else? |  | **AI judgement, needs clinical review** | |
| Thoughts of ending their life | Have you been having thoughts of ending your life? | 6471006 | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Thoughts of harming someone else | Have you had thoughts of harming someone else? This includes thoughts of harming a baby or child. |  | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| Self-harm happening more often or getting more serious | Is the self-harm happening more often, or are the injuries getting more serious? |  | **AI judgement, needs clinical review** | |
| Self-harm wound may be infected | Is a wound from harming yourself getting more painful, red, hot or swollen, or leaking pus? |  | [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/) | |
| Has harmed themselves on purpose | Have you harmed yourself on purpose? For example, by cutting, burning or hitting yourself. |  | [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/) | |

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

### `advice_mh_overdose_or_injury`

**What to do:** Call 999 for an ambulance or go straight to A&E now, even if you feel well. Some overdoses do not cause symptoms for hours or days, but can still be very harmful.

**Look out for:**
- Feeling very sleepy, being sick, or breathing slowly
- Bleeding that will not stop, or blood coming out in spurts

**Get more help when:**
- Call 999 now if the person stops responding or stops breathing
- If you need someone to talk to, call Samaritans free on 116 123, day or night. Or text SHOUT to 85258.

**Where to go:** Call 999 or go straight to A&E. Do not drive yourself. Take any medicine packets or containers with you, so staff know what was taken.

**What you can do yourself:**
- Do not try to make yourself sick
- For a wound that is bleeding, press firmly on it with a clean cloth
- Do not eat or drink anything until you have been checked, unless a doctor says you can

Source: [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/), [Poisoning](https://www.nhs.uk/conditions/poisoning/), [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/)

### `advice_suicidal_thoughts_urgent`

**What to do:** Thank you for telling us. You do not have to cope with these feelings alone. Get help today: call NHS 111 and choose option 2 for mental health, or ask your GP surgery for an emergency appointment.

**Look out for:**
- Making a plan to end your life, or feeling you may act on your thoughts soon
- The thoughts getting stronger, or coming more often
- Feeling you cannot keep yourself safe

**Get more help when:**
- Call 999 or go to A&E now if your life is in danger. This includes if you have badly hurt yourself, taken an overdose, or feel you cannot keep yourself safe.
- Call Samaritans free on 116 123, day or night, if you need to talk. Or text SHOUT to 85258.
- If you are under 19, you can call Childline on 0800 1111

**Where to go:** Call NHS 111 and choose option 2, use 111 online, or ask your GP surgery for an emergency appointment today. If you have a crisis team, call them.

**What you can do yourself:**
- Tell someone you trust how you are feeling. Family or friends can help keep you safe.
- Try to focus on getting through today, not the future
- Stay away from alcohol and drug use, and be around other people if you can
- Do something you usually enjoy, such as spending time with a pet
- It may help to make a safety plan, for example with the Staying Safe website

Source: [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/), [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/)

### `advice_mh_urgent`

**What to do:** Get urgent help for your mental health today. Call NHS 111 and choose option 2 for mental health, or ask your GP surgery for an urgent appointment.

**Look out for:**
- Thoughts of ending your life or harming yourself
- Feeling you cannot keep yourself or someone else safe
- Hearing voices that tell you to harm yourself or others

**Get more help when:**
- Call 999 or go to A&E now if a life is in danger. This includes if someone has badly hurt themselves or taken an overdose. Or if you cannot keep yourself or others safe.
- Call Samaritans free on 116 123, day or night, if you need to talk. Or text SHOUT to 85258.

**Where to go:** Call NHS 111 and choose option 2, use 111 online, or ask your GP surgery for an urgent appointment today. If you have a crisis team, call them.

**What you can do yourself:**
- Tell someone you trust how you are feeling, and try to be around other people
- Stay away from alcohol and drug use

Source: [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/)

### `advice_self_harm_wound_urgent`

**What to do:** Ask your GP surgery for an urgent appointment, or call NHS 111, today. A wound that may be infected needs checking.

**Look out for:**
- Redness or swelling spreading from the wound
- Feeling hot and shivery, or very unwell
- Thoughts of ending your life

**Get more help when:**
- Call 999 or go to A&E if a wound is bleeding a lot, or you have taken an overdose. Do the same if you feel you cannot keep yourself safe.
- Call Samaritans free on 116 123, day or night, if you need to talk. Or call NHS 111 and choose option 2 for mental health.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online, today.

**What you can do yourself:**
- Keep the wound clean and covered with a clean dressing
- Wash your hands before touching the wound

Source: [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/)

### `advice_self_harm_gp`

**What to do:** Speak to a GP about self-harm. They will listen, and can help with treatment and support. It is best to get support as soon as you can.

**Look out for:**
- Thoughts of ending your life
- Self-harm happening more often, or injuries getting more serious
- A wound that gets more painful, red, hot or swollen

**Get more help when:**
- Call 999 or go to A&E if you have badly hurt yourself or taken an overdose. Do the same if you feel you cannot keep yourself safe.
- If you need help today, call NHS 111 and choose option 2 for mental health
- Call Samaritans free on 116 123, day or night, if you need to talk. Or text SHOUT to 85258. If you are under 19, you can call Childline on 0800 1111.

**Where to go:** Make an appointment with a GP. You can bring someone you trust with you.

**What you can do yourself:**
- Keep any wound clean and covered
- When you feel the urge to self-harm, try to wait, distract yourself, or talk to someone
- Tell someone you trust what is going on for you

Source: [Where to get help for self-harm](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/self-harm/getting-help/), [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sh_plan`: The page says call 999 or go to A&E if you feel you may be about to harm yourself. Reading a plan, or feeling you may act soon, as that is AI judgement.
- `rf_sh_preparing`: Clinical knowledge: preparing (a note, giving things away, gathering the means) is a sign of high immediate danger. Treated like the source's 'about to harm yourself'.
- `rf_sh_overdose`: The Poisoning page says the same, and that symptoms may take hours or days to start.
- `rf_sh_voices_harm`: Clinical knowledge: voices telling someone to harm themselves or others, together with thoughts of suicide or self-harm, need assessment now.
- `rf_sh_suicidal_thoughts`: The page lists a GP emergency appointment, NHS 111 and the crisis team for help that is not an immediate danger. The Where to get urgent help for mental health page says 111 or an urgent GP appointment.
- `rf_sh_harm_others`: Clinical knowledge. If they feel they cannot keep someone safe, the emergency rule applies.
- `rf_sh_getting_worse`: Clinical knowledge: self-harm that is getting worse raises the chance of serious harm or suicide. The Self-harm page says some people who self-harm are at a higher chance of suicide, and to get support as soon as possible.
- `rf_sh_wound_infected`: The Self-harm page says speak to a GP about minor injuries because of the chance of infection. Making an infected-looking wound same-day is AI judgement.
- `thoughts_of_suicide_or_self_harm default outcome`: Thoughts of ending your life are handled by the urgent rule above. A 'not sure' to that question keeps the outcome urgent.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| An overdose, or poisoning from a medicine or drug | 1149222004 | very rare | Taken an overdose, or swallowed something harmful: strongly supports; Very unwell after taking a drug: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Breathing slowly or unevenly: supports; Feels sick or has been sick: supports; Heart beating very fast: supports |
| Self-harm (hurting yourself on purpose) | 248062006 | rare | Has harmed themselves on purpose: strongly supports; Self-harm happening more often or getting more serious: supports; Self-harm wound may be infected: supports; Serious injury from self-harm: deep, bleeding a lot, or a bad burn: supports; Feels worthless or very guilty: supports |
| Stress, worry or low mood, or a reaction to grief or a difficult life event |  | common | Something very upsetting happened recently: strongly supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports; Going through a stressful time or big life change: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Problems remembering things: supports; Very sleepy or falling asleep during the day: supports |
| A suicidal crisis (a high chance of acting on thoughts of suicide) | 394685004 | very rare | Has a plan to end their life, or may act on the thoughts soon: strongly supports; Has done something to prepare to end their life: strongly supports; Cannot keep themselves or someone else safe: strongly supports; Thoughts of suicide getting stronger or more frequent: supports; Feels hopeless, or that things will never get better: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
