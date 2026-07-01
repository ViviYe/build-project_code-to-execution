from src.lexer import tokenize
from src.parser import Parser
from src.ast_printer import pretty_ast


def demo(source: str) -> None:
    print("=" * 60)
    print("Source:")
    print(source)

    print("\nTokens:")
    tokens = tokenize(source)
    print(tokens)

    print("\nAST:")
    ast = Parser(tokens).parse()
    print(pretty_ast(ast))


if __name__ == "__main__":
    examples = [
        "1 + 2",
        "1 + 2 * 3",
        "10 + 20 * 3",
    ]

    for source in examples:
        demo(source)
