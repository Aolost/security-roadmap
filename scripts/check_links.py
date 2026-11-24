#!/usr/bin/env python3
"""Check every resource URL in data/sources.yaml over the network and write a Markdown report.

NETWORK-DEPENDENT. This is used by the weekly scheduled workflow and by `make links`.
It is never run by the unit tests, the validator, or the generator.

It is read-only: it reports problems but never edits data/sources.yaml. A maintainer must
recheck a flagged resource by opening it, then update its observed fields and verified_on.

Categories:
  dead       the URL could not be fetched, or the final response was 404, 410, or 5xx
  moved      the observed final destination differs from the recorded final_url
  redirected the requested URL redirects (including redirects already recorded)
  blocked    401, 403, or 429: probably bot protection; needs a manual check in a browser

Exit status: 0 always, unless --fail-on-problems is given (dead or moved entries found).
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCES = REPO_ROOT / "data" / "sources.yaml"
USER_AGENT = "Mozilla/5.0 (compatible; security-roadmap-link-check/0.1)"
MAX_REDIRECTS = 10
TIMEOUT = 30


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401
        return None


_OPENER = urllib.request.build_opener(_NoRedirect)


def fetch_chain(url: str) -> tuple[list[int], str, str | None]:
    """Follow redirects manually. Returns (status chain, final URL, error message)."""
    chain: list[int] = []
    current = url
    for _ in range(MAX_REDIRECTS + 1):
        request = urllib.request.Request(current, headers={"User-Agent": USER_AGENT})
        try:
            with _OPENER.open(request, timeout=TIMEOUT) as response:
                chain.append(response.status)
                return chain, current, None
        except urllib.error.HTTPError as exc:
            chain.append(exc.code)
            location = exc.headers.get("Location") if 300 <= exc.code < 400 else None
            if location:
                current = urljoin(current, location)
                continue
            return chain, current, None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return chain, current, str(getattr(exc, "reason", exc))
    return chain, current, "too many redirects"


def classify(src: dict, chain: list[int], final_url: str, error: str | None) -> list[str]:
    labels = []
    final = chain[-1] if chain else None
    if error or final is None or final in (404, 410) or final >= 500:
        labels.append("dead")
    elif final in (401, 403, 429):
        labels.append("blocked")
    if chain and 300 <= chain[0] < 400:
        labels.append("redirected")
    recorded = src.get("final_url")
    if not error and final is not None and 200 <= final < 300 and recorded not in (None, "unknown"):
        if final_url.rstrip("/") != str(recorded).rstrip("/"):
            labels.append("moved")
    return labels


def build_report(results: list[dict], today: str) -> str:
    def section(title: str, label: str, explain: str) -> list[str]:
        rows = [r for r in results if label in r["labels"]]
        lines = [f"## {title} ({len(rows)})", "", explain, ""]
        if not rows:
            return lines + ["None.", ""]
        for r in rows:
            chain = " → ".join(map(str, r["chain"])) or "no response"
            detail = f"; error: {r['error']}" if r["error"] else ""
            lines.append(f"- `{r['id']}`: <{r['url']}> → <{r['final_url']}> (statuses {chain}{detail})")
        return lines + [""]

    lines = [
        "# Weekly link check report",
        "",
        f"Checked {len(results)} resources from `data/sources.yaml` on {today}.",
        "This report is automated. A maintainer must recheck flagged entries by opening them before",
        "changing any observed field or `verified_on`.",
        "",
    ]
    lines += section("Dead links", "dead", "Could not be fetched, or answered 404, 410, or 5xx.")
    lines += section("Moved destinations", "moved", "The final destination differs from the recorded `final_url`.")
    lines += section("Redirected links", "redirected", "The requested URL redirects (some are already recorded).")
    lines += section("Blocked automated checks", "blocked", "Answered 401, 403, or 429; check manually in a browser.")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Network link check for data/sources.yaml.")
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--output", type=Path, help="write the Markdown report here (default: stdout)")
    parser.add_argument("--fail-on-problems", action="store_true")
    args = parser.parse_args(argv)

    data = yaml.safe_load(args.sources.read_text(encoding="utf-8"))
    results = []
    for src in sorted(data["sources"], key=lambda s: s["id"]):
        chain, final_url, error = fetch_chain(src["url"])
        results.append(
            {"id": src["id"], "url": src["url"], "chain": chain, "final_url": final_url, "error": error,
             "labels": classify(src, chain, final_url, error)}
        )
    report = build_report(results, dt.date.today().isoformat())
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)

    problems = sum(1 for r in results if {"dead", "moved"} & set(r["labels"]))
    print(f"{problems} dead or moved link(s) found.", file=sys.stderr)
    return 1 if (args.fail_on_problems and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
