"""
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these
 steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements
 with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
"""


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        qw = defaultdict(list)

        for i in range(len(nums)):
            qw[nums[i]].append(i)

        qw = dict(sorted(qw.items(), reverse=True))

        if len(qw) <= 1:
            return 0

        ans = []
        ans1 = 0
        i1 = 0

        for i, j in qw.items():

            if i1 == len(qw) - 1:
                break
            else:
                if i1 == 0:
                    ans.append(len(j))
                    ans1 = ans[-1]
                else:
                    ans.append(ans[-1] + len(j))
                    ans1 = ans1 + ans[-1]
            i1 += 1

        return ans1
