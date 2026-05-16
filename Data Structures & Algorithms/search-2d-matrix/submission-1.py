class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def getMatrixRow():
            l, r = 0, len(matrix) - 1

            while l <= r:
                m = (l + r) // 2

                if matrix[m][-1] < target:
                    l += 1
                elif matrix[m][0] > target:
                    r -= 1
                else:
                    return m
            return -1
        
        def getElement():
            row = getMatrixRow()
            l, r = 0, len(matrix[row]) - 1
            while l <= r:
                m = (l + r) // 2

                if matrix[row][m] < target:
                    l += 1
                elif matrix[row][m] > target:
                    r -= 1
                else:
                    return True
            return False
        

        return getElement()