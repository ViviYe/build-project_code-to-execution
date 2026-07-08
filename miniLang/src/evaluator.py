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

    # TODO 1: evaluate Comparison nodes.
    if isinstance(node, Comparison):
        raise NotImplementedError("TODO: evaluate Comparison")

    # TODO 2: evaluate IfStatement nodes.
    if isinstance(node, IfStatement):
        raise NotImplementedError("TODO: evaluate IfStatement")

    # TODO 3: evaluate WhileStatement nodes.
    if isinstance(node, WhileStatement):
        raise NotImplementedError("TODO: evaluate WhileStatement")

    raise TypeError(f"Unknown AST node: {node}")
