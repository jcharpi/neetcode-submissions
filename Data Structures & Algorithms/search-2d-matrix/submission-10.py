class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # binary search on row
        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                break
       
        if l > r:
            return False
        
        # binary search on element in row
        row = matrix[m]
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        return False