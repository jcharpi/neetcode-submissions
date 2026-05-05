# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def nodeSwitch(curr: ListNode, prev: ListNode):
            if curr == None:
                return prev
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return nodeSwitch(curr, prev)
        prev = None
        curr = head

        return nodeSwitch(curr, prev)