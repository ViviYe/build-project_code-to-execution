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
        ast = self.parse(source)
        return evaluate(ast, self.env)
