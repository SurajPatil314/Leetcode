"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
 Output the minimum number of steps to get n 'A'
"""

class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1:
            return 0

        for i in range(2, n + 1):
            if n % i == 0:
                temp = self.minSteps(int(n / i))
                break

        ans = 1 + temp + (i - 1)
        return ans