class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        current = prices[0]
        
        for i in range(len(prices)) :
            if current > prices[i] :
                current = prices[i]
            elif current == prices[i] :
                continue
            else :
                profit = prices[i] - current
                max_profit = max(max_profit, profit)

        return max_profit
