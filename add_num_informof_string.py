'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        for i in num1:
            if i == '0':
                num1.replace(i, '')
            else:
                break

        for i in num2:
            if i == '0':
                num2.replace(i, '')
            else:
                break

        l1 = len(num1)
        l2 = len(num2)

        sum1 = 0
        sum2 = 0

        for i in num1:
            sum1 = sum1 + int(i) * 10 ** (l1 - 1)
            l1 = l1 - 1

        for i in num2:
            sum2 = sum2 + int(i) * 10 ** (l2 - 1)
            l2 = l2 - 1

        return str(sum1 + sum2)
