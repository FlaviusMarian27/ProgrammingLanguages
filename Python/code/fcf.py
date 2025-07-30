def msg(name: str) -> str:
    return f"Hello! My name is {name}!"

f = msg
print(f("John from the balcon"))

def func1(f2, name: str) -> str:
    return f2(name)

print(func1(msg, "Bob"))

def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))