"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
 parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        i1 = 0
        c = 0
        ans = ''
        i2 = 0

        z = []

        for i in s:
            if i.isalpha():
                i1 = 1

            z.append(i)

        while c < len(z):
            if z[c] == '(':
                i2 += 1
                c += 1

            elif z[c] == ')':
                i2 -= 1
                if i2 < 0:
                    del z[c]
                    i2 = 0
                else:
                    c += 1

            else:
                c += 1

        print(i2)
        c = len(z) - 1
        while c >= 0:
            if i2 == 0:
                break
            else:
                if z[c] == '(':
                    del z[c]
                    i2 -= 1
                    c -= 1
                else:
                    c -= 1

        s = ''.join(z)

        return s




