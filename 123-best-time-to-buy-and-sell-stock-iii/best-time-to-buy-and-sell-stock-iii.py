class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # transactions1, transactions2 = 10**5, 10**5
        # profit1, profit2 = 0, 0

        # for price in prices :
        #     transactions1 = min(price, transactions1)
        #     profit1 = max(profit1, price - transactions1)

        #     transactions2 = min(price - profit1, transactions2)
        #     profit2 = max(profit2, price - transactions2)

        # return profit2

    
        dp = [[10**5, 0] * 2 for _ in range(len(prices))]

        for i in range(len(prices)) :
            dp[i][0] = min(dp[i-1][0], prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] - dp[i-1][0])
            dp[i][2] = min(dp[i-1][2], prices[i] - dp[i-1][1])
            dp[i][3] = max(dp[i-1][3], prices[i] - dp[i-1][2])
        
        return dp[-1][3]