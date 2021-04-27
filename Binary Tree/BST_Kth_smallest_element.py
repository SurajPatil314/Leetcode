"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/


Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        if root == None:
            return None
        ans = []

        def inorder(root1):

            if root1 == None:
                return None

            else:
                inorder(root1.left)
                ans.append(root1.val)
                inorder(root1.right)

        inorder(root)
        print(ans)
        return ans[k - 1]



