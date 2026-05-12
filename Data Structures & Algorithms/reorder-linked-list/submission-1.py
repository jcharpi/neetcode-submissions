# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1) find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2) split and reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge list 1 and list 2
        first, second = head, prev
        while first and second:
            temp_first = first.next
            temp_second = second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second
            
        
 
