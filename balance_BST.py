'''
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        if root == None:
            return root

        li = []

        self.inorder(root, li)  # create sorted list using inorder traversal
        le = len(li)
        ana = self.buildBST(li, 0, le - 1)
        return ana

    def inorder(self, root1, li):
        if root1 == None:
            return None
        self.inorder(root1.left, li)
        li.append(root1)
        self.inorder(root1.right, li)

    def buildBST(self, li, mina, maxa):
        if mina > maxa:  # base case
            return None

        mid = (mina + maxa) // 2
        treenode = li[mid]  # Get the middle element and make it root

        treenode.left = self.buildBST(li, mina, mid - 1)
        treenode.right = self.buildBST(li, mid + 1, maxa)

        return treenode