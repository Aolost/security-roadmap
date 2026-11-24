"""Generator tests: deterministic output, agreement with data/sources.yaml, escaping."""

import tempfile
import unittest
from pathlib import Path

import yaml

from tests.helpers import FIXTURES, REPO_ROOT, load_script

generator = load_script("generate_sources")


class DeterminismTest(unittest.TestCase):
    def test_repeated_generation_is_byte_identical(self):
        first = generator.generate().encode("utf-8")
        second = generator.generate().encode("utf-8")
        self.assertEqual(first, second)

    def test_committed_sources_md_matches_generator(self):
        committed = (REPO_ROOT / "SOURCES.md").read_bytes()
        self.assertEqual(committed, generator.generate().encode("utf-8"),
                         "SOURCES.md is stale: run `make sources`")

    def test_every_yaml_entry_appears_once(self):
        data = yaml.safe_load((REPO_ROOT / "data" / "sources.yaml").read_text(encoding="utf-8"))
        text = generator.generate()
        for src in data["sources"]:
            self.assertEqual(text.count(f"\n### {src['id']}\n"), 1, src["id"])
            self.assertIn(f"<{src['url']}>", text)

    def test_check_mode_detects_stale_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "SOURCES.md"
            out.write_text("stale\n", encoding="utf-8")
            self.assertEqual(generator.main(["--output", str(out), "--check"]), 1)
            self.assertEqual(generator.main(["--output", str(out)]), 0)
            self.assertEqual(generator.main(["--output", str(out), "--check"]), 0)


class RenderingTest(unittest.TestCase):
    def setUp(self):
        self.text = generator.generate(FIXTURES / "generator" / "sources.yaml")

    def test_entries_sorted_by_id(self):
        self.assertLess(self.text.index("### alpha-ref"), self.text.index("### zeta-tool"))

    def test_markdown_special_characters_are_escaped(self):
        self.assertIn(r"Pipe \| star \* underscore \_ \[brackets\] \<angle\> \#hash \`tick\`", self.text)
        self.assertIn(r"Title with \& and \| characters", self.text)

    def test_redirect_is_not_reported_as_direct_success(self):
        self.assertIn("requested URL answered HTTP 301 (redirect); final destination "
                      "<https://example.org/new> answered HTTP 200", self.text)
        self.assertIn("200 (after redirect)", self.text)


if __name__ == "__main__":
    unittest.main()
