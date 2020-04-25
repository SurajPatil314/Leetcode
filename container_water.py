"""
https://leetcode.com/problems/container-with-most-water/submissions/


Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        ans = -sys.maxsize
        maxx = -sys.maxsize
        maxy = -sys.maxsize
        while (i < len(height)):
            if maxx < height[i]:
                maxx = height[i]
                j = len(height) - 1
                maxy = -sys.maxsize
                while (j > i):
                    if maxy < height[j]:
                        maxy = height[j]
                        i1 = height[i]
                        j1 = height[j]

                        temp = min(i1, j1) * (j - i)
                        if temp > ans:
                            ans = temp

                    j -= 1
            i += 1

        return ans