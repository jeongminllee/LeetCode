class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res


    def dfs(self, candidates, target, idx, path, res) :
        if target < 0 :
            return
        elif target == 0 :
            res.append(path[:])
            return 

        for i in range(idx, len(candidates)) :
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)