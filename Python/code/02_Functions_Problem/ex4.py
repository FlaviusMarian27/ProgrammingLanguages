def firstDigit(n):
    while n > 9:
        n = n // 10 
    return n

n = int(input("Choose a number:"))
print("First digit is",firstDigit(n))