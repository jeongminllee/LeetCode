class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num) :
            num = str(num)
            for x in range(9) :
                if board[row][x] == num or board[x][col] == num :
                    return False
            
            start_row, start_col = row - row % 3, col - col % 3
            for i in range(3) :
                for j in range(3) :
                    if board[i + start_row][j + start_col] == num :
                        return False
            return True

        def solve_board(board) :
            for i in range(9) :
                for j in range(9) :
                    if board[i][j] == "." :
                        for num in range(1, 10) :
                            if is_valid(board, i, j, str(num)) :
                                board[i][j] = str(num)
                                if solve_board(board) :
                                    return True

                                board[i][j] = "."
                        return False
            return True

        if solve_board(board) :
            for i in board :
                return i

        else :
            return False