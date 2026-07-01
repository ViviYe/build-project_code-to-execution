import unittest
from src.custom_language import CustomLanguage


class TestCustomLanguage(unittest.TestCase):
    def test_run_arithmetic(self):
        lang = CustomLanguage()
        self.assertEqual(lang.run("1 + 2"), 3)

    def test_run_precedence(self):
        lang = CustomLanguage()
        self.assertEqual(lang.run("1 + 2 * 3"), 7)

    def test_run_parentheses(self):
        lang = CustomLanguage()
        self.assertEqual(lang.run("(1 + 2) * 3"), 9)

    def test_variable_assignment_and_lookup(self):
        lang = CustomLanguage()
        self.assertEqual(lang.run("x = 5"), 5)
        self.assertEqual(lang.run("x"), 5)
        self.assertEqual(lang.run("x + 2"), 7)

    def test_environment_persists_between_runs(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        lang.run("y = x * 3")
        self.assertEqual(lang.run("y + 1"), 16)


if __name__ == "__main__":
    unittest.main()
