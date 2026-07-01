import unittest

from src.lexer import tokenize
from src.tokens import TokenType


class TestLexer(unittest.TestCase):

    def test_single_digit_addition(self):
        tokens = tokenize("1+2")
        self.assertEqual(
            [t.type for t in tokens],
            [TokenType.NUMBER, TokenType.PLUS, TokenType.NUMBER, TokenType.EOF],
        )
        self.assertEqual(tokens[0].value, 1)
        self.assertEqual(tokens[2].value, 2)

    def test_multi_digit_numbers(self):
        tokens = tokenize("12 + 345")
        self.assertEqual(tokens[0].value, 12)
        self.assertEqual(tokens[2].value, 345)

    def test_multiplication(self):
        tokens = tokenize("2*3")
        self.assertEqual(
            [t.type for t in tokens],
            [TokenType.NUMBER, TokenType.STAR, TokenType.NUMBER, TokenType.EOF],
        )


if __name__ == "__main__":
    unittest.main()
