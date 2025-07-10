class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dr = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        board_copy = copy.deepcopy(board)

        n, m = len(board), len(board[0])

        for i in range(n) :
            for j in range(m) :
                cnt = 0
                for di, dj in dr :
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m :
                        cnt += board[ni][nj]
                
                    live_or_die = 0
                    if cnt < 2 and board[i][j] == 1 :
                        live_or_die = 0
                    elif 2 <= cnt <= 3 and board[i][j] == 1 :
                        live_or_die = 1
                    elif cnt > 3 and board[i][j] == 1 :
                        live_or_die = 0
                    elif cnt == 3 and board[i][j] == 0 :
                        live_or_die = 1
                    else :
                        live_or_die = board[i][j]
                    
                    board_copy[i][j] = live_or_die

        for i in range(n) :
            for j in range(m) :
                board[i][j] = board_copy[i][j]