class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;

        for (int amt = 1; amt < amount + 1; amt++) {
            for (int coin_value : coins) {
                if (amt - coin_value >= 0) dp[amt] = min(dp[amt], 1 + dp[amt - coin_value]);
            }
        }
        return dp[amount] < amount + 1 ? dp[amount] : -1;
    }
};
