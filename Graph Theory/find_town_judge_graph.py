"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        jud = dict()

        qw = []

        if N == 0:
            return -1
        if N == 1:
            return 1

        for i in trust:
            if i[0] not in qw:
                qw.append(i[0])
            if i[1] not in qw:
                qw.append(i[1])

            if i[0] not in jud:
                jud[i[0]] = []
            jud[i[0]].append(i[1])

        ass = 0
        ans = -1

        for i in qw:
            print(i)
            print('%%%')
            if i in jud:
                continue

            qww = 0

            for k, v in jud.items():
                if ass == 1:
                    ass = 2
                    break
                if i in v:
                    qww = 1
                else:
                    qww = 0
                    break

            if qww == 1:
                ans = i
                ass = 1

            if ass == 2:
                break

        if ans == -1:
            return -1
        else:
            if ass == 1:
                return ans
            else:
                return -1



