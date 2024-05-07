class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k) :
            if k == len(word) :
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k] :
                temp = board[i][j]
                board[i][j] = ''

                if backtrack(i + 1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1,k+1) :
                    return True

                board[i][j] = temp
                return False

        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if backtrack(i, j, 0):
                    return True
        return False