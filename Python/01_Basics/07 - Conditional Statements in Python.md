Conditional statements are used to make decisions in code based on whether a condition is **True** or **False**.

---

## 🧩 if Statement

![[Pasted image 20250722184749.png]]

- Executes a block of code **only if** the condition is true.

```python
x = 10

if x > 0:
    print("Positive number")
```

---
## 🧩 if-else Statement

![[Pasted image 20250722184835.png]]

- Adds an alternative block when the condition is **false**.

```python
x = -5  
if x > 0:     
	print("Positive") 
else:     
	print("Negative or Zero")
```

---

## 🧩 if-elif-else Chain

![[Pasted image 20250722184902.png]]

- Used for **multiple conditions**.

```python
x = 0 
if x > 0:     
	print("Positive") 
elif x == 0:     
	print("Zero") 
else:     
	print("Negative")
```

---

## 🧩 Nested if Statements

![[Pasted image 20250722184951.png]]

- You can place one if-statement **inside another**.

```python
x = 10  
if x > 0:     
	if x % 2 == 0:         
		print("Positive and Even")     
	else:         
		print("Positive and Odd")
```

---

## 🧠 Notes

- Python uses **indentation** to define blocks (typically 4 spaces).
- No need for `()` around conditions or `{}` for blocks.

---

## ✅ Example

```python
age = int(input("Enter your age: "))  
if age >= 18:     
	print("Eligible to vote") 
else:     
	print("Not eligible")
```
