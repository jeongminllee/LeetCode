class Solution:
    def combinationSum(self, candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for i in range(target + 1) :
            if len(dp[i]) != 0 :
                for c in candidates :
                    if i + c <= target :
                        tmp = []
                        for idx in dp[i] :
                            if len(idx) > 0 :
                                if idx[-1] <= c :
                                    tmp.append(idx.copy() + [c])
                            else :
                                tmp.append(idx.copy() + [c])
                        dp[i + c] = tmp if len(dp[i + c]) == 0 else tmp + dp[i + c]
        return dp[target]