# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        # Get to left - 1 node for reference later
        pre_swap = dummy
        for _ in range(left - 1):
            pre_swap = pre_swap.next
        
        # Swap range
        curr = left_temp = pre_swap.next
        prev = None
        n = right - left
        while curr and n > -1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
        
        # Link new ends
        left_temp.next = curr
        pre_swap.next = prev
        
        # point left node at right.next
        
        return dummy.next
        while curr:
            print(curr.val)
            curr = curr.next
        
