import math

class Solution:
    def countPrimes(self, n: int) -> int:
        def prime(number: int) -> bool:
            if number == 1 or number == 0:
                return False
            
            for i in range(2,int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
        
        count = 0
        for i in range(2,n):    
            if prime(i) == True:
                count = count + 1
        return count
    
sol = Solution()
print(sol.countPrimes(10))