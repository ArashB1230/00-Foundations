# Northwind Data

The project uses the public Northwind SQLite sample database for optional integration practice. The database is deliberately not committed because it is a generated binary dependency.

## Source

- Repository: <https://github.com/jpwhite3/northwind-SQLite3>
- Database: <https://raw.githubusercontent.com/jpwhite3/northwind-SQLite3/main/dist/northwind.db>
- Source license: MIT, as stated by the source repository

## Download

From `SQL-and-Data-Structures`, run:

```text
python scripts/download_northwind.py
```

This creates `data/northwind.db`, validates its SQLite integrity, and keeps the file ignored by Git. Use `--output` to choose another local path.

The database contains customers, orders, order details, products, categories, suppliers, and employees. It is suitable for practicing joins, constraints, aggregates, rankings, and reporting.