class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, max_ones = 0;
        for (int r = 0; r < ssize(nums); r++) {
            if (nums[r] == 0) k--;

            while (k < 0) {
                if (nums[l] == 0) k++;
                l++;
            }
            max_ones = max(max_ones, r - l + 1);
        }
        return max_ones;
    }
};