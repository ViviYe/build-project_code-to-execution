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

        if char.isalpha() or char == "_":
            start = i
            while i < len(source) and (source[i].isalnum() or source[i] == "_"):
                i += 1
            tokens.append(Token(TokenType.IDENTIFIER, source[start:i]))
            continue

        single_char_tokens = {
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
            "*": TokenType.STAR,
            "/": TokenType.SLASH,
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "=": TokenType.ASSIGN,
        }

        if char in single_char_tokens:
            tokens.append(Token(single_char_tokens[char]))
            i += 1
            continue

        raise SyntaxError(f"Unexpected character: {char!r}")

    tokens.append(Token(TokenType.EOF))
    return tokens
