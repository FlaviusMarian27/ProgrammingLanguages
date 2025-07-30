- In Python, when defining methods within a class, the first parameter is always ***self***. The parameter self is a convention, not a keyword and it plays a key role in Python's Object-oriented structure.

```Python
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
```

```yaml
#Output
('Toyota', 'Corolla')
```

- ***self in __init__:*** Used to assign values (brand and model) to the specific instance (car1).
- ***self in display_info:*** Refers to the same car1 instance to access its attributes (brand and model).
- Python automatically passes car1 as the first argument to display.

----

### 1. Explicit is better than implicit
- Unlike Java or C++, Python **requires you to explicitly declare `self`**.
- This makes code more **transparent and readable** — no hidden references.

### 2. `self` is not a keyword
- You can technically name it anything, though `self` is the strong convention.

### 3. Methods are just functions

- In Python, a method is just a function defined inside a class.
- The first argument (`self`) is passed automatically when the method is called via an object.

### 4. Consistency and simplicity

- Python avoids "magic". Everything is passed clearly and explicitly.
- The use of `self` aligns with Python's design philosophy: **simple, clean, and explicit**.    

---

## 🧠 Summary

| Concept                | Python                      | Other Languages   |
| ---------------------- | --------------------------- | ----------------- |
| Object reference       | `self`                      | `this` (implicit) |
| Required in method def | ✅ Yes                       | ❌ No              |
| Passed automatically?  | ✅ Yes (when using dot call) | ✅ Yes             |
