
## 🧠 What is a Variable?

- A variable is a name that refers to a value stored in memory.
- Python does **not require explicit type declarations**.

### 🔹 Example:

```python
x = 5
name = "Flavius"
pi = 3.14
```

---
## 📌 Key Points

- Variables are **created when first assigned**.
- Python is **dynamically typed**: no need to declare types.
- Variable type is inferred from the assigned value.

---

## ✅ Rules for Naming Variables

- Can contain letters, digits, and underscore (`_`)
- Must **start with a letter or underscore**
- **Cannot start with a digit**
- **Cannot use reserved keywords**

### ❌ Invalid Examples:

```python
2name = "Wrong" 
class = "Reserved"

```

---

## 🧪 Checking Variable Type

- Use `type()` to check the variable's data type:

```python
`x = 42 print(type(x))  
<class 'int'>
```

---

## 🔁 Multiple Assignments

- You can assign multiple variables in one line:


```python
a, b, c = 1, 2, 3 
x = y = z = 0
```

---

## 🧹 Deleting Variables

- Use `del` to delete a variable:
```python
name = "Flavius" 
del name`
```