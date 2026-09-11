class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        visited = set()
       
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if parent == neighbor:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, None) and len(visited) == n