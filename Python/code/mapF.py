s = ['1','2','3','4']
result = map(int,s)
print(list(result))

result = map(float,s)
print(list(result))

i = [1, 2, 3, 4]
result = map(str,i)
print(list(result))

result = map(hex,i)
print(list(result))

def doubleNumber(value: int) -> int:
    return value * 2

result = list(map(doubleNumber,i))
print(result)

result = list(map(lambda x: x * 2,i))
print(result)

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x,y: x + y,a,b))
print(result)

fruits = ['apples', 'banana', 'peach', 'lemon', 'cherry']
result = list(map(str.upper,fruits))
print(result)

result = list(map(lambda word: word[0],fruits))
print(result)

s = ['  hello  ', '  world ', ' python  ']
result = list(map(str.strip,s)) # strip is for to remove the space between the space
print(result)

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c* 9/5) + 32, celsius))
print(fahrenheit)