# Skills

Published Agent Skills live in this directory.

```text
skills/
  example-skill/
    SKILL.md
    references/
    scripts/
    assets/
```

Each immediate or nested skill directory must contain a `SKILL.md` with YAML frontmatter containing at least `name` and `description`. The frontmatter `name` must equal its directory name and use lowercase kebab-case.

Copy `templates/skill/` when adding the first Skill. Do not keep archived or test `SKILL.md` files under this directory because CC Switch discovers them recursively.
