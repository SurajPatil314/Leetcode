"""
https://leetcode.com/problems/shuffle-the-array/

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        selected = nums[n]
        i = 0
        while (n < len(nums) - 1):
            del nums[n]
            nums.insert(i + 1, selected)
            n = n + 1
            i = i + 2
            selected = nums[n]

        return nums

