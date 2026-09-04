class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited_land = set()
        max_area = 0

        def dfs(r, c):
            if (min(r, c) < 0 or 
                r == ROWS or 
                c == COLS or 
                grid[r][c] == 0 or 
                (r, c) in visited_land):
                return 0
            
            visited_land.add((r, c))
            curr_area = 1
            curr_area += dfs(r - 1, c)
            curr_area += dfs(r, c + 1)
            curr_area += dfs(r + 1, c)
            curr_area += dfs(r, c - 1)

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited_land:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area