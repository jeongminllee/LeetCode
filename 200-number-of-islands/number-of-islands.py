dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        v = [[0]*n for _ in range(m)]

        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == "1" and v[i][j] == 0  :
                    q = deque()
                    q.append((i, j))

                    while q :
                        x, y = q.popleft()
                        for d in range(4) :
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == "1" and v[nx][ny] == 0 :
                                v[nx][ny] = 1
                                q.append((nx, ny))

                    cnt += 1

        return cnt