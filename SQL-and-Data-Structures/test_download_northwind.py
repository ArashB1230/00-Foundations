import sqlite3
import tempfile
import unittest
from pathlib import Path

from scripts.download_northwind import validate_database


class NorthwindDownloadTests(unittest.TestCase):
    def test_accepts_a_valid_sqlite_database(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.db"
            connection = sqlite3.connect(path)
            connection.execute("CREATE TABLE products (id INTEGER PRIMARY KEY)")
            connection.commit()
            connection.close()

            self.assertTrue(validate_database(path))

    def test_rejects_non_sqlite_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "not-a-database.db"
            path.write_text("not sqlite", encoding="utf-8")

            self.assertFalse(validate_database(path))


if __name__ == "__main__":
    unittest.main()