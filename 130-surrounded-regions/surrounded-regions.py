class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        v = [[0] * m for _ in range(n)]
        
        def dfs(si: int, sj: int) :
            v[si][sj] = 1
            
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                ni, nj = si + di, sj + dj

                if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and board[ni][nj] == 'O' :
                    dfs(ni, nj)
                
        for i in range(n) :
            if board[i][0] == 'O' :
                dfs(i, 0)
            if board[i][m-1] == 'O' :
                dfs(i, m-1)

        for j in range(m) :
            if board[0][j] == 'O' :
                dfs(0, j)
            if board[n-1][j] == 'O' :
                dfs(n-1, j)
        
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == 'O' and v[i][j] == 0 :
                    board[i][j] = 'X'