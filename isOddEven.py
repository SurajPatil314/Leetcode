"""
'https://leetcode.com/problems/even-odd-tree/'
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:

        qw = []

        if root.left == None and root.right == None:
            if root.val % 2 == 0:
                return False
            return True

        qw.append(root)

        ans = True

        qw1 = []

        while (len(qw) > 0 or len(qw1) > 0):

            while (len(qw) > 0):
                for i in range(len(qw)):
                    if qw[i].val % 2 == 0:
                        return False
                    if i > 0:
                        if qw[i - 1].val >= qw[i].val:
                            return False

                    if qw[i].left != None:
                        qw1.append(qw[i].left)
                    if qw[i].right != None:
                        qw1.append(qw[i].right)

                qw.clear()

            while (len(qw1) > 0):
                for i in range(len(qw1)):
                    if qw1[i].val % 2 == 1:
                        return False
                    if i > 0:
                        if qw1[i - 1].val <= qw1[i].val:
                            return False

                    if qw1[i].left != None:
                        qw.append(qw1[i].left)
                    if qw1[i].right != None:
                        qw.append(qw1[i].right)

                qw1.clear()

        return ans
