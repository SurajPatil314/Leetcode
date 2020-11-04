"""
https://leetcode.com/problems/increasing-order-search-tree/

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        qw = []
        we = 0

        def inorder(root1):
            if root1 == None:
                return
            inorder(root1.left)
            qw.append(root1.val)
            inorder(root1.right)

        inorder(root)

        root2 = TreeNode(sys.maxsize, None, None)
        root3 = root2

        while (len(qw) > 0):
            if root2.val == sys.maxsize:
                root2.val = qw[0]
                del qw[0]
                root3 = root2
            else:
                root4 = TreeNode(qw[0])
                root3.right = root4
                root3 = root3.right
                del qw[0]

        return root2



