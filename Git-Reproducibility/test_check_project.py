import tempfile
import unittest
from pathlib import Path

from check_project import check_project


class ReproducibilityTests(unittest.TestCase):
    def test_ready_project_has_documentation_ignore_rules_and_tests(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").touch()
            (root / ".gitignore").touch()
            (root / "test_example.py").touch()

            result = check_project(root)

        self.assertTrue(result["ready"])

    def test_incomplete_project_is_not_ready(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = check_project(directory)

        self.assertFalse(result["ready"])


if __name__ == "__main__":
    unittest.main()