class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = 1 << 32

        visited = [[INF] * m for _ in range(n)]
        visited[0][0] = grid[0][0]

        for i in range(n) :
            for j in range(m) :
                if i == 0 and j == 0 :
                    continue

                visited[i][j] = min(
                    visited[i-1][j] if i > 0 else INF, 
                    visited[i][j-1] if j > 0 else INF
                ) + grid[i][j]

        return visited[-1][-1]