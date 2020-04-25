"""
https://leetcode.com/problems/divide-two-integers/


Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        neg = 1

        if dividend == 0:
            return 0

        if divisor == 1:
            return dividend
            return min(2147483647, max(-dividend if neg else dividend, -2147483648))
        if divisor == -1:
            return min(2147483647, max(-dividend if neg else dividend, -2147483648))

        elif dividend < 0:
            if divisor < 0:
                neg = 0
                divisor = divisor * -1
                dividend = dividend * -1

            else:
                dividend = dividend * -1

        else:
            if divisor > 0:
                neg = 0
            else:
                divisor = divisor * -1

        if dividend == divisor:
            if neg == 1:
                return -1
            return 1

        if dividend < divisor:
            return 0

        sum1 = divisor

        while (sum1 <= dividend):
            curq = 1
            while (sum1 + sum1 <= dividend):
                sum1 = sum1 + sum1
                curq = curq + curq
            dividend = dividend - sum1
            sum1 = divisor
            count = count + curq

        return min(2147483647, max(-count if neg else count, -2147483648))