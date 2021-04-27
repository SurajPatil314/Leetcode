"""
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/


You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

Replace keyi and the bracket pair with the key's corresponding valuei.
If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.
"""


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        qw = {}

        for i in knowledge:
            qw[i[0]] = i[1]


        ans1 = []

        start = 0
        temp = ''
        temp1 = ''

        for i in range(len(s)):

            if s[i] == '(':
                start = 1

                if temp1 != '':
                    ans1.append(temp1)

                temp1 = ''

            elif s[i] == ')':
                start = 0
                if temp in qw:
                    ans1.append(qw[temp])
                else:
                    ans1.append('?')

                temp = ''
            else:

                if start == 0:
                    temp1 = temp1 + s[i]
                else:
                    temp = temp + s[i]

        if temp1 != '':
            ans1.append(temp1)

        ans = ''.join(ans1)
        return ans
