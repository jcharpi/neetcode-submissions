class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Given
        # grid[i][j] = 1: land
        # grid[i][j] = 0: water

        # Cells are connected horizontally and vertically
        # Exactly one island

        # Goal
        # Find the island, dfs each cell in all 4 directions: for each side that is not land ++
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            count = 0
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r + 1, c)
            count += dfs(r, c - 1)
            return count
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)