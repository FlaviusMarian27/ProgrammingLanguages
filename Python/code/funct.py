def firstFunction():
    print("Prima mea functie!")
    
firstFunction()

print("\nFirst function!")
def evenOdd1(x: int) -> str:
    if x % 2 == 0:
        return "Even1"
    else:
        return "Odd1"
    
print(evenOdd1(16))
print(evenOdd1(7))

def evenOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

print("\nDefault Arguments")
def myFun(x, y = 50):
    print("X: ", x)
    print("Y: ", y)

myFun(10)

print("\nKeyword Arguments")
def student(first_name, last_name):
    print(first_name,last_name)

student(first_name="John",last_name="Marston")
student(last_name="Morgan",first_name="Arthur")

print("\nPositional Arguments")
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

print("\nArbitrary Keyword Arguments")
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

print("\nPython Function within Functions")
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()
    
f1()

print("\nAnonymous Functions in Python")
def cube(x):
    return x * x * x #without lambda

cube_l = lambda x : x * x * x
print(cube(3))
print(cube_l(4))

print("\nReturn Statement in Python Function")
def square_value(x):
    return x**2

print(square_value(4))
print(square_value(-2))

print("\nass by Reference and Pass by Value")
def myFun(x):
    x[0] = 20

lst = [10, 11, 13, 15, 17]
print("Lista initiala: ", lst)

myFun(lst)
print("Lista modificata: ", lst)

def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y
    
x = 1
y = 2
print(x,"and",y)
x,y = swap(x,y)
print(x,"and",y)

print("\nRecursive Function")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Result: ",factorial(5))
