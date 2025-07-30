In Python, functions are **first-class citizens**.  
This means they can be:

✅ Passed as arguments  
✅ Returned from other functions  
✅ Assigned to variables  
✅ Stored in data structures

---

## ✅ What does "First-Class" mean?

A programming language supports first-class functions if functions in that language are treated like any other object (e.g., integers, strings, lists).

---

## 🔹 1. Assigning a Function to a Variable

```python
def greet(name):
    return f"Hello, {name}!"

hello = greet
print(hello("Alice"))  # ➜ Hello, Alice!
```

## 🔹 2. Passing a Function as Argument
```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, message):
    print(func(message))

speak(shout, "Python is awesome")  # ➜ PYTHON IS AWESOME
speak(whisper, "Python is awesome")  # ➜ python is awesome
```

---

## 🔹 3. Returning a Function from Another Function

```python
def outer():
    def inner():
        print("This is inner")
    return inner

fn = outer()
fn()  # ➜ This is inner
```

---

## 🔹 4. Storing Functions in Data Structures
```python
def add(x, y): return x + y
def sub(x, y): return x - y

ops = {
    "add": add,
    "sub": sub
}

print(ops["add"](2, 3))  # ➜ 5
```

---

## 🔁 Summary

| Feature              | Supported in Python? |
| -------------------- | -------------------- |
| Assign to variable   | ✅ Yes                |
| Pass as argument     | ✅ Yes                |
| Return from function | ✅ Yes                |
| Store in collections | ✅ Yes                |

- Python functions are first-class — this makes functional programming and advanced patterns like decorators possible.