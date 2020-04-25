"""
https://leetcode.com/problems/push-dominoes/
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        org = []
        org1 = []

        i = 0
        av = 0
        for i1 in dominoes:
            org.append(i1)
            if i1 == 'L' or i1 == 'R':
                av = 1

        if av == 0:
            return dominoes

        while i < len(org):

            if org[i] == '.':
                fl = i
                fr = i
                wo = '.'
                l = 0
                r = 0
                while (fl >= 0 and fr < len(org)):
                    print(dominoes[i])

                    if dominoes[fl] == 'L':
                        l = 2
                    if dominoes[fl] == 'R':
                        l = 1

                    if dominoes[fr] == 'R':
                        r = 2
                    if dominoes[fr] == 'L':
                        r = 1

                    if l == 1 and r == 1:
                        wo = '.'
                        break

                    if l == 2 and r == 2:
                        wo = '.'
                        break

                    if l == 1:
                        wo = 'R'
                        break

                    if r == 1:
                        wo = 'L'
                        break

                    if (fl == 0 or l == 2) and (fr == len(org) - 1 or r == 2):
                        break

                    if fl > 0 and l != 2:
                        fl = fl - 1
                    if fr < len(org) - 1 and r != 2:
                        fr = fr + 1

                org[i] = wo

            i += 1

        return ''.join(org)






