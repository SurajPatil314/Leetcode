"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()

        if len(nums) == 0:
            return -1

        if nums[-1] == 0:
            return -1

        for i in range(1, nums[-1] + 1):
            count = 0
            j = 0
            while (count <= i + 1) and j < len(nums):
                if nums[j] >= i:
                    count += 1
                j += 1

            if count == i:
                return i

        return -1

