# Definition for a binary tree node.
"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.


"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        t1 = []
        t2 = []

        ans = []

        if root1 != None:
            t1.append(root1)

        if root2 != None:
            t2.append(root2)

        while (len(t1) > 0 or len(t2) > 0):

            while (len(t1) > 0):
                qw1 = t1[-1]
                del t1[-1]
                ans.append(qw1.val)
                if qw1.left != None:
                    t1.append(qw1.left)
                if qw1.right != None:
                    t1.append(qw1.right)

            while (len(t2) > 0):
                qw2 = t2[-1]
                del t2[-1]
                ans.append(qw2.val)
                if qw2.left != None:
                    t2.append(qw2.left)
                if qw2.right != None:
                    t2.append(qw2.right)

        if len(ans) > 0:
            ans.sort()

        return ans