# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        prev = None
        while second_head:
            temp = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = temp
        
        second_head = prev
        while head and second_head:
            temp_first = head.next
            temp_second = second_head.next
            head.next = second_head
            second_head.next = temp_first
            head = temp_first
            second_head = temp_second