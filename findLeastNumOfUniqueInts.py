"""

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = {}

        for i in arr:
            if i in count:
                count[i] = count.get(i) + 1
            else:
                count[i] = 1

        count1 = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}

        ans = len(count1)
        for i, j in count1.items():
            if k <= 0:
                break
            else:
                if count1[i] <= k:
                    k = k - count1.get(i)
                    ans -= 1

                else:
                    k = k - count1.get(i)

        return ans