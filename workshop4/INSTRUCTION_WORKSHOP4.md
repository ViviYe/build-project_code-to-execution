# Workshop 4 Homework: From Trees to Execution

## Goal

In Workshop 3, you built the front half of TinyLang:

```text
source code → lexer → tokens → parser → AST
```

In Workshop 4, you will build the execution half:

```text
AST → evaluator → result
```

Then you will add memory:

```text
environment → variables → assignment
```

By the end, your language should support:

```text
>>> 1 + 2 * 3
7

>>> x = 5
5

>>> x + 2
7

>>> y = x * 3
15

>>> y + 1
16
```

## Estimated Time

This homework should take around **2–3 hours**.

| Part | Task | Time |
|---|---|---:|
| 0 | Read architecture and run tests | 10–15 min |
| 1 | Implement arithmetic evaluator | 35–45 min |
| 2 | Implement `Environment` | 25–35 min |
| 3 | Implement variable lookup | 25–35 min |
| 4 | Implement assignment | 35–45 min |
| 5 | Connect `CustomLanguage.run()` | 20–30 min |
| 6 | Add your own tests / stretch | 20–30 min |

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
│   ├── environment.py        # TODO: implement program memory
│   ├── evaluator.py          # TODO: execute AST nodes
│   └── custom_language.py    # TODO: connect parse + evaluate
├── tests/
│   ├── test_environment.py
│   ├── test_evaluator.py
│   └── test_custom_language.py
└── solutions/
    ├── environment_solution.py
    ├── evaluator_solution.py
    └── custom_language_solution.py
```

## What Is Provided

This week, the lexer and parser are mostly provided so you can focus on execution.

The starter code already parses:

```text
1 + 2 * 3
(1 + 2) * 3
x
x = 5
y = x + 2
```

Your job is to make those ASTs **run**.

## How to Run the REPL

From this folder:

```bash
python custom_language.py
```

Try:

```text
>>> 1 + 2 * 3
>>> x = 5
>>> x + 2
>>> :env
>>> quit
```

At first, many commands will fail because the evaluator and environment contain TODOs.

## How to Run Tests

Run all tests:

```bash
python -m unittest discover tests
```

Run one test file:

```bash
python -m unittest tests.test_evaluator
```

Run one specific test:

```bash
python -m unittest tests.test_custom_language.TestCustomLanguage.test_variable_assignment_and_lookup
```

On Windows, use `py` instead of `python` if needed:

```bash
py -m unittest discover tests
```

# Assignment Tasks

## Part 1 — Evaluate Numbers and Arithmetic

Open:

```text
src/evaluator.py
```

Complete:

```python
evaluate(Number(...), env)
evaluate(BinaryOp(...), env)
```

Required operators:

```text
+
-
*
/
```

Expected behavior:

```python
run("1 + 2")        # 3
run("1 + 2 * 3")    # 7
run("(1 + 2) * 3")  # 9
```

## Part 2 — Implement Environment

Open:

```text
src/environment.py
```

Complete:

```python
define(name, value)
get(name)
assign(name, value)
```

The environment is the memory of the interpreter.

If a variable does not exist, raise `NameError`.

## Part 3 — Evaluate Variables

In `src/evaluator.py`, support:

```python
Variable("x")
```

Concept:

```text
Number node   → return its value
Variable node → ask environment for its value
```

## Part 4 — Evaluate Assignment

In `src/evaluator.py`, support:

```python
Assignment("x", Number(5))
```

Assignment should:

1. Evaluate the right-hand side
2. Store the result in the environment
3. Return the assigned value

## Part 5 — Connect CustomLanguage

Open:

```text
src/custom_language.py
```

Complete:

```python
run(source)
```

It should:

```text
source → tokens → parser → AST → evaluator → result
```

Important: the same `Environment` should persist across multiple calls to `run()`.

This should work:

```python
lang = CustomLanguage()

lang.run("x = 5")
lang.run("x + 2")  # 7
```

## Part 6 — Add Tests

Add at least **3 new tests** of your own.

Good examples:

```python
x = 5
x + 2
```

```python
x = 5
x = 10
x
```

```python
x = 2 + 3
x * 4
```

# Stretch Goals

Optional if you finish early:

1. Add exponentiation: `2 ** 3`
2. Add unary minus: `-5`
3. Improve error messages
4. Add a `clear` command to reset the REPL environment
5. Print the environment after each assignment for debugging

## Submission Checklist

Before submitting, make sure:

- [ ] `python -m unittest discover tests` runs
- [ ] arithmetic expressions work
- [ ] variable lookup works
- [ ] assignment works
- [ ] environment persists across multiple `run()` calls
- [ ] you added at least 3 tests of your own
