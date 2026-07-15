# Workshop 5 Homework: Control Flow

## Goal

In Workshop 4, TinyLang learned how to execute expressions and remember variables:

```text
x = 5
y = x + 2
```

In Workshop 5, TinyLang learns how to make decisions and repeat work:

```text
if x > 3: y = 10
while x < 5: x = x + 1
```

By the end, your language should support:

```text
>>> x = 0
0
>>> while x < 3: x = x + 1
3
>>> x
3
>>> if x == 3: y = 100
100
>>> y
100
```

For the homework starter code, `if` and `while` bodies are written on the same line after `:` to keep parsing simple.

## Estimated Time

This homework should take around **2-3 hours**.

| Part | Task | Time |
|---|---|---:|
| 0 | Read architecture and run tests | 10-15 min |
| 1 | Implement boolean/comparison evaluation | 35-45 min |
| 2 | Implement `IfStatement` evaluation | 35-45 min |
| 3 | Implement `WhileStatement` evaluation | 45-60 min |
| 4 | Connect and test in the REPL | 20-30 min |
| 5 | Add your own tests / stretch | 20-30 min |

## Project Structure

```text
TinyLang/
├── README.md
├── custom_language.py
├── src/
│   ├── tokens.py
│   ├── lexer.py
│   ├── ast_nodes.py
│   ├── parser.py
│   ├── ast_printer.py
│   ├── environment.py
│   ├── evaluator.py          # TODO: comparisons, if, while
│   └── custom_language.py
├── tests/
│   ├── test_comparisons.py
│   ├── test_if_statement.py
│   ├── test_while_statement.py
│   └── test_custom_language_control_flow.py
└── solutions/
    └── evaluator_solution.py
```

## Syntax Supported

Arithmetic:

```text
1 + 2 * 3
```

Variables:

```text
x = 5
x + 2
```

Comparisons:

```text
x > 3
x < 10
x == 5
x != 0
x >= 5
x <= 8
```

If statements:

```text
if x > 3: y = 10
```

While loops:

```text
while x < 5: x = x + 1
```

## How to Run the REPL

```bash
python custom_language.py
```

Try:

```text
>>> x = 0
>>> while x < 3: x = x + 1
>>> x
>>> if x == 3: y = 100
>>> y
>>> :env
>>> quit
```

## How to Run Tests

Run all tests:

```bash
python -m unittest discover tests
```

Verbose mode:

```bash
python -m unittest discover tests -v
```

Run one test file:

```bash
python -m unittest tests.test_while_statement
```

Run one specific test:

```bash
python -m unittest tests.test_custom_language_control_flow.TestCustomLanguageControlFlow.test_while_loop_updates_environment
```

On Windows, use `py` instead of `python` if needed:

```bash
py -m unittest discover tests
```

# Assignment Tasks

## Part 1 — Evaluate Comparisons

Open `src/evaluator.py`.

Complete support for:

```text
>
<
>=
<=
==
!=
```

Expected behavior:

```python
lang.run("3 > 2")     # True
lang.run("3 < 2")     # False
lang.run("5 == 5")    # True
lang.run("5 != 5")    # False
```

## Part 2 — Evaluate IfStatement

Support:

```python
IfStatement(condition, body)
```

Evaluation rule:

```text
evaluate condition

if condition is True:
    evaluate body

otherwise:
    do nothing
```

Expected behavior:

```python
lang.run("x = 5")
lang.run("if x > 3: y = 10")
lang.run("y")  # 10
```

## Part 3 — Evaluate WhileStatement

Support:

```python
WhileStatement(condition, body)
```

Evaluation rule:

```text
while condition is True:
    evaluate body
```

Expected behavior:

```python
lang.run("x = 0")
lang.run("while x < 3: x = x + 1")
lang.run("x")  # 3
```

Use the provided `max_iterations` guard to avoid accidental infinite loops.

## Part 4 — Add Tests

Add at least **3 new tests** of your own.

# Stretch Goals

Optional:

1. Add `and` / `or`
2. Add `else`
3. Support multi-line blocks instead of one-line bodies
4. Add a better infinite-loop error message
5. Add `break`
6. Add `print(...)` as a built-in
