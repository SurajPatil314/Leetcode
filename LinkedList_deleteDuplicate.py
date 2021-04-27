"""
https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/


Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that
have any of those values.

Return the linked list after the deletions.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        head1 = head
        qw = defaultdict(int)

        while (head1 != None):
            qw[head1.val] = qw[head1.val] + 1

            head1 = head1.next

        head1 = None
        head2 = head
        head3 = head

        while (head2 != None):
            if qw[head2.val] > 1:
                if head1 == None:
                    head3 = head2.next
                else:
                    head1.next = head2.next
                head2 = head2.next

            else:
                if head1 == None:
                    head1 = head2
                    head3 = head1
                else:
                    head1 = head2
                head2 = head2.next

        return head3



