class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search first indicies to find which row
        # binary search on that row

        row_l, row_r = 0, len(matrix) - 1
        out = []

        while row_l <= row_r:
            row_mid = (row_l + row_r) // 2
            print(row_mid)
            if matrix[row_mid][0] > target:
                row_r = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_l = row_mid + 1
            else:
                break
        
        if not (row_l <= row_r):
            return False
        
        # get row from now updated row_l and row_r values
        # regular binary search on that row
        row_mid = (row_l + row_r) // 2

        l, r = 0, len(matrix[row_mid]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row_mid][m] > target:
                r = m - 1
            elif matrix[row_mid][m] < target:
                l = m + 1
            else:
                return True
        return False
