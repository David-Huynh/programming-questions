class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(0,9)}
        cols = {i:[] for i in range(0,9)}
        grid = {i:[] for i in range(0,9)}
        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                if num in rows[row_index] or num in cols[col_index] or num in grid[col_index//3 + 3*(row_index//3)]:
                    return False
                if not num == ".":
                    rows[row_index].append(num)
                    cols[col_index].append(num)
                    grid[col_index//3 + 3*(row_index//3)].append(num)
        return True