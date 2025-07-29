 **Recursion** is a programming technique where a function calls itself to solve smaller instances of a problem.

---

![[Pasted image 20250729134346.png]]

## 🧠 Key Concepts

- Every recursive function must have a **base case** (stop condition).
- Without a base case, recursion leads to infinite calls and a stack overflow.
- Python has a recursion limit (default: ~1000).

---

## ✅ Basic Structure of Recursive Function

```python
def recursive_function(parameters):
	if base_case_condition:
		return base_result
	else:
		return recursive_function(modified_parameters)
```

---
## 📌 Example 1: Print Numbers from 1 to n

```Python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end=" ")

print_numbers(5)
# Output: 1 2 3 4 5
```

---
## ⚠️ RecursionError

- If recursion is too deep or the base case is missing:

```Python
def bad_recursion():
    return bad_recursion()

bad_recursion()  # ➜ RecursionError: maximum recursion depth exceeded
```

- Use `sys.setrecursionlimit(n)` to increase the limit if really needed.

---
## 📌 Example 3: Sum of First n Numbers

```Python
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(5))  # Output: 15
```

## ✅ When to Use Recursion

- When a problem can be divided into similar subproblems.
- Useful in: trees, graphs, divide and conquer, backtracking.

---
## Types of Recursion in Python

- [***Tail Recursion***](https://www.geeksforgeeks.org/dsa/tail-recursion/): This occurs when the recursive call is the last operation executed in the function, with no additional work or calculation following the recursive call. In many programming languages, tail recursion can be optimized by the compiler into iterative loops to improve performance and prevent stack overflow.

- **Non-Tail Recursion**: This occurs when there are operations or calculations that follow the recursive call. This type prevents the compiler or interpreter from optimizing the recursion into an iteration.

```Python
def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)

# Example usage
print(tail_fact(5))  
print(nontail_fact(5))
```

---
## 🔁 Summary

- Recursive functions call themselves.    
- Must include a **base case**.
- Can simplify complex problems like factorial, Fibonacci, etc.