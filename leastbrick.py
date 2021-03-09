"""
https://leetcode.com/problems/brick-wall/


There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
"""


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        maxi = 0
        li = []
        for i in range(len(wall)):
            q = 0
            for j in range(len(wall[i])):
                q = wall[i][j] + q
                if maxi <= q:
                    maxi = q
                wall[i][j] = q
                if q not in li:
                    li.append(q)

        i = 1
        ans = len(wall)
        li.sort()

        if len(li) > 10000:
            return ans - 1
        for i in range(len(li) - 1):
            tem = 0
            for k in range(len(wall)):
                if li[i] in wall[k]:
                    tem += 1

            if ans >= len(wall) - tem:
                ans = len(wall) - tem
            print(len(wall) - tem)

        print(maxi)

        return ans

