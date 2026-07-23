from src.ast_nodes import *
from src.environment import Environment
from src.evaluator import evaluate as base_evaluate
# Reference patch for the two new cases:
def evaluate_function_nodes(node,env,evaluate):
 if isinstance(node,FunctionDefinition): env.define_function(node.name,node); return None
 if isinstance(node,FunctionCall):
  fn=env.get_function(node.name)
  if len(fn.parameters)!=len(node.arguments): raise TypeError(f'{node.name} expected {len(fn.parameters)} arguments, got {len(node.arguments)}')
  values=[evaluate(arg,env) for arg in node.arguments]
  local=Environment(parent=env)
  for parameter,value in zip(fn.parameters,values): local.define(parameter,value)
  return evaluate(fn.body,local)
 raise TypeError(node)
