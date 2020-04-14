"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a
 k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute
  difference is k.
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if len(nums) < 2:
            return 0
        ans1 = []
        nums.sort(reverse=True)

        i = 0
        j = 1

        while (i < (len(nums) - 1)):
            if nums[i] - nums[j] == k:
                if [nums[i], nums[j]] not in ans1:
                    ans1.append([nums[i], nums[j]])
                i += 1
                j = i + 1
            else:
                if nums[i] - nums[j] < k:
                    if j < len(nums) - 1:
                        j += 1
                    else:
                        i += 1
                        j = i + 1
                else:
                    i += 1
                    j = i + 1

        return len(ans1)




