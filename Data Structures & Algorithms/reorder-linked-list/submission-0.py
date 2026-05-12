# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        list_2 = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        list_2 = slow.next
        slow.next = None

        back_head = None
        while list_2:
            temp = list_2.next
            list_2.next = back_head
            back_head = list_2
            list_2 = temp

        while back_head and head:
            temp_head = head.next
            temp_back_head = back_head.next
            head.next = back_head
            back_head.next = temp_head
            head = temp_head
            back_head = temp_back_head
            
        
 
