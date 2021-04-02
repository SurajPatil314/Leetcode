"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        print(intervals)

        ans = 0

        start = 0
        end = 0
        q = []

        for i in range(len(intervals)):

            if len(q) == 0:
                q.append(intervals[i][1])
                ans += 1

            else:
                if min(q) > intervals[i][0]:
                    ans += 1
                else:
                    q.remove(min(q))

                q.append(intervals[i][1])

        return ans


