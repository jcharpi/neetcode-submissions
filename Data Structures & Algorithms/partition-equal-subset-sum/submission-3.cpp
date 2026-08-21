class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = ranges::fold_left(nums, 0, plus<>{});
        if (total % 2 != 0) return false;

        int half_total = total / 2;
        vector<bool> dp(half_total + 1, false);
        dp[0] = true;

        for (int num : nums) {
            for (int sum = half_total; sum >= num; sum--) {
                dp[sum] = dp[sum] || dp[sum - num];
            }
        }
        return dp[half_total];
    }
};
