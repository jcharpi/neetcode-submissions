class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ROWS = ssize(grid), COLS = ssize(grid[0]);
        queue<pair<int, int>> q;
        const vector<pair<int, int>> neighbor_differences = {
            {-1, 0}, {0, 1}, {1, 0}, {0, -1}
        };

        int fresh_count = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 2) q.push({r, c});
                if (grid[r][c] == 1) fresh_count++;
            }
        }

        int minutes = 0;
        while (!q.empty() && fresh_count > 0) {
            int q_size = ssize(q);
            for (int i = 0; i < q_size; i++) {
                auto [r, c] = q.front();
                q.pop();
                for (const pair<int, int>& neighbor_difference : neighbor_differences) {
                    int adjRow = r + neighbor_difference.first;
                    int adjCol = c + neighbor_difference.second;
                    if (min(adjRow, adjCol) < 0 || 
                        adjRow == ROWS || 
                        adjCol == COLS || 
                        grid[adjRow][adjCol] == 2 || 
                        grid[adjRow][adjCol] == 0) continue;
                    
                    q.push({adjRow, adjCol});
                    grid[adjRow][adjCol] = 2;
                    fresh_count--;
                }
            }
            minutes++;
        }
        return fresh_count > 0 ? -1 : minutes;
    }
};
