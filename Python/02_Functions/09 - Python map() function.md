## What is `map()`?

The `map()` function in Python applies a given function to **all** items in an `iterable` (like list, tuple, etc.) and returns a **map object** (which is an iterator).

## Syntax
```python
map(function, iterable) #iterable = list or tuplu
```

- `function`: a function to apply to each item.
- `iterable`: a sequence (list, tuple, etc.).

To get actual results, you need to convert the map object using `list()`, `set()`, or `tuple()`.

---

## Example 1 – Square each number
```python
def square(n):
    return n * n

nums = [1, 2, 3, 4, 5]
squared = list(map(square, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

---

## Example 2 – Using `lambda` with `map()`
```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

---

## Example 3 – Map with multiple iterables

If multiple iterables are passed, the function should accept that many arguments.

```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, nums1, nums2))
print(result)  # Output: [5, 7, 9]
```

---

## Example 4 – Convert strings to integers
```python
str_nums = ['1', '2', '3', '4']
int_nums = list(map(int, str_nums))
print(int_nums)  # Output: [1, 2, 3, 4]
```

---

## Example 5 – Map with different data types
```python
names = ['alice', 'BOB', 'ChArLiE']
normalized = list(map(str.lower, names))
print(normalized)  # Output: ['alice', 'bob', 'charlie']
```

---

## Using `map()` with `set` or `tuple`

You can convert the result to other types:
```python
nums = [1, 2, 3]
squared_set = set(map(lambda x: x ** 2, nums))
squared_tuple = tuple(map(lambda x: x ** 2, nums))

print(squared_set)    # Output: {1, 4, 9}
print(squared_tuple)  # Output: (1, 4, 9)
```

---

## Key Points

- `map()` is lazy – it returns an iterator, not a list.
- Often used with `lambda` for concise operations.
- Works with one or more iterables.
- Stops at the shortest iterable when multiple are used.
- Use `list()`, `set()`, or `tuple()` to materialize results.

---

## Summary

- `map()` is used for transforming data.
- Clean, fast, functional alternative to `for` loops.
- Often used in pipelines with `filter()` and `reduce()`.

**Example:**
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(lambda x: x * 2, nums))
print(result)  # Output: 30
```
****