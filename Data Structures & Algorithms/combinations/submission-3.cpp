class Solution {
private:
    void dfs(int i, vector<int>& curr, vector<vector<int>>& out, int n, int k) {
        if (curr.size() == k) {
            out.push_back(curr);
            return;
        }

        if (i > n) return;

        curr.push_back(i);
        dfs(i + 1, curr, out, n, k); // include

        curr.pop_back();
        dfs(i + 1, curr, out, n, k); // exclude
    }
    
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> out;
        vector<int> curr;
        dfs(1, curr, out, n, k);
        return out;
    }
};