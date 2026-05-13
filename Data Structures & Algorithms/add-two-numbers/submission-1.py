# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_1, dummy_2 = ListNode(0, l1), ListNode(0, l2)
        dummy_out = ListNode(0, None)
        curr = dummy_out
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_nums = v1 + v2 + carry
            digit = sum_nums % 10
            carry = sum_nums // 10

            curr.next = ListNode(digit, None)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_out.next