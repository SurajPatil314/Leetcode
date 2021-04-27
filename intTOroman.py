class Solution:
    def intToRoman(self, num: int) -> str:
        qw = {}

        qw[1] = 'I'
        qw[5] = 'V'
        qw[10] = 'X'
        qw[50] = 'L'
        qw[100] = 'C'
        qw[500] = 'D'
        qw[1000] = 'M'

        we = len(str(num))

        ans = ''

        while (we > 0):

            if we == 1:

                if num < 4:
                    ans = ans + num * qw[1]
                elif num == 4:
                    ans = ans + qw[1] + qw[5]
                elif num == 5:
                    ans = ans + qw[5]
                elif num > 5 and num < 9:
                    ans = ans + qw[5] + (num - 5) * qw[1]
                else:
                    ans = ans + qw[1] + qw[10]

            else:
                we1 = 10 ** (we - 1)
                num1 = int(num // we1)
                num = num - (num1 * we1)

                if num1 < 4:
                    ans = ans + num1 * qw[we1]
                elif num1 == 4:
                    ans = ans + qw[we1] + qw[int(we1 * 5)]
                elif num1 == 5:
                    ans = ans + qw[int(we1 * 5)]
                elif num1 > 5 and num1 < 9:
                    ans = ans + qw[int(we1 * 5)] + (num1 - 5) * qw[we1]
                else:
                    ans = ans + qw[we1] + qw[we1 * 10]

            we -= 1

        return ans


