"""
https://leetcode.com/problems/asteroid-collision/


We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        col = 1

        while (col == 1):
            i = 0
            col = 0

            while (i < len(asteroids) - 1):

                if asteroids[i] > 0 and asteroids[i + 1] < 0:

                    if abs(asteroids[i]) == abs(asteroids[i + 1]):
                        del asteroids[i]
                        del asteroids[i]

                    else:
                        if abs(asteroids[i]) > abs(asteroids[i + 1]):
                            del asteroids[i + 1]
                        else:
                            del asteroids[i]
                    col = 1
                else:
                    i += 1

            if col == 0:
                break

        return asteroids




