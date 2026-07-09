class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = max_dec = 1
        curr_inc = curr_dec = 1

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] < num:
                curr_inc += 1
                max_inc = max(max_inc, curr_inc)
            else:
                curr_inc = 1
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] > num:
                curr_dec += 1
                max_dec = max(max_dec, curr_dec)
            else:
                curr_dec = 1
        
        return max(max_inc, max_dec)