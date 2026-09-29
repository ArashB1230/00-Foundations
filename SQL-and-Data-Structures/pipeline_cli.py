"""Command-line entry point for the ingestion and cleaning workflow."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from data_pipeline import clean_records, read_records, validate_records, write_records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and clean tabular records.")
    parser.add_argument("input", type=Path, help="Input CSV or JSON file")
    parser.add_argument("--required-columns", nargs="*", default=[])
    parser.add_argument("--numeric-columns", nargs="*", default=[])
    parser.add_argument("--key-fields", nargs="*", default=[])
    parser.add_argument("--clean-output", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    records = read_records(args.input)
    issues = validate_records(
        records,
        required_columns=tuple(args.required_columns),
        numeric_columns=tuple(args.numeric_columns),
    )
    cleaned = clean_records(records, key_fields=tuple(args.key_fields))

    if args.clean_output:
        write_records(cleaned.records, args.clean_output)

    print(
        json.dumps(
            {
                "input_rows": len(records),
                "output_rows": len(cleaned.records),
                "duplicate_rows": cleaned.duplicate_rows,
                "validation_issues": [asdict(issue) for issue in issues],
                "output_file": str(args.clean_output) if args.clean_output else None,
            },
            indent=2,
        )
    )
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())