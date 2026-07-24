#!/usr/bin/env python3
"""Validate the repository's Agent Skills front matter without extra dependencies."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def front_matter(path: Path) -> dict[str, str]:
	text = path.read_text(encoding="utf-8")
	if not text.startswith("---\n"):
		raise ValueError("missing opening front-matter delimiter")
	try:
		block = text.split("---\n", 2)[1]
	except IndexError as exc:
		raise ValueError("missing closing front-matter delimiter") from exc
	fields: dict[str, str] = {}
	for line in block.splitlines():
		if not line.strip():
			continue
		if ":" not in line:
			raise ValueError(f"invalid front-matter line: {line}")
		key, value = line.split(":", 1)
		fields[key.strip()] = value.strip()
	return fields


def main() -> None:
	skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
	if not skills:
		raise SystemExit("no skills found")
	errors: list[str] = []
	for path in skills:
		try:
			fields = front_matter(path)
			if set(fields) != {"name", "description"}:
				errors.append(f"{path}: expected only name and description")
			if fields.get("name") != path.parent.name:
				errors.append(f"{path}: name must match directory")
			if not fields.get("description"):
				errors.append(f"{path}: description must not be empty")
			if len(fields.get("name", "")) > 64:
				errors.append(f"{path}: name exceeds 64 characters")
			if len(fields.get("description", "")) > 1024:
				errors.append(f"{path}: description exceeds 1024 characters")
		except ValueError as exc:
			errors.append(f"{path}: {exc}")
	if errors:
		raise SystemExit("\n".join(errors))
	print(f"Validated {len(skills)} Agent Skills.")


if __name__ == "__main__":
	main()
