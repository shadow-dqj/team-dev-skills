# Team Dev Skills

> **PRIVATE REPOSITORY - Internal team use only.** Do not redistribute repository content or grant access outside the authorized team.

A centrally maintained collection of Agent Skills and Claude Code commands for team project development.

Never commit credentials, internal hosts, customer data, private source code, production procedures, or other sensitive material. Project-specific implementation guidance is allowed only when it is necessary for authorized internal development and passes repository validation and review.

## Repository layout

```text
skills/<project>/<skill-name>/SKILL.md  Agent Skills discovered recursively
commands/<command-name>.md              Claude Code slash commands
.claude-plugin/plugin.json              Claude plugin manifest
.claude-plugin/marketplace.json         Claude marketplace manifest
templates/                              Copy-ready contribution templates
scripts/validate_skills.py              Repository validation
```

## Install Skills with CC Switch

CC Switch manages the contents of `skills/`; it does not install the Claude-specific `commands/` directory.

1. Authenticate CC Switch for access to this private GitHub repository using the team's approved GitHub account or token flow.
2. Open **CC Switch > Skills > Repository Management**.
3. Add `shadow-dqj/team-dev-skills`, select branch `main`, and refresh discovery.
4. Install the required skills and select the target agents to synchronize.

CC Switch recursively discovers directories containing `SKILL.md`, so project-specific skills live under `skills/<project>/<skill-name>/`.

Do not paste a personal access token into project files, chat, screenshots, or command history. Follow the team's credential-management process.

## Install Skills and Commands with Claude Code

Private repository installation requires GitHub authentication in the environment where Claude Code runs. After authentication, install directly:

```bash
claude plugin install https://github.com/shadow-dqj/team-dev-skills
```

Marketplace installation is also supported when the private repository is accessible:

```text
/plugin marketplace add shadow-dqj/team-dev-skills
/plugin install team-dev-skills@team-dev-skills
```

Restart Claude Code after installation if prompted.

## Add a Skill

1. Copy `templates/skill/` to `skills/<project>/<skill-name>/`.
2. Replace all placeholders and keep the skill directory name and frontmatter `name` identical.
3. Put detailed material in `references/`, executable helpers in `scripts/`, and static files in `assets/`.
4. Run `python scripts/validate_skills.py` before opening a pull request.

## Add a Command

1. Copy `templates/command/COMMAND.md` to `commands/<command-name>.md`.
2. Replace placeholders and document arguments in `argument-hint`.
3. Run `python scripts/validate_skills.py` before opening a pull request.

## Governance

Changes require review and must pass validation. Use release tags and update `CHANGELOG.md` plus both plugin manifest versions together for releases. See `CONTRIBUTING.md` and `SECURITY.md`.

## License

UNLICENSED. Internal use only. See `LICENSE`.
