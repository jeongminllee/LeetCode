class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**4
        res = 0
        for price in prices :
            min_price = min(min_price, price)
            res = max(res, price - min_price)
            
        return res