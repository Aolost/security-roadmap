"""CLI tests: progress persistence, missing file, corrupt file. Runs `python -m roadmap`."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.helpers import REPO_ROOT


class CliTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.progress = Path(self._tmp.name) / "nested" / "progress.json"

    def run_cli(self, *args):
        env = dict(os.environ, SECURITY_ROADMAP_PROGRESS=str(self.progress))
        return subprocess.run(
            [sys.executable, "-m", "roadmap", *args],
            cwd=REPO_ROOT, env=env, capture_output=True, text=True, timeout=60,
        )


class PersistenceTest(CliTestCase):
    def test_done_persists_across_invocations(self):
        result = self.run_cli("done", "legal-ethics")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.progress.is_file())
        saved = json.loads(self.progress.read_text(encoding="utf-8"))
        self.assertIn("legal-ethics", saved["completed"])

        listing = self.run_cli("list")
        self.assertIn("[x] 0  legal-ethics", listing.stdout)
        self.assertIn("[ ] 1  foundations", listing.stdout)

        nxt = self.run_cli("next")
        self.assertIn("foundations", nxt.stdout)

        status = self.run_cli("status")
        self.assertIn("Overall: 1/7 phases complete", status.stdout)

    def test_unknown_phase_is_rejected_without_writing(self):
        result = self.run_cli("done", "not-a-phase")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown phase ID", result.stderr)
        self.assertFalse(self.progress.exists())

    def test_all_phases_complete(self):
        from roadmap.phases import PHASE_IDS

        for phase_id in PHASE_IDS:
            self.assertEqual(self.run_cli("done", phase_id).returncode, 0)
        self.assertIn("All phases are complete.", self.run_cli("next").stdout)


class MissingFileTest(CliTestCase):
    def test_missing_file_is_a_fresh_start(self):
        result = self.run_cli("status")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Overall: 0/7 phases complete", result.stdout)
        self.assertFalse(self.progress.exists(), "read-only commands must not create the file")
        self.assertIn("legal-ethics", self.run_cli("next").stdout)


class CorruptFileTest(CliTestCase):
    def write_corrupt(self, content: str) -> None:
        self.progress.parent.mkdir(parents=True)
        self.progress.write_text(content, encoding="utf-8")

    def test_invalid_json_is_reported_and_left_untouched(self):
        self.write_corrupt("{not json")
        for args in (("status",), ("list",), ("next",), ("done", "foundations")):
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, 3, args)
            self.assertIn("is not valid JSON", result.stderr)
            self.assertIn("left unchanged", result.stderr)
        self.assertEqual(self.progress.read_text(encoding="utf-8"), "{not json")
        self.assertEqual(list(self.progress.parent.iterdir()), [self.progress], "no stray files")

    def test_wrong_shape_is_reported(self):
        self.write_corrupt('["a list, not an object"]')
        result = self.run_cli("status")
        self.assertEqual(result.returncode, 3)
        self.assertIn("'completed'", result.stderr)


if __name__ == "__main__":
    unittest.main()
