"""
https://leetcode.com/problems/arithmetic-subarrays/

You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        ans = []

        for i in range(len(l)):
            qw = nums[l[i]:r[i] + 1]

            qw.sort()

            if len(qw) > 1:
                er = qw[1] - qw[0]
                temp = True
                for j in range(len(qw)):
                    if j > 0:
                        if qw[j] - qw[j - 1] != er:
                            temp = False
                            break

                if temp == True:
                    ans.append(True)
                else:
                    ans.append(False)


            else:
                ans.append(True)

        return ans
