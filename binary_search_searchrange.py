'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        rside = -1
        lside = -1

        start = 0
        end = len(nums) - 1
        bell = 0

        mid = start + (end - start) // 2

        if len(nums) == 0:
            return [-1, -1]
        if target < nums[start]:
            return [-1, -1]

        if target > nums[end]:
            return [-1, -1]

        if nums[0] == target:
            lside = 0
        if nums[end] == target:
            rside = end

        if lside == 0 and rside == end:
            return [0, end]

        while (start <= end):

            if bell == 1:
                start = mid
                end = mid
                while (start - 1 >= 0 and nums[start - 1] == target):
                    start -= 1

                while (end + 1 < len(nums) and nums[end + 1] == target):
                    end += 1

                return [start, end]
            else:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    bell = 1
                    if rside == -1 and lside == -1:
                        rside = mid
                        lside = mid
                    if rside != -1:
                        lside = mid
                    if lside != -1:
                        rside = mid
                else:
                    if nums[mid] > target:
                        end = mid - 1
                    else:
                        start = mid + 1

        ans = []
        ans.append(lside)
        ans.append(rside)

        return ans