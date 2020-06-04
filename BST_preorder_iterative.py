# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        qw = []
        qw.append(root)

        while (len(qw) > 0):
            zx = qw.pop(0)

            ans.append(zx.val)

            if zx.left:
                qw.insert(0, zx.left)
            if zx.right:
                if not zx.left:
                    qw.insert(0, zx.right)
                else:
                    qw.insert(1, zx.right)

        return ans
