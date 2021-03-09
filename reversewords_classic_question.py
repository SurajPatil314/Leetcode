"""
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = s.split()

        s2.reverse()
        s3 = ""
        for i in range(len(s2)):
            if i == len(s2) - 1:
                s3 = s3 + s2[i]
            else:
                s3 = s3 + s2[i] + " "

        return s3
