"""
https://leetcode.com/problems/top-k-frequent-elements/


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        qw = defaultdict(int)

        for i in range(len(nums)):
            qw[nums[i]] = qw[nums[i]] + 1

        qw = dict(sorted(qw.items(), key=lambda x: x[1], reverse=True))

        ans = []

        for i, j in qw.items():
            if k == 0:
                break
            else:
                ans.append(i)
                k -= 1

        return ans
