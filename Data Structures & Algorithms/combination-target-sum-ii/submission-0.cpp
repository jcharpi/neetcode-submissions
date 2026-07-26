class Solution {
private:
    void dfs(size_t start, int remaining, vector<int>& curr, vector<vector<int>>& out, vector<int>& candidates) {
        if (remaining == 0) {
            out.push_back(curr);
            return;
        }

        for (size_t i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            if (candidates[i] > remaining) break;

            curr.push_back(candidates[i]);
            dfs(i + 1, remaining - candidates[i], curr, out, candidates);
            curr.pop_back();
        }
    }

public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> curr;
        vector<vector<int>> out;
        dfs(0, target, curr, out, candidates);
        return out;
    }
};
