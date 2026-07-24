class Solution {
private:
    void dfs(int start_index, vector<int>& nums, vector<int>& curr, vector<vector<int>>& out, int target) {
        int curr_sum = accumulate(curr.begin(), curr.end(), 0);
        if (curr_sum > target || start_index == nums.size()) return;
        if (curr_sum == target) {
            out.push_back(curr);
            return;
        }

        curr.push_back(nums[start_index]);
        dfs(start_index, nums, curr, out, target); // include same number again
        
        curr.pop_back();
        dfs(start_index + 1, nums, curr, out, target); // exclude number
    }

public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> out;
        vector<int> curr;
        dfs(0, nums, curr, out, target);
        return out;
    }
};
