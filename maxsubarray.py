#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        
        ans=0
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        
        maxa= float('-inf')
        suma=0
        for i in range(len(nums)):
            
            suma= suma+nums[i]
            if(suma>maxa):
                maxa=suma
            if(suma<0):
                suma=0
            
                
                
            
        return maxa
            
        