class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = 1 << 32

        q = []
        heapq.heappush(q, (grid[0][0], 0, 0))
        visited = [[INF] * m for _ in range(n)]
        visited[0][0] = grid[0][0]

        while q :
            val, ci, cj = heapq.heappop(q)
            if (ci, cj) == (n - 1, m - 1) :
                return val
            for di, dj in ((0, 1), (1, 0)) :
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m :
                    if visited[ni][nj] > visited[ci][cj] + grid[ni][nj] :
                        visited[ni][nj] = visited[ci][cj] + grid[ni][nj]
                        heapq.heappush(q, (visited[ni][nj], ni, nj))

        return visited[n-1][m-1]