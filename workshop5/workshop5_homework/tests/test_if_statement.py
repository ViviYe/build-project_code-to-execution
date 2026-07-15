import unittest
from src.custom_language import CustomLanguage

class TestIfStatement(unittest.TestCase):
    def test_if_true_executes_body(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        result = lang.run("if x > 3: y = 10")
        self.assertEqual(result, 10)
        self.assertEqual(lang.run("y"), 10)

    def test_if_false_skips_body(self):
        lang = CustomLanguage()
        lang.run("x = 1")
        result = lang.run("if x > 3: y = 10")
        self.assertIsNone(result)
        with self.assertRaises(NameError):
            lang.run("y")

    def test_if_body_can_use_expression(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        lang.run("if x == 5: y = x + 2")
        self.assertEqual(lang.run("y"), 7)

if __name__ == "__main__":
    unittest.main()
