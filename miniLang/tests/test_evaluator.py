import unittest
from src.ast_nodes import Number, Variable, Assignment, BinaryOp
from src.environment import Environment
from src.evaluator import evaluate


class TestEvaluator(unittest.TestCase):
    def test_number(self):
        env = Environment()
        self.assertEqual(evaluate(Number(5), env), 5)

    def test_addition(self):
        env = Environment()
        self.assertEqual(evaluate(BinaryOp("+", Number(1), Number(2)), env), 3)

    def test_subtraction(self):
        env = Environment()
        self.assertEqual(evaluate(BinaryOp("-", Number(10), Number(3)), env), 7)

    def test_multiplication(self):
        env = Environment()
        self.assertEqual(evaluate(BinaryOp("*", Number(4), Number(5)), env), 20)

    def test_division(self):
        env = Environment()
        self.assertEqual(evaluate(BinaryOp("/", Number(20), Number(4)), env), 5)

    def test_variable_lookup(self):
        env = Environment()
        env.define("x", 5)
        self.assertEqual(evaluate(Variable("x"), env), 5)

    def test_assignment(self):
        env = Environment()
        result = evaluate(Assignment("x", Number(5)), env)
        self.assertEqual(result, 5)
        self.assertEqual(env.get("x"), 5)


if __name__ == "__main__":
    unittest.main()
