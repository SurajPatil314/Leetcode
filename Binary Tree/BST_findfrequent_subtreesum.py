
"""
https://leetcode.com/problems/most-frequent-subtree-sum/


Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as
 the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the
  most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        if root == None:
            return None

        if root.left == None and root.right == None:
            return [root.val]

        sum1 = 0
        sum11 = 0
        sum22 = 0
        sum12 = self.subtree(root.left, sum1, sum11, sum22)
        sum123 = self.subtree(root.right, sum1, sum11, sum22)

        self.ans.append(sum12 + sum123 + root.val)

        # print(self.ans)
        ans1 = {}

        for i in self.ans:
            if i in ans1:
                ans1[i] = ans1.get(i) + 1
            else:
                ans1[i] = 1

        sord = sorted(ans1.items(), key=lambda x: x[1])
        # print(sord)
        ans2 = []
        temp = 0
        for i in range(len(sord) - 1, -1, -1):
            if i == len(sord) - 1:
                ans2.append(sord[i][0])
                temp = sord[i][1]
            else:
                if temp == sord[i][1]:
                    ans2.append(sord[i][0])
                else:
                    break

        return ans2

    def subtree(self, root1, sum1, sum11, sum22) -> int:

        if root1.left == None and root1.right == None:
            self.ans.append(root1.val)
            return root1.val

        else:

            sum111 = self.subtree(root1.left, sum1, sum11, sum22)
            sum222 = self.subtree(root1.right, sum1, sum11, sum22)
            # sum11 = sum111+root1.val
            # sum22 = sum222+root1.val
            self.ans.append(sum111 + sum222 + root1.val)
            '''
            print('!!!')
            print(root1.val)
            print(sum111)
            print(sum222)
            '''

            return (sum111 + sum222 + root1.val)



