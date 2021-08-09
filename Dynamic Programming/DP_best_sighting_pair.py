"""
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
"""

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = -sys.maxsize
        # prev keeps track of best encountered till now A[i]+i.
        # ans keeps finding better results across all j's.

        prev = 0

        for p1 in range(len(A)):
            ans = max(prev + A[p1] - p1, ans)
            prev = max(prev, A[p1] + p1)

        return ans


