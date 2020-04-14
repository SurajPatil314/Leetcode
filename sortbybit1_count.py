'''
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their
 binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hmap = {}
        arr.sort()
        repeat = {}
        ans = []
        for i in arr:
            if i == 0:
                ans.append(0)
            else:
                temp = bin(i)
                co = temp.count('1')
                hmap[i] = co

                if i in repeat:
                    repeat[i] = repeat.get(i) + 1
                else:
                    repeat[i] = 1

        hmap1 = sorted(hmap.items(), key=lambda kv: kv[1])

        for i in hmap1:
            if repeat[i[0]] > 1:
                for i4 in range(repeat[i[0]]):
                    ans.append(i[0])
            else:
                ans.append(i[0])

        return ans

