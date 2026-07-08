from src.tokens import Token, TokenType
from src.ast_nodes import Number, Variable, Assignment, BinaryOp


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def peek(self) -> Token:
        return self.tokens[self.current]

    def peek_next(self) -> Token:
        if self.current + 1 >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.current + 1]

    def advance(self) -> Token:
        token = self.peek()
        self.current += 1
        return token

    def match(self, *token_types: TokenType) -> bool:
        if self.peek().type in token_types:
            self.advance()
            return True
        return False

    def consume(self, token_type: TokenType, message: str) -> Token:
        if self.peek().type == token_type:
            return self.advance()
        raise SyntaxError(message)

    def parse(self):
        node = self.parse_program()
        self.consume(TokenType.EOF, "Expected end of input")
        return node

    def parse_program(self):
        if self.peek().type == TokenType.IDENTIFIER and self.peek_next().type == TokenType.ASSIGN:
            name = self.advance().value
            self.consume(TokenType.ASSIGN, "Expected '=' after variable name")
            value = self.parse_expression()
            return Assignment(name, value)

        return self.parse_expression()

    def parse_expression(self):
        left = self.parse_term()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            op_token = self.tokens[self.current - 1]
            op = "+" if op_token.type == TokenType.PLUS else "-"
            right = self.parse_term()
            left = BinaryOp(op, left, right)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.match(TokenType.STAR, TokenType.SLASH):
            op_token = self.tokens[self.current - 1]
            op = "*" if op_token.type == TokenType.STAR else "/"
            right = self.parse_factor()
            left = BinaryOp(op, left, right)

        return left

    def parse_factor(self):
        token = self.peek()

        if token.type == TokenType.NUMBER:
            self.advance()
            return Number(token.value)

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return Variable(token.value)

        if token.type == TokenType.LEFT_PAREN:
            self.advance()
            expr = self.parse_expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
            return expr

        raise SyntaxError(f"Expected number, variable, or parenthesized expression, got {token}")
