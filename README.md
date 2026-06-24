# Workshop 3 Starter Code: From Text to Trees

In Workshop 2, you evaluated trees that were already built by hand.

In Workshop 3, you will start building those trees automatically from source code.

## Big Goal

Turn source code like this:

```text
1 + 2 * 3
```

into tokens:

```text
NUMBER(1) PLUS NUMBER(2) STAR NUMBER(3) EOF
```

then into an AST:

```text
      +
     / \
    1   *
       / \
      2   3
```

## What You Implement This Week

Required:

1. Complete the lexer in `src/lexer.py`
2. Complete the parser in `src/parser.py`
3. Complete the AST pretty-printer in `src/ast_printer.py`
4. Run and pass the tests

Optional stretch:

1. Add `-` and `/`
2. Add parentheses
3. Improve parser error messages

## What Is Included But Mostly For Workshop 4

`src/custom_language.py` contains a future `CustomLanguage` class with a REPL-style loop and TODOs for evaluation and environment handling.

This is included now so you can see where the project is going, but Workshop 3 focuses on:

```text
source code → tokens → AST
```

not full execution yet.

## How To Run The Demo

From this folder:

```bash
python demo.py
```

This prints tokens and ASTs for example expressions.

## How To Use The Interactive CLI

```bash
python custom_language.py
```

Try:

```text
>>> 1 + 2 * 3
```

For Workshop 3, it will show tokens and AST only. Evaluation is intentionally left for Workshop 4.

## How To Run Tests

Run all tests:

```bash
python -m unittest discover tests
```

Run one test file:

```bash
python -m unittest tests.test_lexer
```

Run one specific test:

```bash
python -m unittest tests.test_parser.TestParser.test_precedence
```

On Windows, use `py` instead of `python` if needed:

```bash
py -m unittest discover tests
```

## Suggested Time

This homework is designed to take around **2–3 hours**.

Recommended order:

1. Read the files and run the demo: 10–15 min
2. Implement the lexer: 40–50 min
3. Implement the parser: 60–75 min
4. Implement pretty printing: 20–30 min
5. Run/debug tests: 20–30 min
6. Optional stretch: 20–40 min
