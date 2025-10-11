class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(si: int, sj: int) -> None:
            q = deque()
            q.append((si, sj))
            v[si][sj] = 1

            while q :
                ci, cj = q.popleft()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                    ni, nj = ci + di, cj + dj
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj] == '1' and v[ni][nj] == 0 :
                        q.append((ni, nj))
                        v[ni][nj] = 1


        n, m = len(grid), len(grid[0])
        v = [[0] * m for _ in range(n)]
        cnt = 0

        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == '1' and v[i][j] == 0 :
                    bfs(i, j)
                    cnt += 1

        return cnt