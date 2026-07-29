class Solution {
private:
    void dfs(int start, vector<int>& curr, vector<vector<int>>& out, int n, int k) {
        if (curr.size() == k) {
            out.push_back(curr);
            return;
        }

        for (int i = start; i < n + 1; i++) {
            curr.push_back(i);
            dfs(i + 1, curr, out, n, k); // include
            curr.pop_back();
        }
    }
    
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> out;
        vector<int> curr;
        dfs(1, curr, out, n, k);
        return out;
    }
};