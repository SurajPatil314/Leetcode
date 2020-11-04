"""
https://leetcode.com/problems/minimum-path-sum/


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        i = len(grid)
        j = len(grid[0])

        grid1 = []
        for i1 in range(len(grid)):
            qw = []
            for j1 in range(len(grid[i1])):
                qw.append(0)
            grid1.append(qw)

        for i1 in range(len(grid)):

            for j1 in range(len(grid[i1])):
                grid1[i1][j1] = grid[i1][j1]
                if (i1 > 0 and j1 > 0):
                    grid1[i1][j1] = grid1[i1][j1] + min(grid1[i1 - 1][j1], grid1[i1][j1 - 1])
                elif (i1 > 0):
                    grid1[i1][j1] = grid1[i1][j1] + grid1[i1 - 1][j1]
                elif (j1 > 0):
                    grid1[i1][j1] = grid1[i1][j1] + grid1[i1][j1 - 1]
                else:
                    grid1[i1][j1] = grid1[i1][j1]

        return grid1[len(grid) - 1][len(grid[i1]) - 1]


