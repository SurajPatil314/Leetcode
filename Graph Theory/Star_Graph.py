"""
https://leetcode.com/problems/find-center-of-star-graph/

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one
 center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes
 ui and vi. Return the center of the given star graph.
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        qw = defaultdict(int)

        high = 0

        for i in edges:
            if i[0] > high:
                high = i[0]
            if i[1] > high:
                high = i[1]
            qw[i[1]] = qw[i[1]] + 1
            qw[i[0]] = qw[i[0]] + 1

        for i, j in qw.items():
            if j == high - 1:
                return i
