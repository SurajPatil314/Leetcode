v"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
 to left for the next level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root == None:
            return None

        ans = []
        if root.left == None and root.right == None:
            ans.append([root.val])
            return ans

        qw = []
        qw.append(root)
        qw1 = []
        ans1 = []
        ans2 = []
        while(len(qw)>0 or len(qw1)>0):
            left = 1
            ans1 = []
            ans2 = []
            while(len(qw)>0):
                zx = qw.pop(0)
                ans1.append(zx.val)
                if zx.left:
                    qw1.append(zx.left)
                if zx.right:
                    qw1.append(zx.right)


            if len(ans1)>0:
                ans.append(ans1)



            while(len(qw1)>0):
                zx = qw1.pop(0)
                ans2.append(zx.val)
                if zx.left:
                    qw.append(zx.left)
                if zx.right:
                    qw.append(zx.right)

            ans2.reverse()


            if len(ans2)>0:
                ans.append(ans2)

        return ans

