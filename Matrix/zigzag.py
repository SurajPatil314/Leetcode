"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""

import numpy


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        x1 = []

        po = 0
        start = 0
        rev = 0

        if numRows == 1:
            return s

        while (po < len(s)):
            # print(x1)
            if start == 0 or start == numRows - 1:
                x2 = []

                for i in range(numRows):
                    if po >= len(s):
                        x2.append(None)
                        po += 1
                    else:
                        x2.append(s[po])
                        po += 1

                x1.append(x2)

                if start == 0:
                    start = numRows - 2
                    rev = 0
                else:
                    start = 1
                    rev = 1



            else:
                x2 = []

                for i in range(numRows):
                    if po >= len(s):
                        x2.append(None)
                        po += 1
                    else:
                        if i == start:
                            x2.append(s[po])
                            po += 1
                        else:
                            x2.append(None)

                x1.append(x2)

                if rev == 0:
                    start = start - 1
                else:
                    start = start + 1

        x3 = numpy.transpose(x1)

        ans = []

        for i in range(len(x3)):
            for j in range(len(x3[i])):
                if x3[i][j] != None:
                    ans.append(x3[i][j])

        ans1 = ""
        return ans1.join(ans)






