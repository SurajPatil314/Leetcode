"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with
 different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the
 row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order
as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
output the original matrix.
"""

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = 0
        col = 0
        nums1 = [[0 for i in range(c)] for j in range(r)]
        print(nums1)
        li = []
        for i in nums:
            for j in i:
                li.append(j)
            if col == 0:
                col = len(i)
            row = row + 1

        if row * col == r * c:
            count1 = 0
            for i1 in range(r):
                for j1 in range(c):
                    nums1[i1][j1] = li[count1]
                    count1 += 1
            return nums1

        else:
            return nums
