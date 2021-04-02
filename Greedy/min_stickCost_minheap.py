"""
https://leetcode.com/problems/minimum-cost-to-connect-sticks/

You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where
 sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the
sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.
"""


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(list(sticks)) >= 2:
            l = heapq.heappop(sticks)
            r = heapq.heappop(sticks)
            heapq.heappush(sticks, l + r)
            res += l + r
        return res