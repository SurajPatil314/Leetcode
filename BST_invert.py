# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root == None:
            return root

        def conv(root1):
            if root1:
                temp = root1.left
                root1.left = root1.right
                root1.right = temp
                conv(root1.left)
                conv(root1.right)

        conv(root)

        return root


