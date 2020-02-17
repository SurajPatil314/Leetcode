"""
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.ans = 0
        if not root:
            return 0

        def path(root: TreeNode):

            left = 0
            right = 0
            if not root:
                return 0

            if (root.left != None):
                if (root.left.val == root.val):
                    left = path(root.left)
                else:
                    path(root.left)

            if (root.right != None):
                if (root.right.val == root.val):
                    right = path(root.right)
                else:
                    path(root.right)

            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        path(root)
        return self.ans




