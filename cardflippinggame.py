"""
Share
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i.

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.
"""
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = 2001
        seen = {}

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                if backs[i] not in seen:
                    seen[backs[i]] = 0

        for i in range(len(fronts)):
            if backs[i] in seen and fronts[i] in seen:
                continue
            else:
                if backs[i] not in seen:
                    if backs[i] < ans:
                        ans = backs[i]
                if fronts[i] not in backs:
                    if fronts[i] < ans:
                        ans = fronts[i]

        if ans == 2001:
            return 0
        else:
            return ans
