"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        qw = {}
        ans = ''

        if len(s) < 2:
            return s

        for i in s:
            if i in qw:
                qw[i] = qw.get(i) + 1
            else:
                qw[i] = 1

        qw1 = sorted(qw.items(), key=lambda x: x[1], reverse=True)

        for i in qw1:
            temp = i[0] * i[1]
            ans = ans + temp

        return ans

