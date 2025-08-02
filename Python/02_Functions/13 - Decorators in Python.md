### ✅ What is a decorator?
- A **decorator** is a function that takes another function and extends its behavior without explicitly modifying it.
- Decorators are applied using the `@decorator_name` syntax above a function.

### 📌 Why use decorators?
- Follows the **DRY** principle (Don't Repeat Yourself).
- Cleanly adds extra functionality to existing code.
- Common use cases: **logging**, **authentication**, **timing**, **caching**, etc.

---

### 🧱 Key concepts

#### 1. Functions are objects
```python
def shout(text):
    return text.upper()

print(shout("hello"))         # => HELLO
yell = shout
print(yell("hello"))          # => HELLO
```

#### 2. Functions can be defined inside other functions
```python
def greet(name):
    def say_hello():
        return "Hello " + name
    return say_hello

greeting = greet("Alice")
print(greeting())             # => Hello Alice
```

#### 3. Functions can be passed as arguments
```python
def call_func(func):
    return func()

def say_hi():
    return "Hi!"

print(call_func(say_hi))      # => Hi!
```

---

### 🧩 Basic decorator example
```python
def decorator_func(original_func):
    def wrapper_func():
        print("Before the function runs")
        original_func()
        print("After the function runs")
    return wrapper_func

@decorator_func
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Before the function runs
Hello!
After the function runs
```

---

### ⚙️ Decorators with arguments
If the decorated function takes arguments:
```python
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def greet(name):
    print("Hello", name)

greet("Maria")
```

---

### 🔁 Chained decorators (multiple decorators)
```python
def decor1(func):
    def wrapper():
        print("Decor1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decor2")
        func()
    return wrapper

@decor1
@decor2
def say_hi():
    print("Hi")

say_hi()
```

**Output:**
```
Decor1
Decor2
Hi
```

---

### 🧠 TL;DR - Core ideas
- Decorators are functions that modify the behavior of other functions.
- Use `@decorator_name` syntax to apply them.
- Can add pre- and post-function logic.
- Can be combined (stacked) and accept arguments.

---

### 📚 Real-world examples
- `@staticmethod`, `@classmethod` – in classes.
- `@login_required` – in Django.
- `@app.route(...)` – in Flask.

---

### 🏁 Bonus tip
Decorators can also be implemented using **classes** with `__call__`, though this is less common for beginners.