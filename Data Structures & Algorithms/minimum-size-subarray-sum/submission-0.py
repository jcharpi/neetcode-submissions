class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = window_sum = 0
        min_length = float('inf')
        
        for r, num in enumerate(nums):
            window_sum += num
            print(f"{l}, {r}: {window_sum}")

            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1
            
        return 0 if sum(nums) < target else min_length