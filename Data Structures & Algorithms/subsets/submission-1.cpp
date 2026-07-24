class Solution {
private:
    void dfs(vector<int>& nums, int i, vector<int>& curr, vector<vector<int>>& out) {
        if (i == nums.size()) {
            out.push_back(curr);
            return;
        }

        curr.push_back(nums[i]);
        dfs(nums, i + 1, curr, out);

        curr.pop_back();
        dfs(nums, i + 1, curr, out);
    }
    
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> out;
        vector<int>curr;
        dfs(nums, 0, curr, out);
        return out;
    }
};
