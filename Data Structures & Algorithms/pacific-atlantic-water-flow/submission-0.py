class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if (min(r, c) < 0 or 
                r == ROWS or 
                c == COLS or
                (r, c) in visited 
                or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            # Where does pacific reach?
            dfs(0, c, pacific, heights[0][c])

            # Where does atlantic reach?
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            # Where does pacific reach?
            dfs(r, 0, pacific, heights[r][0])

            # Where does atlantic reach?
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        return list(atlantic & pacific)