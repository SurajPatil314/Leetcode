"""
https://leetcode.com/contest/weekly-contest-190/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        st = []
        start = 0
        end = k
        num = 0
        ans = 0
        for i in s:
            if num < k:
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                    st.append(num)

                    if len(st) > ans:
                        ans = len(st)


            else:
                start += 1
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                    st.append(num)

                if len(st) > 0:
                    if st[0] < start:
                        del st[0]

                if len(st) > ans:
                    ans = len(st)

            num += 1

        return ans

