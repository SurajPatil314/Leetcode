"""
https://leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

class Solution:

    def numTrees(self, n: int) -> int:
        arr = [0] * (n + 1)

        if n < 2:
            return 1

        if n == 2:
            return 2

        if n == 3:
            return 5

        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        arr[3] = 5

        def rec(k: int) -> int:
            ans = 0
            i1 = 0
            i2 = k
            while (i2 > 0):
                ans = ans + (arr[i1] * arr[i2 - 1])
                i1 += 1
                i2 -= 1

            return ans

        for i in range(4, n + 1):
            arr[i] = rec(i)

        return arr[n]









