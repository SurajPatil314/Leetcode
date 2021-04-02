"""
https://leetcode.com/problems/maximum-average-subtree/

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:

        def subtree(root1, ele):
            if root1 == None:
                return [0, 0]

            if root1.left == None and root1.right == None:
                if root1.val > self.ans:
                    self.ans = root1.val / 1
                return [root1.val, 1]

            qw1 = subtree(root1.left, [0, 0])
            qw2 = subtree(root1.right, [0, 0])

            qw3 = (qw1[0] + qw2[0] + root1.val) / (qw1[1] + qw2[1] + 1)
            if qw3 > self.ans:
                self.ans = qw3

            return [qw1[0] + qw2[0] + root1.val, qw1[1] + qw2[1] + 1]

        subtree(root, [0, 0])

        return self.ans
