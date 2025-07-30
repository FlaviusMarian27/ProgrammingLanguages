class gfg:
    def __init__(self,topic):
        self._topic = topic
        
    def topic(self):
        print("Topic:",self._topic)
        
ins = gfg("Python")

ins.topic()

class Circle:
    def __init__(self, r: int):
        self.r = r
        
    def area(self): #method
        a = 3.14 * self.r ** 2
        return a
    
ins = Circle(5)
print("Area of the circle is:",ins.area())

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display_info method
print(car1.display())  # Output: This car is a Toyota Corolla

class BankAccount:
    def __init__(self, amount: int):
        self.amount = amount
        
    def deposit(self, amount: int):
        self.amount = self.amount + amount
        return self.amount
    
    def withdraw(self, amount: int):
        if self.amount >= amount:
            self.amount = self.amount - amount
            print("Succes!")
            return self.amount
        else:
            print("Insufficient funds!")
            return self.amount
    
    def check_balance(self):
        print("Current sold:",self.amount)
        
ins = BankAccount(1000)
ins.check_balance()
print("After deposit:",ins.deposit(500))
print("After withdraw:",ins.withdraw(800))
ins.check_balance()