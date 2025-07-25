class Solution:
    def series(self, n):
        if n == 0:
            return 0
        else:
            fib = [0,1]
            for i in range(2,n + 1):
                next_value = fib[i-1] + fib[i-2]
                fib.append(next_value)
        return fib
    
sol = Solution()
print(sol.series(5))