# Run report: published vignette sets

Knowledge base 0.4.0. 45 published vignettes. Structured mode, no LLM.

> **A sense check only.** These vignettes were written by other people for other purposes. They use coarser triage categories than this project, and some come from outside the UK. The published text was mapped onto this project's question list by AI, which loses detail. Not for clinical use.

## Semigran 2015

45 vignettes: 8 within current coverage, 37 outside it.

### Within current coverage

- Same coarse category as published: 7 of 8 (88%)
- More urgent than published: 1
- **Less urgent than published: 0**

| Case | Complaint | Published | Engine | Engine outcome | Decided by |
| --- | --- | --- | --- | --- | --- |
| semigran2015_06 | chest pain for 24 hours | emergency | emergency | emergency / emergency_ambulance | rf_cp_with_sweating_sickness_or_breathlessness |
| semigran2015_12 | sudden shortness of breath for 30 minutes, with left-sided chest pain that is worse on breathing in | emergency | emergency | emergency / emergency_ambulance | rf_cp_with_sweating_sickness_or_breathlessness |
| semigran2015_17 | sudden fever, nausea, vomiting and sore throat | non emergency | non emergency | urgent / urgent_care | rf_st_high_temperature |
| semigran2015_18 | sore throat, fever and headache for 2 days | non emergency | non emergency | urgent / urgent_care | rf_st_high_temperature |
| semigran2015_24 | fever, sore throat and fatigue for a week, gradually getting worse | non emergency | non emergency | urgent / urgent_care | rf_st_high_temperature |
| semigran2015_28 | burning and aching pain on the right side of the chest for 5 days, followed by a blistering rash in the same area | non emergency | non emergency | routine / general_practice | chest_pain_default |
| semigran2015_34 | sore throat, headache and dry cough for 2 days | self care | self care | self_manageable / self_care | sore_throat_default |
| semigran2015_44 | runny nose and sore throat for 2 days | self care | non emergency | urgent / urgent_care | rf_st_high_temperature |

### Outside current coverage: a test of the "not covered" behaviour

The engine should say it does not cover these, run the universal red-flag screen, and give a cautious default. It should never guess.

- Returned as "not covered": 37 of 37 (100%)
- Published as emergencies: 13. Of these, the universal red-flag screen raised an emergency in 2. **The other 11 received the cautious default, which is less urgent than published.** This is the limit of covering only a few presenting symptoms.
- Published as self-care: 13. All received the cautious default, which is over-triage by design.
- Engine outcomes: emergency 2, urgent 35
