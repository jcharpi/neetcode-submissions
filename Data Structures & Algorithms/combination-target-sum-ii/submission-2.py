class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                out.append(curr.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return

            # include
            curr.append(candidates[i])
            dfs(i + 1, curr, curr_sum + candidates[i])
            curr.pop()

            # skip duplicates
            while (i + 1 < len(candidates) and candidates[i] == candidates[i + 1]):
                i += 1
            dfs(i + 1, curr, curr_sum)

        dfs(0, [], 0)
        return out
