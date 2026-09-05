public class Solution {
    public int ShortestPathBinaryMatrix(int[][] grid) {
        int ROWS = grid.Length, COLS = grid[0].Length;

        if (grid[0][0] != 0 || grid[ROWS - 1][COLS - 1] != 0) return -1;

        HashSet<(int r, int c)> visited = new HashSet<(int, int)> { (0, 0) };
        Queue<(int r, int c)> q = new Queue<(int, int)>();
        q.Enqueue((0, 0));

        (int RowDelta, int ColDelta)[] neighborDifferences = {
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        };

        int length = 1;
        while (q.Count > 0) {
            int qSize = q.Count;
            for (int i = 0; i < qSize; i++) {
                (int r, int c) = q.Dequeue();
                if (r == ROWS - 1 && c == COLS - 1) return length;

                foreach ((int rowDelta, int colDelta) in neighborDifferences) {
                    int adjRow = r + rowDelta, adjCol = c + colDelta;
                    if (Math.Min(adjRow, adjCol) < 0 || 
                        adjRow == ROWS || 
                        adjCol == COLS || 
                        visited.Contains((adjRow, adjCol)) || 
                        grid[adjRow][adjCol] == 1) continue;
                    visited.Add((adjRow, adjCol));
                    q.Enqueue((adjRow, adjCol));
                }
            }
            length++;
        }
        return -1;
    }
}