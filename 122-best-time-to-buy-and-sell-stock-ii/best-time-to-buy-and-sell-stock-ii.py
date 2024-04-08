class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr = prices[0]

        for p in prices[1:] :
            if curr > p :
                curr = p

            elif curr < p :
                ans += p - curr
                curr = p
        return ans