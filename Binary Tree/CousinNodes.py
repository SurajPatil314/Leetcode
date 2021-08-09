"""
https://leetcode.com/problems/cousins-in-binary-tree/


In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        qw = []
        qw2 = []

        qw.append(root)
        qw2.append(root.val)

        while (len(qw) > 0):
            qw1 = []
            qw22 = []
            qw222 = {}

            while (len(qw) > 0):
                qw11 = qw.pop(0)

                if qw11.left != None:
                    qw1.append(qw11.left)
                    qw22.append(qw11.left.val)
                    qw222[qw11.left.val] = qw11.val
                if qw11.right != None:
                    qw1.append(qw11.right)
                    qw22.append(qw11.right.val)
                    qw222[qw11.right.val] = qw11.val

            if x in qw22 and y in qw22:
                if qw222[x] == qw222[y]:
                    return False
                else:
                    return True

            if x in qw22:
                return False
            if y in qw22:
                return False

            qw = qw1

        return False
