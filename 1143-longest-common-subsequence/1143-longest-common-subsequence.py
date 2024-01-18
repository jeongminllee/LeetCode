class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp 설정
        for i in range(1, m + 1) :
            for j in range(1, n + 1) :
                if text1[i - 1] == text2[j - 1] :   # 완전 탐색 - 같으면
                    dp[i][j] = dp[i - 1][j - 1] + 1 # 다음 배열에 + 1
                else :                              # 다르면
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 인접 백터? 배열?에서 최대값을 불러온다.
        return dp[m][n]