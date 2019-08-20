/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null)
        {
            return null;
        }
        
        
        else
        {
          
            ListNode last= head;
            ListNode dhead= head;
            while(last.next!=null)
            {
                last=last.next;
            }
            
             
            for(int i=0;i<k;i++)
            {
                last.next= dhead;
                dhead= dhead.next;
            }
           return dhead;
        }
    }
}
