# Foundations

This folder builds the habits needed for reliable data and machine-learning work. Every project is dependency-light, runnable with Python's standard library, and backed by focused tests.

## Projects

| Project | What it teaches | How to verify |
| --- | --- | --- |
| `python-and-git` | CLI design, JSON output, and project inspection | `python -m unittest discover -s . -p "test_*.py"` |
| `Python-Data-Structures` | Stack, queue, generics, and binary search | `python -m unittest discover -s . -p "test_*.py"` |
| `SQL-Analytics` | SQLite schema design, aggregates, and window functions | `python -m unittest discover -s . -p "test_*.py"` |
| `Git-Reproducibility` | Documentation, ignore rules, and readiness checks | `python -m unittest discover -s . -p "test_*.py"` |
| `SQL-and-Data-Structures` | Ingestion, validation, cleaning, SQLite storage, and reports | `python -m unittest discover -s . -p "test_*.py"` |

## Recommended order

1. Learn the command-line and reproducibility checks.
2. Implement and test the core data structures.
3. Practice relational analytics in SQLite.
4. Run the integrated data pipeline from ingestion to reporting.

Each project is intentionally small. Read its README, run its tests, inspect the implementation, and extend it with one new test before moving on.