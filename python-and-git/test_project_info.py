import tempfile
import unittest
from pathlib import Path

from project_info import inspect_project


class ProjectInfoTests(unittest.TestCase):
    def test_reports_missing_required_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = inspect_project(directory, ("README.md", "pyproject.toml"))

        self.assertFalse(result["ready"])
        self.assertEqual(result["missing_files"], ["README.md", "pyproject.toml"])

    def test_ignores_generated_directories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Example\n", encoding="utf-8")
            (root / "__pycache__").mkdir()
            (root / "__pycache__" / "ignored.pyc").write_bytes(b"compiled")
            result = inspect_project(root)

        self.assertTrue(result["ready"])
        self.assertEqual(result["files"], ["README.md"])


if __name__ == "__main__":
    unittest.main()