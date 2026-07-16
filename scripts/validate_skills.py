#!/usr/bin/env python3
"""Validate published Skills and Claude Code commands without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ABSOLUTE_PATH_RE = re.compile(r"(?:[A-Za-z]:\\|/(?:Users|home|etc|var)/)")
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"(?:github_pat_|gh[pousr]_)[A-Za-z0-9_]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic API key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, "missing or malformed YAML frontmatter"

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"\'')
        fields[key.strip()] = value
    return fields, None


def validate_text_file(path: Path, errors: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{path.relative_to(ROOT)}: file is not valid UTF-8 text")
        return

    if ABSOLUTE_PATH_RE.search(text):
        errors.append(f"{path.relative_to(ROOT)}: contains a local absolute path")

    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"{path.relative_to(ROOT)}: contains a possible {label}")

    if path.suffix.lower() != ".md":
        return

    for target in MARKDOWN_LINK_RE.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")


def validate_skills(errors: list[str]) -> None:
    seen: set[str] = set()
    for skill_file in sorted((ROOT / "skills").rglob("SKILL.md")):
        skill_dir = skill_file.parent
        fields, error = parse_frontmatter(skill_file)
        relative = skill_file.relative_to(ROOT)
        if error:
            errors.append(f"{relative}: {error}")
            continue

        name = fields.get("name", "")
        description = fields.get("description", "")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{relative}: name must use lowercase kebab-case")
        if name != skill_dir.name:
            errors.append(f"{relative}: name must match directory '{skill_dir.name}'")
        if not description:
            errors.append(f"{relative}: description is required")
        if name in seen:
            errors.append(f"{relative}: duplicate skill name '{name}'")
        seen.add(name)


def validate_commands(errors: list[str]) -> None:
    for command in sorted((ROOT / "commands").rglob("*.md")):
        if command.name == "README.md":
            continue
        fields, error = parse_frontmatter(command)
        relative = command.relative_to(ROOT)
        if error:
            errors.append(f"{relative}: {error}")
            continue
        if not fields.get("description"):
            errors.append(f"{relative}: description is required")
        if not NAME_RE.fullmatch(command.stem):
            errors.append(f"{relative}: filename must use lowercase kebab-case")


def validate_manifests(errors: list[str]) -> None:
    paths = [
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
    ]
    for path in paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")


def main() -> int:
    errors: list[str] = []
    validate_manifests(errors)
    validate_skills(errors)
    validate_commands(errors)

    for root_name in ("skills", "commands"):
        for path in sorted((ROOT / root_name).rglob("*")):
            if path.is_file():
                validate_text_file(path, errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = sum(1 for _ in (ROOT / "skills").rglob("SKILL.md"))
    command_count = sum(
        1 for path in (ROOT / "commands").rglob("*.md") if path.name != "README.md"
    )
    print(f"Validation passed: {skill_count} skills, {command_count} commands")
    return 0


if __name__ == "__main__":
    sys.exit(main())
