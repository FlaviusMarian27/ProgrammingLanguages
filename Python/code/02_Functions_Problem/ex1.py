'''
Here one integer n is given. You need to write the complete function 
returnValueFunction that takes n as a parameter and uses the return 
keyword to return double the value of n.

Examples:
Input: n = 2
Output: 4
Explanation: 2 * 2 = 4

Constraints:
1 ≤ n ≤ 5
'''
def returnValueFunction(n):
    return 2 * n

n = int(input())
if 1 > n or n > 5:
    print("Numar invalid!")
else:
    print(returnValueFunction(n))
