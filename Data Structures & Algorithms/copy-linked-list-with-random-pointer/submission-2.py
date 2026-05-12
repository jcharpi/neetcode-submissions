"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hm but what do we store? node as key, our deep node as value? this seems sketchy with duplciate elements
        # so flow here > handle val and .next in one pass, make our new nodes, then random in another
        # we will go through each node in original and check that it's random node's value in our hm
        # is set to the random node of our node in the hm?
        hm = {}

        curr = head
        while curr:
            hm[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        new_curr = head
        while new_curr:
            hm[new_curr].next = hm[new_curr.next] if new_curr.next in hm else None
            hm[new_curr].random = hm[new_curr.random] if new_curr.random in hm else None
            new_curr = new_curr.next

        return hm[head] if hm else None






