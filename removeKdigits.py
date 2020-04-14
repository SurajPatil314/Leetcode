"""
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        res = []

        for i in num:
            while res and res[-1] > i and k > 0:
                k = k - 1
                res.pop()

                if k == 0:
                    break

            res.append(i)

            if len(res) == 1 and i == '0' and k >= 0:
                res.pop()

        if not res:
            return '0'

        if k > 0:
            ans = res[:-k]
            if ans:
                return ''.join(ans)
            else:
                return '0'

        return ''.join(res)
