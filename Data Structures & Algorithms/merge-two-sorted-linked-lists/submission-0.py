# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        last = merged

        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next
        if list1:
            last.next = list1
        elif list2:
            last.next = list2
        
        return merged.next
        # check 1 and 1
        # start with l2's 1 (irrelevant) [1]
        # l2 = 3
        # l2.val is 3 > l1.val 1, so point merged.next to l1.val [1 > 1]
        # l1 = 2
        # l1.val < l2.val: so point next to l1.val [1 > 1 > 2]
        # l2 = 4
        # l2.val < l1.val: point next to l2.val [1 > 1 > 2 > 3]
        # l2 = 5
        # l1.val < l2.val: point next to l1.val [1 > 1 > 2 > 3 > 4]
        # break out of loop if one completes
        # see which remains and point next to it [1 > 1 > 2 > 3 > 4 > 5]

