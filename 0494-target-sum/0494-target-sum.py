class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        for x in nums:
            step = defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step

        return count[target]

    
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         total = sum(nums)
#         if total<target or (total - target)%2!=0:
#             return 0
#         bag = (total - target)//2
#         dp = [0 for i in range(bag+1)]
#         dp[0] = 1
#         for i in range(len(nums)):
#             for j in range(bag,nums[i]-1,-1):
#                 dp[j] += dp[j-nums[i]]
        
#         return dp[bag]