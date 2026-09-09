class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int ROWS = ssize(grid), COLS = ssize(grid[0]);
        queue<pair<int, int>> q;


        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (grid[r][c] == 0) q.push({r, c});
            }
        }

        vector<pair<int, int>> neighbors = {
            {-1, 0}, {0, 1}, {1, 0}, {0, -1}
        };

        int length = 1;
        while (!q.empty()) {
            int q_size = ssize(q);
            for (int i = 0; i < q_size; i++) {
                auto [r, c] = q.front();
                q.pop();

                for (const auto& [dr, dc] : neighbors) {
                    int adj_row = r + dr, adj_col = c + dc;
                    if (min(adj_row, adj_col) < 0 || 
                        adj_row == ROWS || 
                        adj_col == COLS || 
                        grid[adj_row][adj_col] != numeric_limits<int>::max()) continue;
                    q.push({adj_row, adj_col});
                    grid[adj_row][adj_col] = length;
                }
            }
            length++;
        }
    }
};
