def fun1(msg):
    def fun2():
        print(msg)
    fun1()
    
print("Hello")

def fun1():
    msg = "Geeks for geeks!"
    def fun2():
        print(msg)
    fun2()
fun1()

def fun1():
    a = 45
    
    def fun2():
        nonlocal a
        a = 54
        print(a)
    
    fun2()
    print(a)

fun1()

def fun1(a): # outer function
    
    def fun2(): # inner function
        print(a)
    return fun2  # returning function without parentheses

closure_func = fun1("Hello, Closure!")
closure_func()

def process_data(data):
    
    def clean_data():
        return [item.strip() for item in data]
    
    def clean_data_map():
        return list(map(str.strip,data))
        
    return clean_data()

print(process_data(["  Python  ","  Inner Function  "]))

def process_data(data):
    
    def clean_data_map():
        return list(map(str.strip,data))
        
    return clean_data_map()

print(process_data(["  Python  ","  Inner Function  "]))