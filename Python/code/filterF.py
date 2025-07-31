def even(n: int) -> int:
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
result = list(filter(even,a))
print(result)

b = list(filter(lambda x: x % 2 == 0,a)) #for the filter
print(b)

c = list(map(lambda x: x * 2,b)) #for operations
print(c)

