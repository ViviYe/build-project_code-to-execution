from src.tokens import Token, TokenType

KEYWORDS = {
    "if": TokenType.IF,
    "while": TokenType.WHILE,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "True": TokenType.TRUE,
    "False": TokenType.FALSE,
}

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
            text = source[start:i]
            token_type = KEYWORDS.get(text, TokenType.IDENTIFIER)
            if token_type == TokenType.TRUE:
                tokens.append(Token(TokenType.TRUE, True))
            elif token_type == TokenType.FALSE:
                tokens.append(Token(TokenType.FALSE, False))
            elif token_type == TokenType.IDENTIFIER:
                tokens.append(Token(TokenType.IDENTIFIER, text))
            else:
                tokens.append(Token(token_type))
            continue

        if i + 1 < len(source):
            two = source[i:i + 2]
            two_char_tokens = {
                ">=": TokenType.GREATER_EQUAL,
                "<=": TokenType.LESS_EQUAL,
                "==": TokenType.EQUAL_EQUAL,
                "!=": TokenType.BANG_EQUAL,
            }
            if two in two_char_tokens:
                tokens.append(Token(two_char_tokens[two]))
                i += 2
                continue

        single_char_tokens = {
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
            "*": TokenType.STAR,
            "/": TokenType.SLASH,
            ">": TokenType.GREATER,
            "<": TokenType.LESS,
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "=": TokenType.ASSIGN,
            ":": TokenType.COLON,
        }

        if char in single_char_tokens:
            tokens.append(Token(single_char_tokens[char]))
            i += 1
            continue

        raise SyntaxError(f"Unexpected character: {char!r}")

    tokens.append(Token(TokenType.EOF))
    return tokens
