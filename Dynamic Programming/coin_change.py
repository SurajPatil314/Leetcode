"""
https://leetcode.com/problems/coin-change-2/


You are given coins of different denominations and a total amount of money. Write a function to compute the number of
 combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        qw = []
        if amount == 0:
            return 1

        if len(coins) < 1:
            return 0

        for i in range(len(coins)):
            qw1 = [0] * (amount + 1)
            qw.append(qw1)

        for i in range(len(coins)):
            for j in range(amount + 1):
                if j == 0:
                    qw[i][j] = 1
                else:
                    if coins[i] <= j:
                        if i > 0:
                            qw[i][j] = qw[i][j - coins[i]] + qw[i - 1][j]
                        else:
                            if j % coins[i] == 0:
                                qw[i][j] = 1
                            else:
                                qw[i][j] = 0
                    else:
                        if i > 0:
                            qw[i][j] = qw[i - 1][j]
                        else:
                            qw[i][j] = 0

        return qw[len(coins) - 1][amount]

