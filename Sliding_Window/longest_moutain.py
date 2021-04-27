"""
https://leetcode.com/problems/longest-mountain-in-array/

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no
mountain subarray.
"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        j = 1

        ans = 0

        start = 0
        end = 0
        i1 = 0

        if len(arr) < 3:
            return 0

        while ( j < len(arr)):

            if j == len(arr) - 1:

                if arr[j - 1] > arr[j]:
                    if end == 1:
                        end = 0
                        tempans = j - i1 + 1
                        if tempans > ans:
                            ans = tempans
                        tempans = 1
                        start = 1
                        i1 = j - 1
                        j = j + 1
                    else:
                        if start == 1:
                            tempans = j - i1 + 1
                            if tempans > ans:
                                ans = tempans
                                tempans = 1
                                start = 1
                        j += 1
                        start = 0
                        end = 0

                elif arr[j - 1] < arr[j]:
                    if end == 1:
                        end = 0
                        tempans = j - i1
                        if tempans > ans:
                            ans = tempans
                        tempans = 1
                        start = 1
                        i1 = j - 1
                        j = j + 1
                    else:
                        if start == 0:
                            start = 1
                            i1 = j - 1
                        j += 1
                elif arr[j - 1] == arr[j]:
                    j += 1
                    start = 0
                    end = 0


            else:

                if arr[j - 1] < arr[j]:
                    if end == 1:
                        end = 0
                        tempans = j - i1
                        if tempans > ans:
                            ans = tempans
                        tempans = 1
                        start = 1
                        i1 = j - 1
                        j = j + 1
                    else:
                        if start == 0:
                            start = 1
                            i1 = j - 1
                        j += 1
                elif arr[j - 1] == arr[j]:

                    if end == 1:
                        end = 0
                        tempans = j - i1
                        if tempans > ans:
                            ans = tempans
                        tempans = 0
                        start = 0
                        j = j + 1
                    j += 1
                    start = 0
                    end = 0
                else:
                    if start == 1:
                        end = 1
                        j += 1
                    else:
                        j += 1
                        start = 0
                        end = 0

        return ans
