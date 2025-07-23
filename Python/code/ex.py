'''name = input("Un nume: ")
age = int(input("O varsta: "))
name = "Alin"
age = 20
print("Hello", name,", you are", age, "years")

num1 = int(input("Numarul 1: "))
num2 = int(input("Numarul 2: "))

sum = num1 + num2
print("Suma:",sum)

prod = num1 * num2
print("Produsul:",prod)

if num1 > num2:
    imp = num1 // num2
else:
    imp = num2 // num1
    
print("Impartire:",imp)

#==========================================================

value_int = 3
value_float = 3.14
value_string = "John"

print("Int:", value_int)
print("Float:", value_float)
print("String:", value_string)

age = int(input("Alege o varsta: "))
is_adult = age >= 18
if is_adult:
    print("Este adult!")
else:
    print("Este minor!")

#===========================================
import math

radius = float(input("Raza cercului:"))
area = math.pi * (radius ** 2)
print(f"Aria cercului este: {area}")

number = int(input("Alege un numar: "))
if number % 2 == 0:
    print("Este par!")
else:
    print("Este impar!")

#==========================================
nota = int(input("Nota: "))

if nota >= 9:
    print("Excellent!")
elif nota >= 7:
    print("Good!")
elif nota >= 3:
    print("Pass!")
else:
    print("Fail!")
#=====================================
for i in range(10):
    print(i, end = " ")
print()

for i in range(1,100):
    print(i,end = " ")
    if i % 10 == 0:
        print()
print()
'''
n = int(input("Alege un numar de elemente:"))

numere = list()
#print("Lista de numere:\n", numere)
suma = 0
for i in range(n):
    x = int(input(f"Elementul {i + 1}: "))
    suma = suma + x
    numere.append(x)

print("Lista de numere:\n", numere)
print("Media:",suma// len(numere))