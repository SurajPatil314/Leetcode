"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        def ispal(l, r):

            while (l < r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        l = 0
        r = len(s) - 1
        while (l < r):

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if ispal(l + 1, r) or ispal(l, r - 1):
                    return True
                else:
                    return False

        return False
