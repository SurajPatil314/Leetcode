"""
https://leetcode.com/problems/rearrange-words-in-a-sentence/


Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths.
 If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.
"""


class Solution:
    def arrangeWords(self, text: str) -> str:

        text1 = text.split(' ')
        print(text1)
        text1.sort(key=len)
        ans = ''
        for i in range(len(text1)):
            if i == 0:
                ans = ans + text1[i].capitalize() + ' '
            elif i < len(text1) - 1:
                ans = ans + text1[i].lower() + ' '
            else:
                ans = ans + text1[i].lower()

        return ans
