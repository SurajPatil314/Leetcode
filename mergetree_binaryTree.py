"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
 are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 == None and t2 == None:
            return None

        if t1 == None:
            return t2
        if t2 == None:
            return t1

        leftval = self.mergeTrees(t1.left, t2.left)

        if leftval != None:
            if t1.left == None:
                t1.left = leftval

        rightval = self.mergeTrees(t1.right, t2.right)

        if rightval != None:
            if t1.right == None:
                t1.right = rightval

        t1.val = t1.val + t2.val

        return t1




