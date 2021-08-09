"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        prute = []
        qrute = []

        def lca(p, w):
            nonlocal prute, qrute

            if p.parent == p or p.parent == None:
                if w == 0:
                    prute.append(p)
                else:
                    qrute.append(p)
                return
            else:
                if w == 0:
                    prute.append(p)
                else:
                    qrute.append(p)
                lca(p.parent, w)
                return

        lca(p, 0)
        lca(q, 1)

        for i in range(len(prute)):
            if prute[i] in qrute:
                return prute[i]
