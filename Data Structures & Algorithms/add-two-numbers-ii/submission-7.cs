/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);

        ListNode prev1 = null;
        while (l1 != null) {
            ListNode temp = l1.next;
            l1.next = prev1;
            prev1 = l1;
            l1 = temp;
        }

        ListNode prev2 = null;
        while (l2 != null) {
            ListNode temp = l2.next;
            l2.next = prev2;
            prev2 = l2;
            l2 = temp;
        }
        
        int carry = 0;
        while (prev1 != null || prev2 != null || carry > 0) {
            int currSum = (prev1?.val ?? 0) + (prev2?.val ?? 0) + carry;
            carry = currSum / 10;

            result.next = new ListNode(currSum % 10, result.next);

            prev1 = prev1?.next;
            prev2 = prev2?.next;
        }

        return result.next;
    }
}