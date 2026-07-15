from dataclasses import dataclass
from enum import Enum, auto
from typing import Any
class TokenType(Enum):
 NUMBER=auto(); IDENTIFIER=auto(); DEF=auto(); IF=auto(); WHILE=auto(); TRUE=auto(); FALSE=auto()
 PLUS=auto(); MINUS=auto(); STAR=auto(); SLASH=auto(); GREATER=auto(); LESS=auto(); GREATER_EQUAL=auto(); LESS_EQUAL=auto(); EQUAL_EQUAL=auto(); BANG_EQUAL=auto()
 LEFT_PAREN=auto(); RIGHT_PAREN=auto(); COMMA=auto(); COLON=auto(); ASSIGN=auto(); EOF=auto()
@dataclass(frozen=True)
class Token:
 type: TokenType
 value: Any=None
