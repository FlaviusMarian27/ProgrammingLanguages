## Lambda Functions

- Lambda functions are anonymous functions in Python, meaning they do not have a name.
- In Python, we know the ***def*** keyword is used to define a normal function in Python.
- Similarly, the lambda keyword is used to define an anonymous function in Python.

**Syntax:**
```python
lambda arguments: expression
```

- ***lambda:*** The keyword to define the function.
- ***arguments:*** A comma-separated list of input parameters (like in a regular function).
- **expression:*** A single expression that is evaluated and returned.
---
- Can take any number of arguments.
- Can have only one expression.
- Often used as short, throwaway functions.

**Example:**
```python
x = lambda a, b: a + b
print(x(5, 6))  # Output: 11
```

---

## Lambda Inside a Function

You can use `lambda` inside a function to generate other functions dynamically.

**Example:**
```python
def myfunc(n):
    return lambda a: a * n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))  # Output: 22
print(tripler(11))  # Output: 33
```

---

## The `filter()` Function

```python
filter(function, iterable)
```

- The `filter()` unction in Python takes in a `function` and a `list` as arguments.
- This offers an elegant way to filter out all the elements of a sequence `"sequence"`, for which the function returns True.

**Example:**
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6, 8]
```

---

## The `map()` Function

```python
map(function, iterable)
```

- The map() in Python takes in a `function` and a `list` as an argument. 

- The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item.

**Example:**
```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

## The `reduce()` Function

```python
from functools import reduce
reduce(function, iterable)
```

- The reduce() function in Python takes in a `function` and a `list` as an argument. 
- The function is called with a `lambda function` and an `iterable` and a new reduced result is returned. 
- This performs a repetitive operation over the pairs of the `iterable`. 
- The reduce() function belongs to the `functools` module.

**Example:**
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # Output: 15
```

**Another Example (Product):**
```python
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120
```

---

## Summary Table

| Function | Purpose                            |
|----------|------------------------------------|
| `lambda`| Anonymous function                  |
| `filter`| Filters elements based on a condition |
| `map`   | Transforms each element             |
| `reduce`| Combines elements into a single result |

---

## When to Use

- `lambda`: For simple, one-line functions.
- `filter()`: To filter values from a list/iterable.
- `map()`: To transform or modify every element.
- `reduce()`: To combine values into one result (e.g., sum, product).

---

## Notes

- All three (`filter`, `map`, `reduce`) take:
  - a function
  - an iterable
- Promote functional programming in Python.
- `reduce()` is no longer built-in in Python 3 — you must `import` it.

---

## Full Example Using All Three

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 1: Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

# Step 2: Square them
squares = list(map(lambda x: x**2, evens))

# Step 3: Sum them
total = reduce(lambda x, y: x + y, squares)

print("Even numbers:", evens)
print("Squares:", squares)
print("Sum of squares:", total)
```

**Output:**
```
Even numbers: [2, 4, 6, 8]
Squares: [4, 16, 36, 64]
Sum of squares: 120
```
