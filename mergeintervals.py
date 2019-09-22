'''
Given a collection of intervals, merge all overlapping intervals.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return None

        if len(intervals) == 1:
            return intervals

        subans = []
        ans = []
sbi.00384@sbi
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        for subq in intervals:

            if i == 0:
                print(subq)
                ans.append(subq)
                i = i + 1
            else:
                print(subq)
                temp = []
                print(ans[i - 1])
                temp = ans[i - 1]

                if temp[1] >= subq[0]:
                    if temp[1] >= subq[1]:
                        print('aquired')
                    else:
                        temp[1] = subq[1]
                        del ans[i - 1]
                        ans.append(temp)
                else:
                    ans.append(subq)
                    i = i + 1

        return ans


