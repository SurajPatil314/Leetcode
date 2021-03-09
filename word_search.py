"""
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        ans = []

        for i in range(len(searchWord)):
            ans1 = []

            if i == 0:
                for j in products:
                    if j[0] == searchWord[0]:
                        ans1.append(j)

                if len(ans1) > 3:
                    ans1.sort()
                    ans1 = ans1[:3]
                else:
                    if len(ans1) > 0:
                        ans1.sort()

                ans.append(ans1)

            else:
                # print('###')
                for j in products:
                    # print(searchWord[:i+1])
                    # print(j[:i+1])

                    if j[:i + 1] == searchWord[:i + 1]:
                        ans1.append(j)

                if len(ans1) > 3:
                    ans1.sort()
                    ans1 = ans1[:3]
                else:
                    if len(ans1) > 0:
                        ans1.sort()

                ans.append(ans1)

        return ans


