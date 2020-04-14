#https://leetcode.com/problems/divisor-game/submissions/
'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
'''

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True

        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            for j in range(1, int(i / 2)):
                if i % j == 0 and dp[i - j] == 0:
                    dp[i] = 1
                    break
        return dp[N] == 1
