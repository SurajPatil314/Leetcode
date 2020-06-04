"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        top = []
        left = []
        ans = 0
        i1 = 0
        j1 = 0
        cl = 0
        i2 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if len(top) > i and len(left) > j:
                    ans1 = min(top[j], left[i])
                    if grid[i][j] < ans1:
                        ans = ans + (ans1 - grid[i][j])

                else:
                    i1 = 0
                    j1 = 0
                    if cl == 0:
                        i2 = 0
                        cl = 1
                    else:
                        i2 = i2 + 1
                    top1 = 0
                    left1 = 0
                    while (i1 < len(grid)):
                        if top1 < grid[i1][j]:
                            top1 = grid[i1][j]
                        i1 += 1

                    while (j1 < len(grid[0])):
                        if left1 < grid[i2][j1]:
                            left1 = grid[i2][j1]
                        j1 += 1

                    top.append(top1)
                    left.append(left1)

                    ans1 = min(top[j], left[i])

                    if grid[i][j] < ans1:
                        ans = ans + (ans1 - grid[i][j])

        return ans



