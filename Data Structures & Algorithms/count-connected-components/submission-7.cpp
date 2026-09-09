class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> adj_list(n);
        for (const vector<int>& edge : edges) {
            int n1 = edge[0], n2 = edge[1];
            adj_list[n1].push_back(n2);
            adj_list[n2].push_back(n1);
        }

        unordered_set<int> visited;
        function<void(int vert)> dfs = [&](int vert) -> void {
            if (visited.contains(vert)) return;

            visited.insert(vert);
            for (int connected_node : adj_list[vert]) dfs(connected_node);
        };

        int out = 0;
        for (int vert = 0; vert < n; vert++) {
            if (!visited.contains(vert)) {
                out++;
                dfs(vert);
            }
        }
        return out;
    }
};
