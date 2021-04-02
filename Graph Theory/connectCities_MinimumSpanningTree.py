"""
https://leetcode.com/problems/connecting-cities-with-minimum-cost/


You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and
city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1)
that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible,
 return -1.
"""


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def find(i: int) -> int:
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]

        if N < 2 or not connections:
            return 0
        connections.sort(key=lambda l: l[2])

        roots = [i for i in range(N + 1)]
        res = 0
        for x, y, v in connections:
            rx, ry = find(x), find(y)
            if rx != ry:
                res += v
                roots[rx] = ry
        return res if len({find(i) for i in range(1, N + 1)}) == 1 else -1
