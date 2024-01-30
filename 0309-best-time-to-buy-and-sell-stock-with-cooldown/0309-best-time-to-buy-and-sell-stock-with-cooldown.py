class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if not prices :
            return 0
        
        hold = [0] * n
        unhold = [0] * n
        
        hold[0] = -prices[0]
        
        for i in range(1, n) :
            hold[i] = max(hold[i - 1], unhold[i - 2] - prices[i])
            unhold[i] = max(unhold[i - 1], hold[i - 1] + prices[i])
            
        return unhold[-1]