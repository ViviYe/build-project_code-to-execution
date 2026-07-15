import unittest
from src.custom_language import CustomLanguage

class TestComparisons(unittest.TestCase):
    def test_greater(self):
        self.assertEqual(CustomLanguage().run("3 > 2"), True)

    def test_less(self):
        self.assertEqual(CustomLanguage().run("3 < 2"), False)

    def test_equal_equal(self):
        self.assertEqual(CustomLanguage().run("5 == 5"), True)

    def test_bang_equal(self):
        self.assertEqual(CustomLanguage().run("5 != 5"), False)

    def test_greater_equal(self):
        self.assertEqual(CustomLanguage().run("5 >= 5"), True)

    def test_less_equal(self):
        self.assertEqual(CustomLanguage().run("4 <= 5"), True)

if __name__ == "__main__":
    unittest.main()
