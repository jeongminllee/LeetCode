class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = 1 << 32

        q = deque()
        q.append((0, 0))
        visited = [[INF] * m for _ in range(n)]
        visited[0][0] = grid[0][0]

        while q :
            ci, cj = q.popleft()

            for di, dj in ((0, 1), (1, 0)) :
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m :
                    if visited[ni][nj] > visited[ci][cj] + grid[ni][nj] :
                        visited[ni][nj] = visited[ci][cj] + grid[ni][nj]
                        q.append((ni, nj))

        return visited[n-1][m-1]