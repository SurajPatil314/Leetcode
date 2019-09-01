'''
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
class Solution:
   
        
'''
 def smallestRangeI(self, A: List[int], K: int) -> int:
        
        if len(A)<2:
            return 0
        else:
            diff=max(A)-min(A)
            print(K)
            print(max(A)-min(A))
            if diff<(2*K) or diff==(2*K):
                return 0
            else:
                return diff-2*K