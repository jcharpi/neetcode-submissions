class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []
        def dfs(i):
            if i == len(nums):
                out.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)

        dfs(0)
        return out