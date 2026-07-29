class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []
        nums.sort()
        
        def dfs(i):
            if i == len(nums):
                out.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1) # include
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1) # exclude

        dfs(0)
        return out
