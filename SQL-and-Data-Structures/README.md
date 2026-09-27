# SQL and Data Structures

Status: In progress

Build a dependency-free data pipeline in small steps: parse CSV/JSON files, validate schemas and values, clean records, remove duplicates, store the result in SQLite, and produce analytical reports.

## Current scope

- `data_pipeline.py`: CSV/JSON ingestion, validation, normalization, duplicate detection, and output writing
- `pipeline_cli.py`: command-line workflow for validating and cleaning a file
- `test_data_pipeline.py`: focused tests for the ingestion and cleaning steps

Run the tests with:

```text
python -m unittest discover -s . -p "test_*.py"
```

Run the pipeline from this folder:

```text
python pipeline_cli.py orders.csv --required-columns order_id customer --numeric-columns amount --key-fields order_id --clean-output cleaned/orders.csv
```

The command prints a JSON summary and returns exit code `1` when validation issues are found. It keeps the first record for each key and reports the original row numbers of duplicates.