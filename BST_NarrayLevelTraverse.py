"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/


Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root == None:
            return None

        ans = []

        if root.children == None:
            ans.append([root.val])
            return ans

        sta = []
        sta.append(root)

        sta1 = []

        temp1 = []
        temp2 = []

        while len(sta) > 0 or len(sta1) > 0:

            temp1 = []
            while len(sta) > 0:
                qw = sta.pop(0)
                temp1.append(qw.val)

                if qw.children != None:
                    for i in qw.children:
                        sta1.append(i)

            if len(temp1) > 0:
                ans.append(temp1)

            temp2 = []
            while len(sta1) > 0:
                qw = sta1.pop(0)
                temp2.append(qw.val)

                if qw.children != None:
                    for i in qw.children:
                        sta.append(i)

            if len(temp2) > 0:
                ans.append(temp2)

        return ans


