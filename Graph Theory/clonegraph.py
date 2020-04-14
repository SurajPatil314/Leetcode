"""
# Definition for a Node.
https://leetcode.com/problems/clone-graph/submissions/
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        qu = []
        nodeq = {}

        qu.append(node)

        while len(qu) > 0:

            qu1 = qu.pop(0)

            if qu1.val not in nodeq:
                nodeq[qu1.val] = Node(qu1.val)

            for j in qu1.neighbors:
                if j.val not in nodeq:
                    nodeq[j.val] = Node(j.val)
                    qu.append(j)
                nodeq[qu1.val].neighbors.append(nodeq[j.val])

        return nodeq[1]