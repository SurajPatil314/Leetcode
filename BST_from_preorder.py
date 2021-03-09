"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def rec(j, roo2):

            if roo2 == None:
                roo2 = TreeNode(j)
                return
            else:
                if (j > roo2.val):
                    if (roo2.right == None):
                        roo2.right = TreeNode(j)
                        return
                    else:
                        rec(j, roo2.right)

                else:
                    if (roo2.left == None):
                        roo2.left = TreeNode(j)
                        return
                    else:
                        rec(j, roo2.left)

                return

        if len(preorder) > 0:
            roo = TreeNode(preorder[0])

            for i in range(1, len(preorder)):
                roo2 = roo
                rec(preorder[i], roo2)

            return roo





