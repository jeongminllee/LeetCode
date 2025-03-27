class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        res = 0

        for price in prices :
            if current < price :
                res += price - current
            current = price
            

        return res