class Solution {
public:
    int rob(vector<int>& nums) {
        if (ssize(nums) == 1) return nums.front();

        auto rob_range = [&](int start, int end) {
            int two_houses_back = 0, one_house_back = 0;
            for (int i = start; i < end; i++) {
                int curr = max(two_houses_back + nums[i], one_house_back);
                two_houses_back = one_house_back, one_house_back = curr;
            }
            return max(two_houses_back, one_house_back);
        };

        int skip_first = rob_range(1, ssize(nums));
        int skip_last = rob_range(0, ssize(nums) - 1);
        return max(skip_first, skip_last);
    }
};
