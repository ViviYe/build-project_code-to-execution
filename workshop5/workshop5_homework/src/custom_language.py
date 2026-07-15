from src.lexer import tokenize
from src.parser import Parser
from src.environment import Environment
from src.evaluator import evaluate

class CustomLanguage:
    def __init__(self):
        self.env = Environment()

    def parse(self, source: str):
        tokens = tokenize(source)
        parser = Parser(tokens)
        return parser.parse()

    def run(self, source: str):
        ast = self.parse(source)
        return evaluate(ast, self.env)

    def repl(self) -> None:
        print("TinyLang REPL")
        print("Type 'exit' or 'quit' to stop.")
        print("Type ':env' to inspect the environment.")
        print()
        while True:
            try:
                source = input(">>> ").strip()
                if source in {"exit", "quit"}:
                    break
                if source == ":env":
                    print(self.env)
                    continue
                if not source:
                    continue
                print(self.run(source))
            except Exception as exc:
                print(f"Error: {exc}")
