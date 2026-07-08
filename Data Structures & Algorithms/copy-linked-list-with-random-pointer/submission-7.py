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
        clones = { None : None }

        curr = head
        while curr:
            copy = Node(curr.val)
            clones[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            clones[curr].next = clones[curr.next]
            clones[curr].random = clones[curr.random]
            curr = curr.next

        return clones[head]