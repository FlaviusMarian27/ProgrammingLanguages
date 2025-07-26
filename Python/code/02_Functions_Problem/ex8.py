class Solution:
    def jugglerSequence(self, n):
        lista = [n]
        while True:
            if n == 1:
                break
            if n % 2 == 0:
                n = int(n**0.5)
            else:
                n = int(n**1.5)
            lista.append(n)
        return lista

n = int(input("Alege un numar:"))
sol = Solution()
print(sol.jugglerSequence(n))        