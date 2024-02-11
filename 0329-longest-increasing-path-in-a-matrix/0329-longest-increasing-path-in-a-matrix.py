class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:        
        R = len(matrix)
        C = len(matrix[0])
        dp = [[0] * C for r in range(R)]
        def dfs(i, j):
            if not dp[i][j]:
                var = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and var > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < R - 1 and var > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j and var > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < C - 1 and var > matrix[i][j+1] else 0
                )
            return dp[i][j]
        return max(dfs(x,y) for x in range(R) for y in range(C))