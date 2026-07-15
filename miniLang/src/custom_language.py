from src.environment import Environment
from src.evaluator import evaluate
from src.lexer import tokenize
from src.parser import Parser
class CustomLanguage:
 def __init__(self): self.env=Environment()
 def parse(self,source): return Parser(tokenize(source)).parse()
 def run(self,source): return evaluate(self.parse(source),self.env)
 def repl(self):
  print('MiniLang Workshop 6')
  while True:
   try:
    s=input('>>> ').strip()
    if s in {'quit','exit'}: break
    if s==':env': print(self.env.values); continue
    if s==':functions': print(sorted(self.env.functions)); continue
    if not s: continue
    r=self.run(s)
    if s.startswith('def '): print('Function defined')
    elif r is not None: print(r)
   except Exception as e: print(f'{type(e).__name__}: {e}')
