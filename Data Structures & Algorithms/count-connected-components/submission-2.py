class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()
        def dfs(vert):
            if vert in visited:
                return
            
            visited.add(vert)
            for connected_vert in adj_list[vert]:
                dfs(connected_vert)

        out = 0
        print(adj_list)
        for vert in range(n):
            if vert not in visited:
                dfs(vert)
                out += 1
        return out