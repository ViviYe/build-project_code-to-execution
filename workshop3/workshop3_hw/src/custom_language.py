from src.lexer import tokenize
from src.parser import Parser
from src.ast_printer import pretty_ast
from src.evaluator import evaluate


class CustomLanguage:
    # Tiny language shell.
    #
    # Workshop 3:
    #     source -> tokens -> AST
    #
    # Workshop 4:
    #     AST -> evaluation result
    #     variables
    #     environment

    def __init__(self):
        # Workshop 4 TODO:
        # This will store variables later, for example:
        # self.env["x"] = 5
        self.env = {}

    def parse(self, source: str):
        tokens = tokenize(source)
        parser = Parser(tokens)
        return parser.parse()

    def inspect(self, source: str) -> None:
        # Show tokens and AST without evaluating.
        tokens = tokenize(source)
        ast = Parser(tokens).parse()

        print("Tokens:")
        print(tokens)

        print("\nAST:")
        print(pretty_ast(ast))

    def eval(self, source: str):
        # Workshop 4 TODO.
        #
        # Eventually:
        #     source -> tokens -> AST -> result
        #
        # For Workshop 3, this intentionally raises NotImplementedError.
        ast = self.parse(source)
        return evaluate(ast)

    def repl(self) -> None:
        # A tiny input loop.
        #
        # For Workshop 3, the REPL shows tokens and AST.
        # For Workshop 4, it will evaluate programs.

        print("CustomLanguage REPL")
        print("Workshop 3 mode: source -> tokens -> AST")
        print("Type 'exit' or 'quit' to stop.")
        print()

        while True:
            try:
                source = input(">>> ").strip()

                if source in {"exit", "quit"}:
                    break

                if not source:
                    continue

                self.inspect(source)
                print()

            except Exception as exc:
                print(f"Error: {exc}")
                print()
