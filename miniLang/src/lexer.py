from src.tokens import Token,TokenType
KEYWORDS={'def':TokenType.DEF,'if':TokenType.IF,'while':TokenType.WHILE,'true':TokenType.TRUE,'false':TokenType.FALSE,'True':TokenType.TRUE,'False':TokenType.FALSE}
def tokenize(source):
 out=[]; i=0
 while i<len(source):
  c=source[i]
  if c.isspace(): i+=1; continue
  if c.isdigit():
   s=i
   while i<len(source) and source[i].isdigit(): i+=1
   out.append(Token(TokenType.NUMBER,int(source[s:i]))); continue
  if c.isalpha() or c=='_':
   s=i
   while i<len(source) and (source[i].isalnum() or source[i]=='_'): i+=1
   t=source[s:i]; k=KEYWORDS.get(t,TokenType.IDENTIFIER)
   out.append(Token(k, True if k==TokenType.TRUE else False if k==TokenType.FALSE else t if k==TokenType.IDENTIFIER else None)); continue
  two=source[i:i+2]
  m2={'>=':TokenType.GREATER_EQUAL,'<=':TokenType.LESS_EQUAL,'==':TokenType.EQUAL_EQUAL,'!=':TokenType.BANG_EQUAL}
  if two in m2: out.append(Token(m2[two])); i+=2; continue
  m1={'+':TokenType.PLUS,'-':TokenType.MINUS,'*':TokenType.STAR,'/':TokenType.SLASH,'>':TokenType.GREATER,'<':TokenType.LESS,'(':TokenType.LEFT_PAREN,')':TokenType.RIGHT_PAREN,',':TokenType.COMMA,':':TokenType.COLON,'=':TokenType.ASSIGN}
  if c in m1: out.append(Token(m1[c])); i+=1; continue
  raise SyntaxError(f'Unexpected character: {c!r}')
 out.append(Token(TokenType.EOF)); return out
