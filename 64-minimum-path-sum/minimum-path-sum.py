class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = 1<<32
        
        dp = [[INF] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n) :
            for j in range(m) :
                if i == 0 and j == 0 :
                    continue
                    
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i][j-1]
                ) + grid[i][j]

        return dp[-1][-1]