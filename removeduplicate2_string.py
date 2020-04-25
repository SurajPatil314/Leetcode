"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
 causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        s1 = set(s)
        b = ''
        while s != b:
            b = s
            for i in s1:
                s = s.replace(i * k, '')

        return s