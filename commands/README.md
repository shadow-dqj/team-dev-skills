# Commands

Claude Code slash commands live in this directory as Markdown files with YAML frontmatter.

```text
commands/
  review-ticket.md
  project/
    plan-release.md
```

Commands are distributed through the Claude plugin manifest. CC Switch only discovers and installs resources under `skills/` that contain `SKILL.md`.

Copy `templates/command/COMMAND.md` when adding the first Command.
