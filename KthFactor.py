"""
https://leetcode.com/problems/the-kth-factor-of-n/


Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        qw = []
        fac = 0

        i = 1
        while (i <= n):

            if n % i == 0:
                i1 = n / i

                if i not in qw:
                    qw.insert(fac, i)
                if int(i1) not in qw:
                    qw.insert(len(qw), int(i1))
                fac += 1
                if fac == k:
                    return i

                if i1 <= i:
                    if i1 == i:
                        if i not in qw:
                            qw.insert(fac, i)
                    break
            i += 1

        if not qw:
            return -1

        if len(qw) > 0:
            qw.sort()

        if len(qw) > 0:
            if len(qw) < k:
                return -1
            else:
                return qw[k - 1]

        else:
            return -1



