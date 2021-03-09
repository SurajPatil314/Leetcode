"""
https://leetcode.com/problems/rearrange-spaces-between-words/

You are given a string text of words that are placed among some number of spaces. Each word consists of one or more
lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is
 maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned
  string should be the same length as text.

Return the string after rearranging the spaces.
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:

        totalspace = 0
        nword = 0
        s = False
        qw = []
        qw = text.split()
        for i in text:
            if i == ' ':
                totalspace += 1

        lastspace = 0
        finalspace = 0
        if len(qw) > 1:
            finalspace = int(totalspace / (len(qw) - 1))
            lastspace = int(totalspace % (len(qw) - 1))
        else:
            lastspace = totalspace
            finalspace = totalspace
        totalspace = totalspace - lastspace

        df = ''

        for i in range(finalspace):
            df = df + ' '

        if len(qw) == 1:
            if lastspace > 0:
                ans = qw[0] + df
                return ans
            else:
                return text

        if totalspace == 0:
            return text

        ans = "" + qw[0]
        del qw[0]

        while (totalspace > 0 and len(qw) > 0):
            ans = ans + df + qw[0]
            del qw[0]
            totalspace = totalspace - finalspace

        if lastspace > 0:
            for i in range(lastspace):
                ans = ans + ' '

        return ans

