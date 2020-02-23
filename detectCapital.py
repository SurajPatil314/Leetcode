"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = 0
        upper = 0
        upper1 = 0

        for i in range(len(word)):
            if i == 0:
                if word[i].islower():
                    lower = 1
                else:
                    upper = 1
            elif i == 1:
                if upper == 1:
                    if word[i].islower():
                        upper1 = 0
                    else:
                        upper1 = 1
                else:
                    if word[i].isupper():
                        return False
            else:
                if lower == 1:
                    if word[i].isupper():
                        return False
                elif upper1 == 1:
                    if word[i].islower():
                        return False
                else:
                    if word[i].isupper():
                        return False

        return True