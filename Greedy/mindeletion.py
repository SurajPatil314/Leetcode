"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string
 "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        qw = defaultdict(int)
        qw1 = []
        ans = 0

        for i in s:
            qw[i] = qw[i] + 1

        for i, j in qw.items():
            if j in qw1:
                j1 = j
                while True:
                    if j1 in qw1:
                        ans += 1
                        j1 -= 1
                    elif j1 == 0:
                        break
                    elif j1 not in qw1:
                        qw1.append(j1)
                        break

            else:
                qw1.append(j)

        return ans
