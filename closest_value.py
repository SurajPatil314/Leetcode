"""
https://leetcode.com/problems/closest-binary-search-tree-value/


Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = sys.maxsize
    ans1 = None

    def closestValue(self, root: TreeNode, target: float) -> int:

        if root.left == None and root.right == None:
            return root.val

        def trav(root1, target):

            if root1.left == None and root1.right == None:
                if abs(root1.val - target) < self.ans:
                    self.ans = abs(root1.val - target)
                    self.ans1 = root1.val
                    return

                return

            else:
                if abs(root1.val - target) < self.ans:
                    self.ans = abs(root1.val - target)
                    self.ans1 = root1.val

                if root1.left:
                    trav(root1.left, target)

                if root1.right:
                    trav(root1.right, target)

                return

        trav(root, target)

        return self.ans1






