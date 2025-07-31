s = ['1','2','3','4']

result = list(map(int,s))
sq = list(map(lambda x: x ** 2, result))
print(sq)

nums = [5, 12, 7, 18, 2]
result = list(filter(lambda x: x > 10,nums))
print(result)

f = ['3.14', '2.71', '0.577']
result = list(map(float,f))
print(result)

i = [10, 15, 255]
result = list(map(hex,i))
print(result)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
result1 = list(map(lambda x: x * 2, result))
print(result1)

names = ['Alice', '', 'BOB', 'charlie', '']
result = list(filter(None,names))
result1 = list(map(str.lower,result))
print(result1)

from functools import reduce
nums = [1, 2, 3, 4]

result = reduce(lambda x,y: x * y,nums)
print(result)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0,nums))
result1 = list(map(lambda x: x ** 2, result))
result2 = reduce(lambda x,y: x + y,result1)
print(result2)

s = ['3', '6', '10', '15', '20']
result = list(map(int,s))
result1 = list(filter(lambda x: x % 3 == 0, result))
result2 = reduce(lambda x,y: x + y, result1)
print(result2)

names = ['Ana', 'Ion', 'Elena', 'Mihai', 'Al']
result = list(map(str.upper,names))
result1 = list(filter(lambda x: len(x) > 3, result))
print("Names number:",len(result1))
print(result1)