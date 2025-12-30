class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 1차원 배열로 바꿔서 생각하자.
        # board : List[List[int]] => List[int] 로
        n = len(board)
        board2 = [-1]
        for i in range(n-1, -1, -1) :
            dr = n - i
            if dr % 2 == 1 :
                for j in range(n) :
                    board2.append(board[i][j])
            else :
                for j in range(n-1, -1, -1) :
                    board2.append(board[i][j])
        start = 1
        
        q = deque()
        
        if board2[start] == -1 :
            q.append((start, 0))
        else :
            q.append((board2[start], 0))
        
        visited = [0] * len(board2)
        visited[start] = 1

        while q :
            curr, cnt = q.popleft()
            if curr == n ** 2 :
                return cnt
            for di in (1,2,3,4,5,6) :
                nxt = board2[min(curr + di, n**2)]
                
                if nxt == -1 and visited[min(curr + di, n**2)] == 0:
                    q.append((min(curr + di, n**2), cnt + 1))
                    visited[min(curr + di, n**2)] = 1
                elif nxt != -1 and visited[min(nxt, n**2)] == 0 :
                    q.append((min(nxt, n**2), cnt + 1))
                    visited[min(nxt, n**2)] = 1
        return -1