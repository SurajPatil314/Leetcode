"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.
"""
class Solution:
    def lastRemaining(self, n: int) -> int:

        if n < 2:
            return n

        qw = []
        for i in range(1, n + 1):
            qw.append(i)
        ans = 0
        i = 0
        while True:
            if n == 1:
                break

            del qw[i]
            if i < 0:
                if ((0 - i) >= len(qw)):
                    i = 0
                else:
                    i = i - 1
                n = n - 1
            else:

                if (i >= len(qw) - 1):
                    i = -1
                else:
                    i = i + 1
                n -= 1

        return qw[0]

