# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head == None:
            return None

        head2 = head
        head3 = head
        head4 = head
        head5 = head
        count = 0
        if head.next:
            head3 = head.next
            head4 = head3
            if head.next.next == None:
                return head
        else:
            return head

        while (head2 != None):
            if count == 0:

                if head2.next.next:
                    head2.next = head2.next.next
                    head2 = head2.next
                    count += 1
            else:
                if head2.next:
                    head4.next = head2.next
                    head4 = head4.next
                    if head2.next.next:
                        head2.next = head2.next.next
                    else:
                        head5 = head2
                        head4.next = None
                        head5.next = None
                        head2.next = None


                else:
                    head5 = head2
                    head4.next = None
                    head5.next = None
                    head2.next = None

                head2 = head2.next

        head5.next = head3

        return head

