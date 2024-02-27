# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         dp = [[] for _ in range(target + 1)]
#         dp[0] = [[]]
#         for i in range(target + 1) :
#             if len(dp[i]) != 0 :
#                 for c in candidates :
#                     if i + c <= target :
#                         tmp = []
#                         for idx in dp[i] :
#                             if len(idx) > 0 :
#                                 if idx[-1] <= c :
#                                     tmp.append(idx.copy() + [c])
#                             else :  # len(idx) <= 0 :
#                                 tmp.append(idx.copy() + [c])
#                         dp[i + c] = tmp if len(dp[i + c]) == 0 else tmp + dp[i + c]
#         return dp[target]
    
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, index, path, result):
        if target < 0:
            return  # backtracking
        if target == 0:
            result.append(path)
            return  # end condition
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], result)