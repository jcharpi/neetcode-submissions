class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> cache(ssize(nums), 1);

        for (int i = ssize(nums) - 1; i > -1; i--) {
            for (int j = i + 1; j < ssize(nums); j++) {
                if (nums[i] < nums[j]) {
                    cache[i] = max(cache[i], 1 + cache[j]);
                }
            }
        }
        return ranges::max(cache);
    }
};
