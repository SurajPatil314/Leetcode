"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell
 such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is
|x0 - x1| + |y0 - y1|.
"""

from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        q.append(['#'])
        cnt_land, cnt_water = 0, 0
        N = len(grid)

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append([i, j])
                    cnt_land += 1
                else:
                    cnt_water += 1

        if cnt_water == 0 or cnt_land == 0:
            return -1

        dist = -1
        while len(q) > 1:
            arr = q.popleft()
            if arr[0] == '#':
                dist += 1
                q.append(['#'])
            else:
                i, j = arr[0], arr[1]
                if i > 0 and grid[i - 1][j] == 0:
                    q.append([i - 1, j])
                    grid[i - 1][j] = 1
                if i < N - 1 and grid[i + 1][j] == 0:
                    q.append([i + 1, j])
                    grid[i + 1][j] = 1
                if j > 0 and grid[i][j - 1] == 0:
                    q.append([i, j - 1])
                    grid[i][j - 1] = 1
                if j < N - 1 and grid[i][j + 1] == 0:
                    q.append([i, j + 1])
                    grid[i][j + 1] = 1
        return dist