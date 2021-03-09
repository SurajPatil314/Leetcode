"""
https://leetcode.com/problems/closest-divisors/


Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.
"""


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        ans1 = sys.maxsize
        ans2 = 0
        num1 = num + 1
        num2 = num + 2
        for i in range(1, int(math.sqrt(num + 1)) + 1):
            if (num + 1) % i == 0:
                if abs(num1 / i - i) < abs(ans1 - ans2):
                    ans1 = int(num1 / i)
                    ans2 = i

                    if ans1 == ans2:
                        return [ans1, ans2]

        for i in range(1, int(math.sqrt(num + 2)) + 1):
            if num2 % i == 0:
                if abs(num2 / i - i) < abs(ans1 - ans2):
                    ans1 = int(num2 / i)
                    ans2 = i
                    if ans1 == ans2:
                        return [ans1, ans2]

        return [ans1, ans2]



