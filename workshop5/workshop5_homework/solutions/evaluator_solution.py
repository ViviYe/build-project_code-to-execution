from src.ast_nodes import Number, Boolean, Variable, Assignment, BinaryOp, Comparison, IfStatement, WhileStatement
from src.environment import Environment

def evaluate(node, env: Environment, max_iterations: int = 1000):
    if isinstance(node, Number):
        return node.value

    if isinstance(node, Boolean):
        return node.value

    if isinstance(node, BinaryOp):
        left = evaluate(node.left, env, max_iterations)
        right = evaluate(node.right, env, max_iterations)
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
        value = evaluate(node.value, env, max_iterations)
        env.define(node.name, value)
        return value

    if isinstance(node, Comparison):
        left = evaluate(node.left, env, max_iterations)
        right = evaluate(node.right, env, max_iterations)
        if node.op == ">":
            return left > right
        if node.op == "<":
            return left < right
        if node.op == ">=":
            return left >= right
        if node.op == "<=":
            return left <= right
        if node.op == "==":
            return left == right
        if node.op == "!=":
            return left != right
        raise ValueError(f"Unknown comparison operator: {node.op}")

    if isinstance(node, IfStatement):
        if evaluate(node.condition, env, max_iterations):
            return evaluate(node.body, env, max_iterations)
        return None

    if isinstance(node, WhileStatement):
        last_result = None
        iterations = 0
        while evaluate(node.condition, env, max_iterations):
            if iterations >= max_iterations:
                raise RuntimeError("Maximum loop iterations exceeded")
            last_result = evaluate(node.body, env, max_iterations)
            iterations += 1
        return last_result

    raise TypeError(f"Unknown AST node: {node}")
