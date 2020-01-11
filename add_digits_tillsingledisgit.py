'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        num1 = str(num)
        for i in num1:
            sum = sum + int(i)

        if sum > 9:
            sum = sum % 9
            if sum == 0:
                return 9
        return sum