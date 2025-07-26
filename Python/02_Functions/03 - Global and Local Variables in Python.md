
### 🔹 Local Variables

- Defined **inside a function**. 
- Accessible **only within that function**.
- Created when the function is called, destroyed when it ends.

```python
def func():     
	x = 10  # local variable     
	print(x)  
func()  # Output: 10 
# print(x) → Error: x is not defined
```

---
## 🔹Global Variables

- Defined outside all functions.
- Can be accessed anywhere in the code, including inside functions (read-only).
- If you try to assign to a global variable inside a function without declaring it global, Python treats it as local, which can cause errors.

```python
x = 20  # global variable
def func():
    print(x)  # works fine (reading)
func()  # Output: 20
```

---

## Why do we use Local and Global variables in Python?

```python
def fun():
    s = "Me too."
    print(s)

s = "I love Geeksforgeeks"
fun()   
print(s)
```

- Inside ***fun()***, ***s*** is a local variable set to "Me too." and prints that value. Outside, the global ***s*** remains "I love Geeksforgeeks", so printing ***s*** afterward shows the global value.

---
### ❗ Modifying Global Variable Inside Function

- You need to use the `global` keyword if you want to **modify** the global variable inside a function.

```python
x = 5  
def update():     
	global x     
	x = x + 1  	

update() 
print(x)  # Output: 6
```

Without `global`, it would raise `UnboundLocalError`.

---
### 🔹 global vs nonlocal

- `global` is used to refer to variables outside the function (in the global scope).
- `nonlocal` is used in **nested functions** to refer to variables in the **enclosing function scope**.

```python
def outer():     
	x = 10     
	def inner():         
		nonlocal x         
		x = 20     
	inner()     
	print(x)  
outer()  # Output: 20
```

| ***Comparison basis*** | **Global Variable**                                                                          | ***Local Variable***                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Definition             | Declared outside the functions                                                               | Declared within the functions                                                               |
| Lifetime               | They are created  the execution of the program begins and are lost when the program is ended | They are created when the function starts its execution and are lost when the function ends |
| Data Sharing           | Offers Data Sharing                                                                          | It doesn't offers Data Sharing                                                              |
| Scope                  | Can be access throughout the code                                                            | Can access only inside the function                                                         |
| Parameters needed      | Parameter passing is not necessary                                                           | Parameter passing is necessary                                                              |
| Storage                | A fixed location selected by the compiler                                                    | They are  kept on the stack                                                                 |
| Value                  | Once the value changes it is reflected throughout the code                                   | once changed the variable don't affect other functions of the program                       |

