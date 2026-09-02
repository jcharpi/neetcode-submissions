class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int ROWS = ssize(grid), COLS = ssize(grid[0]);
        set<pair<int, int>> visited_land;
        int island_count = 0;

        function<void(int r, int c)> dfs = [&](int r, int c) -> void {
            if (min(r, c) < 0 || 
                r == ROWS || 
                c == COLS || 
                visited_land.contains({r, c}) || 
                grid[r][c] == '0') return;

            visited_land.insert({r, c});
            dfs(r - 1, c);
            dfs(r, c + 1);
            dfs(r + 1, c);
            dfs(r, c - 1);
        };

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1' && !visited_land.contains({r, c})) {
                    dfs(r, c);
                    island_count++;
                }
            }
        }

        return island_count;
    }
};
