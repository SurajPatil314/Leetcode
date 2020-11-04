"""

https://leetcode.com/problems/count-number-of-teams/

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).


"""


class Solution:
    def numTeams(self, rating: List[int]) -> int:

        count = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if ((rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])):
                        count += 1

        return count
