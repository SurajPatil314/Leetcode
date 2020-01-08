"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
"""


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        if len(bits) == 1:
            if bits[0] == 0:
                return True
            else:
                False
        elif len(bits) == 2:
            if bits[0] == 0:
                return True
            else:
                False
        else:
            qw = False
            i = 0
            while i < len(bits):
                if (bits[i] == 1 and i + 1 < len(bits)):
                    qw = False
                    i = i + 2
                else:
                    qw = True
                    i = i + 1

            return qw
