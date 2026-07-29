class Solution {
private:
    void dfs(int i, vector<int>& curr, vector<vector<int>>& out, const vector<int>& nums) {
        if (i == nums.size()) {
            out.push_back(curr);
            return;
        }

        curr.push_back(nums[i]);
        dfs(i + 1, curr, out, nums); // include

        curr.pop_back();
        while (i + 1 < nums.size() && nums[i] == nums[i + 1]) i++;
        dfs(i + 1, curr, out, nums); // exclude
    }

public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> out;
        vector<int> curr;

        sort(nums.begin(), nums.end());
        dfs(0, curr, out, nums);
        return out;
    }
};
