"""
https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ans = 0
        ans1 = 0
        visited = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if [i, j] not in visited:
                        bfs = []
                        land = 0
                        bfs.append([i, j])
                        visited.append([i, j])
                        ans1 = 1
                        while (len(bfs) > 0):
                            qw = bfs.pop()
                            i1 = qw[0]
                            j1 = qw[1]

                            #########
                            if i1 - 1 >= 0:
                                if [i1 - 1, j1] not in bfs and [i1 - 1, j1] not in visited:
                                    if grid[i1 - 1][j1] == 1:
                                        ans1 += 1
                                        bfs.append([i1 - 1, j1])
                                        visited.append([i1 - 1, j1])
                            ##########
                            if i1 + 1 <= len(grid) - 1:
                                if [i1 + 1, j1] not in bfs and [i1 + 1, j1] not in visited:
                                    if grid[i1 + 1][j1] == 1:
                                        ans1 += 1
                                        bfs.append([i1 + 1, j1])
                                        visited.append([i1 + 1, j1])
                            #########
                            if j1 - 1 >= 0:
                                if [i1, j1 - 1] not in bfs and [i1, j1 - 1] not in visited:
                                    if grid[i1][j1 - 1] == 1:
                                        ans1 += 1
                                        bfs.append([i1, j1 - 1])
                                        visited.append([i1, j1 - 1])

                            #########
                            if j1 + 1 <= len(grid[0]) - 1:
                                if [i1, j1 + 1] not in bfs and [i1, j1 + 1] not in visited:
                                    if grid[i1][j1 + 1] == 1:
                                        ans1 += 1
                                        bfs.append([i1, j1 + 1])
                                        visited.append([i1, j1 + 1])

                        if ans1 > ans:
                            ans = ans1

        return ans




