"""
https://leetcode.com/problems/product-of-array-except-self/


Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numzero = 0

        qw = 0
        nz = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if nz == 0:
                    qw = nums[i]
                    nz = 1
                else:
                    qw = qw * nums[i]

            else:
                numzero += 1

        ans = []

        if qw == 0:
            ans = [0] * len(nums)
            return ans

        for i in range(len(nums)):

            if numzero > 1:
                ans.append(0)
            elif numzero == 1:
                if nums[i] == 0:
                    ans.append(qw)
                else:
                    ans.append(0)
            else:
                ans.append(int(qw / nums[i]))

        return ans

