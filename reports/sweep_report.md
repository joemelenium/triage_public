# Risk setting sweep: dev set

Knowledge base 0.4.0. 48 cases.

The danger class lines say how likely a condition must be before it changes the outcome. Each row reruns the same cases at a different level of caution.

The cases are AI-drafted and not clinically approved, and the likelihoods are AI estimates. Not for clinical use.

| Setting | Below minimum safe | Red flags gate failed | Acuity matches | Over-triage | Raised by conditions | Lowered by conditions | Items read per case |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rules only (conditions switched off) | 0 | 0 | 40 of 48 | 8 of 48 | 0 | 0 | 21.6 |
| Single-cause method instead of the network | 0 | 0 | 40 of 48 | 8 of 48 | 3 | 5 | 23.9 |
| Less cautious (lines doubled) | 0 | 0 | 42 of 48 | 6 of 48 | 1 | 4 | 23.3 |
| As set in settings.yaml | 0 | 0 | 42 of 48 | 6 of 48 | 1 | 4 | 23.2 |
| More cautious (lines halved) | 0 | 0 | 40 of 48 | 8 of 48 | 1 | 4 | 23.2 |
| Much more cautious (lines quartered) | 0 | 0 | 37 of 48 | 11 of 48 | 4 | 3 | 23.4 |

## Outcome profile at each setting

| Setting | emergency ambulance | emergency department | urgent care | general practice | community pharmacy | self care |
| --- | --- | --- | --- | --- | --- | --- |
| Rules only (conditions switched off) | 10 | 6 | 18 | 4 | 4 | 6 |
| Single-cause method instead of the network | 10 | 6 | 13 | 10 | 3 | 6 |
| Less cautious (lines doubled) | 10 | 6 | 14 | 8 | 4 | 6 |
| As set in settings.yaml | 10 | 6 | 14 | 8 | 4 | 6 |
| More cautious (lines halved) | 10 | 6 | 14 | 8 | 4 | 6 |
| Much more cautious (lines quartered) | 10 | 6 | 15 | 8 | 3 | 6 |
