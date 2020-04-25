"""
https://leetcode.com/problems/count-complete-tree-nodes/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0

    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        self.inorder(root)
        return self.count

    def inorder(self, root1):
        if root1 == None:
            return None

        self.inorder(root1.left)
        self.count += 1
        self.inorder(root1.right)



