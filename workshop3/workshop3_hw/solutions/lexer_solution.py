from src.tokens import Token, TokenType


def tokenize(source: str) -> list[Token]:
    tokens = []
    i = 0

    while i < len(source):
        char = source[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit():
            start = i
            while i < len(source) and source[i].isdigit():
                i += 1
            tokens.append(Token(TokenType.NUMBER, int(source[start:i])))
            continue

        if char == "+":
            tokens.append(Token(TokenType.PLUS))
            i += 1
            continue

        if char == "*":
            tokens.append(Token(TokenType.STAR))
            i += 1
            continue

        if char == "-":
            tokens.append(Token(TokenType.MINUS))
            i += 1
            continue

        if char == "/":
            tokens.append(Token(TokenType.SLASH))
            i += 1
            continue

        if char == "(":
            tokens.append(Token(TokenType.LEFT_PAREN))
            i += 1
            continue

        if char == ")":
            tokens.append(Token(TokenType.RIGHT_PAREN))
            i += 1
            continue

        raise SyntaxError(f"Unexpected character: {char!r}")

    tokens.append(Token(TokenType.EOF))
    return tokens
