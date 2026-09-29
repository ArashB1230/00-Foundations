"""SQLite schema and analytical queries for order data."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from typing import Any


Order = tuple[str, str, float]


def create_database(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer TEXT NOT NULL,
            amount REAL NOT NULL CHECK (amount >= 0)
        );
        """
    )


def insert_orders(connection: sqlite3.Connection, orders: Iterable[Order]) -> None:
    connection.executemany(
        "INSERT INTO orders(order_id, customer, amount) VALUES (?, ?, ?)",
        orders,
    )
    connection.commit()


def customer_totals(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT customer, COUNT(*) AS order_count, ROUND(SUM(amount), 2) AS total_amount
        FROM orders
        GROUP BY customer
        ORDER BY total_amount DESC, customer ASC
        """
    ).fetchall()
    return [dict(row) for row in rows]


def ranked_orders(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT order_id, customer, amount,
               RANK() OVER (PARTITION BY customer ORDER BY amount DESC) AS customer_rank
        FROM orders
        ORDER BY customer, customer_rank, order_id
        """
    ).fetchall()
    return [dict(row) for row in rows]