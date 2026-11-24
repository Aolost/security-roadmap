"""`roadmap` command-line interface: list, next, done ID, status."""

from __future__ import annotations

import argparse
import sys

from . import __version__, progress
from .phases import PHASE_IDS, PHASES, get_phase

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_PROGRESS_ERROR = 3


def _load_or_report(path) -> dict[str, str] | None:
    try:
        return progress.load(path)
    except progress.ProgressError as exc:
        print(f"error: {exc}", file=sys.stderr)
        print(
            "The file was left unchanged. Fix it, or move it aside to start fresh, then run the command again.",
            file=sys.stderr,
        )
        return None


def _mark(done: bool) -> str:
    return "[x]" if done else "[ ]"


def cmd_list(completed: dict[str, str]) -> int:
    width = max(len(p.id) for p in PHASES)
    for phase in PHASES:
        weeks = f"{phase.weeks} week" + ("" if phase.weeks == 1 else "s")
        print(f"{_mark(phase.id in completed)} {phase.number}  {phase.id:<{width}}  {phase.title} ({weeks})")
    return EXIT_OK


def cmd_next(completed: dict[str, str]) -> int:
    for phase in PHASES:
        if phase.id not in completed:
            print(f"Next: phase {phase.number}, {phase.id}: {phase.title}")
            print(f"Read: {phase.doc}")
            print(f"When finished: roadmap done {phase.id}")
            return EXIT_OK
    print("All phases are complete.")
    return EXIT_OK


def cmd_done(completed: dict[str, str], phase_id: str, path) -> int:
    phase = get_phase(phase_id)
    if phase is None:
        print(f"error: unknown phase ID '{phase_id}'. Valid IDs: {', '.join(PHASE_IDS)}", file=sys.stderr)
        return EXIT_USAGE
    if phase_id in completed:
        print(f"{phase_id} was already marked complete on {completed[phase_id]}.")
        return EXIT_OK
    completed[phase_id] = progress.today()
    progress.save(path, completed)
    print(f"Marked {phase_id} complete.")
    return EXIT_OK


def cmd_status(completed: dict[str, str], path) -> int:
    done = [p for p in PHASES if p.id in completed]
    total_weeks = sum(p.weeks for p in PHASES)
    done_weeks = sum(p.weeks for p in done)
    percent = round(100 * len(done) / len(PHASES))
    print(f"Overall: {len(done)}/{len(PHASES)} phases complete ({percent}%), {done_weeks}/{total_weeks} planned weeks")
    for phase in PHASES:
        when = f"completed {completed[phase.id]}" if phase.id in completed else "incomplete"
        print(f"  {_mark(phase.id in completed)} {phase.id}: {when}")
    print(f"Progress file: {path}")
    return EXIT_OK


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="roadmap",
        description="Track your progress through the security-roadmap phases. Progress is stored locally only.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")
    sub.add_parser("list", help="list the phases and whether each is complete")
    sub.add_parser("next", help="show the next incomplete phase")
    done = sub.add_parser("done", help="mark a phase complete by its ID")
    done.add_argument("phase_id", metavar="ID", help=f"one of: {', '.join(PHASE_IDS)}")
    sub.add_parser("status", help="show overall and per-phase progress")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path = progress.progress_path()
    completed = _load_or_report(path)
    if completed is None:
        return EXIT_PROGRESS_ERROR
    if args.command == "list":
        return cmd_list(completed)
    if args.command == "next":
        return cmd_next(completed)
    if args.command == "done":
        return cmd_done(completed, args.phase_id, path)
    return cmd_status(completed, path)
