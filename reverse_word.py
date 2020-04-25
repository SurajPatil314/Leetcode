"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""


class Solution:
    def reverseWords(self, s: str) -> str:

        i = len(s) - 1

        qw = s.split(' ')
        print(qw)

        ans = ''
        q = 0
        for i in qw:
            i1 = i[::-1]
            if q == 0:
                ans = ans + i1
            else:
                ans = ans + ' ' + i1
            q += 1

        return ans
