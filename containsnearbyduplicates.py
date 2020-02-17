"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
 such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False
        else:
            count = 0
            k1 = 0
            as1 = []
            for i in range(0, len(nums)):
                if count == 0:
                    k1 = k + 1
                    for j in range(0, k + 1):
                        if j < len(nums):
                            if nums[j] in as1:
                                return True
                            else:
                                as1.append(nums[j])
                else:
                    if i >= k1:
                        del as1[0]
                        if nums[i] in as1:
                            return True
                        else:
                            as1.append(nums[i])
                count = count + 1

            return False

