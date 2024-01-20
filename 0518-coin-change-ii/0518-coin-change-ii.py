class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) 
        dp[0] = 1
        for coin in coins :
            for i in range(coin, amount + 1) :
                dp[i] += dp[i - coin]
        return dp[amount]

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         coins.sort()
#         coins = [-1] + coins
        
#         dp = [[0] * (amount + 1) for _ in range(len(coins))]
#         for i in range(1, len(coins)) :
#             dp[i][0] = 1
            
#         for i_coin in range(1, len(coins)) :
#             for i_money in range(1, amount + 1) :
#                 coin = coins[i_coin]
#                 if i_money - coin >= 0 :
#                     dp[i_coin][i_money] = dp[i_coin - 1][i_money] + dp[i_coin][i_money - coin]
#                 else :
#                     dp[i_coin][i_money] = dp[i_coin - 1][i_money]
                    
#         return dp[len(coins) - 1][amount]
            