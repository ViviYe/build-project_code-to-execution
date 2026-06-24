from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    STAR = auto()

    # Stretch / future operators
    MINUS = auto()
    SLASH = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    EOF = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Any = None

    def __repr__(self) -> str:
        if self.value is None:
            return self.type.name
        return f"{self.type.name}({self.value})"
