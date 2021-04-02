"""
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dm = {}

        np = 1

        for i in range(len(gas)):
            if gas[i] - cost[i] > -1:
                dm[i] = gas[i] - cost[i]
                np = 0

        if np == 1:
            return -1

        dm1 = dict(sorted(dm.items(), key=lambda x: x[1], reverse=True))

        print(dm1)

        for i, j in dm1.items():
            # print(i)
            # print('&&&')

            found = 0
            start = 1

            qw = gas[i]
            i1 = i
            while start <= len(gas):
                if i1 == i:
                    qw = gas[i]
                else:
                    if i1 == len(gas):
                        i1 = 0

                    if i1 == 0:
                        qw = qw - cost[len(cost) - 1] + gas[i1]
                    else:
                        qw = qw - cost[i1 - 1] + gas[i1]

                    if qw < cost[i1]:
                        found = 1
                        print('11')
                        break

                # print(i1)
                # print(qw)
                # print('##')

                start += 1
                i1 += 1

            if found == 0:
                return i

        return -1


