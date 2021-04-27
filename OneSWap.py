"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        def qw(s, li):
            for i in s:
                li.append(i)

            return li

        i = 0

        s11 = qw(s1, [])
        s22 = qw(s2, [])

        pos = []

        for i in range(len(s11)):
            if s11[i] != s22[i]:
                pos.append(i)

        if len(pos) == 2:
            i1 = pos[0]
            i2 = pos[1]

            s11[i1], s11[i2] = s11[i2], s11[i1]

            if s11 == s22:
                return True
            else:
                return False

        else:
            return False





