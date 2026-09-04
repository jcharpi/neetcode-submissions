public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
        int ROWS = grid.Length, COLS = grid[0].Length;
        HashSet<(int r, int c)> visitedLand = new HashSet<(int r, int c)>();
        int maxArea = 0;

        int Dfs(int r, int c) {
            if (Math.Min(r, c) < 0 || 
                r == ROWS || 
                c == COLS || 
                grid[r][c] == 0 || 
                visitedLand.Contains((r, c))) return 0;

            visitedLand.Add((r, c));
            int currArea = 1;
            currArea += Dfs(r - 1, c);
            currArea += Dfs(r, c + 1);
            currArea += Dfs(r + 1, c);
            currArea += Dfs(r, c - 1);

            return currArea;
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1 && !visitedLand.Contains((r, c))) {
                    maxArea = Math.Max(maxArea, Dfs(r, c));
                }
            }
        }
        return maxArea;
    }
}
