from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()
    TRUE = auto()
    FALSE = auto()
    IF = auto()
    WHILE = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    GREATER = auto()
    LESS = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    EQUAL_EQUAL = auto()
    BANG_EQUAL = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    ASSIGN = auto()
    COLON = auto()
    EOF = auto()

@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Any = None

    def __repr__(self) -> str:
        if self.value is None:
            return self.type.name
        return f"{self.type.name}({self.value})"
