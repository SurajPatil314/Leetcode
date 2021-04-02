"""
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0

        if len(s) == 0:
            return True

        if len(t) == 0 or len(s) > len(t):
            return False

        ans = False

        if len(s) == 1:
            if s in t:
                return True
            else:
                return False

        while (i < len(t)):
            if t[i] == s[0]:
                i1 = i + 1
                j = 1

                while (i1 < len(t)):

                    if j == len(s):
                        return True
                    else:
                        if t[i1] == s[j]:
                            i1 += 1
                            j += 1
                        else:
                            i1 += 1

                if j == len(s):
                    return True

            i += 1

        return False

