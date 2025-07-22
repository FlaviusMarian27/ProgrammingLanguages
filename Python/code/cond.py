age = int(input("Choose the age: "))

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
    
age1 = 20
s = "Adult" if age1 >= 18 else "Minor"
print(s)

number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")