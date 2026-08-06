class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) return n;

        pair<int, int> dp = { 1, 2};
        for (int i = 3; i <= n; i++) {
            dp = {dp.second, dp.first + dp.second};
        }

        return dp.second;
    }
};
