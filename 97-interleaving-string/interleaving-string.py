class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3) :
            return False
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n+1) :
            for j in range(m+1) :
                if j - 1 >= 0 and dp[i][j-1] :
                    if s3[i+j-1] == s2[j-1] :
                        dp[i][j] = 1
                
                if i - 1 >= 0 and dp[i-1][j] :
                    if s3[i+j-1] == s1[i-1] :
                        dp[i][j] = 1

        return dp[n][m]