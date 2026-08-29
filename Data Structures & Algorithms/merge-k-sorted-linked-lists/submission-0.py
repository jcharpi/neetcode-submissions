# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out = ListNode(0)
        min_heap = []
        count = 0
        for num_list in lists:
            if not num_list:
                continue
            
            min_heap.append((num_list.val, count, num_list.next))
            count += 1

        heapq.heapify(min_heap)
        curr = out
        while min_heap:
            val, count, next_node = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            if (next_node):
                heapq.heappush(min_heap, (next_node.val, count, next_node.next))
                count += 1
            curr = curr.next
        return out.next
