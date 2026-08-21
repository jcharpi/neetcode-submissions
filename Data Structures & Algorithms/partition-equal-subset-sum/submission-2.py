class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half_total = total // 2
        dp = [False] * (half_total + 1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(half_total, num - 1, -1):                
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[half_total]