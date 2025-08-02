class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(number: int) -> int:
            suma = 0
            while number != 0:
                digit = number % 10
                suma = suma + digit ** 2
                number = number // 10
            return suma
        
        result = sumDigits(n)
        while result != 1:
            if result == 2 or result == 4:
                    return False
            else:
                result = sumDigits(result)
        return True
        
sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(91))