class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] != 0:
            return -1

        visited = {(0, 0)}
        queue = deque([(0, 0)])
        neighbors = [
            [-1, -1], [-1, 0], [-1, 1], 
            [0, -1], [0, 1], 
            [1, -1], [1, 0], [1, 1]]

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in neighbors:
                    adj_row, adj_col = r + dr, c + dc
                    if (min(adj_row, adj_col) < 0 or 
                        adj_row == ROWS or 
                        adj_col == COLS or 
                        (adj_row, adj_col) in visited 
                        or grid[adj_row][adj_col] == 1):
                        continue
                    queue.append((adj_row, adj_col))
                    visited.add((adj_row, adj_col))
            length += 1
        return -1