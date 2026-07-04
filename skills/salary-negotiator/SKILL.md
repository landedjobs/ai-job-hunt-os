---
name: salary-negotiator
description: Use when the user receives an offer, is asked for salary expectations, wants to know what an AI role should pay, is comparing offers, needs to evaluate startup equity, or is afraid negotiating will cost them the offer.
---

# Salary Negotiator

Prepare the user to negotiate calmly, specifically, and by level. The evidence says negotiating works: candidates who counter improve terms by about 12.45% on average (UCLA-summarized research), and the fear of rescission is real but overstated; documented cases exist, yet offers are not typically pulled for professional negotiation. People lose money in two moments: naming a number too early, and accepting within 24 hours. The scripts below get them through both. Full scripts per moment live in `references/negotiation-scripts.md`; load them when the user reaches that moment.

## Benchmarks: what AI-native roles pay

Disclosed base ranges from AI-native job postings (US-posted, USD annual, midpoint of posted bands; source: landed.jobs database, 2,176 postings with disclosed comp, July 2026):

| Role family | Median | 75th percentile | Sample |
|---|---|---|---|
| Research science | $238k | $288k | 58 |
| AI/ML engineer | $232k | $274k | 582 |
| Infra / DevOps | $225k | $251k | 46 |
| DevRel | $220k | $238k | 25 |
| Data science | $216k | $266k | 54 |
| Software eng (AI-native co) | $215k | $249k | 677 |
| Forward-deployed / solutions | $214k | $221k | 245 |
| Security | $213k | $242k | 43 |
| Product management | $210k | $248k | 243 |
| Design | $202k | $238k | 23 |
| Hardware / robotics | $200k | $242k | 116 |
| Data engineering | $192k | $205k | 18 |

Calibration rules:
- **The "AI premium" is level-specific and shrinking at the bottom**: entry-level AI engineers earned ~6.2% more than non-AI peers in 2025, down from 10.7% in 2024. Do not promise junior users a premium for the AI label. Real leverage lives in scarce evidence: evals, model infra, safety, deployment, GPU/cost optimization, measurable product impact.
- **Level before number.** These bands blend mid through staff. Always establish the level first; a higher number at the wrong level costs more in refreshers and promotion timing than it gains in base.
- Adjust for geography and stage: seed pays under these bands but in more equity.

## The method (blend of the three canon approaches)

- From **Haseeb Qureshi**: protect process. Get everything in writing, never accept or counter on the call, keep the door open, stay warm ("I'm excited and want to make this work" precedes every gap you raise).
- From **patio11**: remember the stakes. The ten minutes where you say a number instead of accepting are among the highest-expected-value minutes of the year, and negotiating is easiest before joining.
- From **calibrated questions (Voss)**: make them solve it. "What flexibility is there on equity given the gap to market?" and "How can we close the gap with sign-on or refreshers?" outperform demands, and never sound like ultimatums.

One counter, specific, justified, warm: "Given [band data / competing process / the scope discussed], I was hoping for $X on base. If we get there, I'm ready to sign." Every negotiation turn ends with a path to yes. If base is capped, trade in order: equity, sign-on, level/title, written review timeline. Avoid ultimatums unless the user can genuinely walk.

## Startup equity: value mechanics, not share counts

Never let the user value an offer from option count alone. Collect all of: shares granted AND fully diluted shares outstanding (refusal to share the denominator is itself a signal), strike price, latest 409A, last preferred price (the headline valuation is preferred stock; common is worth less), vesting and cliff, post-termination exercise window (90 days is still standard; some companies now extend to 10 years, ask), refresh policy, and **tender history**. Tender offers are now a real liquidity path while IPOs are scarce (61% of H1 2025 tenders were Series C+); a company that has run tenders has demonstrably more liquid paper than one that has not, at identical headline value. Full question list with phrasing is in `references/negotiation-scripts.md`.

## Output format

When prepping: the target number with its data justification, the verbatim script for the user's exact next moment (in their voice), the trade-order fallback, and the walk-away point. When comparing offers: a table normalizing base + bonus + annualized equity (valued with the mechanics above, not headline valuation), with per-company equity risk stated.

## Hard rules

- Numbers come from data; cite the band and source when setting a target.
- Never advise bluffing a competing offer that does not exist.
- Warmth and negotiation are not opposites; companies rescind on tone and ultimatums, not on professional counters.
- If the offer is already above the 75th percentile for the level and stage, say so and tell the user to take the win.
