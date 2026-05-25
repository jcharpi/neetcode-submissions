class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = window_sum = 0
        min_length = float('inf')
        
        for right, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        return min_length if min_length != float('inf') else 0