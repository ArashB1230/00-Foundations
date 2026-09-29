# SQL and Data Structures

This project combines the foundational ideas of structured data handling with practical SQL storage. It teaches how data moves from raw input to cleaned records and then into a database for analysis.

## Goal

The goal is to build a small data pipeline that performs common preprocessing tasks and stores the output in SQLite. This is one of the most realistic foundation projects because it mirrors how real data projects begin.

## What you will practice

- reading data from source files,
- validating and cleaning records,
- handling missing or inconsistent values,
- converting raw data into a usable structure,
- storing cleaned data in SQLite,
- generating simple reports from the database.

## Typical workflow

1. Load the source data.
2. Inspect columns and content.
3. Validate fields and clean inconsistencies.
4. Store the cleaned result in a SQLite database.
5. Run simple queries or summary reports.

## Why this matters

Before building ML models, data must be cleaned, structured, and trusted. This project teaches the discipline of turning messy raw input into a reliable data source.

## Tools and concepts covered

- Python data processing,
- SQLite database structure,
- validation and cleanup logic,
- data pipeline design,
- reporting from stored data.

## Validation

Run the tests for this project:

```bash
python -m unittest discover -s . -p "test_*.py"
```

## Learning takeaway

A good model depends on a reliable pipeline. This project demonstrates that solid analytics begins before the model ever runs.
