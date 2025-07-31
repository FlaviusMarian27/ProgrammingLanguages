from functools import reduce

def add(x: int, y: int) -> int:
    return x + y

a = [1,2,3,4,5]
result = reduce(add,a)
print(result)

result = reduce(lambda x,y: x + y, a)
print(result)

import functools
import operator

a = [1,3,5,6,2]
print(functools.reduce(operator.add,a))

print(functools.reduce(operator.mul,a))

print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

from itertools import accumulate
from operator import add

# Cumulative sum with accumulate
a = [1, 2, 3, 4, 5]
res = accumulate(a, add)

print(list(res))