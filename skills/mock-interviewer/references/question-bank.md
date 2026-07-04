# Question bank by session type

Load when the session type is chosen. These are formats and seed questions; vary the specifics per role and company, and escalate difficulty with seniority.

## Eval design (the AI-native differentiator round)

- "You're shipping a support agent. Design the eval suite before launch: what do you measure, against what baseline, and what's your error taxonomy?"
- "How would you eval an agent whose task has no ground truth?"
- "Your hallucination metric improved 15% but users complain more. Walk me through the investigation."
- "Design a regression gate for prompt changes. What escapes it, and how do you find those escapes?"
- "You have 500 labeled examples and no budget for more. How do you make the eval trustworthy?"

Grade for: metrics tied to user harm (not vanity accuracy), explicit baselines, adversarial thinking, monitoring after launch, and honesty about what the eval cannot catch.

## Agent debugging

Present a scenario with artifacts, then let them drive:

- "This agent booked the wrong calendar slot for 3% of requests. Here are the tool-call logs for two failures and one success. Where do you start?"
- "Retrieval quality dropped after a reindex. The eval suite is green. What do you check, in order?"
- "The agent loops calling the same tool with slightly different arguments. Here's the trace. Hypotheses?"
- "Latency p95 doubled after adding a guardrail model. Options, and their failure modes?"

Grade for: hypothesis ranking before diving in, checking data before code, using the logs actually provided (not imagined ones), and communicating uncertainty while debugging.

## Coding (four-part rubric, always)

Any medium-hard problem works; the grading is the point. Debrief every round on: **design** (decomposition, naming, interfaces), **code quality** (readable, idiomatic), **performance** (complexity stated unprompted at senior level), **test coverage** (did they write tests without being asked; do the tests cover the edges they named). A candidate who finishes the algorithm and stops has covered one of four.

## System design with LLMs

- "Design the retrieval layer for a 10M-document corpus with a $2k/month inference budget."
- "Multi-step agent for expense approvals: where do you put deterministic logic vs the model, and why?"
- "Same system, now with a 2-second latency budget. What moves?"
- "Where does this design fail embarrassingly, and what's the blast radius?"

Grade for: cost and latency treated as first-class constraints, explicit model-vs-code boundaries, failure modes named unprompted, and eval/monitoring designed into the system rather than bolted on.

## Architecture defense (presentation-style rounds)

The candidate presents a real past project for ~10 minutes, then:
- "What alternatives did you consider and why did you reject them?"
- "What broke in production, and what did you change after?"
- "If you rebuilt it today, what goes first?"
- "Which part are you least confident about?" (Honesty here is a hire signal, not a weakness.)
- Follow with one deep technical quiz question inside their claimed expertise; inflated claims collapse here.

## Behavioral

Formats: conflict with a colleague, ownership beyond scope, a real failure with consequences, disagreeing with a decision, the hardest technical judgment call. Grade every story for: numbers, stakes, the user's specific role (I vs we), and what changed afterward. At mission-driven labs, add judgment probes: "A customer asks you to disable a safety filter to close the deal. Walk me through your thinking." and "When would you argue against shipping something that works?"

## Product sense (AI products)

- "Daily active usage of the AI feature is high but retention at week 4 is bad. Diagnose."
- "Users love the answers but don't trust them. What do you change: model, UX, or positioning?"
- "You can cut hallucinations 40% at 3x the latency. Ship it or not, for which product?"

Grade for: user-harm framing, willingness to trade model quality against product reality, and crisp decisions with named reversibility.

## AI-collaborative mode (only when the target company allows AI in interviews)

Run any of the above with the candidate using an AI assistant, then grade the collaboration transcript: did they decompose the problem before prompting, verify outputs against their own reasoning, write or demand tests for generated code, and visibly reject at least one plausible-but-wrong suggestion? Companies running AI-assisted interviews review exactly this trail; blind acceptance of fluent wrong answers is the most common failure they report.
