"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        tw = ['a', 'b', 'c']
        th = ['d', 'e', 'f']
        fo = ['g', 'h', 'i']
        fi = ['j', 'k', 'l']
        si = ['m', 'n', 'o']
        se = ['p', 'q', 'r', 's']
        ei = ['t', 'u', 'v']
        ni = ['w', 'x', 'y', 'z']

        if len(digits) == 0:
            return []

        ans = []

        for i in range(len(digits)):
            if i == 0:
                if digits[i] == '2':
                    ans.extend(tw)
                elif digits[i] == '3':
                    ans.extend(th)
                elif digits[i] == '4':
                    ans.extend(fo)
                elif digits[i] == '5':
                    ans.extend(fi)
                elif digits[i] == '6':
                    ans.extend(si)
                elif digits[i] == '7':
                    ans.extend(se)
                elif digits[i] == '8':
                    ans.extend(ei)
                else:
                    ans.extend(ni)
            else:
                if digits[i] == '2':
                    ans1 = []
                    for j in ans:
                        for j1 in tw:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '3':
                    ans1 = []
                    for j in ans:
                        for j1 in th:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '4':
                    ans1 = []
                    for j in ans:
                        for j1 in fo:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '5':
                    ans1 = []
                    for j in ans:
                        for j1 in fi:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '6':
                    ans1 = []
                    for j in ans:
                        for j1 in si:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '7':
                    ans1 = []
                    for j in ans:
                        for j1 in se:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                elif digits[i] == '8':
                    ans1 = []
                    for j in ans:
                        for j1 in ei:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)
                else:
                    ans1 = []
                    for j in ans:
                        for j1 in ni:
                            j2 = j + j1
                            ans1.append(j2)
                    ans = []
                    ans.extend(ans1)

        return ans

