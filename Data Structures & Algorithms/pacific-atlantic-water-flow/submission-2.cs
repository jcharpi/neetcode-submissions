public class Solution {
    public List<List<int>> PacificAtlantic(int[][] heights) {
        int ROWS = heights.Length, COLS = heights[0].Length;
        HashSet<(int r, int c)> pacific = new HashSet<(int, int)>();
        HashSet<(int r, int c)> atlantic = new HashSet<(int, int)>();

        void Dfs(int r, int c, HashSet<(int r, int c)> visited, int prevHeight) {
            if (Math.Min(r, c) < 0 ||
                r == ROWS ||
                c == COLS ||
                heights[r][c] < prevHeight ||
                visited.Contains((r, c))) return;
            
            visited.Add((r, c));
            Dfs(r - 1, c, visited, heights[r][c]);
            Dfs(r, c + 1, visited, heights[r][c]);
            Dfs(r + 1, c, visited, heights[r][c]);
            Dfs(r, c - 1, visited, heights[r][c]);
        }

        for (int r = 0; r < ROWS; r++) {
            Dfs(r, 0, pacific, heights[r][0]);
            Dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]);
        }

        for (int c = 0; c < COLS; c++) {
            Dfs(0, c, pacific, heights[0][c]);
            Dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]);
        }

        return pacific.Intersect(atlantic).Select(coords => new List<int> { coords.r, coords.c }).ToList();
    }
}
