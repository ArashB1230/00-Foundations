"""Download and validate the public Northwind SQLite sample database."""

from __future__ import annotations

import argparse
import sqlite3
import tempfile
from pathlib import Path
from urllib.request import urlopen


SOURCE_URL = "https://raw.githubusercontent.com/jpwhite3/northwind-SQLite3/main/dist/northwind.db"


def validate_database(path: str | Path) -> bool:
    """Return whether a SQLite file passes SQLite's integrity check."""
    connection: sqlite3.Connection | None = None
    try:
        connection = sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)
        result = connection.execute("PRAGMA integrity_check").fetchone()
    except sqlite3.Error:
        return False
    finally:
        if connection is not None:
            connection.close()
    return result == ("ok",)


def download_database(destination: str | Path, url: str = SOURCE_URL) -> Path:
    """Download to a temporary file, validate it, then move it into place."""
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".db", delete=False) as temporary:
        temporary_path = Path(temporary.name)
        try:
            with urlopen(url, timeout=30) as response:
                while chunk := response.read(1024 * 1024):
                    temporary.write(chunk)
            temporary.close()
            if not validate_database(temporary_path):
                raise ValueError("downloaded file is not a valid SQLite database")
            temporary_path.replace(target)
        finally:
            temporary_path.unlink(missing_ok=True)

    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Download the Northwind SQLite database.")
    parser.add_argument("--output", type=Path, default=Path("data/northwind.db"))
    args = parser.parse_args()
    output = download_database(args.output)
    print(f"Downloaded Northwind database to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())