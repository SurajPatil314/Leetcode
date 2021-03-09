"""
https://leetcode.com/problems/rabbits-in-forest/


In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits
 have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        qw = []

        qw1 = {}

        for i in answers:

            if i == 0:
                qw.append(0)
            else:
                if i in qw1:
                    if qw1.get(i) > (i):
                        qw.append(i)
                        qw1[i] = 1
                    else:
                        qw1[i] = qw1.get(i) + 1
                else:
                    qw1[i] = 1
                    if i not in qw:
                        qw.append(i)

        ans = 0

        for i in qw:
            ans = ans + i + 1

        return ans
