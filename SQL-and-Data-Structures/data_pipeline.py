"""Small, dependency-free ingestion and cleaning helpers."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


Record = dict[str, Any]


@dataclass(frozen=True)
class ValidationIssue:
    row_number: int | None
    field: str | None
    message: str


@dataclass(frozen=True)
class CleanResult:
    records: list[Record]
    duplicate_rows: list[int]


def read_records(path: str | Path) -> list[Record]:
    """Read a CSV file or a JSON array of objects into row dictionaries."""
    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        with file_path.open(newline="", encoding="utf-8-sig") as file:
            return [dict(row) for row in csv.DictReader(file)]

    if suffix == ".json":
        with file_path.open(encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError("JSON input must be an array of objects")
        return [dict(row) for row in data]

    raise ValueError(f"Unsupported input format: {suffix or 'missing extension'}")


def write_records(records: list[Record], path: str | Path) -> None:
    """Write row dictionaries as CSV or a formatted JSON array."""
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if suffix == ".json":
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=2, ensure_ascii=False)
            file.write("\n")
        return

    if suffix == ".csv":
        fieldnames = list(dict.fromkeys(key for record in records for key in record))
        with file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        return

    raise ValueError(f"Unsupported output format: {suffix or 'missing extension'}")


def validate_records(
    records: list[Record],
    required_columns: tuple[str, ...] = (),
    numeric_columns: tuple[str, ...] = (),
) -> list[ValidationIssue]:
    """Return schema and value issues without modifying the input records."""
    issues: list[ValidationIssue] = []
    available_columns = set().union(*(record.keys() for record in records))

    for column in required_columns:
        if column not in available_columns:
            issues.append(ValidationIssue(None, column, "required column is missing"))

    for row_number, record in enumerate(records, start=1):
        for column in required_columns:
            if column in record and _is_blank(record[column]):
                issues.append(ValidationIssue(row_number, column, "required value is blank"))

        for column in numeric_columns:
            if column not in record or _is_blank(record[column]):
                continue
            try:
                float(str(record[column]).strip())
            except (TypeError, ValueError):
                issues.append(ValidationIssue(row_number, column, "value must be numeric"))

    return issues


def clean_records(records: list[Record], key_fields: tuple[str, ...] = ()) -> CleanResult:
    """Trim text, convert blank values to None, and remove later duplicates."""
    cleaned: list[Record] = []
    duplicate_rows: list[int] = []
    seen_keys: set[tuple[Any, ...]] = set()

    for row_number, record in enumerate(records, start=1):
        normalized = {
            key: _normalize_value(value)
            for key, value in record.items()
        }
        fields = key_fields or tuple(normalized.keys())
        row_key = tuple(normalized.get(field) for field in fields)

        if row_key in seen_keys:
            duplicate_rows.append(row_number)
            continue

        seen_keys.add(row_key)
        cleaned.append(normalized)

    return CleanResult(cleaned, duplicate_rows)


def _is_blank(value: Any) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def _normalize_value(value: Any) -> Any:
    if _is_blank(value):
        return None
    return value.strip() if isinstance(value, str) else value