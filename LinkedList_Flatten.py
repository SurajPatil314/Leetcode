"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
 which may or may not point to a separate doubly linked list. These child lists may have one or more children of their
  own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first
 level of the list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if head == None:
            return None

        ll = []
        ans = []
        dummy = Node()
        dummy.next = head
        head1 = head

        while head1:
            ans.append(head1.val)
            if not head1.child:
                if not head1.next and len(ll) > 0:
                    top = ll.pop()
                    head1.next = top
                    top.prev = head1
            else:
                nt = head1.next
                if nt:
                    ll.append(nt)
                head1.next = head1.child
                head1.child.prev = head1
                head1.child = None
            head1 = head1.next
        return dummy.next