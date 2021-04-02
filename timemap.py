"""
https://leetcode.com/problems/time-based-key-value-store/


Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
"""


class TimeMap:

    def __init__(self):

        latest = 0

        self.qw = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.qw[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.qw:
            qw1 = self.qw[key]

            if timestamp < qw1[0][1]:
                return ""

            ans = qw1[0][0]

            for i in range(len(qw1) - 1, -1, -1):
                if timestamp == qw1[i][1]:
                    return qw1[i][0]
                else:
                    if timestamp > qw1[i][1]:
                        ans = qw1[i][0]
                        break

            return ans

        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)