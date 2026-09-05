public class Solution {
    public int OrangesRotting(int[][] grid) {
        int ROWS = grid.Length, COLS = grid[0].Length;
        Queue<(int r, int c)> q = new Queue<(int, int)>();
        (int dr, int dc)[] neighborDifferences = {
            (-1, 0), (0, 1), (1, 0), (0, -1)
        };
        
        int freshCount = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 2) q.Enqueue((r, c));
                if (grid[r][c] == 1) freshCount++;
            }
        }

        int minutes = 0;
        while (q.Count > 0 && freshCount > 0) {
            int qSize = q.Count;
            for (int i = 0; i < qSize; i++) {
                (int r, int c) = q.Dequeue();

                foreach ((int rDelta, int cDelta) in neighborDifferences) {
                    int adjRow = r + rDelta, adjCol = c + cDelta;
                    if (Math.Min(adjRow, adjCol) < 0 || 
                        adjRow == ROWS || 
                        adjCol == COLS || 
                        grid[adjRow][adjCol] == 2 || 
                        grid[adjRow][adjCol] == 0) continue;
                    
                    q.Enqueue((adjRow, adjCol));
                    grid[adjRow][adjCol] = 2;
                    freshCount--;
                }
            }
            minutes++;
        }

        return freshCount > 0 ? -1 : minutes;
    }
}
