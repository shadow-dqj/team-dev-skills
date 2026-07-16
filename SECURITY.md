# Security Policy

Agent Skills and commands are executable instructions from an agent's perspective. Treat every contribution as code.

## Reporting

Do not open a public issue for a vulnerability or accidental secret disclosure. Use GitHub's private vulnerability reporting or Security Advisory feature for this repository.

If a credential is committed, revoke it immediately. Removing it from the latest commit is not sufficient because it remains in Git history.

## Maintainer checklist

- Review scripts, shell commands, external URLs, and requested permissions.
- Reject instructions that exfiltrate data, bypass approval, weaken security controls, or hide side effects.
- Require explicit confirmation before destructive, production, financial, or externally visible actions.
- Keep release tags immutable and review dependency or tool-install instructions.
- Verify that examples use placeholders rather than real infrastructure or credentials.

## Supported versions

Only the latest release on the default branch receives security updates during the template phase.
