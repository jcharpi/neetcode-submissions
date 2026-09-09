public class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int ROWS = grid.Length, COLS = grid[0].Length;
        var queue = new Queue<(int r, int c)>();
        (int r, int c)[] neighbors = {
            (-1, 0), (0, 1), (1, 0), (0, -1)
        };

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 0) queue.Enqueue((r, c));
            }
        }

        int length = 1;
        while (queue.Count > 0) {
            int queueSize = queue.Count;
            for (int i = 0; i < queueSize; i++) {
                (int r, int c) = queue.Dequeue();

                foreach ((int dr, int dc) in neighbors) {
                    int adjRow = r + dr, adjCol = c + dc;
                    if (Math.Min(adjRow, adjCol) < 0 || 
                        adjRow == ROWS || 
                        adjCol == COLS || 
                        grid[adjRow][adjCol] != int.MaxValue) continue;
                    
                    queue.Enqueue((adjRow, adjCol));
                    grid[adjRow][adjCol] = length;
                }
            }
            length++;
        }
    }
}
