class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        current = prices[0]

        for price in prices :
            if current > price :
                current = price
            elif current == price :
                continue
            else :
                max_profit += price - current
                current = price

        return max_profit