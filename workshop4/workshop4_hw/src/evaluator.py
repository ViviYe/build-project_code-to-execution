from src.ast_nodes import Number, Variable, Assignment, BinaryOp
from src.environment import Environment


def evaluate(node, env: Environment):
    if isinstance(node, Number):
        # TODO: return the number's value.
        raise NotImplementedError("TODO: evaluate Number")

    if isinstance(node, BinaryOp):
        # TODO:
        # 1. evaluate left child
        # 2. evaluate right child
        # 3. apply node.op
        raise NotImplementedError("TODO: evaluate BinaryOp")

    if isinstance(node, Variable):
        # TODO: look up node.name in env.
        raise NotImplementedError("TODO: evaluate Variable")

    if isinstance(node, Assignment):
        # TODO:
        # 1. evaluate node.value
        # 2. store it in env
        # 3. return the stored value
        raise NotImplementedError("TODO: evaluate Assignment")

    raise TypeError(f"Unknown AST node: {node}")
