'''
Here two integers a and b are given. The given input and its values 
are passed as arguments to the function argumentFunction. The argumentFunction 
is responsible to return (a+b). You need to write this function.

Examples:
Input: a = 2, b = 3
Output: 5
Explanation: 2 + 3 = 5
'''
def argumentFunction(a: int, b: int) -> int:
    return a + b 

a = int(input())
b = int(input())
result = argumentFunction(a,b)
print("Result:", result)