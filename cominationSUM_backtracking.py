"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
 combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        temp = []
        ans = []
        candidates.sort()

        self.helper(temp, candidates, 0, target, ans)

        return ans

    def helper(self, temp: List[int], candidates: List[int], i: int, target: int, ans):
        if (target <= 0):
            if (target == 0):
                ans.append(list(temp))
            return

        for j in range(i, len(candidates)):
            temp.append(candidates[j])
            self.helper(temp, candidates, j, target - candidates[j], ans)
            temp.pop()
