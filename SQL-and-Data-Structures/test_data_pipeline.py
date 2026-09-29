import json
import tempfile
import unittest
from pathlib import Path

from data_pipeline import clean_records, read_records, validate_records, write_records


class DataPipelineTests(unittest.TestCase):
    def test_reads_csv_and_reports_invalid_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "orders.csv"
            path.write_text(
                "order_id,customer,amount\n1, Ana ,12.50\n2,,not-a-number\n",
                encoding="utf-8",
            )

            records = read_records(path)
            issues = validate_records(
                records,
                required_columns=("order_id", "customer"),
                numeric_columns=("amount",),
            )

        self.assertEqual(records[0]["customer"], " Ana ")
        self.assertEqual(
            [(issue.row_number, issue.field, issue.message) for issue in issues],
            [
                (2, "customer", "required value is blank"),
                (2, "amount", "value must be numeric"),
            ],
        )

    def test_reads_json_and_cleans_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "orders.json"
            path.write_text(
                json.dumps(
                    [
                        {"order_id": "1", "customer": " Ana "},
                        {"order_id": "1", "customer": "Ana"},
                        {"order_id": "2", "customer": "Bo"},
                    ]
                ),
                encoding="utf-8",
            )

            result = clean_records(read_records(path), key_fields=("order_id",))

        self.assertEqual(result.duplicate_rows, [2])
        self.assertEqual(
            result.records,
            [
                {"order_id": "1", "customer": "Ana"},
                {"order_id": "2", "customer": "Bo"},
            ],
        )

    def test_writes_cleaned_records_as_csv(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cleaned.csv"
            write_records(
                [{"order_id": "1", "customer": "Ana", "amount": None}],
                path,
            )

            self.assertEqual(
                path.read_text(encoding="utf-8"),
                "order_id,customer,amount\n1,Ana,\n",
            )


if __name__ == "__main__":
    unittest.main()