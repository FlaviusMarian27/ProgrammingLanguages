## What are Inner Functions?

- An inner function is a function defined inside another function.
- It is also known as a nested function.
- Inner functions can access variables from the enclosing scope (closure behavior).

---

## Syntax Example

```python
def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")

    inner_function()

outer_function()
```

### Output:
```
Outer function  
Inner function
```

---

## Why Use Inner Functions?

- **Encapsulation**: Hide helper functionality that shouldn't be accessed from outside.
- **Closures**: Inner functions can remember variables from the enclosing scope.
- **Logical grouping**: Keeps related logic together.

---

## Example – Accessing Outer Variables

```python
def outer(name):
    def inner():
        print(f"Hello, {name}!")
    inner()

outer("Alice")
```

### Output:
```
Hello, Alice!
```

- `inner()` uses `name` from `outer()` – this is closure behavior.

---

## Returning Inner Functions

You can return the inner function itself (not call it), allowing **function factories** or delayed execution.

```python
def outer(name):
    def inner():
        print(f"Hello, {name}")
    return inner

func = outer("Bob")
func()
```

### Output:
```
Hello, Bob
```

---

## Closures Explained

A **closure** is a function object that remembers values from its enclosing scope even if the outer function is done executing.

```python
def power_of(x):
    def power(n):
        return n ** x
    return power

square = power_of(2)
cube = power_of(3)

print(square(4))  # 16
print(cube(2))    # 8
```

---

## Checking Closure Contents

You can inspect the closure using `. __closure__`

```python
def make_multiplier(x):
    def multiply(n):
        return x * n
    return multiply

double = make_multiplier(2)
print(double.__closure__[0].cell_contents)  # 2
```

---

## Key Points Recap

- Inner functions are defined inside another function.
- They have access to variables from the outer function.
- Can be used for:
  - Encapsulation
  - Closures
  - Function factories
  - Logical organization
- Returned inner functions keep a reference to variables from the outer scope.

---

## Real-life Use Case – Logging Decorator

```python
def logger(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function finished execution")
    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello()
```

### Output:
```
Function is being called  
Hello!  
Function finished execution
```
