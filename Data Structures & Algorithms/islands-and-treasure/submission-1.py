# Matrix BFS

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    adj_row, adj_col = r + dr, c + dc
                    if (min(adj_row, adj_col) < 0 or
                        adj_row == ROWS or 
                        adj_col == COLS or 
                        grid[adj_row][adj_col] != 2**31 - 1):
                        continue
                    queue.append((adj_row, adj_col))
                    grid[adj_row][adj_col] = length
            length += 1