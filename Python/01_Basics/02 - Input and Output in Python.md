## 📥 Input in Python

- The `input()` function is used to get input from the user.
- It always returns data as a **string**.
- You can convert it using `int()`, `float()`, etc.

#### 🔹 Example:

```python
name = input("Enter your name: ")
print("Hello,", name)

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("Age:", age)
print("Height:", height)
``````

---
## 📥 Output in Python

- The `print()` function is used to display output to the console.
- You can print text, variables, or multiple items at once.

``` Python
print("Python is awesome")
x = 10
y = 5
print("Sum =", x + y)
```

---
## ⚙️ Customizing Output

##### ✅ `sep` parameter
- Controls the separator between printed items:
```Python
print("Python", "Java", "C++", sep=" | ")
# Output: Python | Java | C++
```

#### ✅ `end` parameter
- Controls what is printed at the end (default is newline `\n`):
```Python
print("Hello", end=" ")
print("World")
# Output: Hello World
```

## 🧠 Formatted Output

#### 🔹f-strings (Python 3.6+)

```Python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

#### 🔹.format() method
```Python
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
```
