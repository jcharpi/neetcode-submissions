public class Solution {
    public int NumIslands(char[][] grid) {
        if (grid == null || grid.Length == 0) return 0;

        int ROWS = grid.Length;
        int COLS = grid[0].Length;
        HashSet<(int r, int c)> visitedLand = new HashSet<(int r, int c)>();
        int islandCount = 0;

        void Dfs(int r, int c) {
            if (Math.Min(r, c) < 0 || 
                r == ROWS || 
                c == COLS ||
                grid[r][c] == '0' || 
                visitedLand.Contains((r, c))) return;
            
            visitedLand.Add((r, c));
            Dfs(r - 1, c);
            Dfs(r, c - 1);
            Dfs(r + 1, c);
            Dfs(r, c + 1);
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1' && !visitedLand.Contains((r, c))) {
                    Dfs(r, c);
                    islandCount++;
                }
            }
        }

        return islandCount;
    }
}
