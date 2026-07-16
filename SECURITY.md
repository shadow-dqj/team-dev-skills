# Security Policy

Agent Skills and commands are executable instructions from an agent's perspective. Treat every contribution as code and every project-specific reference as internal information.

## Reporting

Report vulnerabilities or accidental disclosures through GitHub's private vulnerability reporting or Security Advisory feature, or through the team's approved private security channel. Do not place sensitive details in broadly visible issues, chats, screenshots, or logs.

If a credential is committed, revoke it immediately. Removing it from the latest commit is not sufficient because it remains in Git history.

## Maintainer checklist

- Confirm the repository remains private and collaborators still require access.
- Review scripts, shell commands, external URLs, and requested permissions.
- Reject instructions that exfiltrate data, bypass approval, weaken security controls, or hide side effects.
- Require explicit confirmation before destructive, production, financial, or externally visible actions.
- Keep release tags immutable and review dependency or tool-install instructions.
- Verify examples use placeholders rather than real infrastructure or credentials.
- Minimize project-specific fingerprints and do not include source code when a path or rule is sufficient.

## Supported versions

Only the latest release on the default branch receives security updates.
