<a name="top"></a>

<div align="center">

<a href="https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-ai-job-hunt-os&utm_content=repo-home"><img src="https://static.b100x.ai/email/landed-wordmark.png" alt="Landed" width="200"></a>

<img src="https://static.b100x.ai/github-repos/images/ai-job-hunt-os/banner.svg" alt="AI Job Hunt OS" width="100%">

![Skills](https://img.shields.io/badge/6%20Claude%20skills-ff5b29?style=flat-square) ![Format](https://img.shields.io/badge/Agent%20Skills%20standard-6C2BD9?style=flat-square) [![Validate](https://github.com/landedjobs/ai-job-hunt-os/actions/workflows/validate.yml/badge.svg)](https://github.com/landedjobs/ai-job-hunt-os/actions/workflows/validate.yml) [![Stars](https://img.shields.io/github/stars/landedjobs/ai-job-hunt-os?style=social)](https://github.com/landedjobs/ai-job-hunt-os)

**Six Claude skills that run your AI job hunt like an operating system.**
Decode the JD · research the company · tailor the resume · write outreach that gets replies · drill the interview · negotiate the offer.

[Install](#install) · [The skills](#the-skills) · [How they chain](#how-they-chain) · [Stay in the loop](#stay-in-the-loop)

</div>

---

> Job hunting is a loop, not a lottery: decode what the role wants, prove you match it, reach a human, practice the room, negotiate the number. These skills make Claude run each step properly. They deliberately avoid frozen market-wide benchmarks: current compensation and hiring claims must be sourced when the skill runs.

## What's inside

```
ai-job-hunt-os/
├── CLAUDE.md                          shared rules: your profile, honesty, human voice
├── README.md                          you are here
└── skills/
    ├── jd-decoder/
    │   └── SKILL.md                   what the posting actually wants + apply/skip verdict
    ├── company-researcher/
    │   └── SKILL.md                   the brief a well-connected friend would give you
    ├── resume-tailor/
    │   └── SKILL.md                   your true story, told in the JD's language
    ├── cold-outreach-writer/
    │   └── SKILL.md                   messages busy people actually answer
    ├── mock-interviewer/
    │   └── SKILL.md                   realistic drills with honest scoring
    └── salary-negotiator/
        └── SKILL.md                   negotiation method + current-data sourcing rules
```

<a name="install"></a>
## Install

**Claude Code** (30 seconds):

```bash
git clone https://github.com/landedjobs/ai-job-hunt-os.git
cp -r ai-job-hunt-os/skills/* ~/.claude/skills/
```

Then just talk to Claude: "here's a JD, should I apply?" and the right skill kicks in. Keep `CLAUDE.md` in your working folder (or paste it into your project's CLAUDE.md) so the shared rules apply.

**Claude.ai** (web/desktop): download this repo as a zip (green Code button), then upload the skill folders you want under Settings → Capabilities → Skills.

**Any Agent Skills client**: these are standard `SKILL.md` files per the open [Agent Skills](https://code.claude.com/docs/en/skills) format; they work in any agent that supports it.

<a name="the-skills"></a>
## The skills

| Skill | What it does | Use it when |
|---|---|---|
| `jd-decoder` | Separates real requirements from wishlist, translates the loaded phrases, gives an apply / stretch / skip verdict | Before every application |
| `company-researcher` | Business, funding, AI-native or AI-washed, team intel, talking points, questions to ask | Before applying, again before the loop |
| `resume-tailor` | Rewrites your resume for one specific JD without inventing anything, with a change log that teaches the pattern | Every application that passed the decoder |
| `cold-outreach-writer` | Three message variants + follow-up plan, under 120 words, payload first | Reaching hiring managers and referrers |
| `mock-interviewer` | Behavioral, technical AI/ML, or LLM system design sessions with real follow-ups and 1-5 scoring | The week before the loop |
| `salary-negotiator` | Scripts for every negotiation moment + a method for sourcing current, comparable compensation | The screen question, and the day the offer lands |

<a name="how-they-chain"></a>
## How they chain

One target role, start to signed offer:

```
jd-decoder ──► company-researcher ──► resume-tailor ──► cold-outreach-writer ──► mock-interviewer ──► salary-negotiator
   verdict         the brief            the resume          the referral            the reps             the number
```

Each skill picks up the previous one's output, so you never paste the same JD twice. `CLAUDE.md` holds your profile so you never repeat your background.

<a name="stay-in-the-loop"></a>
## Stay in the loop

These skills are the manual loop. [landed](https://www.landed.jobs/?utm_source=github&utm_medium=referral&utm_campaign=github-ai-job-hunt-os&utm_content=repo-home) is the agent that runs it for you daily: fresh AI-native roles matched to you, application answers drafted, interview prep queued.

Resume tailoring and cold outreach stay in this repo: they are open-source skills you run yourself in Claude. landed does not rewrite your resume or send outreach for you.

- ⭐ **Star this repo**: new skills get added (interview-question mining, offer comparison, visa-aware search are queued).
- 📬 **[Fresh roles](https://www.landed.jobs/jobs?utm_source=github&utm_medium=referral&utm_campaign=github-ai-job-hunt-os&utm_content=jobs)**: every open role landed tracks, by role family, refreshed daily with pay and the companies hiring.
- 🧰 **[More free tools](https://www.landed.jobs/open-source?utm_source=github&utm_medium=referral&utm_campaign=github-ai-job-hunt-os&utm_content=open-source)**: the other open-source repos landed maintains, from interview questions to portfolio projects.

## License

MIT. Use it, fork it, share it with someone mid job hunt.
