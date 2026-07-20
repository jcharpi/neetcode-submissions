class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int max_consecutive = 0;

        for (int num : nums_set) {
            if (nums_set.contains(num - 1)) continue;

            int length = 0;
            while (nums_set.contains(length + num)) {
                length++;
                max_consecutive = max(max_consecutive, length);
            }
        }
        return max_consecutive;
    }
};
