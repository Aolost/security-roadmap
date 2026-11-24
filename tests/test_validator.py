"""Validator tests: the real repository data passes; each broken fixture fails for its reason."""

import datetime as dt
import unittest

from tests.helpers import FIXTURES, REPO_ROOT, load_script

validator = load_script("validate_sources")
TODAY = dt.date(2026, 1, 1)


def run_fixture(name: str) -> list[str]:
    root = FIXTURES / name
    return validator.validate(root / "sources.yaml", sorted((root / "docs").glob("*.md")), today=TODAY)


class RepositoryDataTest(unittest.TestCase):
    def test_repository_sources_are_valid(self):
        errors = validator.validate(validator.DEFAULT_SOURCES, validator.default_doc_paths())
        self.assertEqual(errors, [])


class BrokenFixtureTest(unittest.TestCase):
    def assert_single_error(self, fixture: str, expected: str) -> None:
        errors = run_fixture(fixture)
        self.assertTrue(errors, f"{fixture} should fail validation")
        self.assertTrue(all(expected in e for e in errors), errors)

    def test_valid_fixture_passes(self):
        self.assertEqual(run_fixture("valid"), [])

    def test_duplicate_id(self):
        self.assert_single_error("duplicate_id", "duplicate id 'fixture-alpha'")

    def test_missing_field(self):
        self.assert_single_error("missing_field", "'why_included' is a required property")

    def test_unknown_phase_reference(self):
        self.assert_single_error("unknown_phase_reference", "unknown source reference 'src:does-not-exist'")

    def test_bad_url_scheme(self):
        self.assert_single_error("bad_url_scheme", "uses scheme 'ftp'")

    def test_future_verification_date(self):
        self.assert_single_error("future_date", "'2999-01-01' is in the future")

    def test_orphaned_source(self):
        self.assert_single_error("orphaned_source", "orphaned source 'fixture-beta'")

    def test_cli_exit_status(self):
        root = FIXTURES / "duplicate_id"
        code = validator.main(["--sources", str(root / "sources.yaml"), "--docs-dir", str(root / "docs")])
        self.assertEqual(code, 1)


class RedirectConsistencyTest(unittest.TestCase):
    def base(self, **overrides):
        src = {
            "id": "x", "url": "https://example.org/a", "final_url": "https://example.org/a",
            "http_status": 200, "final_http_status": 200, "verified_on": "2025-01-01",
        }
        src.update(overrides)
        return validator.check_source(src, TODAY)

    def test_redirect_recorded_as_direct_success_is_rejected(self):
        errors = self.base(http_status=301)
        self.assertTrue(any("is a redirect" in e for e in errors), errors)

    def test_inaccessible_final_status_is_rejected(self):
        errors = self.base(final_http_status=404)
        self.assertTrue(any("not a success" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
