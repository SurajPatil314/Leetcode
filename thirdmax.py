'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the
maximum number. The time complexity must be in O(n).
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        nums1 = []

        for num in nums:
            if num not in nums1:
                nums1.append(num)

        print(nums1)

        if len(nums1) < 3:
            return max(nums1)
        if len(nums1) == 3:
            return min(nums1)

        ans = 0
        for i in range(0, 3):
            ans = max(nums1)
            if (i < 2):
                print(ans)
                nums1.remove(ans)

        return ans
