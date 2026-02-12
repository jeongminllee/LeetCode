class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        curr = prices[0]
        for i in range(1, len(prices)) :
            if curr > prices[i] :
                curr = prices[i]
            else :
                dp[i] = prices[i] - curr

        return max(dp)