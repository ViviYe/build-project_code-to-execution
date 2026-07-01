from src.ast_nodes import Number, BinaryOp


def pretty_ast(node, indent: str = "") -> str:
    # Return a readable multi-line representation of an AST.

    if isinstance(node, Number):
        # TODO:
        # Return something like: Number(1)
        raise NotImplementedError("TODO: pretty print Number")

    if isinstance(node, BinaryOp):
        # TODO:
        # Return a multi-line representation of a BinaryOp.
        #
        # Hint:
        # left = pretty_ast(node.left, indent + "  ")
        # right = pretty_ast(node.right, indent + "  ")
        raise NotImplementedError("TODO: pretty print BinaryOp")

    raise TypeError(f"Unknown AST node: {node}")
