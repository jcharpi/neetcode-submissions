"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        original_to_clone = {}
        def dfs(original):
            if original in original_to_clone:
                return original_to_clone[original]
            
            clone = Node(original.val)
            original_to_clone[original] = clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)
