# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Get middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split halves & flip
        print(slow.val)
        second_half = slow.next
        slow.next = None

        prev, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 3. Iterate on both halves
        first, second = head, prev
        max_sum = 0
        while first and second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum