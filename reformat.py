"""
https://leetcode.com/problems/reformat-the-string/submissions/

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by
another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""

class Solution:
    def reformat(self, s: str) -> str:
        ans = ''
        chara = []
        inti = []

        if len(s) < 2:
            return s
        for i in s:
            if i.isdigit():
                inti.append(str(i))
            else:
                chara.append(str(i))

        if len(chara) == 0 or len(inti) == 0:
            return ans

        if len(chara) > len(inti):

            j1 = 0
            j2 = 0
            turn = 0
            while (j2 < len(inti) + 1):
                if turn == 0:
                    if j1 < len(chara):
                        ans = ans + chara[j1]
                    j1 = j1 + 1
                    turn = 1
                else:
                    if j2 < len(inti):
                        ans = ans + inti[j2]
                    j2 = j2 + 1
                    turn = 0




        else:

            j1 = 0
            j2 = 0
            turn = 0
            while (j2 < len(chara) + 1):
                if turn == 0:
                    if j1 < len(inti):
                        ans = ans + inti[j1]
                    j1 = j1 + 1
                    turn = 1
                else:
                    if j2 < len(chara):
                        ans = ans + chara[j2]
                    j2 = j2 + 1
                    turn = 0

        return ans

