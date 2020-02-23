"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        ans1 = []
        ans1.append(1)
        ans1.append(10)

        c = 9

        if n > 10:
            n = 10
        for i in range(2, n + 1):
            ans1.append((ans1[-1] - ans1[-2]) * c + ans1[-1])
            c = c - 1

        return ans1[-1]

