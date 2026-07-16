# Contributing

## Scope

This public repository is for reusable project-development Skills and Claude Code commands. Contributions must be generic enough to publish publicly.

Never include:

- credentials, tokens, certificates, connection strings, or private keys;
- internal hostnames, IP addresses, VPN details, or production procedures;
- private source code, customer data, contracts, or non-public business rules;
- copied third-party content without compatible licensing and attribution.

## Add a Skill

1. Copy `templates/skill/` to `skills/<skill-name>/`.
2. Use a globally unique lowercase kebab-case name.
3. Keep the main `SKILL.md` focused and move detailed material to `references/`.
4. Review every script as executable code and document prerequisites and side effects.
5. Run `python scripts/validate_skills.py`.

## Add a Command

1. Copy `templates/command/COMMAND.md` to `commands/<command-name>.md`.
2. Define a focused workflow and clear argument contract.
3. Require confirmation for destructive or externally visible actions.
4. Run `python scripts/validate_skills.py`.

## Pull requests

Keep one logical change per pull request. Explain activation conditions, supported agents, manual testing, and security considerations. At least one maintainer should review content that can execute commands or access external systems.

## Releases

Use semantic versions. Update `CHANGELOG.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` together. Prefer signed release tags and do not rewrite published tags.
