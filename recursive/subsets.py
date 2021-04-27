"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        if len(nums) == 0:
            return [[]]

        def rec(pointer, nums, li):

            if pointer == len(nums):
                if li not in ans:
                    ans.append(li)
                return

            else:

                rec(pointer + 1, nums, li)
                rec(pointer + 1, nums, li + [nums[pointer]])

                return

        li = list()
        rec(0, nums, li)

        return ans
