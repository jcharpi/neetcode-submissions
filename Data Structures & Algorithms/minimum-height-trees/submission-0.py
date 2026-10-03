class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def dfs(root, visited):
            max_height = 0
            visited.add(root)
            for dest in adj_list[root]:
                if dest not in visited:
                    max_height = max(max_height, dfs(dest, visited) + 1)
            
            return max_height
        
        heights = [dfs(node, set()) for node in range(n)]
        min_height = min(heights)

        out = []
        for node in range(n):
            if heights[node] == min_height:
                out.append(node)
        return out



