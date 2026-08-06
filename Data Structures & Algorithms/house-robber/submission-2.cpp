class Solution {
public:
    int rob(vector<int>& nums) {
        int rob = 0, skip = 0;
        for (int curr : nums) {
            tie(rob, skip) = pair{skip + curr, max(rob, skip)};
        }
        return max(rob, skip);
    }
};
