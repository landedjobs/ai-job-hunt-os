# Contributing

Contributions that make a skill more accurate, actionable, or easier to run are welcome.

## Before opening a pull request

1. Keep each skill in `skills/<skill-name>/SKILL.md`.
2. Keep the front matter limited to a valid `name` and `description`. The name must match the directory.
3. Never invent a candidate fact, employer fact, market statistic, or benchmark.
4. Do not add a time-sensitive exact number without a public source, publication date, sample definition, and limitation in `SOURCES.md`.
5. Prefer a sourcing instruction over a frozen market-wide benchmark when the value changes over time or depends on geography, level, or company stage.
6. Run `python3 scripts/validate-skills.py`.

Use plain language, preserve uncertainty, and make outputs defensible in a real interview or negotiation.
