class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        curr = []

        def dfs(start_index):
            curr_sum = sum(curr)
            if curr_sum == target:
                out.append(curr[:])
                return
            
            if start_index == len(nums) or curr_sum > target:
                return
            
            curr.append(nums[start_index])
            dfs(start_index)

            curr.pop()
            dfs(start_index + 1)

        dfs(0)
        return out