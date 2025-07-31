## What is `filter()`?

The `filter()` function constructs an iterator from elements of an iterable for which a function returns `True`.

## Syntax
```python
filter(function, iterable)
```

- `function`: function that returns `True` or `False`.
- `iterable`: sequence (list, tuple, etc.) to filter.

Returns a filter object (iterator), typically converted using `list()`, `set()`, or `tuple()`.

---

## Example 1 – Filter even numbers
```python
def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, nums))
print(evens)  # Output: [2, 4, 6]
```

---

## Example 2 – Using `lambda` with `filter()`
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

---

## Example 3 – Remove empty strings
```python
data = ["apple", "", "banana", "", "cherry"]
filtered = list(filter(None, data))
print(filtered)  # Output: ['apple', 'banana', 'cherry']
```

- Passing `None` as the function removes all falsy values:
  - `''`, `0`, `None`, `False`, `[]`, etc.

---

## Example 4 – Filter based on length
```python
names = ["Bob", "Alice", "Eve", "John", "Charlie"]

# Keep names longer than 3 characters
filtered = list(filter(lambda x: len(x) > 3, names))
print(filtered)  # Output: ['Alice', 'John', 'Charlie']
```

---

## Using `filter()` with sets and tuples

```python
nums = (1, 2, 3, 4, 5, 6)
evens = tuple(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: (2, 4, 6)

s = {0, 1, 2, 3, 4}
filtered = set(filter(lambda x: x > 2, s))
print(filtered)  # Output: {3, 4}
```

---

## Key Points

- `filter()` is lazy — it returns an iterator.
- Commonly used with `lambda` for inline filters.
- If function is `None`, it removes falsy values.
- Only keeps elements where `function(element)` is `True`.

---

## filter() vs List Comprehension

Equivalent:
```python
# With filter()
list(filter(lambda x: x % 2 == 0, nums))

# With list comprehension
[x for x in nums if x % 2 == 0]
```

- List comprehensions are more Pythonic and readable in many cases.
- `filter()` is more functional-style and works well in pipelines.

---

## Summary Table

| Task                    | Code Example                                 |
|-------------------------|----------------------------------------------|
| Filter even numbers     | `filter(lambda x: x % 2 == 0, nums)`         |
| Remove empty strings    | `filter(None, strings)`                      |
| Filter by length        | `filter(lambda x: len(x) > 3, names)`        |
| Convert result to list  | `list(filter(...))`                          |

---

## Common Use with map() and reduce()

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Filter even, then square them, then sum
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
)

print(result)  # Output: 56  (2² + 4² + 6² = 4 + 16 + 36)
```
