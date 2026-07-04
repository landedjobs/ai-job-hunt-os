---
name: jd-decoder
description: Use when the user shares a job posting and asks whether to apply, what the posting really means, whether a job is real or a ghost listing, what a salary band signals, or how to prioritize between several postings.
---

# JD Decoder

Treat every posting as a probabilistic signal, not a promise. Two base rates frame the work: Greenhouse classifies 18-22% of postings on its platform in any quarter as ghost jobs (positions not being actively filled), and in a 2024 ResumeBuilder survey 40% of hiring managers admitted their company posted a fake listing that year. Those are different instruments, so never quote them as one number; the takeaway is that most postings are real, a meaningful minority are not, and effort should follow the odds.

## Process

### Step 1: Score ghost risk before anything else
One point each (0-6):

1. Posted or reposted for 45+ days with no edits
2. No named team, manager, or concrete problem; responsibilities read as template
3. Not listed on the company's own careers page (job-board only)
4. Company had layoffs in the last 6 months in this function
5. No recruiter activity visible (no LinkedIn posts about the role, no outreach happening)
6. Extremely wide or missing comp band with no explanation

0-1: real, tailor deeply. 2-3: probably real, tailor moderately and verify. 4+: verify before investing; offer to draft a short note to the likely hiring manager asking "is this role actively interviewing?" That question is legitimate, cheap, and converts uncertainty into information. A repost alone is NOT proof of fake: budgets change, finalists fall through, some roles are evergreen.

### Step 2: Classify every requirement
Four piles: **must-have** (early, repeated, connected to responsibilities), **signal** (tells you the team's stack and pain), **nice-to-have** (long comma lists; candidates matching 100% of a wishlist do not exist and the hiring manager knows it), **compliance filler**. Tailor only to must-haves and signals.

### Step 3: Translate loaded language into diligence questions, not verdicts
Posting-language studies are weak evidence of anything, so convert phrases into interview questions instead of conclusions:
- "Fast-paced" → "What changed in the last two quarters that created this role?"
- "Wear many hats" → "Which three functions does this role own in the first 90 days?"
- "0 to 1 / founding" → equity must be a real conversation; if the comp section is silent on it, that is a question.
- A hyper-specific requirement ("migrating off LangChain") → they have that exact problem now; direct-hit evidence here is the user's opening line.
- One role asking for research + infra + customer-facing + data + sales engineering → unicorn trap; the role is underscoped in their heads. Generate clarifying questions and lower the tailoring investment.

### Step 4: Decode the comp band
A very wide band ($50k+ spread) measurably lowers applicant trust when unexplained (Washington State University study), but the expert move is decoding, not avoiding: does it span multiple levels? Multiple geos? Is the top reachable for external hires? Flag which question applies and queue it for the screen. Band position also signals leveling; map level by scope (ownership, ambiguity, cross-functional impact), never by years alone. Years-of-experience lines are soft; two years shipping production AI regularly beats five adjacent, and you should say when the user should apply anyway.

### Step 5: Verdict
Exactly one of:
- **Apply now**: strong match on must-haves, low ghost risk. List the 2-3 evidence points to lead with.
- **Stretch, apply anyway**: 60-80% of must-haves and the gaps are learnable. Name each gap and its one-line honest framing.
- **Verify first**: good match but ghost risk 4+. Provide the verification note.
- **Skip**: fundamental mismatch or the decoded reality contradicts what the user wants. One sentence why, so the next "apply" verdict is trusted.

Be willing to say skip; a decoder that always says apply is useless. But remember the base rates: most postings are real, and false negatives are expensive in a scarce market.

## Output format

1. Ghost-risk score with the checklist shown
2. What they actually need (3-5 bullets, plain language)
3. Must-haves vs wishlist (two short lists)
4. Decoded phrases and the diligence questions they generate
5. Comp band read + leveling estimate, with what to verify
6. Verdict with reasoning

Label every inference as an inference. If the user shares multiple postings, rank them by (fit × ghost-risk-adjusted odds) and say where to spend this week's effort.
