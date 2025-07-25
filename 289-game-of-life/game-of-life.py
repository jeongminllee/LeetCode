class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)

        n, m = len(board), len(board[0])

        di = [-1, 1, 0, 0, -1, -1, 1, 1]
        dj = [0, 0, -1, 1, -1, 1, -1, 1]

        for i in range(n) :
            for j in range(m) :
                cnt = 0 # 1의 갯수 세기
                
                for d in range(8) :
                    ni, nj = i + di[d], j + dj[d]

                    if 0 <= ni < n and 0 <= nj < m :
                        cnt += board[ni][nj]
                
                if cnt < 2 and board[i][j] :
                    board_copy[i][j] = 0
                elif 2 <= cnt <= 3 and board[i][j] :
                    board_copy[i][j] = 1
                elif cnt > 3 and board[i][j]:
                    board_copy[i][j] = 0
                elif cnt == 3 and not board[i][j]:
                    board_copy[i][j] = 1
                else :
                    board_copy[i][j] = board[i][j]

        for i in range(n) :
            for j in range(m) :
                board[i][j] = board_copy[i][j]
