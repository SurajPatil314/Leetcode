"""
#https://leetcode.com/problems/two-city-scheduling/


There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
 and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        for i in costs:
            q = abs(i[0] - i[1])
            i.append(q)

        cos = sorted(costs, key=lambda x: x[2], reverse=True)
        print(cos)

        ta1 = 0
        ta2 = 0

        z = 0
        z1 = len(cos) // 2
        while (z < len(cos)):
            if cos[z][0] > cos[z][1]:
                if ta2 < z1:
                    ans = ans + cos[z][1]
                    ta2 += 1
                else:
                    ans = ans + cos[z][0]
                    ta1 += 1
            else:
                if ta1 < z1:
                    ans = ans + cos[z][0]
                    ta1 += 1
                else:
                    ans = ans + cos[z][1]
                    ta2 += 1
            z += 1

        return ans


