class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        curr = []

        def dfs(start, remaining):
            if remaining == 0:
                out.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                
                curr.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                curr.pop()
        candidates.sort()
        dfs(0, target)
        return out
