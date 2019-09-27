class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        countb = 0
        counta = 0
        countl = 0
        counto = 0
        countn = 0

        counter = 0

        for ch in text:
            if ch == 'b':
                countb += 1
            if ch == 'a':
                counta += 1
            if ch == 'l':
                countl += 1
            if ch == 'o':
                counto += 1
            if ch == 'n':
                countn += 1

        return min(countb, counta, countl // 2, counto // 2, countn)

