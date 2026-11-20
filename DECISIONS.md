# Decisions

Each significant choice and the reason for it. Newest sections at the bottom.

Items marked **OWNER TO CONFIRM** were made by the build so that work could
continue. They are clinical or policy calls and should not be treated as settled.

## Decisions made by the owner (brief v0.2)

1. **Sourced rules decide the outcome. Probabilities only choose questions.**
   The probabilities would be AI estimates, so an outcome resting on them could
   not be defended.
2. **Only an emergency red flag stops the session early.** A less serious red
   flag sets a minimum outcome, and the rest of the red-flag screen is still
   completed so that a more serious flag is not missed.
3. **The risk rule is kept as a switched-off experiment.** It can be turned on
   in `settings.yaml` later, where published research gives real figures. It
   reports separately and never changes the outcome.
4. **Personal, standalone project.** No NHS branding, no links to NHS systems,
   no Langfuse export, no SNOMED code checking. SNOMED fields are left empty.
5. **Run locally for now.** Hosting is deferred. The design still meets the
   hosting requirements in the brief (section 4.7).

## Step 2: skeleton

6. **The engine keeps nothing between turns.** Each call is given all the
   answers so far and works everything out again. This is simple, makes the
   engine easy to test, and means a hosted demo would never need to store what
   a visitor enters.
7. **Every finding is answered yes, no or not sure.** One answer shape keeps
   the rules and the code simple. Things like duration are asked as a yes or no
   question ("more than a week?"). Age-based findings are worked out from the
   age when it is given as context.
8. **Red flags are asked together in "screens".** A screen is one "do any of
   these apply?" question covering several red flags. Every red flag has to be
   checked, so asking them one at a time saves nothing and costs many
   interactions. The simplest sore throat case went from 13 interactions to 9.
   The trade-off is that each screen is longer to read, so the record reports
   both the number of interactions and the number of items shown.
9. **"Not sure" to a whole screen means its items are then asked one by one.**
   Otherwise one "not sure" would mark every red flag as unknown and send
   everyone to an emergency outcome.
10. **Non-red-flag questions are only asked if the answer could raise the
    outcome.** Once a rule at some level has fired, questions that could only
    lead to the same or a lower level are skipped. This is where adaptive
    questioning saves interactions.
11. **Outcomes are compared on acuity, level of care and timeframe only.** The
    explanatory detail text does not make two outcomes different.
12. **Ties are broken in a fixed order:** most urgent first, then a rule that
    definitely fired before one chosen out of caution, then the order in the
    files. This is what makes the engine deterministic.
13. **Source pages are kept as text snapshots in `sources/nhs_uk/`.** This lets
    a reviewer, or a separate session writing test cases, see exactly what the
    content was drafted from and when.
14. **Examples are not evaluation cases.** The files in `examples/` were written
    alongside the knowledge base, so they prove the engine runs. They say
    nothing about how well it triages.
15. **Dependencies so far: PyYAML, pydantic, pytest.** FastAPI and uvicorn will
    be added with the API.
16. **Patient sex is not used yet.** The brief asks for how common a cause is
    by age and sex. Age is supported. Sex can be passed in but no content uses
    it yet. All of this only affects question order.

## Clinical and policy calls: OWNER TO CONFIRM

17. **How NHS website wording maps to the working scales.** For example "See a
    GP" becomes routine, general practice, no fixed time, because the website
    labels that advice "non-urgent". It could arguably be "soon". The full
    mapping is written at the top of `knowledge_base/settings.yaml`.
18. **When two source pages disagree, the more urgent one is used**, and the
    difference is written in the rule's note. This follows "when unsure, go
    up", but it will over-triage in places. There are three such cases in the
    chest pain module.
19. **Two chest pain rules rest on an AI reading of the source**, not a direct
    statement: pain that is worse on breathing in, and pain or swelling in one
    leg. Both are treated as urgent. They are marked in the module file.
20. **"Are you worried about your symptoms?" is kept for sore throat** because
    the source lists it as a reason for urgent advice. It is likely to
    over-triage and needs a clinical decision.
21. **The "not covered" outcome is urgent, urgent care, today.** The source
    says to get help from NHS 111 if you are not sure what to do. Treating
    that as "urgent" is a cautious placeholder.
22. **Safeguarding is not screened.** The working levels of care have no route
    for a non-medical safety need, so it is unclear what outcome to give.
23. **Thoughts of suicide without immediate risk are not screened.** Only
    serious self-harm or feeling about to self-harm is, as an emergency. Mental
    health routes come in a later wave.
24. **Two source pages were past their own review date when accessed**
    (Chest pain, and the urgent and emergency care pages). They were used
    anyway, and this is noted in the source log.

## Independent check of Wave 0 content

An independent session compared the drafted content with the source pages. It
did not edit anything. Its report led to these changes.

25. **Chest pain: pain that is there now is an emergency. The "see a GP"
    default applies only once the pain has stopped.** The Pulmonary embolism
    page says 999 or A&E for "pain in your chest". The Chest pain page says to
    see a GP for pain that comes and goes or has gone. Following both gives this
    split, and it removes the earlier exception to "the more urgent source
    wins". The owner asked for a pragmatic resolution. It will over-triage some
    ongoing pain that is not serious, and it is listed for clinical review.
    NICE guidance was not used: the brief bars it until permission is confirmed.
26. **Missed red flags were added:** chest pain with passing out (emergency),
    and sudden confusion as a universal red flag (emergency). The second is
    listed in the source for people who are short of breath, so checking it for
    everyone is AI judgement.
27. **Question wording was corrected where it had drifted from the source:**
    signs of a stroke (now includes "you think you are having a stroke" and two
    more signs), "pale" not "very pale", "tight or squeezed" without "heavy",
    and "swelling inside the mouth and throat" not "mouth or throat".
28. **Advice now names every emergency and urgent sign the rules use.** Separate
    advice was added for worsening angina, for coughing up blood, and for a
    lump or mouth ulcer, so the advice matches the reason for the outcome.
29. **Screens no longer carry a source.** A screen is a way of asking several
    questions together. Each finding and each rule in it has its own source.
    Two citations were also corrected.

## Step 3: harness

30. **Vignette authors see only the source pages, the format and the question
    list.** The owner agreed the question list could be shared. It holds each
    question's id and wording and nothing about rules, outcomes or advice.
    Without it the simulated patient could not answer the engine's questions.
31. **Authors are not told how source wording maps to the outcome scales.**
    They choose for themselves. So some disagreements (for example "routine"
    against "soon") are differences of mapping, not of triage. That is
    deliberate: it keeps the cases independent, and those disagreements are
    logged for clinical review.
32. **Every quote a vignette cites is checked by machine** against the saved
    source page. A vignette whose quote is not on the page is refused. This
    stops invented sources.
33. **The main run gives the engine full patient context, and answers "no" to
    anything the vignette does not mention.** The "not sure" run is a separate
    stress test (owner decision).
34. **What counts as a red flag being detected.** The engine must have
    established every finding that makes up the red flag, and the outcome must
    be at least as urgent as the vignette says the flag needs. Two special
    cases: if the engine had already reached an emergency outcome and stopped,
    a flag it never asked about counts as passed, because the owner's rule is
    never to ask more after an emergency. If a vignette's red flag cannot be
    expressed with any question on the list, it counts as failed, because the
    engine has no way to find it.
35. **"Advice is specific to the case" is only a word check.** Each vignette
    lists what the advice should mention and words to look for. A proper
    judgement of advice quality needs a person.
36. **The fixed-order baseline** asks every question one at a time in file
    order and stops only for an emergency outcome. It uses the same rules, so
    any difference in outcome from the engine would be a defect.
37. **Consistency in structured mode** is tested two ways: the same case
    repeated, and the same patient volunteering more or less at the start.
    Reworded opening statements are stored now and will be used when the
    conversational mode exists.
38. **Published vignette sets get a coarse comparison only** (emergency,
    non-emergency, self-care), are converted by a separate session, and are
    reported separately as a sense check.
39. **The disagreements log and the review packs are generated**, so they
    always match the latest run and the current knowledge base.

## Wave 0 evaluation

40. **Two content defects found by the development set were fixed**, because
    the sources clearly supported the test cases. A "heavy" chest is now a red
    flag for chest pain. Stable, diagnosed angina that settles as usual now
    gets self-care with the angina treatment instructions, not urgent help.
41. **The engine gained "default exceptions".** Rules can only raise an outcome
    above a module's default. An exception is the one way to go below it, for a
    specific sourced situation. If an exception cannot be settled, it is not
    applied, so missing information never lowers an outcome.
42. **When the question list changes, the case authors update their own
    mapping.** The session that writes the content never edits a test case. The
    authors were told to leave stories, expected outcomes and sets unchanged.
43. **The remaining disagreements were left alone and logged** in
    `review/disagreements.md`. They are differences between source pages,
    differences in how wording maps to the scales, or the points in item 45.
    None is a case where the source clearly supports the test case.
44. **The holdout set was run once, after the fixes, and not tuned against.**
    It showed no gate failure and no new kind of problem, so it was not
    replaced.
45. **After an "A&E" emergency, the engine checks for ambulance-level signs
    before stopping** (owner decision, brief v0.3). Stopping on any emergency
    had lost the difference between "call 999" and "999 or A&E" in three test
    cases. The engine now stops at once only on the most urgent outcome.
    Otherwise it asks just the emergency red-flag questions that could still
    raise the outcome, which is one or two questions, and then stops. Because
    this changed the engine after the holdout set had been run, the holdout
    results are no longer from unseen cases. A fresh holdout set should be
    written before Wave 1 results are relied on.
46. **The published wording of external vignettes is not stored**, only facts
    about each case. The brief says not to copy journal text, and it is not
    confirmed that the article's licence covers wording gathered from third
    parties.
47. **The "not sure" stress test matched the main run** because the authors
    listed an answer for every question. It will only bite when cases leave
    things unstated.
48. **Coverage is reported against the NHS website Symptoms A to Z** by
    `python triage.py coverage`.

## Conditions and SNOMED CT codes in the output (brief v0.4)

49. **The output follows the shape of other condition-based engines, not their
    method** (owner decision). It now carries a ranked list of possible
    conditions, each with an id, medical name, common name, likelihood, the
    acuity it would need and a SNOMED CT code. Sourced rules still decide the
    outcome. Conditions do not, because their likelihoods are AI estimates.
50. **SNOMED CT codes are proposed from memory and then checked in the NHS
    SNOMED CT Browser, UK Edition** (owner decision). The name the browser
    returns is recorded in `sources/snomed_codes.yaml`. The engine refuses to
    load a code that is not in that log.
51. **A code is used only where the concept means the same as the question.**
    21 of 49 findings and 10 of 13 conditions have one. The rest are left
    empty, mostly because the question combines several things (for example
    "feel sick or have been sick") and no single concept fits. Checking caught
    three codes or names remembered wrongly. Two codes (light-headedness and
    coughing up blood) could not be checked because the browser returned an
    error, so they are left empty.
52. **Matching a concept to a question is AI judgement.** The check confirms
    the code exists and what it is called. It does not confirm it is the right
    concept for the question. That needs clinical or terminology review, and
    the review packs now show each match.

## Condition-based method (brief v0.5)

53. **Likely conditions now influence the outcome** (owner decision). The aim
    is to mock up how a commercial condition-based engine would
    perform, and it will never be used clinically. So best-judgement estimates
    are used where no more accurate figure exists. This reverses item 1.
54. **The outcome is the most urgent of the rules and the condition-based
    level.** The condition-based level is the first acuity level, working down
    from the most urgent, where the chance of a condition needing that level or
    more exceeds its threshold. Thresholds are in `settings.yaml`.
55. **Likely conditions can raise an outcome but not lower it.** This keeps the
    sourced red flags and rules as a floor. Whether they should also lower it
    is open decision 11 in the brief.
56. **A suspected emergency from likely conditions does not stop the
    questions.** Only an emergency shown by the patient's own answers does.
    More answers are what confirm or rule out a suspicion.
57. **New questions tell the possible conditions apart** (for example whether
    chest pain comes on with effort). One is asked only if a yes or a no would
    move the chance of a more serious condition by at least 5 points, and at
    most 6 are asked. The one expected to move it most goes first.
58. **"Comes on with effort" and "comes and goes" count as one piece of
    evidence**, so a "no" to one does not cancel a "yes" to the other.
59. **Stopping is no longer exact in this mode.** The engine stops when no
    answer is likely to change the outcome, so the fixed-order baseline, which
    asks everything, can occasionally end somewhere different. In "rules only"
    mode the two still always agree.
60. **The risk setting sweep is built** (`python triage.py sweep`). It reruns
    the development cases with conditions off and at four levels of caution.
61. **The test cases predate the new questions.** Their authors have not yet
    said how each patient would answer them, so the simulated patient says "no"
    and likely conditions rarely come into play. The cases need updating, and
    new cases written, before the results say much about this method.

## Conditions can lower outcomes, with a risk balance (brief v0.6)

62. **Likely conditions can now lower an outcome as well as raise it** (owner
    decision). This replaces item 55.
63. **Firm rules are a floor. Soft rules and defaults give way to the
    conditions.** Each rule is firm unless marked `soft: true` in its module
    file. Four are soft today: ongoing chest pain, chest pain that comes and
    goes, chest pain worse on breathing in, and being worried about a sore
    throat. These were chosen because the source pages disagree about them, or
    they rest on an AI reading, or they are not signs of illness.
64. **Risk balance through uneven thresholds** (owner direction). A 5% chance
    of an emergency condition is enough for an emergency outcome. An urgent
    condition needs 15%, "soon" 25% and routine 35%. Below all of those the
    level is self-care. The numbers are best-judgement placeholders.
65. **An outcome is lowered only when something explains the patient.** A
    finding the patient said yes to must point to a condition that is at least
    20% likely and needs no more than the lower level. That finding cannot be
    the one that triggered the rule being lowered. And if "something not on
    the list" is 50% likely or more, nothing is lowered. This stops a run of
    "no" answers from sending someone to self-care.
66. **A soft emergency rule does not stop the questions.** Only an emergency
    firmly shown by the patient's answers does, because the follow-up answers
    are what confirm or lower a soft one.
67. **Question choice weights conditions by seriousness.** A question is asked
    if an answer would noticeably move the amount of serious illness in play,
    or would change the outcome outright. At most 8 such questions are asked.
68. **The test cases are being updated for the new questions, and the holdout
    set replaced**, by their original authors. The old holdout set had been run
    several times and no longer counted as unseen.

## Danger classes (brief v0.7)

69. **Danger classes replace the single per-level thresholds** (owner
    decision). Each condition is critical, serious, moderate or minor, by how
    bad a miss would be. Starting lines, all best judgement, to tune:
    critical possible 1% / likely 3%; serious 5% / 15%; moderate 15% / 30%;
    minor 30% / 50%. "Likely" gives the level the condition needs; "possible"
    gives one step below. This replaces item 64.
70. **Conditions in the same class needing the same level are added
    together**, so several small chances of something dangerous are not each
    ignored.
71. **A symptom's default can be a floor** (`floor: true`). The chest pain
    default is, because the source says to get medical advice for any chest
    pain. This was found by the test cases: five chest pain cases had been
    lowered to self-care when a minor cause was very likely.
72. **A condition the patient is already diagnosed with** (`diagnosed_by`) does
    not on its own raise the outcome. Found by the test cases: stable,
    diagnosed angina was being sent for urgent help because angina was likely.
73. **Questions are asked if an answer could move the danger-weighted risk by
    1 point** (was 3). At 3 the engine never asked about swollen glands or
    tiredness, so it could not notice glandular fever. This adds about one
    question to an ordinary case.
74. **The holdout set was run three times during this work.** Two of the fixes
    above were prompted by development cases, but the same problems also
    showed in the holdout set, so it can no longer be treated as unseen.
    A fresh holdout set is needed before results are relied on.

## Plain language (brief v0.8)

75. **Plain language is enforced, not just aimed for** (owner request). A list
    of medical words is in `knowledge_base/plain_language.yaml`. Each has a
    plain meaning and the phrases that count as explaining it. If a question,
    advice entry or condition name uses the word without one of those
    phrases, the engine refuses to load. Reviewers can add words.
76. **The names of possible conditions lead with plain words**, with the
    medical term in brackets, for example "Angina (chest pain caused by
    narrowed blood vessels to the heart)". The medical name is kept
    separately in the record for evaluators.
77. **Reading level is measured** with the Flesch-Kincaid grade, a rough
    standard formula. All patient text has a median of grade 3.7, about a
    reading age of 9. No line of 10 or more words may be above grade 9. The
    formula is unreliable on short phrases, so those are not held to the
    per-line limit. Long sentences were split to meet it.
78. **Questions can be "only asked if"** another answer is yes. "Is your
    angina worse than before?" is only asked after "yes, I have been
    diagnosed with angina". Found by walking through a made-up patient.
79. **Not yet covered by the plain-language check:** the plain-English
    rationale, which uses the short labels of findings. It is written for
    evaluators as much as patients, and a patient-facing version is a job for
    the demo page.
80. **The NHS digital service manual's "A to Z of NHS health writing" is now
    built in** (owner suggestion). It lists words people misunderstand and
    what to use instead, based on NHS user research. 33 of its word swaps that
    apply to triage text (for example "fever" to "high temperature", "nausea"
    to "feeling sick", "risk" to "chance", "chronic" to "for a long time") are
    in `knowledge_base/plain_language.yaml`, and the engine refuses to load
    patient text that uses them. It is under the Open Government Licence. A
    snapshot is in `sources/`.
81. **Medical words the A to Z does not cover** (angina, tonsils, CPR and so
    on) stay on the "explain" list, with AI-drafted explanations for review.
82. **The reading level check is a rough guard, not proof.** The service
    manual's health literacy guide recommends readability scores only to help
    prioritise, and testing with real users to know whether content works.

## Independent design and evaluation review

Two independent reviews were run: one probed the engine's logic with about
90,000 made-up patients, the other looked at the harness from the evaluation
programme's point of view. Every finding was reproduced before it was acted on.

83. **The outcome is now the most urgent of three parts:** firm rules (a
    floor), the level each symptom's likely conditions call for (can only
    raise), and soft rules and ordinary defaults, each lowered only on its own
    evidence. Before, a danger sign could make a milder cause count as
    "explaining" the patient and lower the outcome. Now adding a danger sign can
    only raise it, and a test checks this on hundreds of made-up patients.
84. **Each presenting symptom's conditions are weighed separately.** Two
    symptoms can have two causes. One symptom's conditions can no longer
    dilute or lower the other's.
85. **A "settled as usual" exception applies only when no rule fired**, and the
    stable angina exception now requires the pain to have stopped. This closed
    a route below the chest pain floor.
86. **"Not sure" never blocks a question the way "no" does.** Being unsure
    about a diagnosis had jammed the engine at "ambulance" with no questions.
87. **A rule held only out of caution is never lowered.** Missing information
    cannot be explained away. (Simpler than the reviewer's proposal to
    recompute as if the answer were yes.)
88. **Red-flag questions do not count towards the question limit**, so they can
    never be cut off. There are a fixed number of them.
89. **A main symptom this tool does not cover keeps its cautious default** even
    when a covered symptom comes with it.
90. **Condition questions are only asked about danger that could still change
    the outcome**, that is, conditions needing more than the outcome already
    guaranteed. The reviewer suggested "only if one answer changes the
    outcome", but that would bring back the problem in item 73 (some
    conditions need two answers before either changes the outcome).
91. **Adult background questions are not asked about children under 16.**
92. **Related findings: a "yes" always beats a "no" in the same group.** Item 58
    is now implemented properly ("comes on with effort" and "comes and goes"
    count as one piece of evidence).
93. **When no age is given, the more cautious starting likelihood is used.**
94. **Not changed: chances are not added across danger classes.** A small chance
    of angina and a larger chance of a chest infection mean different things.
95. **Lowered outcomes are always reported** as AI judgement, naming the rule
    overruled, the milder cause and the finding that pointed to it, even when a
    floor then decides the outcome.

Harness:

96. **The red-flag gate is now about escalation** (was the outcome at least as
    urgent as the flag needs?). Recognition (did the engine find and name it?)
    is a separate score. This removes unfair failures where an engine escalated
    correctly without asking every part of the flag.
97. **The gates are always shown next to over-triage and two useless
    reference engines.** "Always 999, ask nothing" passes both gates on every
    case, so the gates alone mean little.
98. **Ambulance versus A&E is a score, not a gate**, because many sources say
    "999 or A&E" together.
99. **Burden is reported in items and words read**, not "questions", because a
    checklist of 11 items counted as one question flattered the engine. In
    those units the engine reads about the same as asking everything.
100. **The context test now asks whether context led to an outcome at least as
     close to the expected one, and safe.** The old test marked the engine down
     for already being cautious without the context.
101. **Honest labels and baselines:** the variant measure says it tests
     volunteering, not rewording; the safety-netting word check is shown next to
     what one fixed advice text would score; agreement and gates show 95%
     ranges; every report is stamped with the date, versions and git commit.

## Phase 1: the network engine (brief v1.0)

102. **Owner decisions:** match the architecture of commercial condition-based
     engines; aim for full condition coverage; keep NHS red flags as a
     firm floor; allow research and public statistics as sources; no clinical
     review at all. This is a demonstration and proof of concept.
103. **The knowledge base is now one network.** Observations live in
     `observations/`, one file per body system. Each condition is a card in
     `conditions/<body system>/<id>.yaml`. Each main symptom's sourced rules,
     checklists and default are in `entry_symptoms/`. A card's
     `entry_symptoms` says which main symptoms make it a candidate, so one
     condition can belong to several.
104. **Observations can have a parent** with a relation (duration, severity,
     character, what makes it worse or better, location, radiation), as in
     the condition-based engines. A "yes" to a child means "yes" to the parent.
     A "no" to the parent means "no" to its children, which are then never
     asked and never count as missing information. A parent is always asked
     before its children. Loops of parents are refused when the network loads.
105. **Carer wording, sex filter and seriousness** are supported on every
     observation. None of the current content uses them yet.
106. **Every question carries a reason code** (red-flag checklist, red flag,
     sourced rule, condition, default exception) as well as a reason in plain
     words.
107. **The record includes a five-level summary** (ambulance, emergency
     department, see a doctor within 24 hours, see a doctor, self-care) with a
     root cause and the serious evidence found, in the shape condition-based
     engines use. The mapping from this engine's scales is AI judgement.
108. **Behaviour was kept identical.** Before the rebuild, the engine's outcome,
     every question asked, the deciding rule, the red flags and the condition
     likelihoods were saved for 1,576 patients (all test cases, all examples
     and 1,500 made-up patients). After the rebuild all were identical, except
     that conditions with exactly equal likelihoods can now be listed in a
     different order, because the cards load in file order.
109. **Sources widened** (owner decision). NHS pages stay the source for red
     flags and outcomes where they cover them. Otherwise content may use
     published research and public statistics, and the AI's own clinical
     knowledge, labelled "AI judgement". Licensed content (NICE, CKS, BNF) is
     still not copied.

## Phase 2: tools and inference

110. **A noisy-OR Bayesian network is now the default inference method.**
     Several conditions can be present at once, and evidence for one can
     explain away a symptom that points to another. It is the closest published
     equivalent to the "modified Bayesian networks" condition-based engines
     describe. It is calculated exactly ("Quickscore"), checked against a
     brute-force calculation on 120 random patients, and gives the same answer
     every time. Single-cause naive Bayes stays available as a setting.
111. **Why it became the default:** on the development set it matched more
     acuities (42 against 40 of 48) with less over-triage (6 against 8), fewer
     items read, and both gates still passing. On the holdout set it was level
     (14 of 16 each), with two cases more cautious. All design-property tests
     pass under both methods.
112. **Known limitation of the network method:** a link can only make an
     observation more likely, so links marked "argues against" are ignored by
     it. Content that needs that meaning should link the condition to the
     opposite observation.
113. **In the network method, "something not on the list" means "none of the
     listed conditions is present"**, and the likelihoods do not add up to 1.
114. **Network checks.** Loading now refuses an entry symptom with no condition
     cards, and a SNOMED CT code used for two different concepts (a diagnosis
     question and its condition may share one). `python triage.py check` also
     warns about observations nothing uses, and conditions with fewer than two
     observations pointing to them.
115. **A SNOMED CT tool for content building** (`snomed-search`, `snomed-add`)
     queries the NHS SNOMED CT Browser and adds checked codes to the log. It is
     not part of the engine, which makes no network calls. It confirmed the two
     codes that could not be checked before (light-headedness, coughing up
     blood), which are now added.
116. **Checklists use short lines.** Each checklist item has a short form; the
     full question is used when it is asked on its own. Words read per case on
     the development set fell from 388 to 225, against 382 for asking
     everything. Outcomes did not change. Short lines are written to read the
     same for a patient or a carer, so carer wording only replaces full
     questions.
117. **Content pipeline tools and instructions** are in `pipeline/`: a source
     fetcher that saves dated snapshots and logs them, condition self-tests
     (`python triage.py selftest`), and written instructions for the drafting
     and checking agents. The self-tests already show one content weakness: a
     textbook blood clot in the lung ranks fourth among chest pain conditions.
     This is left for the pilot.
118. **Engine-agnostic test cases are deferred.** The fully engine-agnostic
     approach is a simulated patient that reads plain facts and answers any
     engine's questions in its own words, which needs a language model. That
     waits for the language-model decision. Test cases stay in the current
     format meanwhile.

## Phase 3: the chest and breathing pilot

119. **Age bands are "below", not "up to and including".** "Under 5" had been
     stored as "4 or under", so a child of four and a half counted as not under
     5. Added standard observations for under 1, under 16, 65 or over, female
     and male, which condition cards can use to change how common a condition
     is.
120. **Likelihood results are remembered within a run**, since choosing a
     question asks the same thing many times. The answer depends only on the
     method, symptoms and answers, so results are unchanged. The development
     evaluation runs in under 7 seconds instead of 11.
121. **Pilot foundation drafted** by an agent: 98 new observations (36 with a
     parent), entry-symptom files for breathlessness, cough, palpitations,
     coughing up blood and wheezing, and 27 advice entries. A "yes" to one of
     those symptoms during a chest pain session now brings its own red flags in.
122. **A gated question is "no" when its gate is "no"** (for example "is your
     angina worse than before?" for someone with no angina), so a rule using it
     is settled rather than left unknown and treated cautiously. Such a "no" is
     not evidence about any condition, because the question does not apply.
123. **Lowering needs distinguishing evidence.** A finding can only explain a
     patient towards a milder condition if it points to that condition more
     than to any condition needing more urgent care. This closed a remaining way
     a danger sign (a family history of heart disease) could lower an outcome.
124. **The content tools (SNOMED, fetch) run even while the knowledge base does
     not load**, so drafting agents can use them mid-edit.
125. **Heart and chest-wall cards drafted** by an agent: 8 new and 7 updated.
126. **Within an entry symptom, its own main symptom is not evidence.** The
     starting chances on the cards are already among people with that symptom,
     so counting it again inflated every condition linked to it.
127. **Chest-pain-specific questions are only asked if there is chest pain**
     (for example "is the pain there now?"). For a breathless patient with no
     chest pain they do not apply, and so are not evidence. Chest tightness and
     heaviness are not gated, because asthma can cause them without pain.
128. **Old holdout cases moved into development; fresh holdout sets written**
     for all seven entry symptoms, plus mixed-symptom cases: 140 development
     and 54 holdout cases in all.
129. **Files split for parallel building.** Advice is now one file per body
     system in `knowledge_base/advice/`. Sources and SNOMED codes can be logged
     per body system (`sources/source_logs/`, `sources/snomed_codes/`) with the
     `--log` option of `fetch-source` and `snomed-add`. This lets several body
     systems be built at once in separate copies and merged without clashes.
130. **Entry symptoms can say which other Symptoms A to Z pages they cover**
     (`also_covers`), for example foot pain covering heel pain. Coverage counts
     them.
131. **A "dentist" level of care** was added, and a condition card can name the
     level of care it needs when it is not the usual one for its acuity (for
     example a tooth abscess needs a dentist, not a GP).
132. **Breathing and airway cards drafted** by an agent: 21 new cards, chest
     infection reworked as the middle tier between bronchitis and pneumonia,
     and observations and rules for every content gap the case authors found.
133. **Red-flag questions never count towards the question limit** (only the
     other questions do), so condition questions are not crowded out.
134. **Self-tests use a typical age for each condition and volunteer its main
     features**, so they test whether a card is recognisable, separately from
     question choice. 83 of 84 pass.
135. **Flu-like symptoms in someone at higher risk now give urgent without a
     test**, as the NHS flu page says. Found by two development cases.
136. **An entry symptom's own main symptom can set starting chances, but is
     still not evidence.** Before, it was hidden from both, so a card could
     only have one starting chance for all its entry symptoms (asthma was 4% in
     people who wheeze). Now `prevalence_when` can key on it: asthma starts
     common among people who wheeze and uncommon among people who cough.
     Found by the independent check of the pilot.
137. **A "very rare" starting chance (0.2%)** for diseases that only become
     plausible with a telling sign. Tuberculosis, lung cancer, lung scarring
     and bronchiectasis start very rare and become rare with, for example, a
     cough for 3 weeks or coughing up blood. This stops them driving questions
     for an ordinary cold. Other starting chances adjusted by the check: a cold
     is very common; heartburn uncommon except with chest pain; hay fever and
     bronchitis rare under 5; COPD, lung cancer and lung scarring very rare
     under 16.
138. **Checklists below the red-flag levels.** An entry symptom can group its
     "see a GP" signs into one checklist (level `routine`). It is asked after
     the red flags, only if it could still raise the outcome, and counts as one
     ordinary question. A plain cold went from 20 questions to 15.
139. **Pilot check content fixes:** breathlessness with a tight or heavy chest is
     firm A&E for people without asthma (soft for people with asthma);
     breathlessness with fainting is A&E (Pulmonary embolism page); with
     sweating or light-headedness is soft A&E (AI judgement); with a reason for
     a blood clot (operation, long journey, earlier clot, pregnancy, cancer) is
     soft urgent. Yellow or green phlegm needs a high temperature,
     breathlessness or feeling very unwell to be urgent. Sharp chest pain is
     soft. SVT now needs routine care with moderate danger. A new critical card
     for a dangerous heart rhythm (very fast or very slow) and a new question
     about a very slow heartbeat, with red flags for a very slow heartbeat with
     feeling faint, fainting, chest pain or breathlessness.
140. **Chest pain that comes and goes is urgent only when it looks like
     angina** (brought on by activity, tight or squeezing, or with heart risk
     factors). Otherwise it falls to the default, see a GP, as the Chest pain
     page says. **Cough with breathlessness is now soft urgent**, and a new
     firm rule keeps cough with difficulty breathing at urgent. Development
     acuity match went from 111 to 114 of 140, with both gates still 100%.
141. **A known limit of adaptive questioning: a second main symptom that is
     never mentioned or asked about cannot bring in its own red flags.** Found
     when the general body system made "high temperature" an entry symptom: a
     child with chest pain, a high temperature and a stiff neck reached 999
     only if the temperature question happened to be asked. A "gateway" step
     (ask about other main symptoms whose red flags could raise the outcome)
     was tried and rejected: it added 2.6 questions per case on average, and 5
     to a sore throat with a temperature, with no gain in accuracy. Patients
     usually mention their main symptoms at the start. The design property
     test now has the patient mention what is true up front, so it tests the
     decision logic rather than the question path.
142. **Speed.** At most 10 "yes" answers (the strongest) are used in the exact
     calculation, down from 14: 0.013 seconds instead of 0.23 for one
     calculation, with identical development results. The harness now runs
     each case in one pass instead of replaying it after every answer
     (the stateless API is unchanged). The development evaluation went from
     4.5 to 2.5 minutes.
143. **The exact likelihood calculation works on whole tables at once (numpy)**
     instead of one combination of answers at a time. Same results (checked
     against brute force), about 7 times faster on heavy cases; the
     development evaluation now takes 1.5 minutes, down from 4.5. numpy is
     added to the requirements for this.
144. **The design property test now gives each made-up patient 4 true signs**,
     not 12% of all signs. With the larger network, 12% meant nearly every
     patient already needed 999, so the test could not catch a lowered
     outcome.
145. **Speed is never a reason to simplify the engine's reasoning.** Owner
     decision: if the engine needs more computing power, it can be hosted on
     a bigger server. With the faster calculation (143), the cap on "yes"
     answers used in the exact calculation goes back to 14 (it was lowered to
     10 in 142): one calculation now takes 0.02 seconds at 14. Same
     development results, same run time.

## Phase 4: merging the body systems

146. **Ten body systems merged into one network.** Where two or more systems
     built the same condition, there is now one card, in the folder that fits
     best, with the entry symptoms and findings of all of them (the stronger
     band where they differed) and the more cautious danger and level of care.
     Where the starting chance differed by entry symptom, the card keeps one
     base and sets the others with `prevalence_when` on the entry symptoms'
     main observations. These lines are ordered high to low after any risk
     factors and age bands, so a patient with two entry symptoms gets the
     higher starting chance. One exception is marked "keep first" (middle ear
     infection among people with a high temperature, so young children with a
     high temperature do not start at "very common").
147. **One observation per concept.** Same concept, different ids: one id was
     kept and every reference renamed. Ids used by the test cases were always
     kept. Questions that combined several concepts (for example "stiff neck
     with a high temperature or a very bad headache", "very thirsty and
     peeing a lot", "blood in pee or poo") were replaced by rules over the
     single observations. Different specificity became a parent and child
     (for example leg weakness under "pain, tingling, weakness or numbness in
     both legs", arm and leg tingling under pins and needles, high ketones
     under high blood sugar or ketones). Observations were moved to the body
     system they belong to; general history and age bands are in
     `observations/general.yaml`.
148. **Drowsiness:** adults are asked "much sleepier than usual, or hard to
     wake" (`drowsy_hard_to_wake`, 16 or over) and children "limp, floppy or
     hard to wake" (`child_floppy_or_hard_to_wake`). Rules from the brain and
     nerves, urinary and mental health systems that used their own drowsiness
     question now use either of the two.
149. **Kept separate on purpose:** stroke and stroke affecting vision; eye
     stroke and retinal vein occlusion; shingles, shingles near the eye and
     shingles of the ear; hepatitis and other liver problems; leukaemia and
     cancer of the bones or blood in a child with a limp; sickness in
     pregnancy and severe sickness in pregnancy; anxiety or panic and
     generalised anxiety; acute kidney injury and longer-term kidney problems;
     stress or relationship problems (for sexual problems) and stress or low
     mood.
150. **Cross-links between systems**, as the build reports asked: back pain to
     aortic aneurysm, kidney stones and kidney infection; neck pain to
     meningitis; cellulitis to foot and hand pain; pre-eclampsia to headache;
     carpal tunnel and sciatica to pins and needles; pelvic pain and stomach
     pain in pregnancy to appendicitis, UTI, kidney stones and constipation
     (pelvic pain also to prostatitis and hernia); severe sickness in
     pregnancy to feeling sick and diarrhoea and vomiting; strangulated hernia
     and hernia to a lump on the skin; glandular fever, tonsillitis and
     middle ear infection to a high temperature.
151. **Self-test fixes after the merge.** The typical age for a textbook patient
     now comes only from an age band that RAISES the starting chance (a card
     saying "very rare under 16" made its patient 10 years old). Recognition
     is ranked among the entry symptom's own conditions, since other symptoms
     the patient mentions bring in their own causes. The self-tests run on
     all processors. Bile duct cards now also belong to stomach ache, and
     hepatitis starts uncommon among people with yellow skin.
152. **Bleeding after the menopause: see a GP within a few days (soon)**, as a
     floor. The page says see a GP and a specialist within 2 weeks; "within a
     few days" for the GP is AI judgement so the referral can happen in time.
153. **Age, sex and stage of pregnancy are never evidence for a condition.**
     They set its starting chance (`prevalence_when`), and a card can now be
     limited to one sex (`sex: female` or `sex: male`), which rules it out for
     the other sex instead of only making it unlikely. The knowledge base check
     refuses a card that links one of these as evidence. Several baby, older
     adult and pregnancy cards had used age or weeks of pregnancy as evidence,
     because there was no starting chance low enough before the "very rare"
     band; they now start very rare and rise for the right ages or weeks.
     Self-tests: 1,278 of 1,280 pass.
154. **The test-case format checker no longer prints knowledge base errors.**
     One author ran it while the knowledge base was being edited, and its
     crash message showed some condition names and age links. That author's
     general symptoms cases were already written; the ear, nose and throat
     cases came after, and the author judged them not influenced. Recorded as
     a small separation leak. The checker now prints only "try again later".
155. **Fixes from the first run of the 280 development cases** (gates were
     215 of 216 and 277 of 280): severe lower tummy pain and sudden severe
     tummy pain are now kinds of severe tummy pain, so the pregnancy 999 rule
     sees them (a merge gap); a one-sided painful rash gets a pharmacist
     within 3 days (Shingles page); and back and neck pain rules that bundled
     "worried" with "not improving after weeks" were split, so only the
     worried part can be lowered by a likely mild cause.
156. **Independent check of brain and nerves, eyes and mental health.**
     Hierarchy gaps closed: a sudden, extremely painful headache and a severe
     headache painkillers do not help are now kinds of a very painful headache
     (eye, ear and nose rules use that one); a sudden new eyelid droop sits
     under a new droop or small pupil, under a drooping eyelid, so the headache
     rule for a new droop sees it; a dark curtain across the sight is a change
     in sight; a serious self-harm injury is a kind of serious self-harm (the
     universal red flag); a weak arm or a weak leg is numbness or weakness in
     the arms or legs; being knocked out and signs of a broken skull sit under
     serious signs after a head injury. Double vision was kept separate from
     "change in sight" on purpose (it would bring in the vision loss rules and
     override the Double vision page's "see a GP"); instead the headache,
     vertigo and head injury rules name it. Rules: vertigo with tingling (soft
     A&E), with hearing loss (urgent floor, tinnitus left to its own entry
     symptom) and with a severe headache (firm urgent), as the Vertigo page
     says; a sudden eyelid droop with a severe headache is now firm A&E, split
     from the soft double vision part. Starting chances: stroke is common
     among new weakness but rare among headaches, dizziness and pins and
     needles (uncommon at 65 or over); a dangerous heart rhythm no longer
     starts lower for an older person who fainted than a younger one;
     bleeding on the brain is very rare among faints. Overactive thyroid and
     alcohol withdrawal are now causes of a tremor (and withdrawal of a fit).
157. **Independent check of stomach and bowel, urinary and male, and women's
     health.** Hierarchy gaps closed (black poo is a kind of bleeding from the
     bottom; upper right tummy pain is a kind of pain below the ribs for the
     pre-eclampsia rules; discharge and unusual bleeding are kinds of unusual
     vaginal bleeding or discharge). Bundled soft rules split (painkillers not
     helping, heavy bleeding, and passing out are now firm). Constipation that
     stops you pooing or farting with a stomach ache is A&E. 50 one-sex cards
     are limited to that sex (for example ectopic pregnancy, prostatitis), and
     testicular torsion no longer starts common for every boy with a stomach
     ache. Heartburn starts very common among people with indigestion.
158. **Independent check of bones, skin, ear nose and throat, and general
     symptoms.** Hierarchy gaps closed: difficulty breathing is a kind of
     short of breath, and grunting or gasping are kinds of difficulty
     breathing (so the sore throat, hives and insect bite 999 rules see them);
     a rash that does not fade is a kind of rash; a stiff neck a kind of neck
     pain; and several "for 3 weeks" signs sit under their general sign. The
     Hives and Insect bites pages' 999 sign "very confused or drowsy" is now
     covered. A child who cannot put weight on a leg is firm A&E. Starting
     chances lowered for meningitis among neck pain, neck artery tears and
     spinal injury without an injury.
159. **An observation can be part of more than one general observation**
     (`also_part_of`), as two independent checkers asked. "Vomiting" is part
     of "diarrhoea or vomiting" (its parent, which decides question order) and
     of "feel sick or been sick", so the many rules written on the second now
     see a "yes" to vomiting. A "no" to either general one means "no" to
     vomiting. The simulated patient, the case checker and the question list
     for authors all follow it.
160. **Random-patient tests run a quarter of their full rounds by default**
     (`TRIAGE_TEST_SCALE=25`). With 506 conditions the full counts took over
     an hour on this machine. A thorough run, for example on a bigger server,
     sets `TRIAGE_TEST_SCALE=100`. What each test checks is unchanged.
161. **Severe tummy pain is also a kind of severe pain** (`also_part_of`), and
     the stomach pain in pregnancy rules are written on "Is the pain severe?",
     so a "yes" to either question reaches 999 with bleeding. Found by the
     development case for bleeding in pregnancy with severe pain, which used
     the general question. Test fixes: random made-up patients in the
     stop-rule and baseline tests are now made consistent (a "yes" means
     "yes" to its general observations, and nothing is true under a main
     symptom the patient does not have); the baseline threshold scales with
     the number of rounds; the parent-loop test builds its own loop.
162. **Each main symptom has its own allowance of condition questions** (up to
     8 each; the overall limit of 20 questions still applies). Before, the 8
     were shared, so a patient with several main symptoms could use them up on
     one symptom's questions and leave another's serious condition unresolved.
     Found by the random-patient test: a child with a sore throat, hearing loss
     in one ear and a nail change was left at "soon" for possible sudden
     hearing loss, because the questions that would have ruled it out were
     crowded out.
163. **What "adding a danger sign never lowers the outcome" means, exactly.**
     The engine stops asking when no single answer is likely to change the
     outcome, so with fewer answers it can stay more cautious than the patient
     needs. A new sign can lead to more questions and remove that extra
     caution, which is fine. The test now checks the outcome never drops below
     what the patient would need, with every answer known, without the sign.
     A drop below that would be a real fault. (In the case above, two "no"
     answers together lowered the chance of sudden hearing loss from 7% to
     under its threshold, but neither did alone.)
164. **Severe pain in pregnancy is asked one way, on its own.** "Has the pain
     not gone after 30 to 60 minutes of rest?" no longer also asks "is it
     severe?" in the same question: a "yes" could not tell the two apart, so
     severe pain could only ever count as urgent through it. Severity is asked
     by "Is the pain severe?", which is in the 999 checklist for both
     pregnancy symptoms. Bleeding in pregnancy now uses that general question
     too, as stomach pain in pregnancy already did; a "yes" to severe tummy
     pain counts automatically. Made-up patients with each way of saying
     severe pain now all reach 999.
165. **Sinusitis: see a pharmacist (12 and over) or a GP (11 and under)**, as
     the Sinusitis page says. Before, a blocked nose with pain around the
     cheeks, eyes or forehead was self-care unless the pain was severe or the
     nose had been blocked for 3 weeks. Uses the existing mapping: "See a
     pharmacist" is routine at a pharmacy. Two new age observations (12 or
     over, under 12). Three other development cases the engine placed below
     the expected level were checked against their source pages and left as
     they are: fainting, vaginal discharge and wheezing advice that the pages
     label "non-urgent" maps to routine (DECISIONS 17), so those are
     differences of mapping, not gaps.
166. **"Getting worse or not getting better" is urgent only for a cough of
     less than 3 weeks.** That advice comes from the COVID-19 and Flu pages,
     which describe a short illness. A cough of 3 weeks or more is literally
     "not getting better", so it was sent for urgent help, two levels above
     what the Cough and Lung cancer pages give (see a GP). Warning signs such
     as coughing up blood still make it urgent.
167. **Five condition cards now need urgent care (today), not emergency care**,
     because their own source pages say so: septic arthritis, temporal
     arteritis and peritonitis ("Ask for an urgent GP appointment or get help
     from NHS 111"), and ectopic pregnancy ("Contact your GP or call NHS 111
     ... right away"). The same goes for food stuck in the food pipe (AI
     judgement), where being unable to swallow at all is already a 999 red
     flag. All five stay in the critical danger class, so even a small chance
     still sends the patient for urgent help. Their 999 signs (signs of a
     rupture, sudden loss of sight, severe tummy pain, being unable to
     swallow) are red flags and still give 999. Found by an audit of every
     card that needs emergency care against its saved source page; the other
     such cards are emergencies in themselves on their pages (for example
     appendicitis, sepsis, a clot in the lung, a twisted testicle).
168. **Asthma and chest infection cards need routine care (see a GP)**, not
     "soon", as their pages say ("Non-urgent advice: See a GP"). An asthma
     attack, an attack that has just settled (see a GP within 2 days), and
     the warning signs of a chest infection that is getting worse each have
     their own sourced rule, which still applies. Bowel cancer warning signs
     stay at "soon" for the reason in item 152 (the GP visit leads to an
     urgent specialist referral).
169. **Indigestion with sweating or breathlessness: 999 from 45, soft under
     45.** An independent check found sweating alone with indigestion gave
     999 at any age. The Indigestion page itself has no 999 advice; the rule
     comes from the Chest pain page (chest pain that can feel like burning or
     indigestion, with feeling sweaty or short of breath). A tight, squeezing
     or heavy chest stays a firm 999 at any age. Sweating or breathlessness
     stays firm from 45, and under 45 it is soft, so clear signs of heartburn
     can lower it. The heart attack card is now also listed under indigestion,
     so heart risk factors are weighed. To give it the right starting chance,
     a starting-chance line can now need two things at once (`also`): it is
     common with chest pain from 45, uncommon with other chest pain, rare with
     indigestion from 45, and very rare otherwise.
170. **Case wording follow-up.** After the "rest" question was split (item
     164), an independent reviewer, who sees only the cases, source pages and
     question list, re-checked the four cases that used it and changed two to
     use "Is the pain severe?". While checking git it briefly saw a
     knowledge base change in the working tree (this indigestion rule); it
     did not act on it, and it saw nothing about outcomes. The case checker
     now also runs as `python3 harness/validate.py`.
171. **"Hard to wake" now asks only about the danger sign.** The question was
     "much sleepier than usual, or hard to wake?". Someone who is tired or
     sleepy would honestly say yes to the first half and be sent to 999. The
     source pages (Sepsis, Meningitis) mean drowsiness so deep that the
     person is hard to wake. It now asks: "so drowsy that they are hard to
     wake, or cannot stay awake?". Found by an independent check. Test
     results do not move, because the simulated patient answers by question
     id, but the question is now right for a real person.
172. **Two more head injury conditions**: a broken skull (critical, needs
     emergency care) and symptoms that carry on after a head injury
     (post-concussion syndrome, see a GP). Head injury had only two
     condition cards, as an independent check noted. Its triage is still led
     by its 15 sourced red flags; the cards make the list of possible causes
     more complete and let a broken skull raise the outcome on its own.
     SNOMED CT codes checked and logged.
173. **Two condition self-test near-misses are left as they are.** Cervical
     cancer (from bleeding between periods or after sex) ranks 4th and womb
     cancer (from heavy periods) 5th. The self-test patient has every sign on
     the card, and harmless causes of the same signs (thinning of the vagina,
     polyps, harmless changes on the cervix, fibroids) are far more common,
     so a rare cancer below them is realistic. Raising their starting chance
     only to pass the test would make the engine less accurate. Their
     outcomes are still urgent enough for the cancer.
174. **Final run.** Development: both gates pass (216 of 216, 280 of 280),
     acuity 247 of 280, over-triage 28. Holdout, run once at the end with
     nothing tuned against it: both gates pass (83 of 83, 114 of 114),
     acuity 89 of 114, over-triage 20. Results are in the README.

## Interfaces (owner decisions, November 2026)

175. **The API has the common shape of condition-based engine APIs**
     (owner's choice), so an evaluation designed for such an engine can call
     this mock, or a real engine, with little change. `POST /diagnosis` gives the
     next question and the likely conditions; `POST /triage` gives one of
     five triage levels with the outcome, advice and reasons. Only the
     published shape is used (field names and levels); ids are this engine's
     own. Like those APIs, it keeps nothing between calls: the caller sends
     all the evidence each time, and the engine replays the interview from
     it. No new reasoning code: the API wraps the same `run()` the harness
     uses, and tests check it gives the same outcome after the same
     questions. Built with FastAPI, which checks requests and writes the
     API's documentation page.
176. **The demo page is for the owner, on their own computer** (owner's
     choice). One command (`python triage.py serve`), listening on this
     computer only. Plain HTML with no outside libraries, no NHS branding,
     and the disclaimer at the top. It keeps only the evidence so far, in the
     page.
177. **No language layer for now** (owner's choice). People pick their main
     symptom by searching names and everyday words, then answer the
     engine's questions. The engine still makes no network calls.
178. **"See a GP" stays routine** (owner's choice, confirming item 17). The
     NHS website labels it non-urgent. Differences with test cases that
     expected "soon" stay in `review/disagreements.md` for clinical review.
179. **Questions a 12 to 15-year-old may answer themselves no longer talk to
     a parent.** Found by the owner testing a 15-year-old with a sprained
     foot, who was asked "Is your child not using their arm?". Two causes:
     the two pulled-elbow questions were asked up to 16, although pulled
     elbow happens in young children (now up to 5 only), and several
     questions asked up to 16 were written to a parent. Those now use the
     neutral "the person who is unwell" wording already used elsewhere; the
     "your child" wording is still used when someone says they are answering
     for another person. The demo page now ticks "I am answering for someone
     else" for under-12s (it can be unticked). Development results are
     unchanged.
