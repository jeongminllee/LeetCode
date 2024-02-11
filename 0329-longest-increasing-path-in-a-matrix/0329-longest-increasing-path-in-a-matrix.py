class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        for cy in range(m) :
            for cx in range(n) :
                self.dfs(cy, cx, 1, dp, matrix)

        answer = 0

        for cy in range(m) :
            for cx in range(n) :
                answer = max(answer, dp[cy][cx])

        return answer

    def dfs(self, cy, cx, depth, dp, matrix) :
        if dp[cy][cx] >= depth :
            return

        dp[cy][cx] = depth

        dyxs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dy, dx in dyxs :
            ny = cy + dy
            nx = cx + dx

            if self.is_in(ny, nx, matrix) :
                if matrix[ny][nx] > matrix[cy][cx] :
                    self.dfs(ny, nx, depth + 1, dp, matrix)

    def is_in(self, idx_row, idx_col, map) :
        if (0 <= idx_row < len(map)) and (0 <= idx_col < len(map[0])) :
            return True

        return False