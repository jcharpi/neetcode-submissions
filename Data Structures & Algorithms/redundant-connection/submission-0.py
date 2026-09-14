class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = { i : [] for i in range(1, len(edges) + 1) }

        def dfs(vert, target_vert, visited):
            if vert == target_vert:
                return True
            if vert in visited:
                return False

            visited.add(vert)
            for connected_vert in adj_list[vert]:
                if dfs(connected_vert, target_vert, visited):
                    return True
            return False

        for e1, e2 in edges:
            if dfs(e1, e2, set()):
                return [e1, e2]
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        return []