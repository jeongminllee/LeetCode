class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr = prices[0]

        for i in prices[1:] :
            curr = min(curr, i)

            ans = max(ans, i - curr)
        return ans