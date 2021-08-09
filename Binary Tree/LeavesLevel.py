"""
https://leetcode.com/problems/find-leaves-of-binary-tree/

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        qw = defaultdict(list)

        def rec(root1, pos):

            if root1.left == None and root1.right == None:
                qw[0].append(root1.val)
                return 0

            pos1 = -1
            pos2 = -1
            if root1.left:
                pos1 = rec(root1.left, pos)
            if root1.right:
                pos2 = rec(root1.right, pos)

            pos3 = max(pos1, pos2)
            pos3 += 1

            qw[pos3].append(root1.val)

            return pos3

        rec(root, 0)
        ans = []
        for i, j in qw.items():
            ans.append(j)

        return ans

