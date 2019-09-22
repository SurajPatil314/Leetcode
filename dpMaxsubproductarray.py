'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        l = len(nums)

        maxarray = [0] * l
        minarray = [0] * l

        for i in range(0, len(nums)):
            if i == 0:
                maxarray[0] = nums[0]
                minarray[0] = nums[0]
            else:
                a = maxarray[i - 1] * nums[i]
                b = minarray[i - 1] * nums[i]
                c = nums[i]

                maxarray[i] = max(a, b, c)
                minarray[i] = min(a, b, c)

        return max(maxarray)