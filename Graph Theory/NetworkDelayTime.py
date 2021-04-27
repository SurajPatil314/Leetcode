"""
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed
edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a
signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is
impossible for all the n nodes to receive the signal, return -1.
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        qw = []

        for i in range(n):
            qw1 = [0] * n
            qw.append(qw1)

        for i in range(len(times)):
            qw[times[i][0] - 1][times[i][1] - 1] = times[i][2]

        lp = []
        lp.append([k, 0])
        lp2 = {}
        lp2[k] = 0
        visited = []
        visited.append(k)

        n1 = 1

        ans = 0

        while (len(lp) > 0):

            lp1 = []

            print(lp)

            while (len(lp) > 0):
                qw1 = lp.pop()
                for i in range(len(qw)):

                    if qw1[0] - 1 != i:
                        if qw[qw1[0] - 1][i] != 0:

                            if (i + 1) not in visited:
                                n1 += 1
                                lp1.append([(i + 1), qw1[1] + qw[qw1[0] - 1][i]])
                                lp2[i + 1] = qw1[1] + qw[qw1[0] - 1][i]
                                visited.append(i + 1)

                            else:
                                n1 += 1
                                if lp2[i + 1] > (qw1[1] + qw[qw1[0] - 1][i]):
                                    lp1.append([(i + 1), qw1[1] + qw[qw1[0] - 1][i]])
                                    lp2[i + 1] = qw1[1] + qw[qw1[0] - 1][i]
                                    lp1.append([(i + 1), qw1[1] + qw[qw1[0] - 1][i]])
                                if ans < (qw1[1] + qw[qw1[0] - 1][i]):
                                    ans = qw1[1] + qw[qw1[0] - 1][i]

            lp = lp1

        if len(visited) >= n:
            ans = lp2[k]
            for i, j in lp2.items():
                if ans < j:
                    ans = j

            return ans
        return -1




