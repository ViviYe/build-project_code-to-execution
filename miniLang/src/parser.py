from src.tokens import TokenType
from src.ast_nodes import *
class Parser:
 def __init__(self,tokens): self.tokens=tokens; self.current=0
 def peek(self): return self.tokens[self.current]
 def peek_next(self): return self.tokens[min(self.current+1,len(self.tokens)-1)]
 def advance(self): t=self.peek(); self.current+=1; return t
 def match(self,*types):
  if self.peek().type in types: self.advance(); return True
  return False
 def consume(self,t,msg):
  if self.peek().type==t: return self.advance()
  raise SyntaxError(msg)
 def parse(self):
  n=self.program(); self.consume(TokenType.EOF,'Expected end of input'); return n
 def program(self):
  if self.match(TokenType.DEF): return self.function_def()
  if self.match(TokenType.IF):
   c=self.comparison(); self.consume(TokenType.COLON,"Expected ':'"); return IfStatement(c,self.program())
  if self.match(TokenType.WHILE):
   c=self.comparison(); self.consume(TokenType.COLON,"Expected ':'"); return WhileStatement(c,self.program())
  if self.peek().type==TokenType.IDENTIFIER and self.peek_next().type==TokenType.ASSIGN:
   name=self.advance().value; self.advance(); return Assignment(name,self.comparison())
  return self.comparison()
 def function_def(self):
  name=self.consume(TokenType.IDENTIFIER,'Expected function name').value
  self.consume(TokenType.LEFT_PAREN,"Expected '('"); params=[]
  if self.peek().type!=TokenType.RIGHT_PAREN:
   params.append(self.consume(TokenType.IDENTIFIER,'Expected parameter').value)
   while self.match(TokenType.COMMA): params.append(self.consume(TokenType.IDENTIFIER,'Expected parameter').value)
  self.consume(TokenType.RIGHT_PAREN,"Expected ')'"); self.consume(TokenType.COLON,"Expected ':'")
  return FunctionDefinition(name,params,self.program())
 def comparison(self):
  left=self.expression(); ops={TokenType.GREATER:'>',TokenType.LESS:'<',TokenType.GREATER_EQUAL:'>=',TokenType.LESS_EQUAL:'<=',TokenType.EQUAL_EQUAL:'==',TokenType.BANG_EQUAL:'!='}
  if self.peek().type in ops: op=ops[self.advance().type]; return Comparison(op,left,self.expression())
  return left
 def expression(self):
  left=self.term()
  while self.match(TokenType.PLUS,TokenType.MINUS):
   t=self.tokens[self.current-1]; left=BinaryOp('+' if t.type==TokenType.PLUS else '-',left,self.term())
  return left
 def term(self):
  left=self.factor()
  while self.match(TokenType.STAR,TokenType.SLASH):
   t=self.tokens[self.current-1]; left=BinaryOp('*' if t.type==TokenType.STAR else '/',left,self.factor())
  return left
 def factor(self):
  t=self.peek()
  if t.type==TokenType.NUMBER: self.advance(); return Number(t.value)
  if t.type==TokenType.TRUE: self.advance(); return Boolean(True)
  if t.type==TokenType.FALSE: self.advance(); return Boolean(False)
  if t.type==TokenType.IDENTIFIER:
   if self.peek_next().type==TokenType.LEFT_PAREN: return self.call()
   self.advance(); return Variable(t.value)
  if t.type==TokenType.LEFT_PAREN:
   self.advance(); n=self.comparison(); self.consume(TokenType.RIGHT_PAREN,"Expected ')'"); return n
  raise SyntaxError(f'Unexpected token: {t}')
 def call(self):
  name=self.advance().value; self.consume(TokenType.LEFT_PAREN,"Expected '('"); args=[]
  if self.peek().type!=TokenType.RIGHT_PAREN:
   args.append(self.comparison())
   while self.match(TokenType.COMMA): args.append(self.comparison())
  self.consume(TokenType.RIGHT_PAREN,"Expected ')'"); return FunctionCall(name,args)
