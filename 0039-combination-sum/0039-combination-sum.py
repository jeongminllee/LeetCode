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
