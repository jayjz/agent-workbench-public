# v0.1 verification record

Date: 2026-10-26. Environment: Linux, Python 3 with PyYAML 6.0.1; Bash and Git. The runtime model identity is not independently recorded; no model effectiveness evaluation was performed.

## Discovery and preservation

Read all eleven original scaffold files and every original manifest. `git status --short --branch` reported no commits on main and untracked scaffold files; `git log -5 --oneline` failed because no history existed. Git identity was configured as jayjz (email checked locally). No remote existed. Original files were committed unchanged as `04282a5` on `feat/personal-skills-registry-v0.1` before editing. Initial sandboxed Git writes failed read-only; the authorized escalated retry succeeded.

GitHub README discovery succeeded for all six requested repositories through the connector. The root security-audit manifest fetch failed 404, retained as unresolved. `gh repo view jayjz/agent-workbench` first failed in the network sandbox; its authorized retry reported the destination could not be resolved. No credentials or authentication configuration were modified.

## Checks

The first 17-test run had five failures because README/roadmap linked to this record before it existed. The validator correctly rejected the missing references and blocked installer operations. This record resolves the missing artifact; results after rerunning are recorded below.

Final results and remote publication state are recorded after execution. No controlled behavioral evaluation, live Codex discovery, WSL/native Windows test, external-project installation, or production operation is claimed.

A subsequent 21-test run exposed an overly broad test assertion: resolving a foreign symlink may update its access time. The test now verifies inode, mode, size, modification time and exact content/link target, which are the preservation contract. Access time is not treated as a write to user content. No installer behavior was relaxed.

## Successful final checks

- `python3 -m unittest discover -s tests -v`: 21 tests passed, including malformed/duplicate metadata, registry ownership/path errors, missing references, selective installation, no-write preview, conflicts, dangling links, redirected ancestors and idempotence. Tests install only into temporary directories.
- `python3 scripts/validate_skills.py`: 0 errors.
- `bash -n scripts/install-local.sh`: exit 0.
- `bash scripts/install-local.sh --dry-run repo-audit evidence-contract change-verifier`: exit 0, reports three missing user links, creates nothing.
- System skill-creator `quick_validate.py` executed separately for all three active skills: each reported valid.
- `python3 scripts/check_repository.py`: 22 publishable files screened, 0 issues. Pattern coverage is limited; this is not proof of no secrets.
- `git diff --check`: exit 0.

The catalog verification dates refer only to mechanical manifest/registry checks. Skills remain EXPERIMENTAL (legacy change-review DEPRECATED). No behavioral promotion occurred.

The explicitly intended private repository was created at `https://github.com/jayjz/agent-workbench`. Publication uses only `feat/personal-skills-registry-v0.1`; no merge, unrelated repository write or user-level install is included. Exact remote visibility, staged screen and final branch agreement are verified in the execution report.
