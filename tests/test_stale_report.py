"""Stale-source report tests: entries older than 12 months are listed; dates are not changed."""

import datetime as dt
import unittest

from tests.helpers import load_script

stale = load_script("report_stale_sources")


class StaleReportTest(unittest.TestCase):
    def test_only_entries_older_than_twelve_months_are_listed(self):
        sources = [
            {"id": "old", "verified_on": "2024-11-24"},
            {"id": "boundary", "verified_on": "2024-11-25"},
            {"id": "fresh", "verified_on": "2025-06-01"},
        ]
        result = stale.find_stale(sources, dt.date(2025, 11, 25))
        self.assertEqual(result, [("old", "2024-11-24")])
        self.assertEqual(sources[0]["verified_on"], "2024-11-24")


if __name__ == "__main__":
    unittest.main()
