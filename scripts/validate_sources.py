#!/usr/bin/env python3
"""Validate data/sources.yaml and the phase documents that reference it.

Offline only: this script never opens a network connection.

Checks:
  * the YAML matches data/sources.schema.json (required fields, allowed values)
  * IDs are unique
  * URLs use a permitted scheme (https)
  * dates are real calendar dates and not in the future
  * redirect metadata is self-consistent (a 3xx is never recorded as a direct success)
  * every `src:ID` reference in the phase documents resolves to a source
  * every source is referenced by at least one phase document (no orphans)

Exit status: 0 when valid, 1 when any problem is found.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import yaml  # noqa: E402
from jsonschema import Draft202012Validator  # noqa: E402

from roadmap.phases import PHASES  # noqa: E402

DEFAULT_SOURCES = REPO_ROOT / "data" / "sources.yaml"
DEFAULT_SCHEMA = REPO_ROOT / "data" / "sources.schema.json"
PERMITTED_SCHEMES = frozenset({"https"})
UNKNOWN = "unknown"
REFERENCE_RE = re.compile(r"\bsrc:([a-z0-9]+(?:-[a-z0-9]+)*)")


def load_yaml(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _stringify_dates(value: object) -> object:
    """YAML may parse unquoted dates into date objects; the schema expects strings."""
    if isinstance(value, dict):
        return {k: _stringify_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_stringify_dates(v) for v in value]
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    return value


def _format_path(parts: object) -> str:
    out = ""
    for part in parts:  # type: ignore[union-attr]
        out += f"[{part}]" if isinstance(part, int) else f".{part}"
    return out.lstrip(".") or "(root)"


def schema_errors(data: object, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(map(str, e.absolute_path))):
        where = _format_path(err.absolute_path)
        if err.validator == "required":
            errors.append(f"schema: {where}: missing required field ({err.message})")
        else:
            errors.append(f"schema: {where}: {err.message}")
    return errors


def latest_calendar_date() -> dt.date:
    """The latest calendar date anywhere on Earth right now (UTC+14).

    Contributors record `verified_on` in their own time zone, while CI runs in UTC. Comparing
    against the latest date in use anywhere avoids rejecting a date that is already "today"
    for the person who checked the resource, while still rejecting genuinely future dates.
    """
    return (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=14)).date()


def check_date(value: object, label: str, today: dt.date) -> list[str]:
    if not isinstance(value, str):
        return []  # the schema reports the wrong type
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError:
        return [f"{label}: '{value}' is not a valid calendar date"]
    if parsed > today:
        return [f"{label}: '{value}' is in the future (today is {today.isoformat()})"]
    return []


def check_url(value: object, label: str) -> list[str]:
    if not isinstance(value, str) or value == UNKNOWN:
        return []
    parts = urlsplit(value)
    if parts.scheme.lower() not in PERMITTED_SCHEMES:
        allowed = ", ".join(sorted(PERMITTED_SCHEMES))
        return [f"{label}: URL '{value}' uses scheme '{parts.scheme}'; permitted: {allowed}"]
    if not parts.netloc:
        return [f"{label}: URL '{value}' has no host"]
    return []


def check_source(src: dict, today: dt.date) -> list[str]:
    sid = src.get("id", "<no id>")
    errors: list[str] = []
    errors += check_url(src.get("url"), f"{sid}.url")
    errors += check_url(src.get("final_url"), f"{sid}.final_url")
    errors += check_date(src.get("verified_on"), f"{sid}.verified_on", today)

    book = src.get("book")
    if isinstance(book, dict):
        errors += check_url(book.get("details_source"), f"{sid}.book.details_source")
        if src.get("type") != "book":
            errors.append(f"{sid}: 'book' details are only allowed on type 'book'")
    cert = src.get("certification")
    if isinstance(cert, dict):
        errors += check_date(cert.get("checked_on"), f"{sid}.certification.checked_on", today)

    status = src.get("http_status")
    final_status = src.get("final_http_status", status)
    url, final_url = src.get("url"), src.get("final_url")
    if isinstance(status, int):
        if 300 <= status < 400:
            if final_url in (None, UNKNOWN) or final_url == url:
                errors.append(f"{sid}: http_status {status} is a redirect, so final_url must record the observed destination")
            if "final_http_status" not in src:
                errors.append(f"{sid}: redirected resources must record final_http_status")
        elif 200 <= status < 300 and final_url not in (None, UNKNOWN) and final_url != url:
            errors.append(f"{sid}: http_status {status} means no redirect, but final_url differs from url")
    if isinstance(final_status, int) and not 200 <= final_status < 300:
        errors.append(
            f"{sid}: final status {final_status} is not a success; omit resources that could not be confirmed"
        )
    return errors


def collect_references(doc_paths: list[Path]) -> dict[str, list[str]]:
    """Map each referenced source ID to the documents that reference it."""
    refs: dict[str, list[str]] = {}
    for path in doc_paths:
        text = path.read_text(encoding="utf-8")
        for match in REFERENCE_RE.finditer(text):
            refs.setdefault(match.group(1), [])
            if path.name not in refs[match.group(1)]:
                refs[match.group(1)].append(path.name)
    return refs


def default_doc_paths(root: Path = REPO_ROOT) -> list[Path]:
    return [root / phase.doc for phase in PHASES]


def validate(
    sources_path: Path,
    doc_paths: list[Path],
    schema_path: Path = DEFAULT_SCHEMA,
    today: dt.date | None = None,
) -> list[str]:
    """Return a list of human-readable problems; an empty list means valid."""
    today = today or latest_calendar_date()
    errors: list[str] = []

    try:
        data = _stringify_dates(load_yaml(sources_path))
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot read {sources_path}: {exc}"]
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors += schema_errors(data, schema)

    sources = data.get("sources") if isinstance(data, dict) else None
    if not isinstance(sources, list):
        return errors or ["sources: expected a list"]
    sources = [s for s in sources if isinstance(s, dict)]

    seen: dict[str, int] = {}
    for index, src in enumerate(sources):
        sid = src.get("id")
        if isinstance(sid, str):
            if sid in seen:
                errors.append(f"duplicate id '{sid}' (entries {seen[sid]} and {index})")
            else:
                seen[sid] = index
        errors += check_source(src, today)

    missing_docs = [p for p in doc_paths if not p.is_file()]
    for path in missing_docs:
        errors.append(f"phase document not found: {path}")
    refs = collect_references([p for p in doc_paths if p.is_file()])

    for ref_id in sorted(refs):
        if ref_id not in seen:
            docs = ", ".join(refs[ref_id])
            errors.append(f"unknown source reference 'src:{ref_id}' in {docs}")
    for sid in sorted(seen):
        if sid not in refs:
            errors.append(f"orphaned source '{sid}' is not referenced by any phase document")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument(
        "--docs-dir",
        type=Path,
        help="scan every *.md file in this directory instead of the roadmap's phase documents",
    )
    parser.add_argument("--today", type=dt.date.fromisoformat, help="override today's date (YYYY-MM-DD)")
    args = parser.parse_args(argv)

    docs = sorted(args.docs_dir.glob("*.md")) if args.docs_dir else default_doc_paths()
    errors = validate(args.sources, docs, args.schema, args.today)
    if errors:
        print(f"{args.sources}: {len(errors)} problem(s) found", file=sys.stderr)
        for line in errors:
            print(f"  - {line}", file=sys.stderr)
        return 1
    print(f"{args.sources}: OK ({len(docs)} documents scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
