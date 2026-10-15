# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        prev1 = None
        while l1:
            temp = l1.next
            l1.next = prev1
            prev1 = l1
            l1 = temp
        
        prev2 = None
        while l2:
            temp = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = temp
        
        carry = 0
        while prev1 or prev2 or carry > 0:
            val1 = prev1.val if prev1 else 0
            val2 = prev2.val if prev2 else 0
            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10

            dummy.next = ListNode(curr_sum % 10, dummy.next)

            if prev1:
                prev1 = prev1.next
            
            if prev2:
                prev2 = prev2.next
        return dummy.next