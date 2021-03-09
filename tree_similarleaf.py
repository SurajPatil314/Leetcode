"""
https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ans1 = []
        ans2 = []

        def findleaf(root3, tree):
            if root3.left == None and root3.right == None:
                if tree == 1:
                    ans1.append(root3.val)
                else:
                    ans2.append(root3.val)
            else:
                if root3.left != None:
                    findleaf(root3.left, tree)
                if root3.right != None:
                    findleaf(root3.right, tree)

        findleaf(root1, 1)
        findleaf(root2, 2)

        if ans1 == ans2:
            return True
        else:
            return False





