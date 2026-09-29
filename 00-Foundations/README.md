# Foundations

This stage builds the habits required for reliable data and machine-learning work. The projects are intentionally small, dependency-light, and designed to be understood and tested quickly with Python's standard library.

The goal is to establish a solid base before moving into statistics, ML, deep learning, and research. These exercises focus on habits that matter in real projects:
- writing clean and maintainable code,
- testing behavior rather than assumptions,
- using Git and project structure properly,
- understanding data structures and algorithms,
- validating data before analysis,
- documenting and reproducing project workflows.

## Why this stage matters

Strong ML work depends on fundamentals that are easy to overlook:
- code should be readable and debug-friendly,
- project health should be checkable with simple tools,
- data should be handled with structure and validation,
- analysis should be reproducible and reviewable,
- engineering discipline matters as much as model quality.

## Projects in this stage

| Project | What it teaches | How to verify |
| --- | --- | --- |
| `python-and-git` | CLI design, JSON output, project inspection, and practical Git-oriented workflow habits | `python -m unittest discover -s . -p "test_*.py"` |
| `Python-Data-Structures` | Stack, queue, generics, and binary search patterns used in algorithms and software design | `python -m unittest discover -s . -p "test_*.py"` |
| `SQL-Analytics` | SQLite schema design, aggregation, grouping, and analytical querying | `python -m unittest discover -s . -p "test_*.py"` |
| `Git-Reproducibility` | Project readiness checks, documentation, ignore rules, and reproducibility hygiene | `python -m unittest discover -s . -p "test_*.py"` |
| `SQL-and-Data-Structures` | Ingestion, validation, cleaning, SQLite persistence, and reporting pipelines | `python -m unittest discover -s . -p "test_*.py"` |

## Recommended order

1. Learn the command-line basics and reproducibility checks.
2. Implement and test the core data structures.
3. Practice relational analytics in SQLite.
4. Work through the end-to-end data pipeline from ingestion to reporting.
5. Extend one project with an extra test or feature before moving on.

## Learning approach

Each project is intentionally small. The expected workflow is:
- read the project README,
- run the test suite,
- inspect the implementation,
- try to improve or extend it with one new case,
- move on only after the concepts feel concrete.

This stage is meant to build confidence and consistency. Once these fundamentals are solid, the later stages become much easier to understand and execute well.
