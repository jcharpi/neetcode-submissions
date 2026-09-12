class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int ROWS = ssize(heights), COLS = ssize(heights[0]);
        set<pair<int, int>> pacific;
        set<pair<int, int>> atlantic;

        auto dfs = [&](this auto& self, int r, int c, set<pair<int, int>>& visited, int prev_height) -> void {
            if (min(r, c) < 0 ||
                r == ROWS ||
                c == COLS ||
                visited.contains({r, c}) ||
                heights[r][c] < prev_height) return;
            
            visited.insert({r, c});
            self(r - 1, c, visited, heights[r][c]);
            self(r, c + 1, visited, heights[r][c]);
            self(r + 1, c, visited, heights[r][c]);
            self(r, c - 1, visited, heights[r][c]);
        };

        for (int r = 0; r < ROWS; r++) {
            dfs(r, 0, pacific, heights[r][0]);
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]);
        }

        for (int c = 0; c < COLS; c++) {
            dfs(0, c, pacific, heights[0][c]);
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]);
        }

        vector<vector<int>> result;
        for (const auto& coords : pacific) {
            if (atlantic.contains(coords)) {
                result.push_back({coords.first, coords.second});
            }
        }
        return result;
    }
};