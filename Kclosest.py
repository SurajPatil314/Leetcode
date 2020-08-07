"""
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""
import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        qw = {}
        ans = []

        for i in range(len(points)):
            temp = math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            qw1 = str(points[i][0]) + ',' + str(points[i][1])
            qw1

            qw[qw1] = temp

        qw2 = {k: v for k, v in sorted(qw.items(), key=lambda item: item[1])}
        # print(qw2)

        q1 = 0
        for i, j in qw2.items():
            ans1 = i.split(',')
            ans2 = []
            for i1 in ans1:
                ans2.append(int(i1))
            ans.append(ans2)

            q1 = q1 + 1
            if q1 >= K:
                break
            # print(ans1)

        return ans
