import unittest
from src.custom_language import CustomLanguage

class TestWhileStatement(unittest.TestCase):
    def test_while_loop_updates_environment(self):
        lang = CustomLanguage()
        lang.run("x = 0")
        lang.run("while x < 3: x = x + 1")
        self.assertEqual(lang.run("x"), 3)

    def test_while_loop_returns_last_body_result(self):
        lang = CustomLanguage()
        lang.run("x = 0")
        result = lang.run("while x < 3: x = x + 1")
        self.assertEqual(result, 3)

    def test_while_condition_false_immediately(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        result = lang.run("while x < 3: x = x + 1")
        self.assertIsNone(result)
        self.assertEqual(lang.run("x"), 5)

if __name__ == "__main__":
    unittest.main()
