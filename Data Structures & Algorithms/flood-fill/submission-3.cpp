class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        const int ORIGINAL_COLOR = image[sr][sc];
        const int ROWS = ssize(image), COLS = ssize(image[0]);

        if (ORIGINAL_COLOR == color) return image;

        function<void(int r, int c)> fill = [&](int r, int c) -> void {
            if (min(r, c) < 0 || 
                r == ROWS || 
                c == COLS || 
                image[r][c] != ORIGINAL_COLOR
            ) return;

            image[r][c] = color;
            fill(r - 1, c);
            fill(r, c + 1);
            fill(r + 1, c);
            fill(r, c - 1);
        };

        fill(sr, sc);
        return image;
    }
};