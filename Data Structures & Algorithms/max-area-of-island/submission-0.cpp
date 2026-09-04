class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ROWS = ssize(grid), COLS = ssize(grid[0]);
        int max_area = 0;
        set<pair<int, int>> visited_land;

        function<int(int r, int c)> dfs = [&](int r, int c) -> int {
            if (min(r, c) < 0 || 
                r == ROWS || 
                c == COLS || 
                visited_land.contains({r, c}) || 
                grid[r][c] == 0) return 0;
            
            visited_land.insert({r, c});

            int curr_area = 1;
            curr_area += dfs(r - 1, c);
            curr_area += dfs(r, c + 1);
            curr_area += dfs(r + 1, c);
            curr_area += dfs(r, c - 1);

            return curr_area;
        };

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1 && !visited_land.contains({r, c})) {
                    max_area = max(max_area, dfs(r, c));
                }
            }
        }

        return max_area;
    }
};
