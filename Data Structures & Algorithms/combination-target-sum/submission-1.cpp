class Solution {
private:
    void dfs(size_t start_index, const vector<int>& nums, vector<int>& curr, vector<vector<int>>& out, int target) {
        int curr_sum = accumulate(curr.begin(), curr.end(), 0);
        if (curr_sum == target) {
            out.push_back(curr);
            return;
        }
        
        if (curr_sum > target || start_index == nums.size()) return;

        curr.push_back(nums[start_index]);
        dfs(start_index, nums, curr, out, target);

        curr.pop_back();
        dfs(start_index + 1, nums, curr, out, target);
    }

public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> out;
        vector<int> curr;
        dfs(0, nums, curr, out, target);
        return out;
    }
};
