"""
https://leetcode.com/problems/avoid-flood-in-the-city/
"""


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        bucket = 0
        li = {}
        ans = [0] * len(rains)
        points = []
        for i in range(len(rains)):
            if rains[i] == 0:
                if len(li) > bucket:
                    bucket += 1
                    points.append(i)
            else:
                if rains[i] in li:
                    if bucket > 0:
                        i1 = 0
                        qw = li.get(rains[i])
                        i1 = li.get(rains[i]) + 1
                        found = 0
                        if points[-1] < qw:
                            print(points[-1])
                            return []
                        else:
                            for i2 in range(len(points)):
                                if points[i2] > qw:
                                    ans[points[i2]] = rains[i]
                                    points.remove(points[i2])
                                    li[rains[i]] = i
                                    bucket = bucket - 1
                                    found = 1
                                    break

                        if found == 0:
                            return []
                        ans[i] = -1
                    else:
                        return []
                else:
                    ans[i] = -1
                    li[rains[i]] = i

        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 1

        return ans


