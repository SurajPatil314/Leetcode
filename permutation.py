#Given a collection of distinct integers, return all possible permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))