# 🔁 For Loops in Python

The `for` loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, string, or range).

---

## 🔹 Syntax

```python
for variable in sequence:
    # code block
```

---
## 🔹 Example with List

```python
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits:     
	print(fruit)
```

![[Pasted image 20250723133231.png]]

---
## 🔹 Iterating over a String

```python
for letter in "Python":     
	print(letter)
```

---

## 🔹 Using `range()`

```python
for i in range(5):     
	print(i) 
#Output: 0 1 2 3 4
```

With start and end:
```python
for i in range(2, 6):     
	print(i) 
# Output: 2 3 4 5
```

With step:
```python
for i in range(1, 10, 2):     
	print(i) 
# Output: 1 3 5 7 9
```

---

## 🔹 Else with For Loop
```python
for i in range(3):     
	print(i) 
else:     
	print("Loop finished")
```

---

## 🔹 Nested For Loops
```python
for i in range(2):     
	for j in range(3):         
		print(i, j)
```

---

## 🔹 Loop Control Statements

✅ `break` – exits the loop  
✅ `continue` – skips to the next iteration  
✅ `pass` – does nothing (placeholder)

```python
for i in range(5):    
	if i == 3:        
		break     
	print(i)
```

```python
for i in range(5):     
	if i == 2:         
		continue     
	print(i)
```

---

## 🧠 Summary

- `for` works with any iterable
- Use `range()` for numeric loops
- `else` block runs if loop is not broken with `break`
- Nesting is allowed