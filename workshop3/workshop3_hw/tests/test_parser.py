import unittest

from src.lexer import tokenize
from src.parser import Parser
from src.ast_nodes import Number, BinaryOp


class TestParser(unittest.TestCase):

    def parse(self, source):
        return Parser(tokenize(source)).parse()

    def test_number(self):
        self.assertEqual(self.parse("42"), Number(42))

    def test_addition(self):
        ast = self.parse("1 + 2")

        self.assertIsInstance(ast, BinaryOp)
        self.assertEqual(ast.op, "+")
        self.assertEqual(ast.left, Number(1))
        self.assertEqual(ast.right, Number(2))

    def test_multiplication(self):
        ast = self.parse("2 * 3")

        self.assertIsInstance(ast, BinaryOp)
        self.assertEqual(ast.op, "*")
        self.assertEqual(ast.left, Number(2))
        self.assertEqual(ast.right, Number(3))

    def test_precedence(self):
        ast = self.parse("1 + 2 * 3")

        self.assertIsInstance(ast, BinaryOp)
        self.assertEqual(ast.op, "+")
        self.assertEqual(ast.left, Number(1))

        self.assertIsInstance(ast.right, BinaryOp)
        self.assertEqual(ast.right.op, "*")
        self.assertEqual(ast.right.left, Number(2))
        self.assertEqual(ast.right.right, Number(3))


if __name__ == "__main__":
    unittest.main()
