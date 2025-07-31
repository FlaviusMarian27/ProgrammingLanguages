s1 = 'John is 20 years old!'

s2 = lambda func: func.upper()
print(s2(s1))

x = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(x(7))
print(x(-4))
print(x(0))

# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

x = lambda x,y: (x + y,x * y, x // y)
print(x(8,4))

#filter() function - for filter out all elements of sequence
l = [2,5,8,18,12,3,9,4]
even = filter(lambda x: x % 2 == 0, l)
print(list(even))

#map()
l = [1,2,3,4]
power = map(lambda x: x ** 2, l)
print(list(power))

from functools import reduce
l = [1,2,3,4]
x = reduce(lambda x,y: x * y,l)
print(x)