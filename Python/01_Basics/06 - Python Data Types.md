In Python, **data types** define the kind of value a variable can hold. Python is dynamically typed — you don't need to declare the type explicitly.

---

![[Pasted image 20250722122133.png]]

## 🔢 Built-in Data Types

### 1. **Numeric Types**
- **int**: Integer values (e.g., `x = 10`)
- **float**: Decimal values (e.g., `pi = 3.14`)
- **complex**: Complex numbers (e.g., `z = 3 + 4j`)

```python
a = 5
b = 2.0
c = 1 + 2j
```

---
### 2. **Text Type**

- **str**: String of characters (e.g., `name = "Alice"`)

```python
greeting = "Hello, World!"
```

---

### 3. **Boolean Type**

- **bool**: True or False
```python
flag = True
```

---

### 4. **Sequence Types**

- **list**: Ordered, mutable collection
```   python
fruits = ["apple", "banana", "cherry"]
```

- **tuple**: Ordered, immutable collection
```    python
coords = (10, 20)
```

- **range**: Sequence of numbers
```    python
numbers = range(5)
```

---

### 5. **Set Types**

- **set**: Unordered collection of unique items
```    python
nums = {1, 2, 3}
``` 

- **frozenset**: Immutable version of set
```    python
frozen = frozenset([1, 2, 3])
```

---

### 6. **Mapping Type**

- **dict**: Key-value pairs
```python
person = {"name": "Alice", "age": 25}
```

---

### 7. **Binary Types**

- **bytes**, **bytearray**, **memoryview**
```python
b = bytes(5) 
ba = bytearray(5) 
mv = memoryview(bytes(5))
```
---

## 🔍 Type Checking
```python
x = 10 
print(type(x))  # <class 'int'>
```

---

## 🧪 Type Casting

- `int()`, `float()`, `str()`, `list()`, etc.    
```python
x = int("5") 
y = float("3.14")
```