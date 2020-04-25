"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BS
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.asnl = []
        self.root1 = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.root1:
            node = self.root1
            while (node != None):
                self.asnl.append(node)
                node = node.left

            self.root1 = None

        top = self.asnl.pop()

        if top.right:
            self.root1 = top.right

        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """

        if self.root1 or self.asnl:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()