## What is `reduce()`?

The `reduce()` function is used to **apply a function cumulatively** to the items of a sequence, from left to right, so as to reduce the sequence to a single value.

It is part of the `functools` module in Python 3.

## Syntax
```python
from functools import reduce

reduce(function, iterable[, initializer])
```

- `function`: takes two arguments.
- `iterable`: sequence of elements to be reduced.
- `initializer` (optional): value placed before the items of the iterable.

---

## How It Works

```python
reduce(lambda x, y: x + y, [1, 2, 3, 4])
```

This works like:

- Step 1: (1 + 2) = 3
- Step 2: (3 + 3) = 6
- Step 3: (6 + 4) = 10

Final result: `10`

---

## Example 1 – Sum of list elements
```python
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)  # Output: 10
```

---

## Example 2 – Multiply list elements
```python
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)  # Output: 24
```

---

## Example 3 – Find maximum using `reduce()`
```python
from functools import reduce

nums = [3, 8, 1, 6, 7]

max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)  # Output: 8
```

---

## Example 4 – Using initializer
```python
from functools import reduce

nums = [1, 2, 3]

result = reduce(lambda x, y: x + y, nums, 10)
print(result)  # Output: 16
```

In this case:
- Start with 10
- 10 + 1 → 11
- 11 + 2 → 13
- 13 + 3 → 16

---

## reduce() vs accumulate()

If you want to see all intermediate results, use `itertools.accumulate()` instead.

```python
from itertools import accumulate

nums = [1, 2, 3, 4]
result = list(accumulate(nums, lambda x, y: x + y))
print(result)  # Output: [1, 3, 6, 10]
```

---

## Key Points

- `reduce()` is used for aggregating elements into a single result.
- Must be imported from `functools` in Python 3.
- Can use any binary function: sum, product, max, etc.
- `initializer` lets you set a starting value.
- Not as readable as `sum()` or `for` loops — use with care for clarity.

---

## Summary Table

| Use Case             | Code Example                                       |
|----------------------|----------------------------------------------------|
| Sum all elements     | `reduce(lambda x, y: x + y, [1, 2, 3])`            |
| Multiply elements    | `reduce(lambda x, y: x * y, [1, 2, 3])`            |
| Max value            | `reduce(lambda x, y: x if x > y else y, [1, 3, 2])`|
| With initializer     | `reduce(lambda x, y: x + y, [1, 2, 3], 10)`        |

---

## Common Alternatives

- `sum(lst)` – more readable for simple addition.
- `math.prod(lst)` – Python 3.8+ for product.
- `max(lst)` – simpler than using reduce for max.

---

## Functional Programming Chain Example

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# Double each, then sum
result = reduce(lambda x, y: x + y, map(lambda x: x * 2, nums))
print(result)  # Output: 30
```

This combines:
- `map()` to double each number
- `reduce()` to sum them

