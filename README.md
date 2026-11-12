# Python Modules

My solutions to Python Modules 00–03 of the 42 Málaga common core.

| Module | Topic |
| --- | --- |
| [module00](module00) | Python basics: functions, `print`/`input`, type conversion, conditionals, loops and recursion |
| [module01](module01) | Object-oriented programming: classes, encapsulation with getters/setters, inheritance, static and class methods |
| [module02](module02) | Exceptions: `try`/`except`, raising errors, handling different error types, custom exception classes and `finally` |
| [module03](module03) | Collections: `sys.argv`, lists, tuples, sets, dictionaries, generators and comprehensions |

## Running the exercises

Each module has one directory per exercise (`ex0`, `ex1`, …). Requires Python 3.10 or later.

Modules 01–03 are scripts you can run directly:

```sh
python3 module03/ex1/ft_score_analytics.py 1500 2300 1800
```

Module 00 exercises define functions only, so import and call them:

```sh
cd module00/ex0
python3 -c "from ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```
