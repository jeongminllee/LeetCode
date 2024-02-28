class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_val = f'({board[i][j]}) found in row {i}'
                    col_val = f'({board[i][j]}) found in col {j}'
                    box_val = f'({board[i][j]}) found in box {i // 3}-{j // 3}'
                    
                    if row_val in seen or col_val in seen or box_val in seen:
                        return False
                    
                    seen.add(row_val)
                    seen.add(col_val)
                    seen.add(box_val)
        
        return True