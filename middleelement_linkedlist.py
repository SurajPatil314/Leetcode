"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        if not head:
            return None

        head1 = head
        count = 0
        while (head1 != None):
            head1 = head1.next
            count = count + 1
        if count == 1:
            return head
        if count == 2:
            return head.next

        head2 = head

        count = int(count / 2)
        for i in range(count):
            head2 = head2.next

        return head2


