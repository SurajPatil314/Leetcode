"""

https://leetcode.com/problems/maximum-units-on-a-truck/

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.


"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        bo = sorted(boxTypes, key=lambda x: x[1])
        ans = 0
        while (truckSize >= 0):
            if len(bo) > 0:
                if bo[-1][0] <= truckSize:
                    ans = ans + bo[-1][0] * bo[-1][1]
                    truckSize = truckSize - bo[-1][0]
                    del bo[-1]
                else:
                    break
            else:
                break

        if truckSize > 0:
            if len(bo) > 0:
                ans = ans + truckSize * bo[-1][1]

        return ans
