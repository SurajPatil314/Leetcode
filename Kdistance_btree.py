"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        qw = []

        allv = dict()
        qw.append(root)

        while (len(qw) > 0):
            qw1 = []
            while (len(qw) > 0):
                qw2 = qw.pop(0)
                if qw2 not in allv:
                    qw3 = []
                    if qw2.left:
                        qw3.append(qw2.left)
                        qw1.append(qw2.left)
                    if qw2.right:
                        qw3.append(qw2.right)
                        qw1.append(qw2.right)
                    allv[qw2] = qw3
            qw = qw1

        curlev = 0
        visited = []
        visited.append(target)

        ans = []
        ans.append(target)
        ans11 = []
        ans11.append(target.val)

        while (curlev < K):
            ans2 = []
            ans22 = []
            ans11 = []

            while (len(ans) > 0):
                ans1 = ans.pop(0)
                for i, j in allv.items():
                    if i == ans1:
                        for j1 in j:
                            if j1 not in visited:
                                visited.append(j1)
                                ans2.append(j1)
                                ans22.append(j1.val)
                        break

                for i, j in allv.items():
                    u1 = 0
                    for j1 in j:
                        if j1 == ans1:
                            if i not in visited:
                                visited.append(i)
                                ans2.append(i)
                                ans22.append(i.val)
                            u1 = 1
                            break
                    if u1 == 1:
                        break
            ans = ans2
            ans11 = ans22
            curlev += 1

        return ans11

