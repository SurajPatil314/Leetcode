"""
https://leetcode.com/problems/random-pick-index/submissions/


Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:
"""

import collections
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.ans = collections.defaultdict(list)
        for i, x in enumerate(nums):
            self.ans[x].append(i)

    def pick(self, target: int) -> int:
        p = self.ans[target]
        return p[0] if len(p) == 1 else random.choice(p)