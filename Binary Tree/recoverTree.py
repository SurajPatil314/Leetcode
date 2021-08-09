"""
https://leetcode.com/problems/recover-binary-search-tree/

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake.
 Recover the tree without changing its structure.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found = 0

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root1):
            nonlocal x, y, prev

            if root1 == None:
                return

            inorder(root1.left)
            if prev and root1.val < prev.val:
                y = root1

                if x is None:
                    x = prev
                else:
                    return

            prev = root1
            inorder(root1.right)

        x = y = prev = None
        inorder(root)
        x.val, y.val = y.val, x.val
