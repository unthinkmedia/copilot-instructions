import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install_skills.py"
SPEC = importlib.util.spec_from_file_location("install_skills", SCRIPT)
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallerTests(unittest.TestCase):
    def run_installer(self, destination, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--skills-dir", str(destination), *arguments],
            capture_output=True,
            text=True,
        )

    def test_preview_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills"
            result = self.run_installer(destination)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Preview only", result.stdout)
            self.assertFalse(destination.exists())

    def test_conflicts_require_opt_in_and_backups_preserve_contents(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills"
            existing = destination / "ux-review"
            existing.mkdir(parents=True)
            (existing / "personal.txt").write_text("keep my version", encoding="utf-8")
            unrelated = destination / "unrelated"
            unrelated.mkdir()
            rejected = self.run_installer(destination, "--apply")
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual(set(destination.iterdir()), {existing, unrelated})
            installed = self.run_installer(destination, "--apply", "--replace")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            backups = list((Path(temporary) / "skill-backups").glob("*/ux-review/personal.txt"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "keep my version")
            self.assertTrue(unrelated.is_dir())
            for source in (ROOT / ".github" / "skills").iterdir():
                if (source / "SKILL.md").is_file():
                    self.assertEqual((destination / source.name).resolve(), source.resolve())
            repeated = self.run_installer(destination, "--apply")
            self.assertEqual(repeated.returncode, 0, repeated.stderr)
            self.assertIn("No changes needed", repeated.stdout)

    def test_overlapping_paths_are_rejected(self):
        result = self.run_installer(ROOT / ".github" / "skills")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not overlap", result.stderr)

    def test_non_windows_creates_directory_symlink(self):
        source, destination = Path("source"), Path("destination")
        with patch.object(INSTALLER.os, "name", "posix"):
            with patch.object(Path, "symlink_to") as symlink:
                INSTALLER.create_link(source, destination)
                symlink.assert_called_once_with(source, target_is_directory=True)


if __name__ == "__main__":
    unittest.main()
