
Functions are blocks of reusable code that perform a specific task. They help break programs into smaller, manageable pieces.

---

## ✅ Defining a Function

![[Pasted image 20250724121249.png]]

```python
def greet():
    print("Hello, world!")
    ```

## ✅ Calling a Function

```python
greet()  # Output: Hello, world!
```

---

## ✅ Function with Parameters

```Python
def evenOdd1(x: int) -> str:
	if x % 2 == 0:
		return "Even1"
	else:
		return "Odd1"

print(evenOdd1(16))
print(evenOdd1(7)) 

#both are correct

def evenOdd(x):
	if x % 2 == 0:
		return "Even"
	else:
		return "Odd"

print(evenOdd(16))
print(evenOdd(7))
```

```python
def greet(name):     
	print("Hello,", name)  
greet("Alice")
```

---

## ✅ Function with Return Value

```python
def add(x, y):     
	return x + y
	  
result = add(5, 3) 
print("Sum:", result)
```

---

## ✅ Default Arguments

- But once we have a default argument, all the arguments to its right must also have default values.
```Python
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)
```

```python
def greet(name="Guest"):     
	print("Hello,", name)  
greet() 
greet("Bob")
```

---

## ✅ Keyword Arguments

- The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
```Python
def student(first_name, last_name):
	print(first_name,last_name)

student(first_name="John",last_name="Marston")
student(last_name="Morgan",first_name="Arthur")
```

```python
def student(name, age):     
	print("Name:", name)     
	print("Age:", age)  
student(age=20, name="Alice")
```

---

## ✅ Variable-Length Arguments

### *args (non-keyworded):

```python
def total(*numbers):     
	print(sum(numbers))  
total(1, 2, 3, 4)
```

### **kwargs (keyworded):
```python
def print_info(**kwargs):     
	for key, value in kwargs.items():         
		print(key, value)  
print_info(name="Alex", age=25)
```

---

## ✅ Anonymous Functions (lambda)

```python
square = lambda x: x * x 
print(square(5))  # Output: 25
```
---

## ✅Pass by Reference and Pass by Value

- One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function Python, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.
```Python
# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
```

## ✅ Pass Statement (empty function)

```python
def empty_func():     
	pass
```

---

## 🧠 Summary

- Functions improve readability and reusability.
- Use `def` keyword to define a function.
- Can return values using `return`.
- Support default, keyword, and variable-length arguments.
- Use `lambda` for short, one-line anonymous functions.