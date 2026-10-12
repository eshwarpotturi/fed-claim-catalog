# Fed Claim Catalog

**Live page:** https://eshwarpotturi.github.io/fed-claim-catalog/

Companion to the [Rate Call Tracker](https://eshwarpotturi.github.io/rate-call-tracker/).

The tracker starts from a decision and asks who saw it coming. The catalog starts from what forecasters said. It takes 142 Fed rate forecasts made between 2016 and 2026 by banks, surveys and the Fed's own dot plot, turns each into a claim with a deadline, and checks it against what the Fed did.

**What it shows (as of 12 October 2026)**

- Of 112 claims whose deadline has passed, 32 were exactly right, 27 were one move off, 53 were wrong.
- Claims made up to two months before their deadline were right 20 of 27 times. Beyond two months, 12 of 85.
- Every turn was missed: none of the claims for 2019 came true, and all twelve 2022 year totals fell short by 250 bp or more.
- **League table (ranking of houses).** Houses with 5+ checked forecasts are ranked by "beat the pack": for each forecast, the house's result (correct 1, partly 0.5, wrong 0) minus the average of every other house answering the same question in the same report. This controls for easy versus hard questions. Goldman Sachs ranks #1 (+0.14), Deutsche Bank last (−0.19). On raw score BofA and UBS Wealth lead, but mostly on questions everyone got right. The table also shows raw score, average miss in bp, and each house's best call and biggest miss, and can be re-sorted by any of the three.
- 13 published 2026 calls (January's year-end cut forecasts and the Fed's December 2025 dots) need revision after September's hike; 15 can still come true.

**How it works**

| File | What it does |
|---|---|
| `claims/extract.py` | Sends one article to an LLM through LLM Foundry and returns its forecasts as structured claims, each with the phrase it came from. Needs `LLMFOUNDRY_TOKEN`. |
| `claims/claims.json` | The extracted claims and their sources. |
| `claims/fed_path.json` | Every change to the fed funds target range since December 2015, and the meetings left in 2026. |
| `claims/verify.py` | Gives each claim a verdict and rolls verdicts up by house, year and horizon. Writes `claims/verdicts.json`. |
| `claims/build.py` | Builds `index.html` from `claims/template.html` and `claims/base_style.html`. |

To update: add claims to `claims/claims.json` (or run `extract.py` on a new article and paste in the reviewed output), add any new decision to `claims/fed_path.json`, then run `python3 claims/verify.py && python3 claims/build.py`.

**Verdicts:** correct (same target range by the deadline), partly (one 25 bp move off, or right direction but wrong size or meeting within 60 days), wrong, not yet testable, needs revision (needs more moves than meetings left, or a reversal of the Fed's latest move), hard to say (nothing to check).

**Questions you will get**

- *How is this different from the McKinsey energy check?* Same method (mine claims from a corpus, check, benchmark), applied to finance, where outcomes are exact and dated, so verdicts are mechanical rather than judged.
- *Is the LLM doing the scoring?* No. The LLM only extracts claims. Verdicts come from fixed rules in `verify.py`, so the same data always gives the same answer.
- *Why press coverage, not the original notes?* The notes are paywalled. Run on a research team's own notes, the same pipeline rates its analysts.

**Check before sending outside**

- The 2023 levels come from a Bloomberg table of single numbers, read as the top of the target range.
- J.P. Morgan's "3.75% through September 2025" is read as the top of the 3.50%-3.75% range.
- Dot-plot medians and the rate path were entered from the Fed's published tables; the December 2018 and December 2025 medians were checked against the Fed's pages.
- Open-claim checks assume meetings on 28 October and 9 December 2026.

Not investment advice.
