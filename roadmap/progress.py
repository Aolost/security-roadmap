"""Local progress storage for the roadmap CLI.

Progress lives only on the learner's machine, under the platform's configuration
directory. It is never written into the repository and never uploaded.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import tempfile
from pathlib import Path

APP_DIR = "security-roadmap"
FILE_NAME = "progress.json"
ENV_OVERRIDE = "SECURITY_ROADMAP_PROGRESS"
FORMAT_VERSION = 1


class ProgressError(Exception):
    """The progress file exists but cannot be used. It is left untouched."""


def config_dir() -> Path:
    if sys.platform == "win32":
        base = os.environ.get("APPDATA")
        return Path(base) if base else Path.home() / "AppData" / "Roaming"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support"
    base = os.environ.get("XDG_CONFIG_HOME")
    return Path(base) if base else Path.home() / ".config"


def progress_path() -> Path:
    """Where progress is stored. SECURITY_ROADMAP_PROGRESS overrides the location."""
    override = os.environ.get(ENV_OVERRIDE)
    if override:
        return Path(override).expanduser()
    return config_dir() / APP_DIR / FILE_NAME


def load(path: Path) -> dict[str, str]:
    """Return {phase_id: completion date}. A missing file is a fresh start."""
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    except OSError as exc:
        raise ProgressError(f"cannot read {path}: {exc.strerror or exc}") from exc
    except UnicodeDecodeError as exc:
        raise ProgressError(f"{path} is not valid UTF-8 text") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ProgressError(f"{path} is not valid JSON (line {exc.lineno}, column {exc.colno}: {exc.msg})") from exc

    if not isinstance(data, dict) or not isinstance(data.get("completed"), dict):
        raise ProgressError(f"{path} does not contain a 'completed' object")
    completed = data["completed"]
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in completed.items()):
        raise ProgressError(f"{path} has a 'completed' entry that is not a text phase ID and date")
    return dict(completed)


def save(path: Path, completed: dict[str, str]) -> None:
    """Write atomically so an interrupted write cannot leave a half-written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"version": FORMAT_VERSION, "completed": dict(sorted(completed.items()))}
    fd, tmp_name = tempfile.mkstemp(prefix=".progress-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def today() -> str:
    return dt.date.today().isoformat()
