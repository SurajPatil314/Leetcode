"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that
don't appear in arr2 should be placed at the end of arr1 in ascending order.
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            j = arr1.count(i)
            while i in arr1: arr1.remove(i)
            for k in range(j):
                ans.append(i)

        arr1.sort()

        ans.extend(arr1)

        return ans