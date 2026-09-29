import sqlite3
import unittest

from analytics import create_database, customer_totals, insert_orders, ranked_orders


class AnalyticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        create_database(self.connection)
        insert_orders(
            self.connection,
            [("1", "Ana", 12.5), ("2", "Ana", 7.5), ("3", "Bo", 20.0)],
        )

    def tearDown(self) -> None:
        self.connection.close()

    def test_customer_totals(self) -> None:
        totals = {row["customer"]: row for row in customer_totals(self.connection)}
        self.assertEqual(totals["Ana"]["total_amount"], 20.0)
        self.assertEqual(totals["Ana"]["order_count"], 2)
        self.assertEqual(totals["Bo"]["total_amount"], 20.0)

    def test_ranked_orders_uses_window_function(self) -> None:
        ranks = ranked_orders(self.connection)
        self.assertEqual([row["customer_rank"] for row in ranks[:2]], [1, 2])


if __name__ == "__main__":
    unittest.main()