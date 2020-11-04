"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
 The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        ans = ''

        head1 = head

        while (head1 != None):
            ans = ans + str(head1.val)
            head1 = head1.next

        ans1 = 0
        i1 = 0
        for i in range(len(ans) - 1, -1, -1):
            ans1 = ans1 + int(ans[i]) * (2 ** i1)
            i1 += 1

        return ans1

