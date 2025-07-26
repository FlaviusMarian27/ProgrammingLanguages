def greet():
    msg = "Buna ziua!"
    print(msg)

greet()

msg = "Buna"

def greet():
    print("Seara",msg)

greet()
print("Ziua",msg)

def fun():
    print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
fun()
print("Outside Function", s)

def fun():
    s = "Me too."
    print(s)

s = "I love Geeksforgeeks"
fun()   
print(s)