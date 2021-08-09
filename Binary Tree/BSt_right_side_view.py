"""
https://leetcode.com/problems/binary-tree-right-side-view/


Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if root == None:
            return None

        level = 1
        levelcheck = []
        ls = []
        ls.append(root)

        while (True):

            if len(ls) == 0:
                break
            i1 = 0
            while (i1 < len(ls)):
                qs = ls[i1]

                if qs.right != None:
                    levelcheck.append(qs.right)

                if qs.left != None:
                    levelcheck.append(qs.left)

                i1 += 1

            if len(ls) > 0:
                ans.append(ls[0].val)

            ls = []

            i2 = 0
            while (i2 < len(levelcheck)):
                qs = levelcheck[i2]

                if qs.right != None:
                    ls.append(qs.right)

                if qs.left != None:
                    ls.append(qs.left)

                i2 += 1

            if len(levelcheck) > 0:
                ans.append(levelcheck[0].val)

            levelcheck = []

        return ans



