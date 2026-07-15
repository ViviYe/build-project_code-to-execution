# Workshop 6 Homework: Functions & Scope

## Goal
Extend the Workshop 5 MiniLang interpreter with user-defined functions, argument binding, local scope, parent environments, and nested calls.

Supported examples after completion:

```text
>>> def square(x): x * x
Function square defined
>>> square(5)
25
>>> def area(width, height): width * height
Function area defined
>>> area(4, 5)
20
```

Function bodies are one expression or assignment after `:`. Multi-line blocks and explicit `return` come later.

## Estimated effort: 2–3 hours

| Part | Task | Time |
|---|---|---:|
| 0 | Read project and run tests | 10–15 min |
| 1 | Parent-aware variable lookup | 25–35 min |
| 2 | Function storage and lookup | 20–30 min |
| 3 | Function definition evaluation | 20–25 min |
| 4 | Function call evaluation and binding | 45–60 min |
| 5 | Scope, nested calls, errors | 25–35 min |
| 6 | Add four tests + stretch | 20–30 min |

## Run

```bash
python custom_language.py
python -m unittest discover tests -v
```

## Main TODOs

### 1. `src/environment.py`
Implement:

```python
Environment(parent=None)
get(name)
assign(name, value)
define_function(name, function)
get_function(name)
```

Lookup rule:

```text
current scope → parent scope → ... → NameError
```

Local values must shadow parent values.

### 2. `FunctionDefinition`
A definition registers code but does not execute the body.

```text
definition = registration
call = execution
```

### 3. `FunctionCall`
Implement:

```text
find definition
→ validate arity
→ evaluate arguments in caller
→ create Environment(parent=caller)
→ bind parameters
→ evaluate body locally
→ return body result
```

### 4. Required behavior

```text
x = 100
def square(x): x * x
square(5)  # 25
x          # still 100
```

```text
multiplier = 10
def scale(x): x * multiplier
scale(7)   # 70 via parent lookup
```

```text
def square(x): x * x
def double(x): x * 2
double(square(5))  # 50
```

Wrong argument count raises `TypeError`; unknown functions and variables raise `NameError`.

## Add at least four tests
Include a two-parameter function, shadowing, parent lookup, nested calls, and one error case.

## Stretch goals
- Zero-argument functions
- Three or more parameters
- Reject function redefinition
- Debug printing of local environments
- A simple built-in function

## Submission checklist
- [ ] Parent lookup works
- [ ] Local shadowing works
- [ ] Definitions do not execute bodies
- [ ] Calls create fresh local scopes
- [ ] Arguments bind correctly
- [ ] Multiple parameters work
- [ ] Nested calls work
- [ ] Workshop 5 behavior still passes
- [ ] Four student tests added
