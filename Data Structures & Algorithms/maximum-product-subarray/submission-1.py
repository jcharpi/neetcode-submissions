class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = max_product = nums[0]

        for i in range(1, len(nums)):
            prev_min, prev_max = curr_min, curr_max
            curr_min = min(nums[i], prev_min * nums[i], prev_max * nums[i])
            curr_max = max(nums[i], prev_min * nums[i], prev_max * nums[i])
            max_product = max(max_product, curr_max)
        return max_product