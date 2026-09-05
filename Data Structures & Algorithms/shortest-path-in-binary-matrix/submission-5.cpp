class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int ROWS = ssize(grid), COLS = ssize(grid[0]);

        if (grid[0][0] != 0 || grid[ROWS - 1][COLS - 1]) return -1;

        set<pair<int, int>> visited = {{0, 0}};
        deque<pair<int, int>> q = {{0, 0}};
        const vector<pair<int, int>> neighbor_differences = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0, 1},
            {1, -1}, {1, 0}, {1, 1}
        };
        
        int length = 1;
        while (!q.empty()) {
            const int q_size = ssize(q);
            for (int i = 0; i < q_size; i++) {
                const auto [r, c] = q.front();
                q.pop_front();

                if (r == ROWS - 1 && c == COLS - 1) return length;

                for (const pair<int, int>& neighbor_difference : neighbor_differences) {
                    int adj_row = r + neighbor_difference.first;
                    int adj_col = c + neighbor_difference.second;

                    if (min(adj_row, adj_col) < 0 || 
                        adj_row == ROWS || 
                        adj_col == COLS || 
                        visited.contains({adj_row, adj_col}) || 
                        grid[adj_row][adj_col] == 1) continue;
                    q.push_back({adj_row, adj_col});
                    visited.insert({adj_row, adj_col});
                }
            }
            length++;
        }
        return -1;
    }
};