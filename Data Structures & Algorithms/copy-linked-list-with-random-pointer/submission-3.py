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
        clones = {None : None}

        def clone(node):
            if node not in clones:
                clones[node] = Node(node.val)
            return clones[node]

        curr = head
        while curr:
            copy = clone(curr)
            copy.next = clone(curr.next)
            copy.random = clone(curr.random)
            curr = curr.next

        return clones[head]