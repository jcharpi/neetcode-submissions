# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for list_index, head in enumerate(lists):
            if head:
                min_heap.append((head.val, list_index, head.next))
        heapq.heapify(min_heap)

        dummy = ListNode(0)
        tail = dummy
        while min_heap:
            val, list_index, next_node = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next

            if (next_node):
                heapq.heappush(min_heap, (next_node.val, list_index, next_node.next))
        return dummy.next
