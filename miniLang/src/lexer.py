from src.tokens import Token, TokenType


def tokenize(source: str) -> list[Token]:
    # Convert source code into tokens.
    #
    # Example:
    #     "12 + 3" -> [NUMBER(12), PLUS, NUMBER(3), EOF]
    #
    # Required for Workshop 3:
    #     - multi-digit numbers
    #     - +
    #     - *
    #     - whitespace
    #     - EOF
    #
    # Stretch:
    #     - -
    #     - /
    #     - parentheses

    tokens = []
    i = 0

    while i < len(source):
        char = source[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit():
            # TODO:
            # Read the full multi-digit number.
            #
            # Example:
            # source = "123+4"
            # if i starts at 0, we want to read "123" as one token.
            #
            # Hints:
            # start = i
            # while i < len(source) and source[i].isdigit():
            #     i += 1
            # number_text = source[start:i]
            # tokens.append(Token(TokenType.NUMBER, int(number_text)))
            # continue
            raise NotImplementedError("TODO: lex a full number")

        if char == "+":
            # TODO:
            # Add a PLUS token and advance i.
            raise NotImplementedError("TODO: lex +")

        if char == "*":
            # TODO:
            # Add a STAR token and advance i.
            raise NotImplementedError("TODO: lex *")

        # Stretch / future:
        if char == "-":
            raise NotImplementedError("STRETCH TODO: lex -")

        if char == "/":
            raise NotImplementedError("STRETCH TODO: lex /")

        if char == "(":
            raise NotImplementedError("STRETCH TODO: lex (")

        if char == ")":
            raise NotImplementedError("STRETCH TODO: lex )")

        raise SyntaxError(f"Unexpected character: {char!r}")

    tokens.append(Token(TokenType.EOF))
    return tokens
