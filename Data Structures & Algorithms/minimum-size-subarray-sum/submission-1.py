class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = window_sum = total_sum = 0
        min_length = float('inf')
        
        for r, num in enumerate(nums):
            window_sum += num
            total_sum += num

            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1
            
        return 0 if total_sum < target else min_length