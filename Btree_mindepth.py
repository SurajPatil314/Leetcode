"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        if root.left == None:
            ans = self.rec(root.right)
            return ans + 1

        if root.right == None:
            ans = self.rec(root.left)
            return ans + 1

        ans = self.rec(root)

        return ans

    def rec(self, root1):

        if root1 == None:
            return 0

        ans1 = 0
        ans2 = 0
        ans1 = self.rec(root1.left)

        ans2 = self.rec(root1.right)

        if ans1 != 0 and ans2 != 0:
            return min(ans1, ans2) + 1

        elif ans1 == 0 and ans2 == 0:
            return 1

        elif ans1 != 0:
            return ans1 + 1
        elif ans2 != 0:
            return ans2 + 1





