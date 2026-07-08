from src.ast_nodes import Number, Variable, Assignment, BinaryOp


def pretty_ast(node, indent: str = "") -> str:
    if isinstance(node, Number):
        return f"{indent}Number({node.value})"

    if isinstance(node, Variable):
        return f"{indent}Variable({node.name!r})"

    if isinstance(node, Assignment):
        value = pretty_ast(node.value, indent + "  ")
        return (
            f"{indent}Assignment(\n"
            f"{indent}  name={node.name!r},\n"
            f"{indent}  value=\n{value}\n"
            f"{indent})"
        )

    if isinstance(node, BinaryOp):
        left = pretty_ast(node.left, indent + "  ")
        right = pretty_ast(node.right, indent + "  ")
        return (
            f"{indent}BinaryOp(\n"
            f"{indent}  op={node.op!r},\n"
            f"{indent}  left=\n{left},\n"
            f"{indent}  right=\n{right}\n"
            f"{indent})"
        )

    raise TypeError(f"Unknown AST node: {node}")
