from src.tokens import Token, TokenType
from src.ast_nodes import Number, BinaryOp


class Parser:
    # A tiny recursive descent parser.
    #
    # Required grammar:
    #
    #     expression -> term (PLUS term)*
    #     term       -> factor (STAR factor)*
    #     factor     -> NUMBER
    #
    # This grammar makes * bind tighter than +.
    #
    # Stretch grammar with parentheses:
    #
    #     factor -> NUMBER | LEFT_PAREN expression RIGHT_PAREN

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def peek(self) -> Token:
        return self.tokens[self.current]

    def advance(self) -> Token:
        token = self.peek()
        self.current += 1
        return token

    def match(self, token_type: TokenType) -> bool:
        if self.peek().type == token_type:
            self.advance()
            return True
        return False

    def consume(self, token_type: TokenType, message: str) -> Token:
        if self.peek().type == token_type:
            return self.advance()
        raise SyntaxError(message)

    def parse(self):
        expr = self.parse_expression()
        self.consume(TokenType.EOF, "Expected end of expression")
        return expr

    def parse_expression(self):
        # expression -> term (PLUS term)*
        left = self.parse_term()

        # TODO:
        # while self.match(TokenType.PLUS):
        #     right = self.parse_term()
        #     left = BinaryOp("+", left, right)

        return left

    def parse_term(self):
        # term -> factor (STAR factor)*
        left = self.parse_factor()

        # TODO:
        # while self.match(TokenType.STAR):
        #     right = self.parse_factor()
        #     left = BinaryOp("*", left, right)

        return left

    def parse_factor(self):
        # factor -> NUMBER
        token = self.peek()

        if token.type == TokenType.NUMBER:
            # TODO:
            # Consume the number token and return Number(token.value).
            raise NotImplementedError("TODO: parse number")

        # Stretch:
        # if token.type == TokenType.LEFT_PAREN:
        #     self.advance()
        #     expr = self.parse_expression()
        #     self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
        #     return expr

        raise SyntaxError(f"Expected number, got {token}")
