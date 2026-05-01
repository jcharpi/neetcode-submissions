class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # plan: check each row, col, and square. 
        # If element in dict is true, ret false (already been seen)
        # else set element to true
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if(element == "."):
                    continue
                if(element in row[r] or element in col[c] or element in square[(r//3,c//3)]):
                    return False
                
                row[r].add(element)
                col[c].add(element)
                square[(r//3,c//3)].add(element)
        return True
