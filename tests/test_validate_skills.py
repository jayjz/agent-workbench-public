import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_skills.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')

    def change_records(self, update):
        entries = v.records(self.root)
        update(entries)
        (self.root / 'skills/INDEX.md').write_text('\n'.join('```json\n'+json.dumps(e)+'\n```' for e in entries))

    def test_actual_repository(self):
        self.assertEqual(v.validate(ROOT), [])

    def test_missing_metadata(self):
        self.change_records(lambda es: es[0].pop('dependencies'))
        self.assertTrue(v.validate(self.root))

    def test_duplicate_name_ownership(self):
        self.change_records(lambda es: es.append(dict(es[0], ownership='external', source='https://example.com')))
        self.assertTrue(any('duplicate name' in e for e in v.validate(self.root)))

    def test_duplicate_source(self):
        self.change_records(lambda es: es.append(dict(es[-1], name='another')))
        self.assertTrue(any('duplicate canonical' in e for e in v.validate(self.root)))

    def test_path_escape(self):
        self.change_records(lambda es: es[0].update(source='../README.md'))
        self.assertTrue(any('invalid local' in e for e in v.validate(self.root)))

    def test_missing_manifest(self):
        (self.root / 'skills/repo-audit/SKILL.md').unlink()
        self.assertTrue(v.validate(self.root))

    def test_unregistered_manifest(self):
        shutil.copytree(self.root / 'skills/repo-audit', self.root / 'skills/extra')
        self.assertTrue(any('unregistered' in e for e in v.validate(self.root)))

    def test_yaml_errors(self):
        path = self.root / 'skills/repo-audit/SKILL.md'
        original = path.read_text()
        for front in ('---\nname: [\n---\n', '---\nname: repo-audit\nname: duplicate\n---\n', 'no front matter\n', '---\nname: repo-audit\ndescription: 42\n---\n'):
            with self.subTest(front=front):
                path.write_text(front+original.split('---', 2)[-1])
                self.assertTrue(v.validate(self.root))

    def test_missing_reference(self):
        path = self.root / 'skills/repo-audit/SKILL.md'
        path.write_text(path.read_text()+'\n[Guide](references/missing.md)\n')
        self.assertTrue(any('missing/escaping' in e for e in v.validate(self.root)))

    def test_invalid_date_and_lifecycle(self):
        self.change_records(lambda es: es[0].update(last_verified='not-a-date', state='MAGIC'))
        self.assertTrue(v.validate(self.root))
