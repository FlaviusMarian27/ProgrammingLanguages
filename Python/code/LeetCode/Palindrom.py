class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        inv = 0
        while number > 0:
            inv = inv * 10 + number % 10
            number = number // 10
        
        if x == inv:
            return True
        else:
            return False
        
sol = Solution()
x = 127
print("Result:",sol.isPalindrome(x))