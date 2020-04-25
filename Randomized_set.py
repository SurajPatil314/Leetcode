"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
"""

import random


class RandomizedSet:

    def __init__(self):
        self.li = []
        self.dic = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.li.append(val)
            self.dic[val] = self.size
            self.size = self.size + 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            toberemovedindex = self.dic.get(val)
            elmatlastindex = self.li[-1]
            self.li[toberemovedindex] = elmatlastindex
            self.dic[elmatlastindex] = toberemovedindex
            self.li.pop()
            self.dic.pop(val)
            self.size = self.size - 1
            return True

    def getRandom(self) -> int:

        return random.choice(self.li)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()