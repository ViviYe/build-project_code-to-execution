import unittest

from src.ast_nodes import Number, BinaryOp
from src.ast_printer import pretty_ast


class TestAstPrinter(unittest.TestCase):

    def test_number(self):
        output = pretty_ast(Number(1))
        self.assertIn("Number", output)
        self.assertIn("1", output)

    def test_binary_op(self):
        ast = BinaryOp("+", Number(1), Number(2))
        output = pretty_ast(ast)

        self.assertIn("BinaryOp", output)
        self.assertIn("+", output)
        self.assertIn("Number(1)", output)
        self.assertIn("Number(2)", output)


if __name__ == "__main__":
    unittest.main()
