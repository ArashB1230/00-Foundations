import sqlite3
import unittest

from sqlite_store import create_orders_table, customer_report, load_orders


class SQLiteStoreTests(unittest.TestCase):
    def test_loads_orders_and_reports_customer_totals(self) -> None:
        connection = sqlite3.connect(":memory:")
        create_orders_table(connection)
        inserted = load_orders(
            connection,
            [
                {"order_id": "1", "customer": "Ana", "amount": "12.50"},
                {"order_id": "2", "customer": "Ana", "amount": "7.50"},
            ],
        )

        self.assertEqual(inserted, 2)
        self.assertEqual(
            customer_report(connection),
            [{"customer": "Ana", "order_count": 2, "total_amount": 20.0}],
        )
        connection.close()


if __name__ == "__main__":
    unittest.main()