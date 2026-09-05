class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count, queue = 0, deque()
        neighbor_differences = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1

        minutes = 0
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbor_differences:
                    adj_row, adj_col = r + dr, c + dc
                    if (min(adj_row, adj_col) < 0 or 
                        adj_row == ROWS or 
                        adj_col == COLS or 
                        grid[adj_row][adj_col] == 2 or 
                        grid[adj_row][adj_col] == 0):
                        continue
                    grid[adj_row][adj_col] = 2
                    fresh_count -= 1
                    queue.append((adj_row, adj_col))
            minutes += 1
        return minutes if fresh_count == 0 else -1




