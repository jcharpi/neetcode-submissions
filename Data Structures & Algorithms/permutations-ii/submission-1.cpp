class Solution {
private: 
    void dfs(vector<int>& nums, vector<int>& curr, vector<vector<int>>& out) {
        if (nums.empty()) {
            out.push_back(curr);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (i > 0 && num == nums[i - 1]) continue;
            
            curr.push_back(num);
            nums.erase(nums.begin() + i);
            dfs(nums, curr, out);

            curr.pop_back();
            nums.insert(nums.begin() + i, num);
        }
    }
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> out;
        vector<int> curr;
        sort(nums.begin(), nums.end());

        dfs(nums, curr, out);
        return out;
    }
};