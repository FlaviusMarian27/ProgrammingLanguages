class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(number: int) -> bool:
            if number <= 0:
                return False
            
            while number != 1:
                if number % 2 == 0:
                    number = number // 2
                elif number % 3 == 0:
                    number = number // 3
                elif number % 5 == 0:
                    number = number // 5
                else:
                    return False
            return True
        
        count = 0
        number = 1
        while count < n:
            if isUgly(number):
                count = count + 1
            number = number + 1
            
        return number - 1
    
sol = Solution()
print(sol.nthUglyNumber(10))