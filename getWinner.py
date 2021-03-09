"""
https://leetcode.com/problems/find-the-winner-of-an-array-game/


Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
"""


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        count = 0
        temp = sys.maxsize
        l = k

        if k > len(arr):
            return max(arr)
        while (l > 0):
            if count == 0:
                if arr[0] > arr[1]:
                    temp = arr[0]
                    k1 = arr[1]
                    del arr[1]
                    arr.append(k1)

                else:
                    temp = arr[1]
                    k1 = arr[0]
                    del arr[0]
                    arr.append(k1)

                count += 1
                l = k - 1
            else:
                if arr[0] > arr[1]:
                    if temp == arr[0]:
                        l -= 1
                    else:
                        l = k - 1
                        temp = arr[0]
                    k1 = arr[1]
                    del arr[1]
                    arr.append(k1)

                else:
                    if temp == arr[1]:
                        l -= 1
                    else:
                        l = k - 1
                        temp = arr[1]
                    k1 = arr[0]
                    del arr[0]
                    arr.append(k1)

        return temp