from src.ast_nodes import Number, Variable, Assignment, BinaryOp
from src.environment import Environment


def evaluate(node, env: Environment):
    if isinstance(node, Number):
        return node.value

    if isinstance(node, BinaryOp):
        left = evaluate(node.left, env)
        right = evaluate(node.right, env)

        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            return left / right

        raise ValueError(f"Unknown operator: {node.op}")

    if isinstance(node, Variable):
        return env.get(node.name)

    if isinstance(node, Assignment):
        value = evaluate(node.value, env)
        env.define(node.name, value)
        return value

    raise TypeError(f"Unknown AST node: {node}")
