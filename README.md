# Team Dev Skills

A public, centrally maintained collection of Agent Skills and Claude Code commands for team project development.

> This repository currently contains templates only. Do not publish company secrets, internal hosts, credentials, private source code, customer data, or non-public business rules.

## Repository layout

```text
skills/<skill-name>/SKILL.md       Agent Skills discovered by CC Switch
commands/<command-name>.md         Claude Code slash commands
.claude-plugin/plugin.json         Claude plugin manifest
.claude-plugin/marketplace.json    Claude marketplace manifest
templates/                         Copy-ready contribution templates
scripts/validate_skills.py         Repository validation
```

## Install Skills with CC Switch

CC Switch manages the contents of `skills/`; it does not install the Claude-specific `commands/` directory.

1. Open **CC Switch > Skills > Repository Management**.
2. Add `shadow-dqj/team-dev-skills` as a public GitHub repository.
3. Select branch `main` and refresh discovery.
4. Install the required skills and select the target agents to synchronize.

CC Switch recursively discovers directories containing `SKILL.md`, so always place published skills under `skills/<skill-name>/`.

## Install Skills and Commands with Claude Code

Direct GitHub installation installs both resources declared by the plugin manifest:

```bash
claude plugin install https://github.com/shadow-dqj/team-dev-skills
```

Marketplace installation is also supported:

```text
/plugin marketplace add shadow-dqj/team-dev-skills
/plugin install team-dev-skills@team-dev-skills
```

Restart Claude Code after installation if prompted.

## Add a Skill

1. Copy `templates/skill/` to `skills/<skill-name>/`.
2. Replace all placeholders and keep the directory name and frontmatter `name` identical.
3. Put detailed material in `references/`, executable helpers in `scripts/`, and static files in `assets/`.
4. Run `python scripts/validate_skills.py` before opening a pull request.

## Add a Command

1. Copy `templates/command/COMMAND.md` to `commands/<command-name>.md`.
2. Replace placeholders and document arguments in `argument-hint`.
3. Run `python scripts/validate_skills.py` before opening a pull request.

## Governance

Changes require review and must pass validation. Use release tags and update `CHANGELOG.md` plus both plugin manifest versions together for published releases. See `CONTRIBUTING.md` and `SECURITY.md`.

## License

MIT License. See `LICENSE`.
