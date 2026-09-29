class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for (u, v), value in zip(equations, values):
            adj_list[u].append((v, value))
            adj_list[v].append((u, 1.0 / value))
        
        def dfs(u, target, visited):
            if u == target:
                return 1.0
            
            visited.add(u)
            for v, value in adj_list[u]:
                if v not in visited:
                    result = dfs(v, target, visited)
                    if result != -1.0:
                        return result * value
            
            return -1.0
        
        out = []
        for u, v in queries:
            if u not in adj_list or v not in adj_list:
                out.append(-1.0)
            else:
                out.append(dfs(u, v, set()))
        return out