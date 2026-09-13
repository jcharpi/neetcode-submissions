public class Solution {
    public void Solve(char[][] board) {
        int ROWS = board.Length, COLS = board[0].Length;

        void Dfs(int r, int c) {
            if (Math.Min(r, c) < 0 ||
                r == ROWS ||
                c == COLS ||
                board[r][c] != 'O') return;
            
            board[r][c] = 'T';
            Dfs(r - 1, c);
            Dfs(r, c + 1);
            Dfs(r + 1, c);
            Dfs(r, c - 1);
        }

        int[] borderRows = { 0, ROWS - 1 };
        int[] borderCols = { 0, COLS - 1 };

        for (int r = 0; r < ROWS; r++) {
            foreach (int c in borderCols) {
                if (board[r][c] == 'O') Dfs(r, c);
            }
        }

        for (int c = 0; c < COLS; c++) {
            foreach (int r in borderRows) {
                if (board[r][c] == 'O') Dfs(r, c);
            }
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (board[r][c] == 'T') board[r][c] = 'O';
                else if (board[r][c] == 'O') board[r][c] = 'X';
            }
        }
    }
}
