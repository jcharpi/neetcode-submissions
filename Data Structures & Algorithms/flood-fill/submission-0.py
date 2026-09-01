class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        ORIGINAL_COLOR = image[sr][sc]

        if ORIGINAL_COLOR == color:
            return image

        def fill(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != ORIGINAL_COLOR:
                return

            image[r][c] = color
            fill(r - 1, c)
            fill(r, c + 1)        
            fill(r + 1, c)
            fill(r, c - 1)

        fill(sr, sc)
        return image