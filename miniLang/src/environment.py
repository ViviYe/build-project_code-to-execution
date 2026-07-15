class Environment:
 def __init__(self,parent=None):
  self.values={}; self.functions={}
  # TODO: save parent
  self.parent=None
 def define(self,name,value): self.values[name]=value; return value
 def get(self,name): raise NotImplementedError('TODO: parent-aware get')
 def assign(self,name,value): raise NotImplementedError('TODO: parent-aware assign')
 def define_function(self,name,function): raise NotImplementedError('TODO: define_function')
 def get_function(self,name): raise NotImplementedError('TODO: get_function')
 def __repr__(self): return f'Environment(values={self.values}, functions={list(self.functions)}, has_parent={self.parent is not None})'
