"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary
 representation of N.

If there aren't two consecutive 1's, return 0.
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        q = bin(N).replace("0b", "")
        print(q)

        ans = 0
        qw = 0
        po = 0
        for i in q:
            if qw == 1 and i == '0':
                print('gap')
                po = po + 1
            if i == '1':
                if qw == 1:
                    qw = 0
                    po = po + 1
                    if po > ans:
                        print('po::%d' % po)
                        ans = po
                    po = 0
                    qw = 1
                else:
                    qw = 1

        return ans

