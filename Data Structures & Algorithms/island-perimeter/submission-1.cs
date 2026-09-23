public class Solution {
    public int IslandPerimeter(int[][] grid) {
        int ROWS = grid.Length, COLS = grid[0].Length;
        HashSet<(int, int)> visited = new HashSet<(int r, int c)>();

        int Dfs(int r, int c) {
            if (Math.Min(r, c) < 0 || r == ROWS || c == COLS || grid[r][c] == 0) return 1;
            if (visited.Contains((r, c))) return 0;

            visited.Add((r, c));
            int count = 0;
            count += Dfs(r - 1, c);
            count += Dfs(r, c + 1);
            count += Dfs(r + 1, c);
            count += Dfs(r, c - 1);
            return count;
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) return Dfs(r, c);
            }
        }
        return -1;
    }
}