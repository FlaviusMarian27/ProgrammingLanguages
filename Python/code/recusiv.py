def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial:",factorial(5)) 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci:",fibonacci(10))     

def sumPar(n):
    if n == 0:
        return 0
    last_digit = n % 10
    if last_digit % 2 == 0:
        return last_digit + sumPar(n // 10)
    else:
        return sumPar(n // 10)

print("Suma:", sumPar(789))