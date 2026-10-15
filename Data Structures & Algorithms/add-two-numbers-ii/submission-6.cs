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
        // given
        // non-empty linked lists representing two integers
        // most sig dig comes first; each node is 1 digit

        // goal
        // add the numbers and return the sum as a linked list

        // dsa
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
        while (prev1 != null || prev2 != null) {
            int currSum = (prev1 != null ? prev1.val : 0) + (prev2 != null ? prev2.val : 0) + carry;
            int digit = currSum % 10;

            ListNode temp = result.next;
            result.next = new ListNode(digit);
            result.next.next = temp;

            carry = currSum / 10;

            if (prev1 != null) prev1 = prev1.next;
            if (prev2 != null) prev2 = prev2.next;
        }

        if (carry == 1) {
            ListNode temp = result.next;
            result.next = new ListNode(carry);
            result.next.next = temp;
        }
        Console.WriteLine(result.next.val);
        return result.next;
    }
}



//   9 7
// // 9 9 8

// 5 w/ carry: 1
// 9 w/ carry: 1