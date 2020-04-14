"""
https://leetcode.com/problems/number-of-islands/


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
 is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
 surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = []
        all1 = []
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    all1.append([i, j])
        tempc = []
        while (len(all1) > 0):
            qw = all1[0]
            visited = []
            visited.append(qw)
            ans += 1
            tempc.append(qw)
            while (len(tempc) > 0):
                # print(tempc)

                bs = tempc[0]

                del tempc[0]

                tempi = bs[0]
                tempj = bs[1]

                if tempi - 1 >= 0:
                    if grid[tempi - 1][tempj] == '1':
                        sd = [tempi - 1, tempj]
                        if sd not in visited:
                            tempc.append(sd)
                            visited.append(sd)

                if tempj - 1 >= 0:
                    if grid[tempi][tempj - 1] == '1':
                        sd = [tempi, tempj - 1]
                        if sd not in visited:
                            tempc.append(sd)
                            visited.append(sd)

                if tempi + 1 < len(grid):
                    if grid[tempi + 1][tempj] == '1':
                        sd = [tempi + 1, tempj]
                        if sd not in visited:
                            tempc.append(sd)
                            visited.append(sd)

                if tempj + 1 < len(grid[0]):
                    if grid[tempi][tempj + 1] == '1':
                        sd = [tempi, tempj + 1]
                        if sd not in visited:
                            tempc.append(sd)
                            visited.append(sd)

                if bs in all1:
                    all1.remove(bs)

        return ans