"""
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        qw = defaultdict(int)
        ans = []

        if k == 0:
            return ans

        for i in words:
            qw[i] = qw[i] + 1

        qw1 = dict(sorted(qw.items(), key=lambda x: (-x[1], x[0])))

        l = 0
        for i, j in qw1.items():
            if l == k:
                break
            else:
                ans.append(i)
            l += 1

        return ans




