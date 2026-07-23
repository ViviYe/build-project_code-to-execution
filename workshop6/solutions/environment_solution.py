class Environment:
 def __init__(self,parent=None): self.values={}; self.functions={}; self.parent=parent
 def define(self,name,value): self.values[name]=value; return value
 def get(self,name):
  if name in self.values: return self.values[name]
  if self.parent is not None: return self.parent.get(name)
  raise NameError(f'Variable {name!r} is not defined')
 def assign(self,name,value):
  if name in self.values: self.values[name]=value; return value
  if self.parent is not None: return self.parent.assign(name,value)
  raise NameError(f'Variable {name!r} is not defined')
 def define_function(self,name,function): self.functions[name]=function
 def get_function(self,name):
  if name in self.functions: return self.functions[name]
  if self.parent is not None: return self.parent.get_function(name)
  raise NameError(f'Function {name!r} is not defined')
