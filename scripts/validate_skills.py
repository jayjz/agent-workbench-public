#!/usr/bin/env python3
"""Validate local manifests and the machine-readable records in skills/INDEX.md."""
import argparse
import datetime
import json
from pathlib import Path
import re
import sys

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
REQUIRED = {'name', 'job_trigger', 'source', 'ownership', 'state', 'dependencies',
            'runtimes', 'validation', 'last_verified', 'related_repositories', 'limitations'}
STATES = {'PROPOSED', 'EXPERIMENTAL', 'EVALUATED', 'STABLE', 'REJECTED', 'DEPRECATED'}


def records(root):
    text = (root / 'skills/INDEX.md').read_text()
    blocks = re.findall(r'^```json\n(.*?)\n```$', text, re.M | re.S)
    if not blocks:
        raise ValueError('registry contains no JSON records')
    return [json.loads(block) for block in blocks]


def inside(path, parent):
    return path.resolve().is_relative_to(parent.resolve())


def manifest(path):
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n(.*)', text, re.S)
    if not match:
        raise ValueError('missing delimited YAML front matter')
    data = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError('front matter must be a mapping')
    for key in ('name', 'description'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} must be a nonempty string')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', data['name']) or len(data['name']) > 64:
        raise ValueError('invalid skill name')
    if len(data['description']) > 1024:
        raise ValueError('description exceeds 1024 characters')
    if data['name'] != path.parent.name:
        raise ValueError('name differs from directory')
    for section in ('Trigger', 'Non-triggers', 'Procedure', 'Output', 'Verification', 'Limitations'):
        if not re.search(r'^## '+section+r'\s*$', match[2], re.M):
            raise ValueError(f'missing {section} section')
    return data


def validate(root):
    errors = []
    try:
        entries = records(root)
    except (OSError, ValueError) as exc:
        return [str(exc)]
    names, sources, local = set(), set(), set()
    for entry in entries:
        try:
            if not isinstance(entry, dict) or REQUIRED - entry.keys():
                raise ValueError('missing registry metadata')
            for key in REQUIRED - {'last_verified', 'dependencies', 'runtimes', 'related_repositories'}:
                if not isinstance(entry[key], str) or not entry[key].strip():
                    raise ValueError(f'invalid {key}')
            for key in ('dependencies', 'runtimes', 'related_repositories'):
                if not isinstance(entry[key], list) or any(not isinstance(x, str) or not x for x in entry[key]):
                    raise ValueError(f'invalid {key}')
            if entry['name'] in names:
                raise ValueError('duplicate name/ownership')
            names.add(entry['name'])
            if entry['ownership'] not in ('local', 'external'):
                raise ValueError('invalid ownership')
            if entry['state'] not in STATES | ({'UNRESOLVED'} if entry['ownership'] == 'external' else set()):
                raise ValueError('invalid lifecycle')
            if entry['last_verified'] is not None:
                datetime.date.fromisoformat(entry['last_verified'])
                if 'unverified' in entry['validation'].lower():
                    raise ValueError('verification date contradicts status')
            if entry['ownership'] == 'external':
                if not entry['source'].startswith('https://'):
                    raise ValueError('external source must use HTTPS')
                source = entry['source'].rstrip('/')
            else:
                path = root / 'skills' / entry['source']
                if not inside(path, root / 'skills') or path.name != 'SKILL.md' or not path.is_file():
                    raise ValueError('invalid local registry path')
                source = str(path.resolve())
                if manifest(path)['name'] != entry['name']:
                    raise ValueError('registry/manifest name mismatch')
                local.add(path.resolve())
            if source in sources:
                raise ValueError('duplicate canonical source/ownership')
            sources.add(source)
        except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{entry.get('name', '?') if isinstance(entry, dict) else '?'}: {exc}")
    for path in (root / 'skills').rglob('SKILL.md'):
        if path.resolve() not in local:
            errors.append(f'unregistered manifest: {path.relative_to(root)}')
    # Validate local Markdown links throughout owned documentation, excluding runtime state.
    paths = [root / p for p in ('README.md', 'ROADMAP.md')]
    for folder in ('skills', 'knowledge', 'global', 'templates'):
        paths.extend((root / folder).rglob('*.md'))
    for path in paths:
        if not path.is_file():
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#')[0]
            dest = path.parent / target
            if not inside(dest, root) or not dest.exists():
                errors.append(f'{path.relative_to(root)}: missing/escaping reference {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Validation: {len(errors)} error(s)')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
