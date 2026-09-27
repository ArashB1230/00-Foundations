"""Inspect a project folder for basic reproducibility requirements."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_REQUIRED = ("README.md",)
DEFAULT_IGNORED = {".git", "__pycache__", ".venv", "venv"}


def inspect_project(
    path: str | Path,
    required_files: tuple[str, ...] = DEFAULT_REQUIRED,
) -> dict[str, object]:
    """Return a JSON-serializable summary of a project's basic structure."""
    root = Path(path).resolve()
    missing = [name for name in required_files if not (root / name).is_file()]
    tracked_candidates = [
        item.relative_to(root).as_posix()
        for item in root.rglob("*")
        if item.is_file() and not any(part in DEFAULT_IGNORED for part in item.parts)
    ]
    return {
        "path": str(root),
        "exists": root.is_dir(),
        "required_files": list(required_files),
        "missing_files": missing,
        "file_count": len(tracked_candidates),
        "files": sorted(tracked_candidates),
        "ready": root.is_dir() and not missing,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a project's basic structure.")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--required", nargs="*", default=list(DEFAULT_REQUIRED))
    args = parser.parse_args()
    result = inspect_project(args.path, tuple(args.required))
    print(json.dumps(result, indent=2))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())