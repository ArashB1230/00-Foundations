"""Check the files a small project needs before it is shared."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def check_project(path: str | Path) -> dict[str, object]:
    root = Path(path)
    required = {"README.md", ".gitignore"}
    present = {item.name for item in root.iterdir()} if root.is_dir() else set()
    return {
        "path": str(root.resolve()),
        "exists": root.is_dir(),
        "required_files": sorted(required),
        "missing_files": sorted(required - present),
        "has_tests": any(root.glob("test_*.py")),
        "ready": root.is_dir() and required <= present and any(root.glob("test_*.py")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check project reproducibility basics.")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    result = check_project(args.path)
    print(json.dumps(result, indent=2))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())