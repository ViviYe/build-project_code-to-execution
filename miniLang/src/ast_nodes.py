from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class Number: value:int
@dataclass(frozen=True)
class Boolean: value:bool
@dataclass(frozen=True)
class Variable: name:str
@dataclass(frozen=True)
class Assignment: name:str; value:Any
@dataclass(frozen=True)
class BinaryOp: op:str; left:Any; right:Any
@dataclass(frozen=True)
class Comparison: op:str; left:Any; right:Any
@dataclass(frozen=True)
class IfStatement: condition:Any; body:Any
@dataclass(frozen=True)
class WhileStatement: condition:Any; body:Any
@dataclass(frozen=True)
class FunctionDefinition: name:str; parameters:list[str]; body:Any
@dataclass(frozen=True)
class FunctionCall: name:str; arguments:list[Any]
