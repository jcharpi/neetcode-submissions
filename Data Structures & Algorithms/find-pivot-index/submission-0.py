class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        out = [0] * len(nums)
        
        prefix = 0
        for i in range(len(nums)):
            out[i] = prefix
            prefix += nums[i]

        postfix = 0
        for i in range(len(nums) - 1, -1, -1):
            out[i] -= postfix
            postfix += nums[i]
        
        return out.index(0) if 0 in out else -1