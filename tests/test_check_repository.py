import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('screen', Path(__file__).resolve().parents[1] / 'scripts/check_repository.py')
screen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)


class ScreenTests(unittest.TestCase):
    def test_signatures_without_echoing_value(self):
        secret = b'gh' + b'p_' + b'A' * 36
        self.assertEqual(screen.issues('README.md', secret), ['possible credential signature'])

    def test_private_key(self):
        self.assertTrue(screen.issues('fixture.txt', b'-----BEGIN '+b'OPENSSH PRIVATE KEY-----'))

    def test_generated_and_sensitive_paths(self):
        for name in ('.aws/config', '.env.production', 'a/__pycache__/test.pyc', 'data.sqlite', '.codex/state'):
            self.assertTrue(screen.issues(name, b''))

    def test_normal_files(self):
        for name in ('skills/repo-audit/SKILL.md', '.env.example', 'tests/test_check_repository.py'):
            self.assertEqual(screen.issues(name, b'ordinary fixture'), [])
