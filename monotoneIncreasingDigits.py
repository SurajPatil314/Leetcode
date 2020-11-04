"""
https://leetcode.com/problems/monotone-increasing-digits/


Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)


"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:

        if N <= 9:
            return N

        if N == 10:
            return 9

        qw = []

        for i in str(N):
            qw.append(int(i))

        i = len(qw) - 2

        while (i > -1):
            if qw[i] > qw[i + 1]:
                qw[i] = qw[i] - 1
                i1 = i + 1
                while (i1 < len(qw)):
                    qw[i1] = 9
                    i1 = i1 + 1
            else:
                i = i - 1

        s = [str(i) for i in qw]
        res = int("".join(s))
        return (res)

