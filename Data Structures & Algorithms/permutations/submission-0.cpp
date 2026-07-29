class Solution {
private:
    void dfs(vector<int>& nums, vector<int>& curr, vector<vector<int>>& out) {
        if (nums.empty()) {
            out.push_back(curr);
            return;
        }

        for (size_t i = 0; i < nums.size(); i++) {
            int num = nums[i];

            // add current num next in permutations
            nums.erase(nums.begin() + i);
            curr.push_back(num);
            dfs(nums, curr, out);

            // go to next num; keep considering this num for later
            curr.pop_back();
            nums.insert(nums.begin() + i, num);
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> out;
        vector<int> curr;

        dfs(nums, curr, out);
        return out;
    }
};
