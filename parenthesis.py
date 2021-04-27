"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def rec(ans, ban, limit, loop, n):

            if limit == n:

                if loop > 0:
                    for i in range(loop):
                        ban = ban + ')'

                if ban not in ans:
                    ans.append(ban)
                return

            else:

                if loop > 0:
                    rec(ans, ban + ')', limit, loop - 1, n)
                    rec(ans, ban + '(', limit + 1, loop + 1, n)
                else:

                    ban = ban + '('

                    rec(ans, ban, limit + 1, loop + 1, n)

                return

        rec(ans, '', 0, 0, n)
        return ans
