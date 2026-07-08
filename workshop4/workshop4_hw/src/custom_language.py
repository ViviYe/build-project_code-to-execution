from src.lexer import tokenize
from src.parser import Parser
from src.ast_printer import pretty_ast
from src.environment import Environment
from src.evaluator import evaluate


class CustomLanguage:
    def __init__(self):
        self.env = Environment()

    def parse(self, source: str):
        tokens = tokenize(source)
        parser = Parser(tokens)
        return parser.parse()

    def inspect(self, source: str) -> None:
        tokens = tokenize(source)
        ast = Parser(tokens).parse()

        print("Tokens:")
        print(tokens)

        print("\nAST:")
        print(pretty_ast(ast))

    def run(self, source: str):
        # TODO:
        # 1. parse source
        # 2. evaluate AST using self.env
        # 3. return result
        raise NotImplementedError("TODO: implement run()")

    def repl(self) -> None:
        print("TinyLang REPL")
        print("Type 'exit' or 'quit' to stop.")
        print("Type ':env' to inspect the environment.")
        print("Type ':ast <expr>' to inspect the AST.")
        print()

        while True:
            try:
                source = input(">>> ").strip()

                if source in {"exit", "quit"}:
                    break

                if source == ":env":
                    print(self.env)
                    continue

                if source.startswith(":ast "):
                    self.inspect(source[len(":ast "):])
                    continue

                if not source:
                    continue

                result = self.run(source)
                print(result)

            except Exception as exc:
                print(f"Error: {exc}")
