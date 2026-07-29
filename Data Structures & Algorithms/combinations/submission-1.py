class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        curr = []

        def dfs(start):
            if len(curr) == k:
                out.append(curr.copy())
                return
            
            for i in range(start, n + 1):
                curr.append(i)
                dfs(i + 1)
                curr.pop()
            
        dfs(1)
        return out