"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3
of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
"""

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        else:
            ans = 0
            A.sort(reverse=True)
            while True:
                if len(A) < 3:
                    break
                b = A[0]
                c = A[1]
                d = A[2]

                if b < c + d and c < b + d and d < b + c:
                    ans = b + c + d
                    break
                else:
                    A.pop(0)

            return ans
