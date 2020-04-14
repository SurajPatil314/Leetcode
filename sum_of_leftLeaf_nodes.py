"""
https://leetcode.com/problems/sum-of-left-leaves/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans1 = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        self.rec(root)

        return self.ans1

    def rec(self, root1):
        if root1 == None:
            return None
        if root1.left != None and (root1.left.left == None and root1.left.right == None):
            self.ans1 = self.ans1 + root1.left.val

        self.rec(root1.left)
        self.rec(root1.right)

