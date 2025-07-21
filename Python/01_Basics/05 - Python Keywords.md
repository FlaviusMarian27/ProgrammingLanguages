
## 🧠 What are Keywords?

- Keywords are **reserved words** in Python.
- They have **special meaning** and **cannot be used as variable names**.
- Python has **33+ keywords** (can vary by version).

---

## ✅ Common Python Keywords (selection)

| Keyword    | Description                              |
|------------|------------------------------------------|
| `False`    | Boolean false                            |
| `True`     | Boolean true                             |
| `None`     | Represents null/empty                    |
| `and`      | Logical AND                              |
| `or`       | Logical OR                               |
| `not`      | Logical NOT                              |
| `if`       | Conditional statement                    |
| `else`     | Else block                               |
| `elif`     | Else-if condition                        |
| `while`    | While loop                               |
| `for`      | For loop                                 |
| `break`    | Exit current loop                        |
| `continue` | Skip to next loop iteration              |
| `def`      | Define a function                        |
| `return`   | Return from function                     |
| `class`    | Define a class                           |
| `try`      | Start exception handling block           |
| `except`   | Handle exception                         |
| `finally`  | Code that runs after try-except          |
| `import`   | Import a module                          |
| `from`     | Import specific parts from a module      |
| `as`       | Rename a module while importing          |
| `pass`     | Placeholder (does nothing)               |
| `in`       | Membership operator                      |
| `is`       | Identity operator                        |
| `lambda`   | Anonymous function definition            |
| `global`   | Declare global variable                  |
| `nonlocal` | Declare nonlocal variable                |
| `assert`   | Debug check (throws if False)            |
| `raise`    | Raise an exception                       |
| `del`      | Delete a variable/object                 |
| `yield`    | Pause a function, return value (generators) |

---

## 🔍 Check all keywords with `keyword` module:

```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))  # number of keywords
```

---
## ❌ Example of Invalid Use:

```python
if = 5  # ❌ invalid, 'if' is a keyword
```

