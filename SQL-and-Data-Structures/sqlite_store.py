"""Persist cleaned order records and produce a compact analytical report."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from typing import Any

from data_pipeline import Record


def create_orders_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer TEXT NOT NULL,
            amount REAL NOT NULL CHECK (amount >= 0)
        )
        """
    )
    connection.commit()


def load_orders(connection: sqlite3.Connection, records: Iterable[Record]) -> int:
    """Insert valid order records and return the number of inserted rows."""
    rows = [
        (str(record["order_id"]), str(record["customer"]), float(record["amount"]))
        for record in records
    ]
    connection.executemany(
        "INSERT INTO orders(order_id, customer, amount) VALUES (?, ?, ?)",
        rows,
    )
    connection.commit()
    return len(rows)


def customer_report(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    """Return customer totals ordered by revenue, then customer name."""
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT customer, COUNT(*) AS order_count, ROUND(SUM(amount), 2) AS total_amount
        FROM orders
        GROUP BY customer
        ORDER BY total_amount DESC, customer ASC
        """
    ).fetchall()
    return [dict(row) for row in rows]