class Solution:
    def reverseexponentiation(self, n):
        def invNumber(number):
            inv = 0
            while number != 0:
                inv = inv * 10 + number%10
                number = number // 10
            return inv
        result = invNumber(n)
        return int(n**result)
    
n = int(input("Alege un numar:"))
sol = Solution()
print("Result:",sol.reverseexponentiation(n))