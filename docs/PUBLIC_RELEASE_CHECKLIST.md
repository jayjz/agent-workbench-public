# Public release gate (not yet passed)

**Default: NO-GO** until every item below is reviewed. Do not flip GitHub visibility solely because a scanner reports zero hits.

## Inspect all refs and history

Run in a trusted local checkout, ideally a fresh mirror or clean clone with every remote branch and tag fetched. Review outputs locally; do not post sensitive matches in PRs.

```bash
git fetch --all --tags --prune
git branch -a
git log --all --format='%h %an <%ae> %s'
git ls-files -z | xargs -0 -r -n1 printf '%s\n'
python3 scripts/check_repository.py
python3 scripts/check_repository.py --staged
```

Use `gitleaks git --redact .` (or an equivalently configured and validated history scanner) to screen all reachable commit history. Tool availability and results must be recorded; do not claim the scan ran if it did not. Review findings manually, including known test fixtures and false positives.

Review *all* reachable historical blobs/branches, not just current tracked files, for:
- Names, personal email addresses, phone numbers, addresses, account and device identifiers, private usernames, private Notion/database identifiers, screenshots, absolute home paths, and other identity-linkable details.
- Tokens, keys, credentials, signed URLs, secrets in examples and test fixtures.
- Private repo/org references, unpublished work, customer/client information, personal notes and license-incompatible copied material.
- Commit author/committer metadata, branches, tags, PR discussions and release artifacts.
- Disclosures of infrastructure layout, threat-model-sensitive settings, hostnames, network addresses, and audit details that are unnecessary for public documentation.

Do **not** publish scanner matches or sensitive values in an issue. Rotate exposed credentials. If sensitive data exists anywhere in reachable history, assess and execute an explicitly reviewed history-remediation plan **before** publication; normal file deletion is insufficient. Recheck all refs and GitHub cached artifacts after any approved remediation. Never force-push automatically.

## Documentation and licensing

- Review README links, installation instructions, skill names, states, version assumptions and platform support.
- Confirm license choice and permissions for third-party code, images and adapted skill text; add LICENSE only after selecting it.
- Confirm topics/description and release notes are accurate (suggested topics: `agent-skills`, `codex`, `research`, `provenance`, `evaluation`, `developer-tools`).
- Confirm no private contact details or unrestricted contribution promises.
- Check scripts have no side effects outside their described scope.
- Run tests and document actual results, failures and runtime environment.
- Perform a final manual diff and source check of the exact publication commit.
- Only then explicitly authorize the repository visibility change.

## Current limitations

This checklist records **required future checks**, not proof they have passed. Earlier `knowledge/verification.md` describes bounded prior checks, not a whole-history PII audit. GitHub code search of the current indexed branch is not exhaustive and cannot replace the above investigation.
