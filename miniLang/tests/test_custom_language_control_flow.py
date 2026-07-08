import unittest
from src.custom_language import CustomLanguage

class TestCustomLanguageControlFlow(unittest.TestCase):
    def test_if_and_while_together(self):
        lang = CustomLanguage()
        lang.run("x = 0")
        lang.run("while x < 5: x = x + 1")
        lang.run("if x == 5: y = 100")
        self.assertEqual(lang.run("y"), 100)

    def test_arithmetic_still_works(self):
        self.assertEqual(CustomLanguage().run("1 + 2 * 3"), 7)

    def test_variables_still_work(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        self.assertEqual(lang.run("x + 2"), 7)

if __name__ == "__main__":
    unittest.main()
