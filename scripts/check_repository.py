#!/usr/bin/env python3
"""Screen publishable Git content for common secrets and generated artifacts.

Default: tracked working-tree files plus nonignored untracked files.
--staged: exact index blobs. Only file paths/reasons are printed, never matches.
This bounded pattern screen cannot prove absence of secrets.
"""
import argparse
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {'.aws', '.codex', '.agents', '.venv', '__pycache__', 'node_modules', 'secrets', 'credentials', 'dist', 'build'}
PATTERNS = [re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
            re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'),
            re.compile(rb'github_pat_[A-Za-z0-9_]{50,}'),
            re.compile(rb'AKIA[A-Z0-9]{16}'),
            re.compile(rb'sk-(?:proj-)?[A-Za-z0-9_-]{40,}')]


def issues(name, data):
    path = PurePosixPath(name)
    result = []
    if (set(path.parts) & FORBIDDEN_PARTS or
        (path.name.startswith('.env') and path.name != '.env.example') or
        path.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.pyc', '.db', '.sqlite', '.log'}):
        result.append('forbidden/generated path')
    if any(pattern.search(data) for pattern in PATTERNS):
        result.append('possible credential signature')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staged', action='store_true')
    args = parser.parse_args()
    command = ['git', 'ls-files', '-z']
    if not args.staged:
        command.extend(['--cached', '--others', '--exclude-standard'])
    names = sorted(set(subprocess.check_output(command, cwd=ROOT).decode().split('\0')) - {''})
    errors = []
    count = 0
    for name in names:
        if args.staged:
            data = subprocess.check_output(['git', 'show', ':'+name], cwd=ROOT)
        else:
            path = ROOT / name
            if not path.exists():
                continue
            if path.is_symlink():
                errors.append(f'{name}: publishable symlink requires manual review')
                continue
            data = path.read_bytes()
        count += 1
        errors.extend(f'{name}: {issue}' for issue in issues(name, data))
    for error in errors:
        print(error)
    print(f'Content screen: {count} files, {len(errors)} issue(s); limited patterns only')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
