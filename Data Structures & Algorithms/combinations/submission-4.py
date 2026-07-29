class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        curr = []

        def dfs(i):
            if len(curr) == k:
                out.append(curr.copy())
                return
            
            if i > n:
                return

            curr.append(i)
            dfs(i + 1) # include

            curr.pop()
            dfs(i + 1) # exclude
            
        dfs(1)
        return out