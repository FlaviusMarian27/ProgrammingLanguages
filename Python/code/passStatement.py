def func():
    pass

func()

x = 4
if x > 5:
    pass
else:
    print("x is 5 or less")
    
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
        
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Anurag", 30)