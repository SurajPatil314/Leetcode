"""
Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 3:
            return 0

        l = [True] * (n + 1)
        count = 0
        l[0] = False
        l[1] = False

        for i in range(2, n):
            if l[i]:
                count += 1
            for j in range(i * i, n, i):
                l[j] = False

        return count