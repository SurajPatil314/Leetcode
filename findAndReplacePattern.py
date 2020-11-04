"""
https://leetcode.com/problems/find-and-replace-pattern/


You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        ans = []

        for i in words:
            temp = i

            if len(pattern) == len(temp):
                as1 = {}
                got = []
                found = 1
                for i1 in range(len(temp)):
                    if pattern[i1] not in as1:
                        if temp[i1] in got:
                            found = 0
                            break
                        else:
                            as1[pattern[i1]] = temp[i1]
                            got.append(temp[i1])
                    else:
                        if temp[i1] != as1.get(pattern[i1]):
                            found = 0
                            break

                if found == 1:
                    ans.append(temp)

        return ans







