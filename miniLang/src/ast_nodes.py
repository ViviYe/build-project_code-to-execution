from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Number:
    value: int


@dataclass(frozen=True)
class Variable:
    name: str


@dataclass(frozen=True)
class Assignment:
    name: str
    value: Any


@dataclass(frozen=True)
class BinaryOp:
    op: str
    left: Any
    right: Any
