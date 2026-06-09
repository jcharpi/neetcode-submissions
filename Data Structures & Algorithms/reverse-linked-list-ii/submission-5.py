# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        node_before_left = dummy
        for _ in range(left - 1):
            node_before_left = node_before_left.next
        
        # Swap range
        curr = tail = node_before_left.next
        prev = None
        n = right - left
        while n > -1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
        
        # Link new ends
        tail.next = curr
        node_before_left.next = prev
        
        return dummy.next
        
