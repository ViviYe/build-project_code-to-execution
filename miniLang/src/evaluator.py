from src.ast_nodes import *
from src.environment import Environment
def evaluate(node,env):
 if isinstance(node,Number): return node.value
 if isinstance(node,Boolean): return node.value
 if isinstance(node,Variable): return env.get(node.name)
 if isinstance(node,Assignment):
  value=evaluate(node.value,env); env.define(node.name,value); return value
 if isinstance(node,BinaryOp):
  a=evaluate(node.left,env); b=evaluate(node.right,env)
  if node.op=='+': return a+b
  if node.op=='-': return a-b
  if node.op=='*': return a*b
  if node.op=='/': return a/b
  raise ValueError(node.op)
 if isinstance(node,Comparison):
  a=evaluate(node.left,env); b=evaluate(node.right,env)
  if node.op=='>': return a>b
  if node.op=='<': return a<b
  if node.op=='>=': return a>=b
  if node.op=='<=': return a<=b
  if node.op=='==': return a==b
  if node.op=='!=': return a!=b
  raise ValueError(node.op)
 if isinstance(node,IfStatement):
  if evaluate(node.condition,env): evaluate(node.body,env)
  return None
 if isinstance(node,WhileStatement):
  while evaluate(node.condition,env): evaluate(node.body,env)
  return None
 if isinstance(node,FunctionDefinition): raise NotImplementedError('TODO: FunctionDefinition')
 if isinstance(node,FunctionCall): raise NotImplementedError('TODO: FunctionCall')
 raise TypeError(f'Unknown AST node: {node}')
