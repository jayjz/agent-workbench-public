from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.dest = self.base / '.agents/skills'

    def run_install(self, mode, *names):
        return subprocess.run(['bash', str(ROOT / 'scripts/install-local.sh'), mode,
                               '--dest', str(self.dest), *names], text=True, capture_output=True)

    def test_list(self):
        result = self.run_install('--list')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(result.stdout.splitlines()), {'repo-audit', 'evidence-contract', 'change-verifier', 'source-integrity-audit'})
        self.assertFalse(self.dest.exists())

    def test_preview_no_writes_and_check_missing(self):
        self.assertEqual(self.run_install('--dry-run', 'repo-audit').returncode, 0)
        self.assertFalse(self.dest.exists())
        self.assertEqual(self.run_install('--check', 'repo-audit').returncode, 1)
        self.assertFalse(self.dest.exists())

    def test_install_selective_idempotent(self):
        self.assertEqual(self.run_install('--install', 'repo-audit').returncode, 0)
        link = self.dest / 'repo-audit'
        inode = link.lstat().st_ino
        self.assertEqual(link.resolve(), ROOT / 'skills/repo-audit')
        self.assertEqual(self.run_install('--install', 'repo-audit').returncode, 0)
        self.assertEqual(link.lstat().st_ino, inode)
        self.assertEqual(self.run_install('--check', 'repo-audit').returncode, 0)
        self.assertEqual([p.name for p in self.dest.iterdir()], ['repo-audit'])
        self.assertFalse((self.base / '.codex').exists())

    def test_conflicts_preflight_no_partial_install(self):
        for kind in ('file', 'directory', 'dangling', 'foreign'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory(dir=self.base) as tmp:
                self.dest = Path(tmp) / 'skills'
                self.dest.mkdir()
                conflict = self.dest / 'repo-audit'
                if kind == 'file':
                    conflict.write_text('preserve me')
                elif kind == 'directory':
                    conflict.mkdir()
                else:
                    conflict.symlink_to(self.base / ('missing' if kind == 'dangling' else '.'))
                before = conflict.lstat()
                self.assertEqual(self.run_install('--install', 'evidence-contract', 'repo-audit').returncode, 1)
                self.assertFalse((self.dest / 'evidence-contract').exists())
                after = conflict.lstat()
                self.assertEqual((after.st_ino, after.st_mode, after.st_size, after.st_mtime_ns),
                                 (before.st_ino, before.st_mode, before.st_size, before.st_mtime_ns))
                if kind == 'file':
                    self.assertEqual(conflict.read_text(), 'preserve me')
                elif kind in ('foreign', 'dangling'):
                    self.assertEqual(conflict.readlink(), self.base / ('missing' if kind == 'dangling' else '.'))

    def test_symlink_ancestor_refused(self):
        real = self.base / 'real'
        real.mkdir()
        (self.base / 'redirect').symlink_to(real)
        self.dest = self.base / 'redirect/skills'
        self.assertEqual(self.run_install('--install', 'repo-audit').returncode, 1)
        self.assertFalse((real / 'skills').exists())

    def test_invalid_selection(self):
        for names in ((), ('../escape',), ('security-audit',), ('change-review',), ('repo-audit', 'repo-audit')):
            self.assertEqual(self.run_install('--install', *names).returncode, 2)
        self.assertFalse(self.dest.exists())

    def test_destination_file(self):
        self.dest.parent.mkdir()
        self.dest.write_text('preserve')
        self.assertEqual(self.run_install('--install', 'repo-audit').returncode, 1)
        self.assertEqual(self.dest.read_text(), 'preserve')
