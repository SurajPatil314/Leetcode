class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # iteration
        if len(nums) == 1 and nums[0] == target: return 0
		
        temp_nums = sorted(nums)
        l,r = 0, len(temp_nums)-1
        while l <= r:
            mid = (l + r)//2
            if target == temp_nums[mid]:
                return nums.index(temp_nums[mid])
            elif target < temp_nums[mid]:
                r = mid-1
            else:
                l= mid+1
        return -1