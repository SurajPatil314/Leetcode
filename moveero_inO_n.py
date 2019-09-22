'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = len(nums)

        if len(nums) > 1:

            while (i < j - 1):
                if nums[i] == 0:
                    del nums[i]
                    nums.append(0)
                    j = j - 1
                else:
                    i = i + 1


