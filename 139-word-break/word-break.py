class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(dp)) :
            for j in range(i) :
                if dp[j] and s[j:i] in wordSet :
                    dp[i] = True
                    break

        return dp[-1]
