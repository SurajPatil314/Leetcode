"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/


For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        i = 0

        ans = ''
        while i < len(str1) and i < len(str2):

            ans1 = str1[:i + 1]

            if len(str1) % len(ans1) == 0 and len(str2) % len(ans1) == 0:
                if ans1 * int(len(str1) / len(ans1)) == str1 and ans1 * int(len(str2) / len(ans1)) == str2:
                    if len(ans) < len(ans1):
                        ans = ans1

                i += 1
            else:
                i += 1

        return ans
