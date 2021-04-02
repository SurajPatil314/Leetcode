"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


"""

from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        qw = defaultdict(list)
        qw1 = defaultdict(list)

        if N == 1 and len(trust) == 0:
            return 1

        for i in trust:
            qw[i[1]].append(i[0])
            qw1[i[0]].append(i[1])

        ans = []
        for i, j in qw.items():
            if len(j) == N - 1:
                ans.append(i)
        for i in ans:
            if len(qw1[i]) == 0:
                return i

        return -1


