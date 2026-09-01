public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        int ORIGINAL_COLOR = image[sr][sc];
        int ROWS = image.Length;
        int COLS = image[0].Length;

        if (color == ORIGINAL_COLOR) return image;

        void Fill(int r, int c) {
            if (Math.Min(r, c) < 0 || 
                r == ROWS || 
                c == COLS || 
                image[r][c] != ORIGINAL_COLOR
            ) return;

            image[r][c] = color;
            Fill(r - 1, c);
            Fill(r, c + 1);
            Fill(r + 1, c);
            Fill(r, c - 1);
        }

        Fill(sr, sc);
        return image;
    }
}