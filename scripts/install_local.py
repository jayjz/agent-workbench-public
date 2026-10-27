#!/usr/bin/env python3
"""Selectively link local skills; never copy instructions or replace destinations."""
import argparse
import os
from pathlib import Path
import sys

from validate_skills import records, validate

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    for mode in ('dry-run', 'install', 'list', 'check'):
        modes.add_argument('--'+mode, action='store_true')
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents/skills',
                        help='Discovery directory; default ~/.agents/skills; use PROJECT/.agents/skills for project selection')
    parser.add_argument('skills', nargs='*', help='Explicit local skill names; no install-all default')
    args = parser.parse_args()
    errors = validate(ROOT)
    if errors:
        parser.exit(1, '\n'.join(errors)+'\n')
    available = {e['name']: ROOT / 'skills' / e['source'] for e in records(ROOT)
                 if e['ownership'] == 'local' and e['state'] in ('EXPERIMENTAL', 'EVALUATED', 'STABLE')}
    if args.list:
        for name in sorted(available):
            print(name)
        return 0
    if not args.skills or len(set(args.skills)) != len(args.skills):
        parser.error('supply distinct explicit skill names')
    if any(name not in available for name in args.skills):
        parser.error('unknown, external or inactive skill selected')
    dest = args.dest.expanduser().absolute()
    # Reject redirected parents too: do not traverse links into unrelated locations.
    if any(p.is_symlink() for p in (dest, *dest.parents)):
        parser.exit(1, f'refusing symlink destination/ancestor: {dest}\n')
    if dest.exists() and not dest.is_dir():
        parser.exit(1, f'destination is not a directory: {dest}\n')
    planned = []
    conflicts = []
    for name in args.skills:
        source = available[name].parent.resolve()
        target = dest / name
        if target.is_symlink() and target.resolve() == source:
            status = 'OK'
        elif os.path.lexists(target):
            status = 'CONFLICT'
            conflicts.append(target)
        else:
            status = 'MISSING'
        print(f'{status} {target} -> {source}')
        planned.append((source, target, status))
    if conflicts:
        return 1
    if args.check:
        return int(any(status != 'OK' for _, _, status in planned))
    if args.install:
        dest.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for source, target, status in planned:
                if status == 'MISSING':
                    target.symlink_to(source, target_is_directory=True)
                    created.append(target)
        except OSError:
            # Only remove links this invocation created, and only if still ours.
            for target in reversed(created):
                expected = next(s for s, t, _ in planned if t == target)
                if target.is_symlink() and target.resolve() == expected:
                    target.unlink()
            raise
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except OSError as exc:
        print(f'Installation failed: {exc}', file=sys.stderr)
        sys.exit(1)
