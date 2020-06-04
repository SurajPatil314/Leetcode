"""

https://leetcode.com/contest/weekly-contest-190/problems/pseudo-palindromic-paths-in-a-binary-tree/

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic
 if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        temppath = []

        def canFormPalindrome(strr):
            listt = []
            for i in range(len(strr)):
                if (strr[i] in listt):
                    listt.remove(strr[i])
                else:
                    listt.append(strr[i])

            if len(strr) % 2 == 0:
                if len(listt) == 0:
                    return True
                else:
                    return False

            else:
                if len(listt) == 1:
                    return True
                else:
                    return False

        def allpath(root1, temppath):

            if root1 == None:
                return

            elif root1.left == None and root1.right == None:
                temppath.append(str(root1.val))

                str1 = ''.join(temppath)
                qw1 = canFormPalindrome(str1)

                if qw1:
                    self.paths += 1

                del temppath[-1]
                return

            else:
                temppath.append(str(root1.val))

                allpath(root1.left, temppath)

                allpath(root1.right, temppath)

                del temppath[-1]

        if root == None:
            return 0

        allpath(root, temppath)

        return self.paths






