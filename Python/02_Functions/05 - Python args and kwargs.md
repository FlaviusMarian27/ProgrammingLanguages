In Python, `*args` and `**kwargs` are used to pass a variable number of arguments to a function.

---

![[Pasted image 20250729145046.png]]
## 🔹 *args (Non-keyword arguments)

- Used when you want to **pass multiple values as a tuple**.
- Can be any number of arguments.

```python
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3))  # Output: 6
```

## 🔹 **kwargs (Keyword arguments)

- Used when you want to pass **named arguments as a dictionary**.
- Useful when argument names are not known in advance.

```python
def print_info(**kwargs):     
	for key, value in kwargs.items():         
		print(f"{key} = {value}") 
print_info(name="Alice", age=25)

```

---

## ✅ Using both *args and **kwargs

```python
def demo_func(*args, **kwargs):     
	print("Positional:", args)     
	print("Keyworded:", kwargs)
	  
demo_func(1, 2, 3, name="Bob", age=30)
```

Output:
```yaml
Positional: (1, 2, 3) 
Keyworded: {'name': 'Bob', 'age': 30}
```
 
---

## 🧠 Notes

- `*args` → receives values as a tuple  
- `**kwargs` → receives named values as a dictionary
- Names `args` and `kwargs` are just convention. You can rename them (`*values`, `**data`), but `*` and `**` are required.    

---

## ⚠️ Order Matters

When using all types of parameters together, the order must be:

```python
def func(normal, *args, default=10, **kwargs):     
	...
```

---

## ✅ Summary

| Syntax     | Type       | Example Call     |
| ---------- | ---------- | ---------------- |
| `*args`    | Tuple      | `func(1, 2, 3)`  |
| `**kwargs` | Dictionary | `func(a=1, b=2)` |

- Flexible and powerful for dynamic function arguments.    
