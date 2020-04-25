"""
https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        qw = defaultdict()
        newlist = defaultdict()
        if head == None:
            return None

        head2 = head
        i = 0
        newhead = Node(head.val)
        hewheadd = newhead
        newlist[head] = newhead
        while (head2 != None):
            if i > 0:
                temp = Node(head2.val)
                hewheadd.next = temp
                newlist[head2] = temp
                hewheadd = hewheadd.next

            if head2.random:
                qw[head2.val] = head2.random.val
            i += 1
            head2 = head2.next

        nnewhead = head
        newhead1 = newhead
        while (nnewhead != None):
            if nnewhead.random:
                ans = newlist.get(nnewhead.random)
                newhead1.random = ans

            nnewhead = nnewhead.next
            newhead1 = newhead1.next

        return newhead




