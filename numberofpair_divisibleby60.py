"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60

        for i in time:
            count[i % 60] += 1
        pair = 0
        for i in range(1, 30):
            pair = pair + (count[i] * count[60 - i])

        pair = int(pair + (((count[0] - 1) * count[0]) / 2))
        pair = int(pair + (((count[30] - 1) * count[30]) / 2))

        return pair

