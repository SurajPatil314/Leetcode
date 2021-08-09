"""
https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

A new online video game has been released, and in this video game, there are 15-minute rounds scheduled every
quarter-hour period. This means that at HH:00, HH:15, HH:30 and HH:45, a new round starts, where HH represents an
integer number from 00 to 23. A 24-hour clock is used, so the earliest time in the day is 00:00 and the latest is 23:59.

Given two strings startTime and finishTime in the format "HH:MM" representing the exact time you started and finished
 playing the game, respectively, calculate the number of full rounds that you played during your game session.

For example, if startTime = "05:20" and finishTime = "05:59" this means you played only one full round from 05:30 to
 05:45. You did not play the full round from 05:15 to 05:30 because you started after the round began, and you did not
 play the full round from 05:45 to 06:00 because you stopped before the round ended.
If finishTime is earlier than startTime, this means you have played overnight (from startTime to the midnight and from
 midnight to finishTime).

Return the number of full rounds that you have played if you had started playing at startTime and finished at finishTime.
"""


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start = startTime.split(':')
        finish = finishTime.split(':')

        if int(start[0]) == int(finish[0]) and int(start[1]) + 14 > int(finish[1]) and int(start[1]) < int(finish[1]):
            return 0

        if int(start[1]) > 45:
            start[1] = 0
            start[0] = int(start[0]) + 1
        if int(start[1]) > 30 and int(start[1]) < 45:
            start[1] = 45
            start[0] = int(start[0])
        if int(start[1]) > 15 and int(start[1]) < 30:
            start[1] = 30
            start[0] = int(start[0])
        if int(start[1]) > 0 and int(start[1]) < 15:
            start[1] = 15
            start[0] = int(start[0])

        start[0] = int(start[0])
        start[1] = int(start[1])

        if int(finish[1]) > 45:
            finish[1] = 45
            finish[0] = int(finish[0])
        if int(finish[1]) > 30 and int(finish[1]) < 45:
            finish[1] = 30
            finish[0] = int(finish[0])
        if int(finish[1]) > 15 and int(finish[1]) < 30:
            finish[1] = 15
            finish[0] = int(finish[0])
        if int(finish[1]) > 0 and int(finish[1]) < 15:
            finish[1] = 0
            finish[0] = int(finish[0])

        finish[0] = int(finish[0])
        finish[1] = int(finish[1])

        if start[0] > finish[0]:
            finish[0] = finish[0] + 24
        if start[0] == finish[0] and start[1] > finish[1]:
            finish[0] = finish[0] + 24

        ans = (finish[0] - start[0]) * 4
        ans = ans + int(((finish[1] - start[1]) / 15))

        return ans

