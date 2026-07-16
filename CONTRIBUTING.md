# Contributing

## Scope

This private repository is for reusable internal project-development Skills and Claude Code commands. Contributions may include project-specific guidance needed by authorized team members, but must stay focused and avoid unnecessary implementation disclosure.

Never include:

- credentials, tokens, certificates, connection strings, or private keys;
- internal hostnames, IP addresses, VPN details, or production procedures;
- private source code, customer data, contracts, or non-public business data;
- copied third-party content without compatible licensing and attribution.

Do not redistribute repository content or grant access outside the authorized team.

## Add a Skill

1. Copy `templates/skill/` to `skills/<project>/<skill-name>/`.
2. Use a unique lowercase kebab-case skill name that matches its directory.
3. Keep the main `SKILL.md` focused and move detailed material to `references/`.
4. Review every script as executable code and document prerequisites and side effects.
5. Run `python scripts/validate_skills.py`.

## Add a Command

1. Copy `templates/command/COMMAND.md` to `commands/<command-name>.md`.
2. Define a focused workflow and clear argument contract.
3. Require confirmation for destructive or externally visible actions.
4. Run `python scripts/validate_skills.py`.

## Pull requests

Keep one logical change per pull request. Explain activation conditions, supported agents, manual testing, project scope, and security considerations. At least one maintainer should review content that can execute commands, access external systems, or expose project-specific details.

## Releases

Use semantic versions. Update `CHANGELOG.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` together. Prefer signed release tags and do not rewrite published tags.
