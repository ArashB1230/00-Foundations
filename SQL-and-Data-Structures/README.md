# SQL and Data Structures

Status: Complete

Build a dependency-free data pipeline in small steps: parse CSV/JSON files, validate schemas and values, clean records, remove duplicates, store the result in SQLite, and produce analytical reports.

## Current scope

- `data_pipeline.py`: CSV/JSON ingestion, validation, normalization, duplicate detection, and output writing
- `pipeline_cli.py`: command-line workflow for validating and cleaning a file
- `sqlite_store.py`: SQLite persistence and customer reporting
- `scripts/download_northwind.py`: reproducible download and integrity validation for the optional Northwind database
- `data/README.md`: dataset source and usage notes; the binary database stays out of Git
- `test_*.py`: focused tests for ingestion, cleaning, storage, and reporting

Run the tests with:

```text
python -m unittest discover -s . -p "test_*.py"
```

Run the pipeline from this folder:

```text
python pipeline_cli.py orders.csv --required-columns order_id customer --numeric-columns amount --key-fields order_id --clean-output cleaned/orders.csv
```

The command prints a JSON summary and returns exit code `1` when validation issues are found. It keeps the first record for each key and reports the original row numbers of duplicates. The cleaned records can then be loaded with `sqlite_store.load_orders` for reporting.

Download the optional relational practice dataset with:

```text
python scripts/download_northwind.py
```