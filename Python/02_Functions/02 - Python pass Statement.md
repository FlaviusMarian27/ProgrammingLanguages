

The `pass` statement in Python is a **null operation** — it does nothing when executed.

It is used as a placeholder when a statement is syntactically required but no action is needed.

---

## ✅ Syntax

```python
pass
```

## 🔹 Use Cases

### 1. In empty functions or classes:

```python
def my_function():     
	pass  # Will implement later  class MyClass:     pass  # Placeholder
```

---

### 2. Inside conditionals or loops when no action is needed:

```python
x = 10 
if x > 0:     
	pass  # No action needed, but avoids syntax error 
else:     
	print("x is not positive")
```

---

### 3. To define structure without implementation yet (e.g. during prototyping):

```python
def login():     
	pass  

def logout():     
	pass
```

---

## 🧠 Why Use `pass`?

- Prevents syntax errors in places where code is required.
- Useful when planning or testing code structure.
- Makes code syntactically correct until logic is added.

---

## ⚠️ Difference from comments

- Comments are ignored entirely.
- `pass` is an actual statement that gets executed (but does nothing).

```python
if True:     
	pass  # runs and does nothing  
	
# if True:  ← would cause an IndentationError if uncommented without a body
```

---

## ✅ Summary

- `pass` is a placeholder.
- Helps maintain code structure during development.
- Avoids syntax errors when code blocks are required.