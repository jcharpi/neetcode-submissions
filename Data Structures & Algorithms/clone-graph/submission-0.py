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

        adj_list = {}
        def dfs(node):
            if node in adj_list:
                return adj_list[node]
            
            clone = Node(node.val)
            adj_list[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)
