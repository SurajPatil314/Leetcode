"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
 length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def hight(self, root1: TreeNode) -> int:
        if root1 == None:
            return 0

        lhight = self.hight(root1.left)
        rright = self.hight(root1.right)

        if (lhight > rright):
            h = lhight + 1
        else:
            h = rright + 1

        return h

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if root == None:
            return 0

        lhight1 = self.hight(root.left)
        rright1 = self.hight(root.right)

        ldimeter = self.diameterOfBinaryTree(root.left)
        rdimeter = self.diameterOfBinaryTree(root.right)

        return max((lhight1 + rright1), max(ldimeter, rdimeter))
