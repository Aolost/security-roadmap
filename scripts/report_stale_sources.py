#!/usr/bin/env python3
"""List resources whose `verified_on` date is more than 12 months old.

Offline and read-only: this script never changes data/sources.yaml. A stale entry must be
rechecked by actually opening its URL; only then may its observed fields and
`verified_on` be updated.

Exit status is 0 unless --fail-on-stale is given and stale entries exist.
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCES = REPO_ROOT / "data" / "sources.yaml"


def months_before(day: dt.date, months: int) -> dt.date:
    """The same calendar day `months` earlier, clamped to the end of shorter months."""
    total = day.year * 12 + (day.month - 1) - months
    year, month = divmod(total, 12)
    month += 1
    return dt.date(year, month, min(day.day, calendar.monthrange(year, month)[1]))


def find_stale(sources: list[dict], today: dt.date, max_age_months: int = 12) -> list[tuple[str, str]]:
    cutoff = months_before(today, max_age_months)
    stale = []
    for src in sources:
        verified = dt.date.fromisoformat(str(src["verified_on"]))
        if verified < cutoff:
            stale.append((src["id"], verified.isoformat()))
    return sorted(stale)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report resources not rechecked in the last 12 months.")
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--today", type=dt.date.fromisoformat, default=None, help="override today (YYYY-MM-DD)")
    parser.add_argument("--months", type=int, default=12, help="maximum age in months (default 12)")
    parser.add_argument("--fail-on-stale", action="store_true", help="exit 1 when stale entries exist")
    args = parser.parse_args(argv)

    today = args.today or dt.date.today()
    data = yaml.safe_load(args.sources.read_text(encoding="utf-8"))
    stale = find_stale(data["sources"], today, args.months)

    if not stale:
        print(f"No stale sources: every entry was verified within the last {args.months} months.")
        return 0
    print(f"{len(stale)} source(s) last verified more than {args.months} months ago (before "
          f"{months_before(today, args.months).isoformat()}):")
    for sid, verified in stale:
        print(f"- {sid} (verified_on {verified})")
    print("Recheck each URL by opening it, then update its observed fields and verified_on.")
    return 1 if args.fail_on_stale else 0


if __name__ == "__main__":
    sys.exit(main())
