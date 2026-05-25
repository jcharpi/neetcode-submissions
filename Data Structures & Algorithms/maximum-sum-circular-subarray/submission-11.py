class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum = max_sum = nums[0]
        total_sum = curr_max = curr_min = 0

        for num in nums:
            curr_max = max(curr_max, 0) + num
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min, 0) + num
            min_sum = min(min_sum, curr_min)
            total_sum += num

        return max(max_sum, total_sum - min_sum) if max_sum >= 0 else max(nums)