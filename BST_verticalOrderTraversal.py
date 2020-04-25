"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return None

        ans = defaultdict(list)
        ans1 = []

        def helper(root1, vl, lev, ans):
            if not root1:
                return None

            ans[vl].append((lev, root1.val))
            helper(root1.left, vl - 1, lev + 1, ans)
            helper(root1.right, vl + 1, lev + 1, ans)

        helper(root, 0, 0, ans)

        for j in sorted(ans.keys()):
            temp = []
            print(ans[j])
            print(sorted(ans[j]))
            for j1 in sorted(ans[j]):
                temp.append(j1[1])

            ans1.append(temp)

        return ans1

