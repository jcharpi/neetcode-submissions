class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (ssize(edges) != n - 1) return false;

        vector<vector<int>> adj_list(n);
        for (const vector<int>& edge : edges) {
            adj_list[edge[0]].push_back(edge[1]);
            adj_list[edge[1]].push_back(edge[0]);
        }

        unordered_set<int> visited;
        function<bool(int node, int parent)> dfs = [&](int node, int parent) -> bool {
            if (visited.contains(node)) return false;

            visited.insert(node);
            for (int neighbor : adj_list[node]) {
                if (parent == neighbor) continue;
                if (!dfs(neighbor, node)) return false;
            }

            return true;
        };

        return dfs(0, -1) && ssize(visited) == n;
    }
};
