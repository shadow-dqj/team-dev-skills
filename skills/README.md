# Skills

Published internal Agent Skills live in this directory and are discovered recursively.

```text
skills/
  <project>/
    <skill-name>/
      SKILL.md
      references/
      scripts/
      assets/
```

Use a stable lowercase kebab-case project directory for grouping. Each immediate or nested skill directory must contain a `SKILL.md` with YAML frontmatter containing at least `name` and `description`. The frontmatter `name` must equal the skill directory name and use lowercase kebab-case.

CC Switch recursively discovers every directory containing `SKILL.md`. Do not keep archived, duplicate, or test `SKILL.md` files under `skills/`.

Copy `templates/skill/` when adding a Skill, place it under the appropriate project directory, and run `python scripts/validate_skills.py` before review.
