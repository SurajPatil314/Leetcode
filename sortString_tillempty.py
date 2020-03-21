'''
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
'''

class Solution:
    def sortString(self, s: str) -> str:
        ans = ''

        a1 = ''.join(sorted(s))
        a2 = a1[::-1]

        q1 = []
        q2 = []

        for i in a1:
            if i not in q1:
                q1.append(i)
        for i in a2:
            if i not in q2:
                q2.append(i)

        reverse = 0
        e1 = 0
        e2 = 0
        while len(s) > 0:
            if reverse == 0:
                for i in range(len(q1)):
                    if len(s) == 0:
                        break
                    else:
                        if q1[i] in s:
                            ans = ans + q1[i]
                            s = s.replace(q1[i], '', 1)

                reverse = 1
            else:
                for i in range(len(q2)):
                    if len(s) == 0:
                        break
                    else:
                        if q2[i] in s:
                            ans = ans + q2[i]
                            s = s.replace(q2[i], '', 1)
                reverse = 0

        return ans








