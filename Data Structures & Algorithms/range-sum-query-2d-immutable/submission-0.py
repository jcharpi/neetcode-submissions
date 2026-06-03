class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_sums = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(1, ROWS + 1):
            row_sum = 0
            for c in range(1, COLS + 1):
                row_sum += matrix[r - 1][c - 1]
                self.prefix_sums[r][c] = self.prefix_sums[r - 1][c] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_left = self.prefix_sums[row1][col1]
        top_right = self.prefix_sums[row1][col2 + 1]
        bottom_left = self.prefix_sums[row2 + 1][col1]
        bottom_right = self.prefix_sums[row2 + 1][col2 + 1]

        return bottom_right - top_right - bottom_left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
