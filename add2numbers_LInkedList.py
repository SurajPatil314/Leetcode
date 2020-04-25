"""
https://leetcode.com/problems/add-two-numbers-ii/


You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans1 = []
        ans2 = []

        while (l1 != None):
            ans1.append(l1.val)
            l1 = l1.next

        while (l2 != None):
            ans2.append(l2.val)
            l2 = l2.next

        if len(ans1) == 0 and len(asn2) == 0:
            return None

        elif len(ans1) == 0:
            strings = [str(integer) for integer in ans2]
            a_string = "".join(strings)
            asn12 = int(a_string)
            ans = asn12


        elif len(ans2) == 0:
            strings = [str(integer) for integer in ans1]
            a_string = "".join(strings)
            asn11 = int(a_string)
            ans = asn11


        else:
            strings = [str(integer) for integer in ans1]
            a_string = "".join(strings)
            asn11 = int(a_string)

            strings = [str(integer) for integer in ans2]
            a_string = "".join(strings)
            asn12 = int(a_string)

            ans = asn11 + asn12

        ansz = str(ans)

        headf = ListNode(int(ansz[0]))

        headf1 = headf
        for i in range(1, len(ansz)):
            q = ListNode(int(ansz[i]))
            headf1.next = q
            headf1 = headf1.next





        return headf

