
"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by
rotating mat in 90-degree increments, or false otherwise.

"""


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for i in range(4):
            N = len(mat)
            # Transpose the matrix
            for i in range(N):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # swap columns
            for i in range(N):
                for j in range(N // 2):
                    mat[i][j], mat[i][N - j - 1] = mat[i][N - j - 1], mat[i][j]

            if mat == target:
                return True

        return False
