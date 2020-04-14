"""
https://leetcode.com/problems/powerful-integers/


Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.
"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        ans = []

        if bound < 2:
            return ans

        i = 0
        j = 0
        ans1 = 0
        if x == 1 and y == 1:
            return [2]

        if x == 1:
            while ans1 <= bound:
                ans1 = y ** j + 1
                if ans1 not in ans and ans1 <= bound:
                    ans.append(ans1)
                j += 1
            return ans

        if y == 1:
            while ans1 <= bound:
                ans1 = x ** i + 1
                if ans1 not in ans and ans1 <= bound:
                    ans.append(ans1)
                i += 1
            return ans

        bell = 0
        bell1 = 0
        i1 = 0
        while True:
            if bell == 0:
                ans1 = x ** i + y ** j
                if ans1 <= bound:
                    if ans1 not in ans:
                        ans.append(ans1)
                    i += 1
                else:
                    bell = 1
                    ans1 = 0
                    i1 = i
                    i = i - 2
                    j += 1


            else:

                ans1 = x ** i + y ** j
                if ans1 <= bound:
                    if ans1 not in ans:
                        ans.append(ans1)
                    j += 1
                else:
                    if bell1 == 0:
                        if i == 0:
                            bell1 = 1
                            j = 1
                            i = 0
                            ans1 = 0

                    if i < 0:
                        break

                    if i == i1:
                        break
                    if bell1 == 1 and ans1 > bound:
                        i += 1
                        j = 1

                    if bell1 == 0:
                        i -= 1

        return ans




